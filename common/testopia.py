#!/usr/bin/python

"""
  Copyright (c) 2008 Novell, Inc.  All Rights Reserved.

  THIS WORK IS AN UNPUBLISHED WORK AND CONTAINS CONFIDENTIAL PROPRIETARY
  AND TRADE SECRET INFORMATION OF NOVELL, INC. ACCESS  TO  THIS  WORK IS
  RESTRICTED TO (I) NOVELL, INC.  EMPLOYEES WHO HAVE A NEED TO  KNOW HOW
  TO  PERFORM  TASKS WITHIN  THE SCOPE  OF  THEIR   ASSIGNMENTS AND (II)
  ENTITIES OTHER  THAN  NOVELL, INC.  WHO  HAVE ENTERED INTO APPROPRIATE
  LICENSE   AGREEMENTS.  NO  PART  OF  THIS WORK MAY BE USED, PRACTICED,
  PERFORMED COPIED, DISTRIBUTED, REVISED, MODIFIED, TRANSLATED, ABRIDGED,
  CONDENSED, EXPANDED, COLLECTED, COMPILED, LINKED,  RECAST, TRANSFORMED
  OR ADAPTED  WITHOUT THE PRIOR WRITTEN CONSENT OF NOVELL, INC.  ANY USE
  OR EXPLOITATION  OF  THIS WORK WITHOUT AUTHORIZATION COULD SUBJECT THE
  PERPETRATOR  TO CRIMINAL AND CIVIL LIABILITY.


Use this class to access Testopia

Example on how to access this library,

from testopia import Testopia

t = Testopia('jdoe@novell.com', 'jdoepassword')
t.testplan_get(10)


To access a different Testopia server, do

t = Testopia('jdoe@novell.com', 'jdoepassword', host='http://myothertestopiaserver')


Note: Python coding style guide does not advocate a method with more than 6-7
arguments. We've done this here with list, create, and update just to help.

Please do not modify this file. Thank you.

-Airald
"""

__author__="Airald Hapairai, Bracken Mosbacker"
__date__="06/12/2008"
__version__="2.0.0"

import xmlrpclib
from types import ListType, DictType, BooleanType, StringType, IntType, LongType
from datetime import datetime, time

VERBOSE=0
DEBUG=0


class TestopiaError(Exception): pass

