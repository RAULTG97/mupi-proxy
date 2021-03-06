from collections import defaultdict
import json
#import dataset
#import sys
import re
import requests
import time
from netaddr import *


headers = {'Content-Type': 'application/json','Accept': 'application/json'}


class mupi_admin():

	IP_CONTROLLER = "127.0.0.1"
	BASE_URL = 'http://' + str(IP_CONTROLLER) + ':8080/mupi-proxy/'
	
	def main(self):
		self.initial_menu()
		while True:
			while True:
				self.main_menu()
				try:
					opcion = int(input('Select your operation: '))
				except ValueError:
					opcion = -1
					print('ERROR: incorrect value')
				print()

				#BACK
				if opcion == 0:
					break

				#MURT ENTRY
				if opcion == 1:
					while True:
						self.murt_menu()
						try:
							operation = int(input('Select your MURT_ENTRY operation: '))
						except ValueError:
							operation = -1
							print('ERROR: incorrect value')
						if operation == 0:
							break
						elif operation == 1:
							print("Retrieve all MURT Entries present in the database")
							response = self.get_murt_entries()
							self.next_operation(response)
						elif operation == 2:
							print("Add a new MURT Entry into to the database")
							response = self.add_murt_entry()
							self.next_operation(response)
						elif operation == 3:
							print("Retrieve a MURT Entry with a matching ID")
							response = json.dumps(self.get_murt_entry()[0], indent=4)	
							self.next_operation(response)
						elif operation == 4:
							print("Update a MURT Entry with a matching ID")
							response = self.update_murt_entry()
							self.next_operation(response)
						elif operation == 5:
							print("Delete a MURT Entry from the database")
							response = self.delete_murt_entry()
							self.next_operation(response)
						elif operation == 6:
							print("Delete all MURT Entries from the database")
							response = self.delete_murt_entries()
							self.next_operation(response)
						elif operation == 7:
							print("MONITOR MURT ENTRY TABLE")
							while True:
								murt_entries = self.monitor_murt_entries()
								self.print_murt_entries(murt_entries, False)
								time.sleep(2)

				#PROVIDER
				if opcion == 2:
					while True:
						self.providers_menu()
						try:
							operation = input('Select your PROVIDERS operation: ')
						except ValueError:
							print('ERROR: incorrect value')
						if operation == "0":
							break
						elif operation == "1":
							print("Retrieve all Providers present in the database")
							response = self.get_providers()
							self.next_operation(response)
						elif operation == "2":
							print("Add a new Provider into to the database")
							response = self.add_provider()
							self.next_operation(response)
						elif operation == "3":
							print("Retrieve a Provider with a matching ID")
							response = json.dumps(self.get_provider()[0], indent=4)	
							self.next_operation(response)
						elif operation == "4":
							print("Update a Provider with a matching ID")
							response = self.update_provider()
							self.next_operation(response)
						elif operation == "5":
							print("Delete a Provider from the database")
							response = self.delete_provider()
							self.next_operation(response)
						elif operation == "6":
							print("Delete all Providers from the database")
							response = self.delete_providers()
							self.next_operation(response)
						elif operation == "7":
							print("MONITOR MURT ENTRY TABLE")
							while True:
								providers = self.monitor_providers()
								self.print_providers(providers)
								time.sleep(2)
						elif operation == "8":
							print("Who broadcast this channel?")
							response = self.who_has_this_channel()
							self.next_operation(response)
						elif operation == "E":
							print("Enable Provider")
							response = self.enable_provider()
							self.next_operation(response)
						elif operation == "D":
							print("Disable Provider")
							response = self.disable_provider()
							self.next_operation(response)
						else:
							print('ERROR: incorrect value')


				#SDN CONTROLLER
				if opcion == 3:
					while True:
						self.controllers_menu()
						try:
							operation = int(input('Select your SDN-CONTROLLERS operation: '))
						except ValueError:
							operation = -1
							print('ERROR: incorrect value')
						if operation == 0:
							break
						elif operation == 1:
							print("Retrieve all Controllers present in the database")
							response = self.get_controllers()
							self.next_operation(response)
						elif operation == 2:
							print("Add a new Controller into to the database")
							response = self.add_controller()
							self.next_operation(response)
						elif operation == 3:
							print("Retrieve a Controller with a matching ID")
							response = json.dumps(self.get_controller()[0], indent=4)	
							self.next_operation(response)
						elif operation == 4:
							print("Update a Controller with a matching ID")
							response = self.update_controller()
							self.next_operation(response)
						elif operation == 5:
							print("Delete a Controller from the database")
							response = self.delete_controller()
							self.next_operation(response)
						elif operation == 6:
							print("Delete all Controllers from the database")
							response = self.delete_controllers()
							self.next_operation(response)
						elif operation == 7:
							print("MONITOR SDN CONTROLLERS")
							while True:
								controllers = self.monitor_controllers()
								self.print_controllers(controllers)
								time.sleep(2)

				#FLOWS
				if opcion == 4:
					while True:
						self.flows_menu()
						try:
							operation = int(input('Select your FLOWS operation: '))
						except ValueError:
							operation = -1
							print('ERROR: incorrect value')
						if operation == 0:
							break
						elif operation == 1:
							print("MONITOR FLOWS")
							while True:
								flows = self.monitor_flows()
								self.print_flows(flows)
								time.sleep(2)
						elif operation == 2:
							print("Retrieve the flows with a matching MURT Entry ID")
							response = json.dumps(self.get_flows(), indent=4)
							self.next_operation(response)
						elif operation == 3:
							print("Show Switching Mode")
							response = json.dumps(self.get_switching_mode(), indent=4)
							self.next_operation(response)
						elif operation == 4:
							print("Configure Switching Mode")
							response = json.dumps(self.configure_switching_mode(), indent=4)
							self.next_operation(response)

				# PROXY CONTROLLER
				if opcion == 5:
					print("Select the proxy you want to configure:")
					response = self.configure_controller()
					self.next_operation(response)
						
				print()
			break
		print()

		print("EXIT MUPI-PROXY ADMIN")



	#AUXILIAR FUNCTIONS

	# NEXT OPERATION

	def next_operation(information):
		print(information)
		wait = input('Next Operation... ')
		print()

	#MENUS
	def initial_menu():
		print("###########################################################")
		print("#                                                         #")
		print("#                    MUPI-PROXY CLIENT                    #")
		print("#                                                         #")
		print("###########################################################")
		print()

	def main_menu():
		print ("Make your api requests to configure mupi-proxy controller")
		print()
		print('Select')
		print("[1] MURT ENTRY")
		print("[2] PROVIDER")
		print("[3] SDN CONTROLLER")
		print("[4] FLOWS")
		print("[5] CHOOSE YOUR PROXY CONTROLLER")
		print("[0] EXIT")
		print()

	def murt_menu():
		print("###########################################################")
		print("#                   MURT-ENTRY OPERATION                  #")
		print("###########################################################")
		print()
		print('Select')
		print("[1] Retrieve all MURT Entries present in the database")
		print("[2] Add a new MURT Entry into the database")
		print("[3] Retrieve a MURT Entry with a matching ID")
		print("[4] Update a MURT Entry with a matching ID")
		print("[5] Delete a MURT Entry from the database")
		print("[6] Delete all MURT Entries from the database")
		print("[7] Show MURT Table")
		print("[0] Back")
		print()

	def providers_menu():
		print("###########################################################")
		print("#                    PROVIDER OPERATION                   #")
		print("###########################################################")
		print()
		print('Select')
		print("[1] Retrieve all Providers present in the database")
		print("[2] Add a new Provider into the database")
		print("[3] Retrieve a Provider with a matching ID")
		print("[4] Update a Provider with a matching ID")
		print("[5] Delete a Provider from the database")
		print("[6] Delete all Providers from the database")
		print("[7] Show Providers Table")
		print("[8] Give providers for a specific channel")
		print("[E] Enable Provider")
		print("[D] Disable Provider")
		print("[0] Back")
		print()

	def controllers_menu():
		print("###########################################################")
		print("#                 SDN CONTROLLERS OPERATION               #")
		print("###########################################################")
		print()
		print('Select')
		print("[1] Retrieve all Controllers present in the database")
		print("[2] Add a new Controller into the database")
		print("[3] Retrieve a Controller with a matching ID")
		print("[4] Update a Controller with a matching ID")
		print("[5] Delete a Controller from the database")
		print("[6] Delete all Controllers from the database")
		print("[7] Show Controllers Table")
		print("[0] Back")
		print() 

	def flows_menu():
		print("###########################################################")
		print("#                      FLOWS OPERATION                    #")
		print("###########################################################")
		print()
		print('Select')
		print("[1] Retrieve all Flows installed in the switch")
		print("[2] Retrieve all Flows for a specific Murt Entry ID")
		print("[3] Show Switching Mode")
		print("[4] Configure Switching Mode")
		print("[0] Back")
		print()

	#MURT_ENTRY
	def get_murt_entries():
		URL = mupi_admin.BASE_URL + "murtentries"
		print(URL)
		try:
			resp = requests.get( URL, headers = headers)
			response = json.dumps(resp.json(), indent=4)
		except:
			response = "Error"
		return response

	def add_murt_entry():
		URL = mupi_admin.BASE_URL + "murtentries"
		try:
			client_ip = input('Client IP: ')
			downstream_if = input('Downstream Interface: ')
			mcast_group = input('Multicast Group: ')
			mcast_src_ip = input('Multicast Source IP: ')
			upstream_if = input('Upstream Interface: ')
			priority = input('Priority: ')
			status_code = input('MURT Entry Status: [E] Enabled (default) | [D] Disabled: ')
			if status_code == "D":
				status = "Disabled"
			else:
				status = "Enabled"
			switching_mode_code = input('Switching mode: [A] All (default) | [R] Random | [RR] Round Robin ')
			if switching_mode_code == "R":
				switching_mode = "Random"
			elif switching_mode_code == "RR":
				switching_mode = "Round Robin"
			else:
				switching_mode = "All"
			new_entry = {"client_ip":client_ip, "downstream_if":downstream_if, "mcast_group":mcast_group, "mcast_src_ip":mcast_src_ip, "upstream_if":upstream_if, "priority":priority, "status":status, "switching_mode":switching_mode}
			new_entry = json.dumps(new_entry)
			print(new_entry)
			confirmation = input('Type "y" to confirm your entry: ')
			if confirmation == "y":
				resp = requests.post( URL, headers = headers, data=new_entry)
				murt_entry = json.dumps(resp.json(), indent=4)	
			else:
				murt_entry = "Discarded Operation"
				return murt_entry
		except ValueError:
			murt_entry = "Incorrect Values"
		return murt_entry


	def get_murt_entry():
		try:
			murt_entry_id = input('MURT Entry ID: ')
			URL = mupi_admin.BASE_URL + "murtentries/" + str(murt_entry_id)
			resp = requests.get(URL, headers = headers)
			murt_entry = resp.json()
		except ValueError:
			murt_entry = "Incorrect ID"
		return murt_entry, murt_entry_id

	def update_murt_entry():
		try:
			entry, murt_entry_id = mupi_admin.get_murt_entry()
			response = json.dumps(entry, indent=4)
			bad_request = "No murt entry with id: " + str(murt_entry_id)
			bad_request = json.dumps(bad_request, indent=4) 
			if response == bad_request:
				murt_entry = response
			else:
				print(response)
				URL = mupi_admin.BASE_URL + "murtentries/" + str(murt_entry_id)
				new_entry = input('Type the field to update: {"key":"value",...}: ')
				print(new_entry)
				confirmation = input('Type "y" to confirm your entry: ')
				if confirmation == "y":
					resp = requests.put(URL, headers = headers, data=new_entry)
					murt_entry = json.dumps(resp.json(), indent=4)	
				else:
					murt_entry = "Discarded Operation"
		except ValueError:
			murt_entry = "Incorrect Values"
		return murt_entry


	def delete_murt_entry():
		try:
			murt_entry_id = input('MURT Entry ID: ')
			URL = mupi_admin.BASE_URL + "murtentries/" + str(murt_entry_id)
			resp = requests.delete(URL, headers = headers)
			murt_entry = json.dumps(resp.json(), indent=4)
		except:
			murt_entry = "Error"
		return murt_entry

	def delete_murt_entries():
		URL = mupi_admin.BASE_URL + "murtentries"
		try:
			confirmation = input('Type "y" to confirm: ')
			if confirmation == "y":
				resp = requests.delete(URL, headers = headers)
				murt_entry = json.dumps(resp.text, indent=4)	
			else:
				murt_entry = "Discarded Operation"
		except:
			murt_entry = "Error"
		return murt_entry

	def monitor_murt_entries():
		URL = mupi_admin.BASE_URL + "murtentries-table"
		try:
			resp = requests.get(URL, headers = headers)
			murt_entries = resp.json()
		except:
			murt_entries = "Error"
		return murt_entries

	# Print mcast table
	def print_murt_entries(mcast_table, extended):
		if extended:
			print( '{:31} {:14} {:31} {:31} {:12} {:8} {:12} {:16}'.format('client_ip', 'downstream_if', 'mcast_group', 'mcast_src_ip', 'upstream_if', 'priority', 'status', 'id') )
			print( '{:31} {:14} {:31} {:31} {:12} {:8} {:12} {:16}'.format('-------------------------------', '--------------', '-------------------------------', '-------------------------------', '------------', '--------', '------------', '----------------') )
			for key in mcast_table.keys():
				e = mcast_table[key]
				if e['client_ip_first'] != '':
					client_ip = str(IPAddress(e['client_ip_first'])) + '-' + str(IPAddress(e['client_ip_last']))
				else:
					client_ip = ''
				if e['mcast_group_first'] != '':
					mcast_group = str(IPAddress(e['mcast_group_first'])) + '-' + str(IPAddress(e['mcast_group_last']))
				else:
					mcast_group = ''
				if e['mcast_src_ip_first'] != '':
					mcast_src_ip = str(IPAddress(e['mcast_src_ip_first'])) + '-' + str(IPAddress(e['mcast_src_ip_last']))
				else:
					mcast_src_ip = ''
				print( '{:31} {:^14} {:31} {:31} {:^12} {:^8} {:12} {:16}'.format(client_ip, e['downstream_if'], mcast_group, mcast_src_ip, e['upstream_if'], e['priority'], e['status'], key ))
			print( '{:31} {:14} {:31} {:31} {:12} {:8} {:12} {:16}'.format('-------------------------------', '--------------', '-------------------------------', '-------------------------------', '------------', '--------', '------------', '----------------') )
		else:
			print( '{:25} {:14} {:25} {:25} {:12} {:8} {:12}'.format('client_ip', 'downstream_if', 'mcast_group', 'mcast_src_ip', 'upstream_if', 'priority', 'status') )
			print( '{:25} {:14} {:25} {:25} {:12} {:8} {:12}'.format('-----------------', '--------------', '-----------------', '-----------------', '------------', '--------', '------------') )
			for key in mcast_table.keys():
				e = mcast_table[key]
				print( '{:25} {:^14} {:25} {:25} {:^12} {:^8} {:12}'.format(e['client_ip'], e['downstream_if'], e['mcast_group'], e['mcast_src_ip'], e['upstream_if'], e['priority'], e['status']) )
			print( '{:25} {:14} {:25} {:25} {:12} {:8} {:12}'.format('-----------------', '--------------', '-----------------', '-----------------', '------------', '--------', '------------') )
			print()


	#PROVIDERS
	def get_providers():
		URL = mupi_admin.BASE_URL + "providers"
		try:
			resp = requests.get( URL, headers = headers)
			response = json.dumps(resp.json(), indent=4)
		except:
			response = "Error"
		return response

	def add_provider():
		URL = mupi_admin.BASE_URL + "providers"
		try:
			description = input('Provider Description: ')
			mcast_src_ip = input('Multicast Source IP: ')
			upstream_if = input('Upstream Interface: ')
			mcast_groups = input('Multicast Groups [ip1, ip2,...]: ')
			new_provider = {"description":description, "mcast_src_ip":mcast_src_ip, "upstream_if":upstream_if, "mcast_groups":mcast_groups}
			new_provider = json.dumps(new_provider)
			print(new_provider)
			confirmation = input('Type "y" to confirm your entry: ')
			if confirmation == "y":
				resp = requests.post( URL, headers = headers, data=new_provider)
				provider = json.dumps(resp.json(), indent=4)	
			else:
				provider = "Discarded Operation"
		except ValueError:
			provider = "Incorrect Values"
		return provider


	def get_provider():
		try:
			provider_id = input('Provider ID: ')
			URL = mupi_admin.BASE_URL + "providers/" + str(provider_id)
			resp = requests.get(URL, headers = headers)
			provider = resp.json()
		except ValueError:
			provider = "Incorrect ID"
		return provider, provider_id

	def update_provider():
		try:
			provider, provider_id = mupi_admin.get_provider()
			response = json.dumps(provider, indent=4)
			bad_request = "No provider with id: " + str(provider_id)
			bad_request = json.dumps(bad_request, indent=4) 
			if response == bad_request:
				updated_provider = response
			else:		
				print(response)
				URL = mupi_admin.BASE_URL + "providers/" + str(provider_id)
				new_provider = input('Type the field to update: {"key":"value",...}: ')
				print(new_provider)
				confirmation = input('Type "y" to confirm your entry: ')
				if confirmation == "y":
					resp = requests.put(URL, headers = headers, data=new_provider)
					updated_provider = json.dumps(resp.json(), indent=4)	
				else:
					updated_provider = "Discarded Operation"
		except ValueError:
			updated_provider = "Incorrect Values"
		return updated_provider

	def delete_provider():
		try:
			provider_id = input('Provider ID: ')
			URL = mupi_admin.BASE_URL + "providers/" + str(provider_id)
			resp = requests.delete(URL, headers = headers)
			provider = json.dumps(resp.json(), indent=4)
		except:
			provider = "Error"
		return provider

	def delete_providers():
		URL = mupi_admin.BASE_URL + "providers"
		try:
			confirmation = input('Type "y" to confirm: ')
			if confirmation == "y":
				resp = requests.delete(URL, headers = headers)
				provider = json.dumps(resp.text, indent=4)	
			else:
				provider = "Discarded Operation"
		except:
			provider = "Error"
		return provider

	def who_has_this_channel():
		try:
			channel = input('Write the channel ID requested: ')
			URL = mupi_admin.BASE_URL + "channel/" + str(channel)
			resp = requests.get(URL, headers = headers)
			providers = json.dumps(resp.json(), indent=4)	
		except:
			providers = "Error"
		return providers

	def monitor_providers():
		URL = mupi_admin.BASE_URL + "providers-table"
		try:
			resp = requests.get(URL, headers = headers)
			murt_entries = resp.json()
		except:
			murt_entries = "Error"
		return murt_entries

	# Print providers table
	def print_providers(provider_table):
		print( '{:20} {:25} {:20} {:12} {:80} '.format('Description', 'mcast_src_ip', 'upstream_if', 'status', 'mcast_groups'))
		print( '{:20} {:25} {:20} {:12} {:80} '.format('-----------------', '-------------------', '--------------------', '------------', '-----------------') )
		for key in provider_table.keys():
			e = provider_table[key]
			print( '{:20} {:25} {:20} {:12} {:80} '.format(e['description'], e['mcast_src_ip'], e['upstream_if'], e['status'] ,str(e['mcast_groups'])) )
		print( '{:20} {:25} {:20} {:12} {:80} '.format('-----------------', '-------------------', '--------------------', '------------', '-----------------') )
		print()

	def enable_provider():
		try:
			provider_id = input('Provider ID or Upstream IF: ')
			URL = mupi_admin.BASE_URL + "providers/enable/" + str(provider_id)
			resp = requests.get(URL, headers = headers)
			provider = resp.json()
		except ValueError:
			provider = "Incorrect ID"
		return provider

	def disable_provider():
		try:
			provider_id = input('Provider ID or Upstream IF: ')
			URL = mupi_admin.BASE_URL + "providers/disable/" + str(provider_id)
			resp = requests.get(URL, headers = headers)
			provider = resp.json()
		except ValueError:
			provider = "Incorrect ID"
		return provider




	#SDN_CONTROLLERS
	def get_controllers():
		URL = mupi_admin.BASE_URL + "controllers"
		try:
			resp = requests.get( URL, headers = headers)
			response = json.dumps(resp.json(), indent=4)
		except:
			response = "Error"
		return response

	def add_controller():
		URL = mupi_admin.BASE_URL + "controllers"
		try:
			openflow_version = input('OpenFlow Version: ')
			tcp_port = input('TCP port: ')
			ip_address = input('IP ADDRESS: ')
			description = input('Description: ')
			new_controller = {"description":description, "openflow_version":openflow_version, "tcp_port":tcp_port, "ip_address": ip_address}
			new_controller = json.dumps(new_controller)
			print(new_controller)
			confirmation = input('Type "y" to confirm your controller: ')
			if confirmation == "y":
				resp = requests.post( URL, headers = headers, data=new_controller)
				controller = json.dumps(resp.json(), indent=4)	
			else:
				controller = "Discarded Operation"
		except ValueError:
			controller = "Incorrect Values"
		return controller


	def get_controller():
		try:
			controller_id = input('SDN Controller ID: ')
			URL = mupi_admin.BASE_URL + "controllers/" + str(controller_id)
			resp = requests.get(URL, headers = headers)
			controller = resp.json()
		except ValueError:
			controller = "Incorrect ID"
		return controller, controller_id

	def update_controller():
		try:
			controller, controller_id = mupi_admin.get_controller()
			response = json.dumps(controller, indent=4)
			bad_request = "No controller with id: " + str(controller_id)
			bad_request = json.dumps(bad_request, indent=4) 
			if response == bad_request:
				controller = response
			else:	
				print(response)
				URL = mupi_admin.BASE_URL + "controllers/" + str(controller_id)
				new_controller = input('Type the field to update: {"key":"value",...}: ')
				print(new_controller)
				confirmation = input('Type "y" to confirm your entry: ')
				if confirmation == "y":
					resp = requests.put(URL, headers = headers, data=new_controller)
					controller = json.dumps(resp.json(), indent=4)	
				else:
					controller = "Discarded Operation"
		except ValueError:
			controller = "Incorrect Values"
		return controller

	def delete_controller():
		try:
			controller_id = input('SDN Controller ID: ')
			URL = mupi_admin.BASE_URL + "controllers/" + str(controller_id)
			resp = requests.delete(URL, headers = headers)
			controller = json.dumps(resp.json(), indent=4)
		except:
			controller = "Error"
		return controller

	def delete_controllers():
		URL = mupi_admin.BASE_URL + "controllers"
		try:
			confirmation = input('Type "y" to confirm: ')
			if confirmation == "y":
				resp = requests.delete(URL, headers = headers)
				controller = json.dumps(resp.text, indent=4)	
			else:
				controller = "Discarded Operation"
		except:
			controller = "Error"
		return controller

	def monitor_controllers():
		URL = mupi_admin.BASE_URL + "controllers-table"
		try:
			resp = requests.get(URL, headers = headers)
			controllers = resp.json()
		except:
			controllers = "Error"
		return controllers

	#Print controllers table
	def print_controllers(controller_table):
		print( '{:20} {:25} {:20} {:30} '.format('Description', 'OpenFlow-Version', 'TCP Port', 'IP Address'))
		print( '{:20} {:25} {:20} {:30} '.format('-----------------', '-------------------', '--------------------', '-----------------') )
		for key in controller_table.keys():
			e = controller_table[key]
			print( '{:20} {:25} {:20} {:30} '.format(e['description'], e['openflow_version'], e['tcp_port'], e['ip_address']) )
		print( '{:20} {:25} {:20} {:30} '.format('-----------------', '-------------------', '--------------------', '-----------------') )
		print()


	#FLOWS
	def get_flows():
		try:
			murt_entry_id = input('MURT Entry ID: ')
			URL = mupi_admin.BASE_URL + "flows/" + str(murt_entry_id)
			resp = requests.get(URL, headers = headers)
			flows = resp.json()
		except ValueError:
			flows = "Incorrect ID"
		return flows, murt_entry_id

	def monitor_flows():
		URL = mupi_admin.BASE_URL + "flows"
		try:
			resp = requests.get(URL, headers = headers)
			flows = resp.json()
		except:
			flows = "Error"
		return flows

	#Print flows table
	def print_flows(registered_flows):
		print("REAL TIME FLOWS CONFIGURED IN OVSWITCH")
		print("----------------------------------------------------------------------------------------------------------------------------------------------")
		print( '{:30} {:15} {:30} {:30} {:15}'.format('client_ip', 'downstream_if', 'mcast_group', 'mcast_src_ip', 'upstream_if'))
		print( '{:30} {:15} {:30} {:30} {:15}'.format('-----------------------', '-------------', '-----------------------', '-----------------------', '-------------') )
		for key in registered_flows.keys():
			e = registered_flows[key]
			print( '{:30} {:15} {:30} {:30} {:15}'.format(str(e['client_ip']), str(e['downstream_if']), str(e['mcast_group']), str(e['mcast_src_ip']),  str(e['upstream_if'])) )
		print( '{:30} {:15} {:30} {:30} {:15}'.format('-----------------------', '-------------', '-----------------------', '-----------------------', '-------------') )
		print()

	# Retrieve switching mode configure in the controller
	def get_switching_mode():
	 	URL = mupi_admin.BASE_URL + "switching_mode"
	 	try:
	 		resp = requests.get( URL, headers = headers)
	 		mode = resp.json()
	 	except ValueError:
	 		mode = "Incorrect Mode"
	 	return mode

	# Configure switching mode between: All, Random, Round Robin
	def configure_switching_mode():
	 	URL = mupi_admin.BASE_URL + "switching_mode"
	 	try:
	 		switching_mode_code = input('Switching mode: [A] All (default) | [R] Random: All | [RR] Round Robin:  ')
	 		if switching_mode_code == "R":
	 			switching_mode = "Random"
	 		elif switching_mode_code == "RR":
	 			switching_mode = "Round Robin"
	 		else:
	 			switching_mode = "All"
	 		new_mode = {"switching_mode":switching_mode}
	 		new_mode = json.dumps(new_mode)
	 		resp = requests.post( URL, headers = headers, data=new_mode)
	 		mode = resp.json()
	 	except ValueError:
	 		mode = "Incorrect Mode"
	 	return mode

	# CONTROLLER
	def configure_controller():
		try:
			print("Current Controller: " + str(mupi_admin.IP_CONTROLLER))
			controller_ip = input('Type the IP address of the controller: ')
			try:
				controller_ip = str(IPAddress(controller_ip))
				mupi_admin.IP_CONTROLLER = controller_ip
				mupi_admin.BASE_URL = 'http://' + str(mupi_admin.IP_CONTROLLER) + ':8080/mupi-proxy/'
				controller = {"IP_CONTROLLER": controller_ip}
				controller = json.dumps(controller)
			except:
				controller = "Incorrect IP"
		except ValueError:
			controller = "Incorrect IP"
		return controller



if __name__ == '__main__':
	mupi_admin.main(mupi_admin)