class Driver(object):

	view_all=True # By default, a list returns at most 25 elements. We force here to see all.

	def __init__(self, username, password, 
				host="apibugzillastage.provo.novell.com", 
				resource="tr_xmlrpc.cgi", port=80, ssl=False):
		"""Initialize the Testopia driver.

		PARAMETERS
		username	(string)	the account to log into Testopia such as jdoe@novell.com,
		password	(string)	the password for the username,
		host		(string)	the URL of the host hosting testopia, optional
		resource	(string)	the XML rpc door, optional
		port		(integer)	the port of the host, optional
		ssl			(boolean)	True if the host protocol is SSL, False otherwise, optional

		Example: t = Testopia('jdoe@novell.com', 'jdoepassword')
		"""
		#self.server = xmlrpclib.ServerProxy("http" + ("", "s")[ssl] +\
		#			"://%s:%s@%s:%d/%s" % (username, password, host, port, resource), verbose = VERBOSE)
		self.server = xmlrpclib.ServerProxy("http" + ("", "s")[ssl] +\
					"://%s:%s@%s/%s" % (username, password, host, resource), verbose = VERBOSE)


	def do_command(self, verb, args):
		"""Submit a command to the server proxy.
		
		PARAMETERS	
		verb	(string)	the xmlrpc verb,
		args	(list)		the argument list,
		"""
		params = ''
		for arg in args:
			params = ("%s" % str(arg), "%s, %s" % (params, str(arg)))[params!='']
		cmd = "self.server." + verb + "(" + params + ")"
		if DEBUG:
			print cmd
		try:
			return eval(cmd)
		except xmlrpclib.Error, e:
			# Don't print out exception. It prints out username, password in clear text!
			#print "Error while executing cmd \'%s\' --> %s" % ( verb + "(" + params + ")", e)
			print "XMLRPC error while executing cmd \'%s\' " % ( verb + "(" + params + ")")


	################################ Testopia #################################
	
	def testopia_api_version(self):
		"""Get the version of the Testopia API currently running on the server
		
		RETURNS
		(float)	The Testopia API version.
		"""
		return self.do_command("Testopia.api_version", [])
	

	################################ Build ####################################

	#Attribute	   Data Type	  Comments	  Create	  Read	  Update
	#build_id	   integer								  X
	#product_id	   integer					  Required	  X		  X
	#name		   string					  Required	  X		  X
	#description   string					  Optional	  X		  X
	#milestone	   string					  Optional	  X	 	  X
	#isactive	   boolean					  Optional	  X 	  X


	def build_get(self, build_id):
		"""Get A Build by ID.

		PARAMETERS
		build_id	(integer)	Must be greater than 0

		RETURNS
		(dictionary)	A dictionary of key/value pairs for the attributes listed above or a
		dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		build_get(10)
		"""
		return self.do_command("Build.get", [self._number_noop(build_id)])

	def build_check_build(self, name, product):
		"""Get a build by name and product specifiers

		 PARAMETERS	  
		 name		(string)			name of the build.
		 product	(integer/string)	Integer: product of the product in the Database
								 		String: Product name

		 RETURNS
		 (dictionary)	Matching Build object dictionary or error if not found.

		"""
		return self.do_command("Build.check_build",
							[self._string_noop(name),
							self._alphanum_no_option(product)])


	def build_create(self, name, product_id, description=None, milestone=None, isactive=None):
		"""Create A New Build.

		PARAMETERS
		name		(string)	required value
		product_id	(integer)	required value
		description	(string)	optional
		milestone	(string)	optional
		isactive	(boolean)	optional

		RETURNS 
		(dictionary)	A dictionary of key/value pairs for the attributes listed above or a
		dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		build_create('New Build', 1, description='description')
		"""
		return self.do_command("Build.create", [self._options_dict(
												self._string_option("name", name),
												self._number_option("product_id", product_id),
												self._string_option("description", description),
												self._string_option("milestone", milestone),
												self._boolean_option("isactive", isactive))])


	def build_update(self, build_id, name=None, description=None, milestone=None, isactive=None):
		"""Update An Existing Build.

		PARAMETERS
		build_id		(integer)	
		name			(string)	optional
		description		(string)	optional
		milestone		(string)	optional
		isactive		(boolean)	optional

		RETURNS 
		(dictionary)	The modified Build on success or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		build_update(10, product_id = 10, isactive = True)
		"""
		return self.do_command("Build.update", [self._number_noop(build_id),
												self._options_dict(
												self._string_option("name", name),
												self._string_option("description", description),
												self._string_option("milestone", milestone),
												self._boolean_option("isactive", isactive))])


	############################## Environment ##################################

	#Attribute		  Data Type	  Comments	  Create	   Read	  Update
	#environment_id	   integer								 X
	#isactive		   integer					  Required	 X		 X
	#name			   string					  Optional	 X		 X
	#product_id		   integer					  Required	 X		 X


	def environment_get(self, environment_id):
		"""Get An Environment by ID
		
		PARAMETERS
		environment_id	(integer)	Must be greater than 0

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above
		or a dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_get(10)
		"""
		return self.do_command("Environment.get", [self._number_noop(environment_id)])

	def environment_check_environment(self, name, product):
		"""Get an environment by name and product specifiers

		 PARAMETERS
		 name		(string)			name of the environment.
		 product	(integer/string)	Integer: product of the product in the Database
								 		String: Product name

		 RETURNS
		 (dict)	Matching environment object hash or a
		 dictionary containing values for the keys, "faultcode" and "faultstring".
		"""
		return self.do_command("Environment.check_environment",
							[self._string_noop(name),
							self._alphanum_no_option(product)])


	def environment_list(self, environment_id=None, environment_id_type=None,
						 isactive=None, isactive_type=None,
						 name=None, name_type=None,
						 product_id=None, product_id_type=None):
		"""Get A List of Environments Based on A Query

		PARAMETERS
		query	(dict)

		RETURNS
		(list/dict)	A list of Environment dictionaries or a dictionary containing values
		for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_list(environment_id=10, name='Updated Environment Name')
		"""
		return self.do_command("Environment.list", [self._options_ne_dict(
												 self._number_option('environment_id', environment_id),
												 self._search_op('environment_id_type', environment_id_type),
												 self._boolean_option('isactive', isactive),
												 self._search_op('isactive_type', isactive_type),
												 self._string_option('name', name),
												 self._search_op('name_type', name_type),
												 self._number_option('product_id', product_id),
												 self._search_op('product_id', product_id_type),
												 self._boolean_option('viewall', self.view_all),
												 )])


	def environment_create(self, product_id, isactive, name=None):
		"""Create A New Environment
		
		PARAMETERS
		product_id	(integer)
		isactive	(boolean)
		name		(string)	optional

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above
		or a dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_create(1, True)
		"""
		return self.do_command("Environment.create", [self._options_dict(
													 self._number_option('product_id', product_id),
													 self._boolean_option('isactive', isactive),
													 self._string_option('name', name)
													 )])


	def environment_update(self, environment_id, name=None, product_id=None, isactive=None):
		"""Update An Existing Environment.

		PARAMETERS
		environment_id		(integer)
		name				(string)
		product_id			(integer)
		isactive			(boolean)

		RETURNS
		(dict)	The modified environment on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_update(10, name='Updated Environment Name')
		"""
		return self.do_command("Environment.update", [self._number_noop(environment_id),
													  self._options_dict(
													  self._string_option('name', name),
													  self._number_option('product_id', product_id),
													  self._boolean_option('isactive', isactive)
													  )])


	def environment_get_runs(self, environment_id):
		"""Get A List of TestRuns For An Existing Environment

		PARAMETERS
		environment_id	(integer)

		RETURNS
		(list/dict)	A list of TestRun objects on success or a dictionary containing
		values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_get_runs(10)
		"""
		return self.do_command("Environment.get_runs", [self._number_noop(environment_id)])
	
	def environment_get_caseruns(self, environment_id):
		"""Returns the list of case-runs that this Environment is used in.

		PARAMETERS
		environment_id	(integer)

		RETURNS
		(list/dict)	A list of case-run objects on success or a dictionary containing
		values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		environment_get_runs(10)
		"""
		return self.do_command("Environment.get_caseruns", [self._number_noop(environment_id)])


	############################## Product ##################################

	#Attribute			 Data Type	  Comments
	#id					integer
	#name				  string
	#description		   string
	#milestone_url		 string
	#disallow_new		  integer
	#votes_per_user		integer
	#max_votes_per_bug	 integer
	#votes_to_confirm	  integer
	#default_milestone	 string
	#classification_id	 integer

	def product_get(self, product_id):
		"""Used to load an existing product from the database.
		
		PARAMETERS
		product_id	(integer)	representing the ID in the database

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a
		dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get(10)
		"""
		return self.do_command("Product.get", [self._number_noop(product_id)])

	def product_check_product(self, name):
		"""Get a product by name

		 PARAMETERS	  
		 name	(string)	name of the product.

		 RETURNS
		 (dict)	Matching product object hash or a dictionary 
		 containing values for the keys, "faultcode" and "faultstring".
		"""
		return self.do_command("Product.check_product",
							[self._string_noop(name)])

	def product_check_category(self, name, product):
		"""Get a category by name and product specifiers

		 PARAMETERS	  
		 name		(string)			name of the category.
		 product	(integer/string)	integer: product of the product in the Database
								 		string: Product name

		 RETURNS
		(dict)	Matching category object hash or a
		 dictionary containing values for the keys, "faultcode" and "faultstring".
		"""
		return self.do_command("Product.check_category",
							[self._string_noop(name),
							self._alphanum_no_option(product)])
		
	def product_get_category(self, category_id):
		"""Used to load an existing category from the database.
		
		PARAMETERS
		category_id		(integer)	representing the ID in the database

		RETURNS
		(dict)	Matching category object hash or a
		dictionary containing values for the keys, "faultcode" and "faultstring".
		 
		EXAMPLES
		product_get_category(10)
		"""
		return self.do_command("Product.get_category", [self._number_noop(category_id)])
		
	def product_check_component(self, name, product):
		"""Get a component by name and product specifiers

		PARAMETERS
		name	(string)			name of the component.
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		 RETURNS
		 (dict)	Matching component object hash or a
		 dictionary containing values for the keys, "faultcode" and "faultstring".

		"""
		return self.do_command("Product.check_component",
							[self._string_noop(name),
							self._alphanum_no_option(product)])
		
	def product_get_component(self, component_id):
		"""Used to load an existing component from the database.
		
		PARAMETERS
		category_id		(integer)	representing the ID in the database

		RETURNS
		(dict)	Matching component object hash or a
		 dictionary containing values for the keys, "faultcode" and "faultstring".
		 
		EXAMPLES
		product_get_component(10)
		"""
		return self.do_command("Product.get_component", [self._number_noop(component_id)])

	def product_get_milestones(self, product_id):
		"""Get a list of milestones for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict)	A list of Milestone dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_milestones(10)
		"""
		return self.do_command("Product.get_milestones", [self._alphanum_no_option(product_id)])
	
	
	def product_get_components(self, product):
		"""Get a list of components for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list)	A list of component dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_components(10)
		"""
		return self.do_command("Product.get_components", [self._alphanum_no_option(product)])

	def product_get_categories(self, product):
		"""Get a list of categories for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict)	A list of category dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_categories(10)
		"""
		return self.do_command("Product.get_categories", [self._alphanum_no_option(product)])
	
	def product_get_builds(self, product):
		"""Get a list of builds for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict)	A list of build dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_builds(10)
		"""
		return self.do_command("Product.get_builds", [self._alphanum_no_option(product)])
	
	def product_get_cases(self, product):
		"""Get a list of cases for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS 
		(list/dict)	A list of case dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_cases(10)
		"""
		return self.do_command("Product.get_cases", [self._alphanum_no_option(product)])
	
	def product_get_environments(self, product):
		"""Get a list of environments for the given Product.

		PARAMETERS
			product	(integer/string)	integer: product of the product in the Database
								 		string: Product name

		RETURNS
		(list/dict)	A list of environment dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_environments(10)
		"""
		return self.do_command("Product.get_environments", [self._alphanum_no_option(product)])
	
	def product_get_plans(self, product):
		"""Get a list of test plans for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name		

		RETURNS
		(list/dict)	A list of test plan dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_plans(10)
		"""
		return self.do_command("Product.get_plans", [self._alphanum_no_option(product)])
	
	def product_get_runs(self, product):
		"""Get a list of test runs for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict)	A list of test run dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_runs(10)
		"""
		return self.do_command("Product.get_runs", [self._alphanum_no_option(product)])
	
	def product_get_tags(self, product):
		"""Get a list of tags for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict)	A list of tag dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		product_get_tags(10)
		"""
		return self.do_command("Product.get_tags", [self._alphanum_no_option(product)])
	
	def product_get_versions(self, product):
		"""Get a list of versions for the given Product.

		PARAMETERS
		product	(integer/string)	integer: product of the product in the Database
								 	string: Product name

		RETURNS
		(list/dict) A list of version dictionaries or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		:product_get_versions(10)
		"""
		return self.do_command("Product.get_versions", [self._alphanum_no_option(product)])

	############################## Tag #######################################

	#Attribute		 Data Type	  Comments
	#tag_id			integer
	#tag_name		  string
	#case_count		integer
	#plan_count		integer
	#run_count		 integer

	############################## TestPlan ##################################

	#Attribute				  Data Type	  Comments				 Create	  Read	Update
	#author_id				  integer								 Required	  X
	#default_product_version	string								  Required	  X	   X
	#creation_date			  string	 Format: yyyy-mm-dd hh:mm:ss				X
	#isactive				   integer								 Optional	  X	   X
	#name					   string								  Required	  X	   X
	#plan_id					integer											   X
	#product_id				 integer								 Required	  X	   X
	#type_id					integer								 Required	  X	   X


	def testplan_get(self, plan_id):
		"""Get A TestPlan by ID.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get(10)
		"""
		return self.do_command("TestPlan.get", [self._number_noop(plan_id)])


	def testplan_list(self, plan_id=None, plan_id_type=None,
					  name=None, name_type=None,
					  type_id=None, type_id_type=None,
					  creation_date=None, creation_date_type=None,
					  default_product_version=None, default_product_version_type=None,
					  author_id=None, author_id_type=None,
					  isactive=None, isactive_type=None,
					  product_id=None, product_id_type=None):
		"""Get A List of TestPlans Based on A Query.

		PARAMETERS
		plan_id							(integer)	Must be greater than 0
		plan_id_type					(string)	valid search operation,
		name							(string)
		name_type						(string)	valid search operation,
		type_id							(integer)
		type_id_type					(string)	valid search operation,
		creation_date					(string)
		creation_date_type				(string)	valid search operation,
		default_product_version			(string)
		default_product_version_type	(string)	valid search operation,
		author_id						(integer)
		author_id_type					(string)	valid search operation,
		isactive						(boolean)
		isactive_type					(string)	valid search operation,
		product_id						(integer)
		product_id_type					(string)	valid search operation,

		RETURNS
		(list/dict)	A list of TestPlan dictionaries or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testplan_list(plan_id=2, planidtype='lessthan')
		"""
		return self.do_command("TestPlan.list", [self._options_ne_dict(
												 self._number_option('plan_id', plan_id),
												 self._search_op('planidtype', plan_id_type),
												 self._string_option('name', name),
												 self._search_op('name_type', name_type),
												 self._number_option('type_id', type_id),
												 self._search_op('type_id', type_id_type),
												 self._datetime_option('creation_date', creation_date),
												 self._search_op('creation_date_type', creation_date_type),
												 self._string_option('default_product_version', default_product_version),
												 self._search_op('default_product_version_type', default_product_version_type),
												 self._number_option('author_id', author_id),
												 self._search_op('author_id', author_id_type),
												 self._boolean_option('isactive', isactive),
												 self._search_op('isactive_type', isactive_type),
												 self._number_option('product_id', product_id),
												 self._search_op('product_id', product_id_type),
												 self._boolean_option('viewall', self.view_all),
												 )])


	def testplan_create(self, name, product_id, type_id, default_product_version, author_id=None, isactive=None):
		"""Create A New TestPlan.

		PARAMETERS
		name						(string)
		product_id					(integer)
		author_id					(integer)
		type_id						(integer)
		default_product_version		(string)
		isactive					(boolean)	optional

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_create('New Plan", 1, 2,'1.0', author_id=4, isactive=True)
		"""
		return self.do_command("TestPlan.create", [self._options_dict(
												self._string_option('name', name),
												self._number_option('product_id', product_id),
												self._number_option('author_id', author_id),
												self._number_option('type_id', type_id),
												self._string_option('default_product_version', default_product_version),
												self._boolean_option('isactive', isactive),
												)])


	def testplan_update(self, plan_id, name, product_id, type_id, product_version, isactive):
		"""Update An Existing TestPlan.

		PARAMETERS
		plan_id				(integer)
		name				(string)
		product_id			(integer)
		type_id				(integer)
		product_version		(string)
		isactive			(boolean)

		Note: plan_id, author_id, and creation_date can not be modified.

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_update(796, name = 'Hello', product_id = 1, type_id = 5, product_version = 'BETA', isactive = True)
		"""
		return self.do_command("TestPlan.update", [self._number_noop(plan_id),
												self._options_dict(
												self._string_option('name', name),
												self._number_option('product_id', product_id),
												self._number_option('type_id', type_id),
												self._string_option('default_product_version', product_version),
												self._boolean_option('isactive', isactive),
												)])


	def testplan_get_categories(self, plan_id):
		"""Get A List of Categories For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Category objects on success or a dictionary containing values
		for the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_categories(10)
		"""
		return self.do_command("TestPlan.get_categories", [self._number_noop(plan_id)])


	def testplan_get_builds(self, plan_id):
		"""Get A List of Builds For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Build objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_builds(10)
		"""
		return self.do_command("TestPlan.get_builds", [self._number_noop(plan_id)])


	def testplan_get_components(self, plan_id):
		"""Get A List of Components For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Component objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_components(10)
		"""
		return self.do_command("TestPlan.get_components", [self._number_noop(plan_id)])


	def testplan_get_test_cases(self, plan_id):
		"""Get A List of Test Cases For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of TestCase objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_test_cases(10)
		"""
		return self.do_command("TestPlan.get_test_cases", [self._number_noop(plan_id)])


	def testplan_get_test_runs(self, plan_id):
		"""Get A List of Test Runs For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of TestRun objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_test_runs(10)
		"""
		return self.do_command("TestPlan.get_test_runs", [self._number_noop(plan_id)])
	
	def testplan_get_change_history(self, plan_id):
		"""Get A List of Changes For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Change objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_change_history(10)
		"""
		return self.do_command("TestPlan.get_change_history", [self._number_noop(plan_id)])


	def testplan_add_tag(self, plan_ids, tags):
		"""Get A List of Test Runs For An Existing Test Plan.

		PARAMETERS   
		plan_ids	(integer/list/string)	An integer or alias representing the ID in the database,
                							a list of plan_ids or aliases, or a string of comma separated plan_ids.
		tags		(string/list)			A single tag, a list of tags, or a comma separated list of tags. 

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_test_runs(10, 'New Tag')
		"""
		return self.do_command("TestPlan.add_tag", [self._alphanumlist_no_option(plan_ids),
													self._alphalist_no_option(tags)])


	def testplan_remove_tag(self, plan_id, tag_name):
		"""Get A List of Test Runs For An Existing Test Plan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0
		tag_name	(string)	Creates tag if it does not exist

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testplan_remove_tag(10, 'New Tag')
		"""
		return self.do_command("TestPlan.remove_tag", [self._number_noop(plan_id),
													   self._string_noop(tag_name)])


	def testplan_get_tags(self, plan_id):
		"""Get a list of tags for the given TestPlan.

		PARAMETERS
		plan_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Tag dictionaries or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testplan_get_tags(10)
		"""
		return self.do_command("TestPlan.get_tags", [self._number_noop(plan_id)])
	
	def testplan_store_text(self, plan_id, text, author_id = None):
		"""Description: Update the document field of a plan.

 		PARAMETERS
		plan_id			(integer)			Must be greater than 0
        text			(string) 			Text for the document. Can contain HTML.
        [author_id]		(integer/string)	(OPTIONAL) The numeric ID or the login of the author. 
                 							 Defaults to logged in user.

 		RETURNS
 		(list)	Empty on success.
		"""
		if author_id:
			return self.do_command("TestPlan.store_text", [self._number_noop(plan_id), self._string_noop(text), self._number_noop(author_id)])
		else:
			return self.do_command("TestPlan.store_text", [self._number_noop(plan_id), self._string_noop(text)])
		
	def testplan_get_text(self, plan_id, version = None):
		"""The associated large text fields: Action, Expected Results, Setup, Breakdown
           for a given version.

 		PARAMETERS
		plan_id		(integer/string)	Must be greater than 0
                    					or a string representing the unique alias for this plan.
		[version]	(integer)			(OPTIONAL) The version of the text you want returned.
                   						Defaults to the latest.

 		RETURNS
 		(dict)	Text fields and values.
		"""
		if version:
			return self.do_command("TestPlan.get_text", [self._number_noop(plan_id), self._number_noop(version)])
		else:
			return self.do_command("TestPlan.get_text", [self._number_noop(plan_id)])


	def testplan_lookup_type_id_by_name(self, name):
		"""Lookup A TestPlan Type ID By Its Name.

		PARAMETERS
		name	(string)	Cannot be null or empty string

		RETURNS
		(integer)	The TestPlan type id for the respective name or 0 if an error occurs.
		
		EXAMPLES
		testplan_lookup_type_id_by_name('Unit')
		"""
		return self.do_command("TestPlan.lookup_type_id_by_name", [self._string_noop(name)])


	def testplan_lookup_type_name_by_id(self, id):
		"""Lookup A TestPlan Type Name By Its ID.

		PARAMETERS
		id		(integer)	Must be greater than 0

		RETURNS
		(string)	The TestPlan type name for the respective id or empty string if an error occurs.
		
		EXAMPLES
		testplan_lookup_type_name_by_id(10)
		"""
		return self.do_command("TestPlan.lookup_type_name_by_id", [self._number_noop(id)])


	############################## TestCase ##################################

	#Attribute		  Data Type			Comments			 Create	  Read	Update
	#alias			  string									Optional	X	   X
	#arguments		  string									Optional	X	   X
	#author_id		  integer								   Required	X
	#canview			integer											   X
	#case_id			integer											   X
	#case_status_id	 integer								   Required	X	   X
	#category_id		integer								   Required	X	   X
	#creation_date	  string			   Format: yyyy-mm-dd			   X
	#										hh:mm:ss
	#default_tester_id  integer								   Optional	X
	#isautomated		integer								   Required	X	   X
	#plans			  List of TestPlan									  X
	#				   dictionaries
	#priority_id		integer								   Optional	X	   X
	#requirement		string									Optional	X	   X
	#script			 string									Optional	X	   X
	#summary			string									Required	X	   X
	#sortkey			integer								   Optional	X	   X
	#estimated_time	 string			   Format: hh:mm:ss	 Optional	X	   X


	def testcase_get(self, case_id):
		"""Get A TestCase by ID.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_get(1)
		"""
		return self.do_command("TestCase.get", [self._number_noop(case_id)])


	def testcase_list(self, case_id=None, case_id_type=None,
					  alias=None, alias_type=None,
					  arguments=None, arguments_type=None,
					  author_id=None, author_id_type=None,
					  canview=None, canview_type=None,
					  case_status_id=None, case_status_id_type=None,
					  category_id=None, category_id_type=None,
					  creation_date=None, creation_date_type=None,
					  default_tester_id=None, default_tester_id_type=None,
					  isautomated=None, isautomated_type=None,
					  plans=None,
					  priority_id=None, priority_id_type=None,
					  requirement=None, requirement_type=None,
					  script=None, script_type=None,
					  sortkey=None, sortkey_type=None,
					  summary=None, summary_type=None,
					  estimated_time=None, estimated_time_type=None,
					  run_id=None, run_id_type=None):
		"""Get A List of TestCases Based on A Query.

		PARAMETERS
		case_id					(integer)				Must be greater than 0
		case_id_type			(valid search option)	optional
		alias					(string)				optional
		alias_type				(valid search option)	optional
		arguments				(string)				optional
		arguments_type			(valid search option)	optional
		author_id				(integer)				optional
		author_id_type			(valid search option)	optional
		canview					(integer)				optional
		canview_type			(valid search option)	optional
		case_status_id			(integer)				optional
		case_status_id_type		(valid search option)	optional
		category_id				(integer)				optional
		category_id_type		(valid search option)	optional
		creation_date			(string)				Format: yyyy-mm-dd  hh:mm:ss
		creation_date_type		(valid search option)	optional
		default_tester_id		(integer)				optional
		default_tester_id_type	(valid search option)	optional
		isautomated				(boolean)				optional
		isautomated_type		(valid search option)	optional
		plans					(list)					List of TestPlan dictionaries
		priority_id				(integer)				optional
		priority_id_type		(valid search option)	optional
		requirement				(string)				optional
		requirement_type		(valid search option)	optional
		script					(string)				optional
		script_type				(valid search option)	optional
		summary					(string)				optional
		summary_type			(valid search option)	optional
		sortkey					(integer)				optional
		sortkey_type			(valid search option) 	optional
		estimated_time			(string)				Format: hh:mm:ss, optional
		estimated_time_type		(valid search option)	optional
		run_id					(integer)				optional
		run_id_typevalid		(valid search option)	optional

		RETURNS
		(list/dict)	A list of TestCase dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_list(case_id=20, case_id_type='lessthan')
		"""
		return self.do_command("TestCase.list", [self._options_ne_dict(
				   self._number_option('case_id', case_id), self._search_op('caseidtype', case_id_type),
				   self._string_option('alias', alias), self._search_op('alias_type', alias_type),
				   self._string_option('arguments', arguments), self._search_op('arguments_type', arguments_type),
				   self._number_option('author_id', author_id), self._search_op('author_id_type', author_id_type),
				   self._number_option('canview', canview), self._search_op('canview_type', canview_type),
				   self._number_option('case_status_id', case_status_id), self._search_op('case_status_id_type', case_status_id_type),
				   self._number_option('category_id', category_id), self._search_op('category_id_type', category_id_type),
				   self._datetime_option('creation_date', creation_date), self._search_op('creation_date_type', creation_date_type),
				   self._number_option('default_tester_id', default_tester_id), self._search_op('default_tester_id_type', default_tester_id_type),
				   self._boolean_option('isautomated', isautomated), self._search_op('isautomated_type', isautomated_type),
				   self._list_dict_op('plans', plans),
				   self._number_option('priority_id', priority_id), self._search_op('priority_id_type', priority_id_type),
				   self._string_option('requirement', requirement), self._search_op('requirement_type', requirement_type),
				   self._string_option('script', script), self._search_op('script_type', script_type),
				   self._string_option('summary', summary), self._search_op('summary_type', summary_type),
				   self._number_option('sortkey', sortkey), self._search_op('sortkey_type', sortkey_type),
				   self._time_option('estimated_time', estimated_time), self._search_op('estimated_time_type', estimated_time_type),
				   self._number_option('run_id', run_id), self._search_op('runidtype', run_id_type),
				   self._boolean_option('viewall', self.view_all),
				   )])


	def testcase_create_batch(self, values):
		"""
		Description: Creates a new Test Case object and stores it in the database.

 		PARAMETERS      
 		values	(list/dictionary)	A reference to a dictionary or list of dictionaries with keys and values  
              						matching the fields of the test case to be created.
              	
        RETURNS     
		(list/dictionary)	The newly created object dictionary if a single case was created, or
        a list of objects if more than one was created. If any single case threw an 
        error during creation, a dictionary with an ERROR key will be set in its place.
		"""
		return self.do_command("TestCase.create", [values])
	
	def testcase_create(self, status, category, priority, summary, plans, default_tester=None,
						estimated_time=None, isautomated=None, sortkey=None, script=None,
						arguments=None, requirement=None, alias=None, action=None, 
						effect=None, setup=None, breakdown=None, dependson=None, blocks=None, 
						tags=None,bugs=None, components=None):
		"""Create A New TestCase.

		PARAMETERS
		status			(integer/string)
		category		(integer/string)
		priority		(integer/string)
		summary			(string)
		plans			(list)	 			plan ids
		OPTIONAL PARAMETERS
		default_tester	(integer/string)
		estimated_time	(string)			Format: hh:mm:ss, optional,
		isautomated		(boolean)
		sortkey			(integer)
		script			(string)
		arguments		(string)
		requirement		(string)
		alias			(string)
		action			(string)
		effect			(string)	
		setup			(string)	
		breakdown		(string)	
		dependson		(list/string)
		blocks			(list/string)
		tags			(list/string)
		bugs			(list/string)
		components		(list/string)

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_create('New', 3, 1, 'Tests something', [123], alias='anotherName', isautomated=True)
		"""
		return self.do_command("TestCase.create", [self._options_dict(
				   self._alphanum_option('status', status),
				   self._alphanum_option('category', category),
				   self._alphanum_option('priority', priority),
				   self._string_option('summary', summary),
				   self._list_option('plans', plans),
				   self._alphanum_option('default_tester', default_tester),
				   self._string_option('estimated_time', estimated_time),
				   self._boolean_option('isautomated', isautomated),
				   self._number_option('sortkey', sortkey),
				   self._string_option('script', script),
				   self._string_option('arguments', arguments),
				   self._string_option('requirement', requirement),
				   self._string_option('alias', alias),
				   self._string_option('action', action),
				   self._string_option('effect', effect),
				   self._string_option('setup', setup),
				   self._string_option('breakdown', breakdown),
				   self._alphalist_option('dependson', dependson),
				   self._alphalist_option('blocks', blocks),
				   self._alphalist_option('tags', tags),
				   self._alphalist_option('bugs', bugs),
				   self._alphalist_option('components', components)
				   )])


	def testcase_update_batch(self, ids, values):
		"""
		Description: Updates the fields of the selected case or cases.

	 	PARAMETERS      
	 	ids		(integer/string/list)	integer: A single TestCase ID.
	                     				string: A comma separates string of TestCase IDs for batch processing.
	                     				list: An list of case IDs for batch mode processing
	    values	(dict)	dictoinary with keys matching TestCase fields and the new values 
	              		to set each field to.
	
	 	RETURNS  
 		(dict/list)	In the case of a single case it is returned. If a 
      	list was passed, it returns a list of case dictionaries. If the
      	update on any particular case failed, the has will contain a 
      	ERROR key and the message as to why it failed.
		"""
		return self.do_command("TestCase.update", [self._alphanumlist_no_option(ids), values])

	def testcase_update(self, ids, status=None, category=None, priority=None, summary=None, 
					   	default_tester=None, estimated_time=None, isautomated=None, sortkey=None, script=None,
						arguments=None, requirement=None, alias=None, dependson=None, blocks=None):
		"""Update An Existing TestCase.
		
		PARAMETERS
		ids		(integer/string/list)	integer: A single TestCase ID.
	                     				string: A comma separates string of TestCase IDs for batch processing.
	                     				list: An list of case IDs for batch mode processing
		OPTIONAL PARAMETERS                     				
		status				(integer/string)
		category			(integer/string)
		priority			(integer/string)
		summary				(string)
		default_tester		(integer/string)
		estimated_time		(string)	Format: hh:mm:ss
		isautomated			(boolean)
		sortkey				(integer)
		script				(string)
		arguments			(string)
		requirement			(string)
		alias				(string)
		dependson			(list/string)
		blocks				(list/string)

		RETURNS
		(dict)	The modified TestCase on success or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_update(20, summary="Updated Summary")
		"""
		return self.do_command("TestCase.update", [self._alphanumlist_no_option(ids), 
				   self._options_dict(
				   self._alphanum_option('status', status),
				   self._alphanum_option('category', category),
				   self._alphanum_option('priority', priority),
				   self._string_option('summary', summary),
				   self._alphanum_option('default_tester', default_tester),
				   self._string_option('estimated_time', estimated_time),
				   self._boolean_option('isautomated', isautomated),
				   self._number_option('sortkey', sortkey),
				   self._string_option('script', script),
				   self._string_option('arguments', arguments),
				   self._string_option('requirement', requirement),
				   self._string_option('alias', alias),
				   self._alphalist_option('dependson', dependson),
				   self._alphalist_option('blocks', blocks),
				   )])

	
	def testcase_get_text(self, case_id, version = None):
		"""Description: The associated large text fields: Action, author, effect, version

 		PARAMETERS
		case_id		(integer)	Must be greater than 0
		version		(integer)	(OPTIONAL) The version of the text you want returned.
                   				Defaults to the latest.

 		RETURNS
 		(dict)	Text fields and values.
		"""
		if version:
			return self.do_command("TestCase.get_text", [self._number_noop(case_id), self._number_noop(version)])
		else:
			return self.do_command("TestCase.get_text", [self._number_noop(case_id)])


	def testcase_store_text(self, case_id, action, effect, setup, breakdown, author_id=None):
		"""Description: Update the large text fields of a case.

		PARAMETERS
		case_id								(integer)			Must be greater than 0
		action, effect, setup, breakdown	(string) 			Text for these fields.
		[author_id]							(integer/string)	(OPTIONAL) The numeric ID or the login of the author. 
		                  										Defaults to logged in user

		RETURNS
		(integer/dict)	The new document version on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_store_text(1,'New Setup', 'New Breakdown', 'New Action', 'New Expected results', 1)
		"""
		return self.do_command("TestCase.store_text", [self._number_noop(case_id), # This is the proper order
													   self._string_noop(action),
													   self._string_noop(effect),
													   self._string_noop(setup),
													   self._string_noop(breakdown),
													   self._number_noop(author_id)
													   ])


	
	def testcase_attach_bug(self, case_id, bug_id):
		"""Add a bug to the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0
		bug_id		(integer)

		RETURNS
		(list/dict)	An empty list on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_attach_bug(1, 2)
		"""
		return self.do_command("TestCase.attach_bug", [self._number_noop(case_id),
														  self._number_noop(bug_id)])


	def testcase_detach_bug(self, case_id, bug_id):
		"""Remove a bug from the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0
		bug_id		(integer)

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_detach_bug(1, 2)
		"""
		return self.do_command("TestCase.detach_bug", [self._number_noop(case_id),
															 self._number_noop(bug_id)])
	
	
	def testcase_get_bugs(self, case_id):
		"""Get a list of bugs for the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Bug dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_get_bugs(1)
		"""
		return self.do_command("TestCase.get_bugs", [self._number_noop(case_id)])


	def testcase_add_component(self, case_id, component_id):
		"""Add a component to the given TestCase.

		PARAMETERS
		case_id			(integer)	Must be greater than 0
		component_id	(integer)

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_add_component(1, 2)
		"""
		return self.do_command("TestCase.add_component", [self._number_noop(case_id),
														  self._number_noop(component_id)])


	def testcase_remove_component(self, case_id, component_id):
		"""Remove a component from the given TestCase.

		PARAMETERS
		case_id			(integer)	Must be greater than 0
		component_id	(integer)

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_remove_component(1, 2)
		"""
		return self.do_command("TestCase.remove_component", [self._number_noop(case_id),
															 self._number_noop(component_id)])


	def testcase_get_components(self, case_id):
		"""Get a list of components for the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Component dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_get_components(1)
		"""
		return self.do_command("TestCase.get_components", [self._number_noop(case_id)])


	def testcase_add_tag(self, case_id, tags):
		"""Description: Add one or more tags to the selected test cases.

 		PARAMETERS
 		case_ids	(integer/list/string)	An integer or alias representing the ID in the database,
                  							a list of case_ids or aliases, or a string of comma separated case_ids.
        tags		(string/list)			A single tag, an array of tags,
                  							or a comma separated list of tags. 

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testcase_add_tag(10, 'New Tag')
		testcase_add_tag(10, ['tag1', 'tag2'])
		"""
		return self.do_command("TestCase.add_tag", [self._alphanumlist_no_option(case_id),
													self._alphalist_no_option(tags)])


	def testcase_remove_tag(self, case_id, tag_name):
		"""Remove a tag from the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0
		tag_name	(string)

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the keys,
		"faultCode" and "faultString".
		
		EXAMPLES
		testcase_remove_tag(10, 'Old Tag')
		"""
		return self.do_command("TestCase.remove_tag", [self._number_noop(case_id),
													   self._string_noop(tag_name)])


	def testcase_get_tags(self, case_id):
		"""Get a list of tags for the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Tag dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_get_tags(10)
		"""
		return self.do_command("TestCase.get_tags", [self._number_noop(case_id)])
	
	
	def testcase_get_change_history(self, case_id):
		"""Get A List of Changes For An Existing Test Case.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Change objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testcase_get_change_history(10)
		"""
		return self.do_command("TestCase.get_change_history", [self._number_noop(case_id)])


	def testcase_get_case_run_history(self, case_id):
		"""Get A List of case run Changes For An Existing Test Case.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of Change objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testcase_get_case_run_history(10)
		"""
		return self.do_command("TestCase.get_case_run_history", [self._number_noop(case_id)])


	def testcase_calculate_average_time(self, case_id):
		"""Returns an average time for completion accross all runs.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(string)	Time in "HH:MM:SS" format.
		
		EXAMPLES
		testcase_calculate_average_time(10)
		"""
		return self.do_command("TestCase.calculate_average_time", [self._number_noop(case_id)])


	def testcase_lookup_priority_id_by_name(self, name):
		"""Lookup A TestCase Priority ID By Its Name.

		PARAMETERS
		name	(string)	Cannot be null or empty string

		RETURNS
		(integer)	The TestCase priority id for the respective name or 0 if an error occurs.
		
		EXAMPLES
		testcase_lookup_priority_id_by_name('Name')
		"""
		return self.do_command("TestCase.lookup_priority_id_by_name", [self._string_noop(name)])


	def testcase_lookup_priority_name_by_id(self, id):
		"""Lookup A TestCase Category Name By Its ID.

		PARAMETERS
		id		(integer)	Must be greater than 0

		RETURNS
		(string)	The TestCase priority name for the respective id or empty string if an error occurs.
		
		EXAMPLES
		testcase_lookup_priority_name_by_id(10)
		"""
		return self.do_command("TestCase.lookup_priority_name_by_id", [self._number_noop(id)])


	def testcase_lookup_status_id_by_name(self, name):
		"""Lookup A TestCase Status ID By Its Name.

		PARAMETERS
		name	(string)	Cannot be null or empty string

		RETURNS
		(integer)	The TestCase status id for the respective name or 0 if an error occurs.
		
		EXAMPLES
		testcase_lookup_status_id_by_name('Name')
		"""
		return self.do_command("TestCase.lookup_status_id_by_name", [self._string_noop(name)])


	def testcase_lookup_status_name_by_id(self, id):
		"""Lookup A TestCase Category Name By Its ID.

		PARAMETERS
		id		(integer)	Must be greater than 0

		RETURNS
		(string)	The TestCase status name for the respective id or empty string if an error occurs.
		
		EXAMPLES
		testcase_lookup_status_name_by_id(10)
		"""
		return self.do_command("TestCase.lookup_status_name_by_id", [self._number_noop(id)])


	def testcase_link_plan(self, case_ids, plan_ids):
		"""Link A TestPlan To An Existing TestCase.

		PARAMETERS
		case_ids	(integer/list/string)	An integer or alias representing the ID in the database,
                  	 						a list of case_ids or aliases, or a string of comma separated case_ids.
		plan_ids	(integer/list/string)	An integer or alias representing the ID in the database,
                  	 						a list of plan_ids, or a string of comma separated plan_ids.

		RETURNS
		(list/dict)	Empty list or a dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_link_plan(10, [3,4])
		"""
		return self.do_command("TestCase.link_plan", [self._alphanumlist_no_option(case_ids),
																	 self._alphanumlist_no_option(plan_ids)])

	def testcase_unlink_plan(self, case_id, plan_id):
		"""Unlink A TestPlan From An Existing TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0
		plan_id		(integer)

		RETURNS
		(list/dict)	A list of TestPlan dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_unlink_plan(10)
		"""
		return self.do_command("TestCase.unlink_plan", [self._number_noop(case_id),
														self._number_noop(plan_id)])
		
	def testcase_get_plans(self, case_id):
		"""Get a list of tags for the given TestCase.

		PARAMETERS
		case_id		(integer)	Must be greater than 0

		RETURNS
		(list/dict)	A list of TestPlan dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testcase_get_tags(10)
		"""
		return self.do_command("TestCase.get_plans", [self._number_noop(case_id)])
	
	
	def testcase_add_to_run(self, case_ids, run_ids):
		"""Add one or more cases to the selected test runs.

		PARAMETERS
		case_ids	(integer/list/string)	An integer or alias representing the ID in the database,
                  	 						a list of case_ids or aliases, or a string of comma separated case_ids.
		run_ids		(integer/list/string) 	An integer representing the ID in the database
                  							a list of IDs, or a comma separated list of IDs. 

		RETURNS
		(list/dict)	Empty list or a dictionary containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testcase_add_to_run(10, [3,4])
		"""
		return self.do_command("TestCase.add_to_run", [self._alphanumlist_no_option(case_ids),
																	 self._alphanumlist_no_option(run_ids)])


	############################## TestRun ##################################

	#Attribute		   Data Type		 Comments	  Creation	   Read	  Update
	#build_id			integer						 Required	   X		 X
	#environment_id	  integer						 Required	   X		 X
	#manager_id		  integer						 Required	   X		 X
	#notes			   string						  Optional	   X		 X
	#plan				TestPlan hashmap							   X
	#plan_id			 integer						 Required	   X
	#plan_text_version   integer						 Required	   X		 X
	#product_version	 integer						 Optional	   X		 X
	#run_id			  integer										X
	#start_date		  string	 Format: yyyy-mm-dd hh:mm:ss		 X
	#stop_date		   string	 Format: yyyy-mm-dd hh:mm:ss		 X
	#summary			 string						  Required	   X		 X


	def testrun_get(self, run_id):
		"""Get A TestRun by ID.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_get(10)
		"""
		return self.do_command("TestRun.get", [self._number_noop(run_id)])


	def testrun_list(self, run_id=None, run_id_type=None,
					 build_id=None, build_id_type=None,
					 environment_id=None, environment_id_type=None,
					 manager_id=None, manager_id_type=None,
					 notes=None, notes_type=None,
					 plan=None, plan_type=None,
					 plan_id=None, plan_id_type=None,
					 plan_text_version=None, plan_text_version_type=None,
					 product_version=None, product_version_type=None,
					 start_date=None, start_date_type=None,
					 stop_date=None, stop_date_type=None,
					 summary=None, summary_type=None):
		"""Get A List of TestRuns Based on A Query.

		OPTIONAL PARAMETERS
		run_id					(integer)				Must be greater than 0.
		run_id_type				(valid search option)
		build_id				(integer)
		build_id_type			(valid search option)
		environment_id			(integer)
		environment_id_type		(valid search option)
		manager_id				(integer)
		manager_id_type			(valid search option)
		notes					(string)
		notes_type				(valid search option)
		plan					(dict)					TestPlan object
		plan_id					(integer)
		plan_id_type			(valid search option)	
		plan_text_version		(integer)
		plan_text_version_type	(valid search option)	
		product_version			(integer)
		product_version_type	(valid search option)	
		start_date				(string)				Format: yyyy-mm-dd hh:mm:ss
		start_date_type			(valid search option)	
		stop_date				(string)				Format: yyyy-mm-dd hh:mm:ss
		stop_date_type			(valid search option)
		summary					(string)
		summary_type			(valid search option)

		RETURNS
		(list/dict)	A list of TestCase dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testrun_list(run_id=20, run_id_type='lessthan')
		"""
		return self.do_command("TestRun.list", [self._options_ne_dict(
				   self._number_option('run_id', run_id), self._search_op('runid_type', run_id_type),
				   self._number_option('build_id', build_id), self._search_op('build_id_type', build_id_type),
				   self._number_option('environment_id', environment_id), self._search_op('environment_id_type', environment_id_type),
				   self._number_option('manager_id', manager_id), self._search_op('manager_id_type', manager_id_type),
				   self._string_option('notes', notes), self._search_op('notes_type', notes_type),
				   self._list_dict_op('plan', plan),
				   self._number_option('plan_id', plan_id), self._search_op('planid_type', plan_id_type),
				   self._string_option('plan_text_version', plan_text_version), self._search_op('plan_text_version_type', plan_text_version_type),
				   self._number_option('product_version', product_version), self._search_op('product_version_type', product_version_type),
				   self._datetime_option('start_date', start_date), self._search_op('start_date_type', start_date_type),
				   self._datetime_option('stop_date', stop_date), self._search_op('stop_date_type', stop_date_type),
				   self._string_option('summary', summary), self._search_op('summary_type', summary_type),
				   self._boolean_option('viewall', self.view_all),
				   )])


	def testrun_create(self, plan_id, environment, build, manager, summary, product_version=None, 
					plan_text_version=None, notes=None, status=None):
		"""Create A New TestRun.

		PARAMETERS
		plan_id				(integer)			ID of test plan   
		environment			(integer/string)	ID or Name of Environment
		build				(integer/string)	ID or Name of Build
		manager				(integer/string)	ID or Login of run manager
		summary				(string)
		
		OPTIONAL PARAMETERS
		product_version		(string)
		plan_text_version	(integer)
		notes				(string)
		status				(integer) 	0 STOPPED, 1 RUNNING (default)

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_create(1, 1, 1, 1, 'Summary', notes="Some notes")
		"""
		return self.do_command("TestRun.create", [self._options_dict(
				   self._number_option('plan_id', plan_id),
				   self._alphanum_option('environment', environment),
				   self._alphanum_option('build', build),
				   self._alphanum_option('manager', manager),
				   self._number_option('plan_text_version', plan_text_version),
				   self._string_option('summary', summary),
				   self._string_option('notes', notes),
				   self._string_option('product_version', product_version),
				   self._number_option('status', status)
				   )])


	def testrun_update(self, run_id, plan_id=None, build=None, environment=None,
					   manager=None, plan_text_version=None, summary=None,
					   notes=None, product_version=None, status=None):
		"""Update An Existing TestRun.

		PARAMETERS
		run_id				(integer)	Must be greater than 0.
		OPTIONAL PARAMETERS
		plan_id				(integer)
		build				(integer/string)
		environment			(integer/string)
		manager				(integer/string)
		plan_text_version	(integer)
		summary				(string)
		notes				(string)
		product_version		(string)
		status				(integer)	

		RETURNS
		(dict)	The modified TestRun on success or a dictionary containing values for
		the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_update(1, summare="New summary")
		"""
		return self.do_command("TestRun.update", [run_id, self._options_dict(
				   self._number_option('plan_id', plan_id),
				   self._alphanum_option('build', build),
				   self._alphanum_option('environment', environment),
				   self._alphanum_option('manager', manager),
				   self._number_option('plan_text_version', plan_text_version),
				   self._string_option('summary', summary),
				   self._string_option('notes', notes),
				   self._string_option('product_version', product_version),
				   self._number_option('status', status)
				   )])


	def testrun_get_test_cases(self, run_id):
		"""Get A List of TestCases For An Existing Test Run.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of TestCase objects on success or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_get_test_cases(10)
		"""
		return self.do_command("TestRun.get_test_cases", [self._number_noop(run_id)])


	def testrun_get_test_case_runs(self, run_id):
		"""Get A List of TestCase Runs For An Existing Test Run.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of TestCaseRun objects on success or a dictionary
		containing values for the keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_get_test_case_runs(10)
		"""
		return self.do_command("TestRun.get_test_case_runs", [self._number_noop(run_id)])


	def testrun_get_test_plan(self, run_id):
		"""Get A TestPlan For An Existing Test Run.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(dict)	A TestPlan object on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_get_plan(10)
		"""
		return self.do_command("TestRun.get_test_plan", [self._number_noop(run_id)])


	def testrun_add_tag(self, run_ids, tags):
		"""Add a tag to the given TestRun.

		PARAMETERS
		run_ids		(integer/list/string)	An integer or alias representing the ID in the database,
                  							a list of run_ids or aliases, or a string of comma separated run_ids.
       tags			(string/list)			A single tag, an list of tags,
                  							or a comma separated list of tags. 

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_add_tag([10,11], ["Tag1", "tag2"])
		"""
		return self.do_command("TestRun.add_tag", [self._alphanumlist_no_option(run_ids),
													self._alphalist_no_option(tags)])


	def testrun_remove_tag(self, run_id, tag_name):
		"""Remove a tag from the given TestRun.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.
		tag_name	(string)

		RETURNS
		(integer/dict)	The integer , 0, on success or a dictionary containing values for the
		keys, "faultcode" and "faultstring".
		
		EXAMPLES
		testrun_remove_tag(10, "Tag")
		"""
		return self.do_command("TestRun.remove_tag", [self._number_noop(run_id),
													  self._string_noop(tag_name)
													  ])


	def testrun_get_tags(self, run_id):
		"""Get a list of tags for the given TestRun.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of Tag dictionaries or a dictionary containing values for the keys,
		"faultcode" and "faultstring".
		
		EXAMPLES
		testrun_get_tags(10)
		"""
		return self.do_command("TestRun.get_tags", [self._number_noop(run_id)])
	
	def testrun_get_change_history(self, run_id):
		"""Get A List of Changes For An Existing Test Run.

		PARAMETERS
		run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of Change objects on success or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testrun_get_change_history(10)
		"""
		return self.do_command("TestRun.get_change_history", [self._number_noop(run_id)])
	
	
	def testrun_get_completion_report(self, runs):
		"""Get a report of the current status of the selected runs combined.

		PARAMETERS
		runs	(integer/list/string)	An integer representing the ID in the database
                    					a list of integers or a comma separated list of integers.

		RETURNS
		(dict)	A dictionary containing counts and percentages of the combined totals of 
        case-runs in the run. Counts only the most recently statused case-run 
        for a given build and environment. 
                
        EXAMPLES
        testrun_get_completion_report(10)
		testrun_get_completion_report([1,2,3])
		"""
		return self.do_command("TestRun.get_completion_report", [self._alphanumlist_no_option(runs)])


	def testrun_lookup_environment_id_by_name(self, name):
		"""Lookup A TestRun Environment ID By Its Name.

		PARAMETERS
		name	(string)

		RETURNS
		(integer)	The TestRun environment id for the respective name or 0 if an error occurs.
		
		EXAMPLES
		testrun_lookup_environment_id_by_name("Name")
		"""
		return self.do_command("TestRun.lookup_environment_id_by_name", [self._string_noop(name)])


	def testrun_lookup_environment_name_by_id(self, id):
		"""Lookup A TestRun Environment Name By Its ID.

		PARAMETERS
		id		(integer)	Must be greater than 0.

		RETURNS
		(string)	The TestRun environment name for the respective id or empty string if an error occurs.
		
		EXAMPLES
		testrun_lookup_environment_name_by_id(10)
		"""
		return self.do_command("TestRun.lookup_environment_name_by_id", [self._number_noop(id)])


	############################## TestCaseRun ##################################

	#Attribute		   Data Type	  Comments	  Create	   Read  Update
	#assignee			integer		ID value	  Required	 X	 X
	#build_id			integer					  Required	 X	 X
	#canview			 integer								   X
	#case_id			 integer					  Required	 X
	#case_run_id		 integer								   X
	#case_run_status_id  integer								   X
	#case_text_version   integer					  Required	 X
	#close_date		  string	 Format: yyyy-mm-dd hh:mm:ss	X
	#environment_id	  integer					  Required	 X
	#iscurrent		   integer								   X
	#notes			   string					   Optional	 X	 X
	#run_id			  integer					  Required	 X
	#sortkey			 integer								   X
	#testedby			integer		ID value				   X


	def testcaserun_get(self, case_run_id):
		"""Get A TestCaseRun by ID.

		PARAMETERS
		case_run_id		(integer)	Must be greater than 0.

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_get(10)
		"""
		return self.do_command("TestCaseRun.get", [self._number_noop(case_run_id)])
	
	def testcaserun_get_alt(self, run_id, case_id, build_id, environment_id):
		"""Get a testCaseRun by run_id, case_id, build_id, environment_id 

		PARAMETERS
		run_id			(integer)			Test Run Number    
		case_id			(integer/string)	ID or alias of test case 
		build_id		(integer/string)	ID or name of a Build in plan's product    
		environment_id	(integer/string)	ID or name of an Environment in plan's product

		RETURNS
		(dict)	A dictionary of key/value pairs for the attributes listed above on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_get_alt(1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.get", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id)
				   ])		


	def testcaserun_list(self, andor=None, assignee=None,
						 assignee_type=None, build=None,
						 build_id=None, case_id=None,
						 case_run_status=None, case_run_status_id=None,
						 case_summary=None, case_summary_type=None,						 
						 category=None, category_id=None,
						 component=None, environment=None,
						 environment_id=None, isactive=None,
						 isautomated=None, milestone=None,
						 notes=None, notes_type=None,						 
						 plan_id=None, priority=None,
						 priority_id=None, product=None,
						 product_id=None, requirement=None,
						 requirement_type=None,
						 run_id=None, run_product_version=None,						 
						 run_status=None, tags=None,
						 tags_type=None, testedby=None,
						 testedby_type=None):
		"""Get A List of TestCaseRuns Based on A Query.

		OPTIONAL PARAMETERS
		andor				(integer)		1: Author AND tester, 0: OR 
		assignee			(string)		A bugzilla login (email address)
		assignee_type		(integer)		select from email_variants
		build				(string)	
		build_id			(integer)	
		case_id				(list/integer) 
		case_run_status		(string)	
		case_run_status_id	(integer)	
		case_summary		(string)
		case_summary_type	(integer)		select from query_variants	
		category			(string)		Category Name
		category_id			(integer)	
		component			(string)		Component Name  
		environment			(string)
		environment_id		(integer)
		isactive			(integer)		0: Only show current 1: show all
		isautomated			(integer)		1: true 0: false 
		milestone			(string)	
		notes				(string)
		notes_type			(integer)		select from query_variants		
		plan_id				(list/integer) 
		priority			(string)	
		priority_id			(integer)	
		product				(string)	
		product_id			(integer)	
		requirement			(string)	
		requirement_type	(integer)		select from query_variants
		run_id				(list/integer) 		
		run_product_version	(string)		
		run_status			(integer)		1: RUNNING 0: STOPPED
		tags				(string)	
		tags_type			(integer)		select from tag_variants   
		testedby			(string)		A bugzilla login (email address) 
		testedby_type		(integer)		select from email_variants  

		RETURNS
		(list/dict)	A list of TestCaseRun dictionaries or a dictionary containing values for
		the keys on success; on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_list(run=1)
		"""
		return self.do_command("TestCaseRun.list", [self._options_ne_dict(
				   self._number_option('andor', andor), self._string_option('assignee', assignee),
				   self._search_op('assignee_type', assignee_type), self._string_option('build', build),
				   self._number_option('build_id', build_id), self._numlist_option('case_id', case_id),
				   self._string_option('case_run_status', case_run_status), self._number_option('case_run_status_id', case_run_status_id),
				   self._string_option('case_summary', case_summary), self._search_op('case_summary_type', case_summary_type),				   
				   self._string_option('category', category), self._number_option('category_id', category_id),
				   self._string_option('component', component), self._string_option('environment', environment),
				   self._number_option('environment_id', environment_id), self._boolean_option('isactive', isactive),
				   self._boolean_option('isautomated', isautomated), self._string_option('milestone', milestone),
				   self._string_option('notes', notes), self._number_option('environment_id', environment_id),				   
				   self._numlist_option('plan_id', plan_id), self._string_option('priority', priority),
				   self._number_option('priority_id', priority_id), self._string_option('product', product),
				   self._number_option('product_id', product_id), self._string_option('requirement', requirement),
				   self._search_op('requirement_type', requirement_type), self._numlist_option('run_id', run_id),				   
				   self._number_option('run_product_version', run_product_version), self._number_option('run_status', run_status),
				   self._string_option('tags', tags), self._search_op('tags_type', tags_type),
				   self._string_option('testedby', testedby), self._search_op('testedby_type', testedby_type)
				   )])


	def testcaserun_create(self, run_id, case_id, build, environment,
						   assignee=None, status=None, case_run_status_id=None, case_text_version=None, 
						   notes=None, sortkey=None):
		"""Create A New TestCaseRun.

		PARAMETERS
		run_id				(integer)			Test Run Number    
		case_id				(integer/string)	ID or alias of test case 
		build				(integer/string)	ID or name of a Build in plan's product    
		environment			(integer/string)	ID or name of an Environment in plan's product 
		OPTIONAL PARAMETERS
		assignee			(integer/string)	Defaults to test case default tester
		status			 	(string)			Valid: IDLE, PASSED, FAILED, RUNNING, PAUSED, BLOCKED
		case_run_status_id 	(integer)			Valid: 1 (IDLE), 2 (PASSED), 3 (FAILED), 4 (RUNNING), 5 (PAUSED), 6 (BLOCKED)
		case_text_version	(integer)
		notes				(string)
		sortkey				(integer)

		RETURNS
		(dict)	The newly created object dictionary. on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_create(1, 1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.create", [self._options_dict(
				   self._number_option('run_id', run_id),
				   self._number_option('case_id', case_id),
				   self._number_option('build', build),
				   self._number_option('environment', environment),
				   self._number_option('assignee', assignee),
				   self._string_option('status', status),
				   self._number_option('case_run_status_id', case_run_status_id),
				   self._number_option('case_text_version', case_text_version),
				   self._string_option('notes', notes),
				   self._number_option('sortkey', sortkey)
				   )])

	def testcaserun_update(self, caserun_ids, new_build_id=None,
						   new_environment_id=None, status=None, case_run_status_id=None,
						   update_bugs=False, assignee=None, sortkey=None, notes=None):
		"""Update one or more TestCaseRuns.

		PARAMETERS
		caserun_ids			(integer/string/list)	integer: A single TestCaseRun ID.
                     								string:  A comma separates string of TestCaseRun IDs for batch processing.
                        							list:    A list of TestCaseRun IDs for batch mode processing
		OPTIONAL PARAMETERS
		new_build_id		(integer/string)		ID or name of a Build in plan's product (optional)
		new_environment_id	(integer/string)		ID or name of an Environment in plan's product (optional)
		assignee			(integer/string)		Defaults to test case default tester (optional)
		status			 	(string)				Valid: IDLE, PASSED, FAILED, RUNNING, PAUSED, BLOCKED
		case_run_status_id 	(integer)				Valid: 1 (IDLE), 2 (PASSED), 3 (FAILED), 4 (RUNNING), 5 (PAUSED), 6 (BLOCKED)
		notes				(string)
		sortkey				(integer)
		update_bugs			(boolean)

		RETURNS
		(dictionary/list)	In the case of a single object, it is returned. If a 
        list was passed, it returns a list of object dictionaries. If the
        update on any particular object failed, the dictionary will contain an 
        ERROR key and the message as to why it failed.

		Notes: When setting the case_run_status_id to 2 (PASS), the 'Tested by' is updated
		to the user that is currently logged in.
		
		EXAMPLES
		testcaserun_update([1,2,3], 1)
		"""
		return self.do_command("TestCaseRun.update", [
				   self._alphanumlist_no_option(caserun_ids),
				   self._options_dict(
				   self._number_option('build_id', new_build_id),
				   self._number_option('environment_id', new_environment_id),
				   self._boolean_option('update_bugs', update_bugs),
				   self._number_option('assignee', assignee),
				   self._number_option('sortkey', sortkey),
				   self._string_option('notes', notes),
				   self._number_option('case_run_status_id', case_run_status_id),
				   self._string_option('status', status),
				   )])

	def testcaserun_update_alt(self, run_id, case_id, build_id, environment_id, new_build_id=None,
						   new_environment_id=None, status=None, case_run_status_id=None,
						   update_bugs=False, assignee=None, sortkey=None, notes=None):
		"""Update a single TestCaseRun.

		PARAMETERS
		run_id				(integer)			Test Run Number    
		case_id				(integer/string)	ID or alias of test case 
		build_id			(integer/string)	ID or name of a Build in plan's product    
		environment_id		(integer/string)	ID or name of an Environment in plan's product
		OPTIONAL PARAMETERS
		new_build_id		(integer/string)	ID or name of a Build in plan's product (optional)
		new_environment_id	(integer/string)	ID or name of an Environment in plan's product (optional)
		assignee			(integer/string)	Defaults to test case default tester (optional)
		status			 	(string)			Valid: IDLE, PASSED, FAILED, RUNNING, PAUSED, BLOCKED
		case_run_status_id 	(integer)			Valid: 1 (IDLE), 2 (PASSED), 3 (FAILED), 4 (RUNNING), 5 (PAUSED), 6 (BLOCKED)
		notes				(string)
		sortkey				(integer)
		update_bugs			(boolean)

		RETURNS
		(dictionary/list)	In the case of a single object, it is returned. If a 
        list was passed, it returns a list of object dictionaries. If the
        update on any particular object failed, the dictionary will contain an 
        ERROR key and the message as to why it failed.

		Notes: When setting the case_run_status_id to 2 (PASS), the 'Tested by' is updated
		to the user that is currently logged in.
		
		EXAMPLES
		testcaserun_update_alt(1, 1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.update", [
				   self._number_noop(run_id),
				   self._number_noop(case_id),
				   self._number_noop(build_id),
				   self._number_noop(environment_id),
				   self._options_dict(
				   self._number_option('build_id', new_build_id),
				   self._number_option('environment_id', new_environment_id),
				   self._boolean_option('update_bugs', update_bugs),
				   self._number_option('assignee', assignee),
				   self._number_option('sortkey', sortkey),
				   self._string_option('notes', notes),
				   self._number_option('case_run_status_id', case_run_status_id),
				   self._string_option('status', status),
				   )])



	def testcaserun_attach_bug(self, case_run_id, bug_ids):
		"""Add one or more bugs to the selected test case-runs.

		PARAMETERS
		case_run_id		(integer)				Must be greater than 0.
		bug_ids			(integer/list/string)	An integer or alias representing the ID in the database,
                  								a list of bug_ids or aliases, or a string of comma separated bug_ids. 

		RETURNS
		(dict)	Nothing or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_attach_bug(10, [1,2,3])
		"""
		return self.do_command("TestCaseRun.attach_bug", [self._number_noop(case_run_id), 
													self._alphanumlist_no_option(bug_ids)])
		
	def testcaserun_attach_bug_alt(self, run_id, case_id, build_id, environment_id, bug_ids):
		"""Add one or more bugs to the selected test case-runs.

		PARAMETERS
		run_id			(integer)				Test Run Number    
		case_id			(integer/string)		ID or alias of test case 
		build_id		(integer/string)		ID or name of a Build in plan's product    
		environment_id	(integer/string)		ID or name of an Environment in plan's product
		bug_ids			(integer/list/string)	An integer or alias representing the ID in the database,
                  								a list of bug_ids or aliases, or a string of comma separated bug_ids. 

		RETURNS
		(dict)	Nothing or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_attach_bug_alt(1, 1, 1, 1, [1,2,3])
		"""
		return self.do_command("TestCaseRun.attach_bug", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id),
				   self._alphanumlist_no_option(bug_ids)
				   ])
		
	
	def testcaserun_detach_bug(self, case_run_id, bug_ids):
		"""Remove a bug from a test case-run.

		PARAMETERS
		case_run_id		(integer)				Must be greater than 0.
		bug_ids			(integer/list/string)	An integer or alias representing the ID in the database,
                  								a list of bug_ids or aliases, or a string of comma separated bug_ids. 

		RETURNS
		(integer)	0 on sucess or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES testcaserun_detach_bug(10, [1,2,3])
		"""
		return self.do_command("TestCaseRun.detach_bug", [self._number_noop(case_run_id), 
													self._alphanumlist_no_option(bug_ids)])
		
	def testcaserun_detach_bug_alt(self, run_id, case_id, build_id, environment_id, bug_ids):
		"""Remove a bug from a test case-run.

		PARAMETERS
		run_id			(integer)				Test Run Number    
		case_id			(integer/string)		ID or alias of test case 
		build_id		(integer/string)		ID or name of a Build in plan's product    
		environment_id	(integer/string)		ID or name of an Environment in plan's product
		bug_ids			(integer/list/string)	An integer or alias representing the ID in the database,
                  								a list of bug_ids or aliases, or a string of comma separated bug_ids. 

		RETURNS
		(integer)	0 on sucess or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_detach_bug_alt(1, 1, 1, 1, [1,2,3])
		"""
		return self.do_command("TestCaseRun.detach_bug", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id),
				   self._alphanumlist_no_option(bug_ids)
				   ])


	def testcaserun_get_bugs(self, case_run_id):
		"""Get a list of bugs for the given TestCaseRun.

		PARAMETERS
		case_run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of Bug dictionaries or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_get_bugs(10)
		"""
		return self.do_command("TestCaseRun.get_bugs", [self._number_noop(case_run_id)])
	
	def testcaserun_get_bugs_alt(self, run_id, case_id, build_id, environment_id):
		"""Get a list of bugs for the given TestCaseRun.

		PARAMETERS
		run_id			(integer)			Test Run Number    
		case_id			(integer/string)	ID or alias of test case 
		build_id		(integer/string)	ID or name of a Build in plan's product    
		environment_id	(integer/string)	ID or name of an Environment in plan's product

		RETURNS
		(list/dict)	A list of Bug dictionaries or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_get_bugs_alt(1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.get_bugs", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id)
				   ])	
	
	
	def testcaserun_get_history(self, caserun_id):
		"""Get the list of case-runs for all runs this case appears in.
              To limit this list by build or other attribute, see TestCaseRun::list.

		PARAMETERS
		case_run_id		(integer)	Must be greater than 0.

		RETURNS
		(list/dict)	A list of case-run object hashes. or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testcaserun_get_history(10)
		"""
		return self.do_command("TestCaseRun.get_history", [self._number_noop(caserun_id)])
	
	def testcaserun_get_history_alt(self, run_id, case_id, build_id, environment_id):
		"""Get the list of case-runs for all runs this case appears in.

		PARAMETERS
		run_id			(integer)			Test Run Number    
		case_id			(integer/string)	ID or alias of test case 
		build_id		(integer/string)	ID or name of a Build in plan's product    
		environment_id	(integer/string)	ID or name of an Environment in plan's product

		RETURNS
		(list/dict)	A list of case-run object hashes. or a dictionary containing values for
		the keys, "faultCode" and "faultString".
		
		EXAMPLES
		testcaserun_get_history_alt(1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.get_history", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id)
				   ])	
		
		
	def testcaserun_get_completion_time(self, case_run_id):
		"""Returns the time in seconds that it took for this case to complete.

		PARAMETERS
		case_run_id		(integer)	Must be greater than 0.

		RETURNS
		(integer)	Seconds since run was started till this case was completed.
		
		EXAMPLES
		testcaserun_get_history(10)
		"""
		return self.do_command("TestCaseRun.get_completion_time", [self._number_noop(case_run_id)])
	
	def testcaserun_get_completion_time_alt(self, run_id, case_id, build_id, environment_id):
		"""Returns the time in seconds that it took for this case to complete.

		PARAMETERS
		run_id			(integer)			Test Run Number    
		case_id			(integer/string)	ID or alias of test case 
		build_id		(integer/string)	ID or name of a Build in plan's product    
		environment_id	(integer/string)	ID or name of an Environment in plan's product 

		RETURNS
		(integer)	Seconds since run was started till this case was completed.
		
		EXAMPLES
		testcaserun_get_history_alt(1, 1, 1, 1)
		"""
		return self.do_command("TestCaseRun.get_completion_time", [
				   self._number_no_option(run_id),
				   self._number_no_option(case_id),
				   self._number_no_option(build_id),
				   self._number_no_option(environment_id)
				   ])	


	def testcaserun_lookup_status_id_by_name(self, name):
		"""Lookup A TestCaseRun Status ID By Its Name.

		PARAMETERS
		name	(string)	Cannot be null or empty string

		RETURNS
		(list/dict)	A list of Bug dictionaries or a dictionary containing values for the keys on success;
		on error, an XmlRpcException is thrown.
		
		EXAMPLES
		testcaserun_lookup_status_id_by_name("Name")
		"""
		return self.do_command("TestCaseRun.lookup_status_id_by_name", [self._string_noop(name)])


	def testcaserun_lookup_status_name_by_id(self, id):
		"""Lookup A TestCaseRun Status Name By Its ID.

		PARAMETERS
		id		(integer)	Must be greater than 0.

		RETURNS
		(string)	The TestCaseRun status name for the respective id or 0 error occurs.
		
		EXAMPLES
		testcaserun_lookup_status_name_by_id(10)
		"""
		return self.do_command("TestCaseRun.lookup_status_name_by_id", [self._number_noop(id)])

	
	def _alphanum_option(self, option, value):
		"""Returns the string 'option': 'value'. If value is None, then '' where value
		can be a string or a number.

		Example: self._alphanum_option('description', 'Voyage project') returns " 'description' : 'Voyage project',"
		Example: self._alphanum_option("isactive", 1) returns " 'isactive': 1,"
		"""
		if value:
			if type(value) is StringType: 
				return self._string_option(option, value)
			if type(value) is IntType:
				return self._number_option(option, value)
			else: raise TestopiaError("The value '%s' is not a valid string or number" % value)
		return ''
	
		
	def _alphanum_no_option(self, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string or a number

		Example: self._alphanum_no_option('description') returns " 'description', "
		Example: self._alphanum_no_option(1) returns 1
		"""
		if value:
			if type(value) is StringType: 
				return self._string_no_option( value )
			if type(value) is IntType: 
				return self._number_no_option( value )
			else: raise TestopiaError("The value '%s' is not a valid string or number" % value)
		return ''
	
	_alphanum_noop = _alphanum_no_option
	
	def _alphanumlist_no_option(self, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string, number or list

		Example: self._alphanum_no_option('description') returns " 'description', "
		Example: self._alphanum_no_option(1) returns 1
		Example: self._alphanum_no_option([1,2,3]) returns " '[1,2,3]'"
		"""
		if value:
			if type(value) is StringType: 
				return self._string_no_option( value )
			if type(value) is IntType: 
				return self._number_no_option( value )
			if type(value) is ListType:
				return self._list_no_option(value)
			else: raise TestopiaError("The value '%s' is not a valid string, number or list" % value)
		return ''
	
	def _alphanumlist_option(self, option, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string, number or list

		Example: self._alphanum_option('option, 'description')
		Example: self._alphanum_option('option', 1)
		Example: self._alphanum_option('option', [1,2,3])
		"""
		if value:
			if type(value) is StringType: 
				return self._string_option( option, value )
			if type(value) is IntType: 
				return self._number_option( option, value )
			if type(value) is ListType:
				return self._list_option( option, value)
			else: raise TestopiaError("The value '%s' is not a valid string, number or list" % value)
		return ''
	
	def _numlist_no_option(self, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string, number or list

		Example: self._alphanum_no_option(1) returns 1
		Example: self._alphanum_no_option([1,2,3]) returns " '[1,2,3]'"
		"""
		if value:
			if type(value) is IntType: 
				return self._number_no_option( value )
			if type(value) is ListType:
				return self._list_no_option(value)
			else: raise TestopiaError("The value '%s' is not a valid number or list" % value)
		return ''
	
	def _numlist_option(self, option, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string, number or list

		Example: self._alphanum_option('option', 1)
		Example: self._alphanum_option('option', [1,2,3])
		"""
		if value:
			if type(value) is IntType: 
				return self._number_option( option, value )
			if type(value) is ListType:
				return self._list_option( option, value)
			else: raise TestopiaError("The value '%s' is not a valid number or list" % value)
		return ''
	
	def _alphalist_no_option(self, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string or a list

		Example: self._alphanum_no_option('description') returns " 'description', "
		Example: self._alphanum_no_option([1,2,3]) returns " '[1,2,3]'"
		"""
		if value:
			if type(value) is StringType: 
				return self._string_no_option( value )
			if type(value) is ListType:
				return self._list_no_option(value)
			else: raise TestopiaError("The value '%s' is not a valid string or a list" % value)
		return ''
	
	def _alphalist_option(self, option, value): 
		"""Returns the string 'value'. If value is None, then '' where value
		can be a string or a list

		Example: self._alphanum_option( 'option', 'description')
		Example: self._alphanum_option( 'option', [1,2,3])
		"""
		if value:
			if type(value) is StringType: 
				return self._string_option( option, value )
			if type(value) is ListType:
				return self._list_option( option, value )
			else: raise TestopiaError("The value '%s' is not a valid string or a list" % value)
		return ''

	def _boolean_option(self, option, value):
		"""Returns the boolean option when value is True or False, else ''

		Example: _boolean_option('isactive', True) returns " 'isactive': 1,"
		"""
		if value or str(value) == 'False':
			if type(value) is not BooleanType:
				raise TestopiaError("The value for the option '%s' is not of boolean type." % option)
			elif value == False:
				return "\'%s\':0, " % option
			elif value == True:
				return "\'%s\':1, " % option
		return ''


	def _datetime_option(self, option, value):
		"""Returns the string 'option': 'value' where value is a date object formatted in string as yyyy-mm-dd hh:mm:ss.
		If value is None, then we return ''.

		Example: self._time_option('datetime', datetime(2007,12,05,13,01,03)) returns "'datetime': '2007-12-05 13:01:03'"
		"""
		if value:
			if type(value) is not type(datetime(2000,01,01,12,00,00)):
				raise TestopiaError("The option '%s' is not a valid datetime object." % option)
			return "\'%s\':\'%s\', " % (option, value.strformat("%Y-%m-%d %H:%M:%S"))
		return ''


	def _list_dictionary_option(self, option, value):
		"""Verifies that the value passed for the option is in the format of a list
		of dictionaries.

		Example: _list_dictionary_option('plan':[{'key1': 'value1', 'key2': 'value2'}]) verifies that value is a list,
		then verifies that the content of value are dictionaries.
		"""
		if value: # Verify that value is a type of list
			if type(value) is not ListType: # Verify that the content of value are dictionaries,
				raise TestopiaError("The option '%s' is not a valid list of dictionaries." % option)
			else:
				for item in value:
					if type(item) is not DictType:
						raise TestopiaError("The option '%s' is not a valid list of dictionaries." % option)
			return "\'%s\': %s" % (option, value)
		return ''

	_list_dict_op = _list_dictionary_option

	def _list_option(self, option, value):
		"""Verifies that the value passed for the option is in the format of a list

		Example: _list_option('plan', [1,2,3]) verifies that value is a list
		"""
		if value: # Verify that value is a type of list
			if type(value) is not ListType: # Verify that value is a list,
				raise TestopiaError("The value '%s' is not a valid list." % value)
			return "\'%s\': %s," % (option, value)
		return ''
	
	def _list_no_option(self, value):
		"""Verifies that the value passed is a list

		Example: _list_no_option([1,2,3]) verifies that value is a list
		"""
		if value: # Verify that value is a type of list
			if type(value) is not ListType: # Verify that value is a list
				raise TestopiaError("The value '%s' is not a valid list." % value)
			return "%s" % (value)
		return ''
	
	_list_noop = _list_no_option

	def _number_option(self, option, value):
		"""Returns the string " 'option': value," if value is not None, else ''

		Example: self._number_option("isactive", 1) returns " 'isactive': 1,"
		"""
		if value:
			if type(value) is not IntType and type(value) is not LongType:
				raise TestopiaError("The option '%s' is not a valid integer." % option)
			return "\'%s\':%d, " % (option, value)
		return ''


	def _number_no_option(self, number):
		"""Returns the number in number. Just a totally useless wrapper :-)

		Example: self._number_no_option(1) returns 1
		"""
		if type(number) is not IntType and type(number) is not LongType:
			raise TestopiaError("The 'number' parameter is not an integer.")
		return str(number)

	_number_noop = _number_no_option


	def _options_dict(self, *args):
		"""Creates a wrapper around all the options into a dictionary format.

		Example, if args is ['isactive': 1, 'description', 'Voyage project'], then
		the return will be {'isactive': 1, 'description', 'Voyage project'}
		"""
		return "{%s}" % ''.join(args)


	def _options_non_empty_dict(self, *args):
		"""Creates a wrapper around all the options into a dictionary format and
		verifies that the dictionary is not empty.

		Example, if args is ['isactive': 1,", 'description', 'Voyage project'], then
		the return will be {'isactive': 1,", 'description', 'Voyage project'}.
		If args is empty, then we raise an error.
		"""
		if not args:
			raise TestopiaError, "At least one variable must be set."
		return "{%s}" % ''.join(args)

	_options_ne_dict = _options_non_empty_dict


	def _string_option(self, option, value):
		"""Returns the string 'option': 'value'. If value is None, then ''

		Example: self._string_option('description', 'Voyage project') returns " 'description' : 'Voyage project',"
		"""
		if value:
			if type(value) is not StringType:
				raise TestopiaError("The option '%s' is not a valid string." % option)
			return "\'%s\':\'%s\', " % (option, value)
		return ''

	def _string_no_option(self, option):
		"""Returns the string 'option'.

		Example: self._string_no_option("description") returns "'description'"
		"""
		if option:
			if type(option) is not StringType:
				raise TestopiaError("The option '%s' is not a valid string." % option)
			return "\'%s\'" % option
		return ''

	_string_noop = _string_no_option

	def _dict_option(self, option, value):
		"""Returns the string 'option': 'value'. If value is None, then ''

		Example: self._dict_option({'something': 1}, 'Voyage project') returns " '{'something': 1}' : 'Voyage project',"
		"""
		if value:
			if type(value) is not DictType:
				raise TestopiaError("The option '%s' is not a valid string." % option)
			return "\'%s\':\'%s\', " % (option, value)
		return ''

	def _dict_no_option(self, option):
		"""Returns the string 'option'.

		Example: self._dict_no_option({'something': 1}) returns "'{'something': 1}'"
		"""
		if option:
			if type(option) is not DictType:
				raise TestopiaError("The option '%s' is not a valid string." % option)
			return "\'%s\'" % option
		return ''

	_dict_noop = _dict_no_option


	def _time_option(self, option, value):
		"""Returns the string 'option': 'value' where value is a time object formatted in string as hh:mm:ss.
		If value is None, then we return ''.

		Example: self._time_option('time', time(12,00,03)) returns "'time': '12:00:03'"
		"""
		if value:
			if type(value) is not type(time(12,00,00)):
				raise TestopiaError("The option '%s' is not a valid time object." % option)
			return "\'%s\':\'%s\', " % (option, value.strftime("%H:%M:%S"))
		return ''


	def _validate_search_operation_string(self, option, operation):
		"""Validates the operation passed is a valid search operation.

		'operation' -- string, valid search operations

		Valid Search Operations:
			'equals',
			'notequals',
			'isnull',
			'isnotnull',
			'lessthan',
			'greaterthan',
			'regexp',
			'notregexp',
			'anywords',
			'allwords',
			'nowords',
		"""
		VALID_SEARCH_OPERATIONS = ['equals', 'notequals', 'isnull',
				'isnotnull', 'lessthan', 'greaterthan', 'regexp',
				'notregexp', 'anywords', 'allwords', 'nowords',]
		if operation:
			if operation not in VALID_SEARCH_OPERATIONS:
				raise TestopiaError("Not a valid search operation.")
			else:
				return "\'%s\':\'%s\', " % (option, operation)
		return ''

	_search_op = _validate_search_operation_string

	#Shortcuts
	#build_id=build_lookup_id_by_name	Deprecated	this method is no longer userd
	build_id=build_check_build
	check_build=build_check_build
	priority_id=testcase_lookup_priority_id_by_name
	case_status_id=testcase_lookup_status_id_by_name
	caserun_status_id=testcaserun_lookup_status_id_by_name
	type_id=testplan_lookup_type_id_by_name


Testopia = Driver

# vim:ts=4:noexpandtab:
