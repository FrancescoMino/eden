# -*- coding: utf-8 -*-

try:
    # Python 2.7
    from collections import OrderedDict
except:
    # Python 2.6
    from gluon.contrib.simplejson.ordered_dict import OrderedDict

from gluon import current
from gluon.storage import Storage
from gluon.validators import IS_NOT_EMPTY, IS_EMPTY_OR, IS_IN_SET

from s3 import s3_date, S3Represent

T = current.T
settings = current.deployment_settings

"""
    Settings for the EVASS template:
        http://eden.sahanafoundation.org/wiki/Deployments/Italy/EVASS
"""

# Pre-Populate
settings.base.prepopulate = ["EVASS", "demo/users"]

settings.base.system_name = T("EVASS - Sahana Eden for Italy")
settings.base.system_name_short = T("Sahana Eden for Italy")

# Use system_name_short as default email subject (Appended).
settings.mail.default_email_subject = True
# Append name and surname of logged in user to email subject
settings.mail.auth_user_in_email_subject = True

# Theme (folder to use for views/layout.html)
settings.base.theme = "EVASS"
settings.ui.formstyle = "foundation"
settings.ui.filter_formstyle = "foundation_inline"

# Authentication settings
# These settings should be changed _after_ the 1st (admin) user is
# registered in order to secure the deployment
# Should users be allowed to register themselves?
#settings.security.self_registration = False
# Do new users need to verify their email address?
#settings.auth.registration_requires_verification = True
# Do new users need to be approved by an administrator prior to being able to login?
#settings.auth.registration_requires_approval = True

# Allow a new user to be linked to a record (and a new record will be created if it doesn't already exist)
#settings.auth.registration_link_user_to = {"staff":T("Staff"),
#                                           "volunteer":T("Volunteer"),
#                                           "member":T("Member")}

# Always notify the approver of a new (verified) user, even if the user is automatically approved
settings.auth.always_notify_approver = False

# The name of the teams that users are added to when they opt-in to receive alerts
#settings.auth.opt_in_team_list = ["Updates"]
# Uncomment this to set the opt in default to True
#settings.auth.opt_in_default = True
# Uncomment this to request the Mobile Phone when a user registers
settings.auth.registration_requests_mobile_phone = True
# Uncomment this to have the Mobile Phone selection during registration be mandatory
settings.auth.registration_mobile_phone_mandatory = True
# Uncomment this to request the Organisation when a user registers
settings.auth.registration_requests_organisation = True
# Uncomment this to have the Organisation selection during registration be mandatory
settings.auth.registration_organisation_required = True
# Uncomment this to have the Organisation input hidden unless the user enters a non-whitelisted domain
#settings.auth.registration_organisation_hidden = True
# Uncomment this to default the Organisation during registration
#settings.auth.registration_organisation_default = "My Organisation"
# Uncomment this to request the Organisation Group when a user registers
#settings.auth.registration_requests_organisation_group = True
# Uncomment this to have the Organisation Group selection during registration be mandatory
#settings.auth.registration_organisation_group_required = True
# Uncomment this to request the Site when a user registers
#settings.auth.registration_requests_site = True
# Uncomment this to allow Admin to see Organisations in user Admin even if the Registration doesn't request this
#settings.auth.admin_sees_organisation = True
# Uncomment to set the default role UUIDs assigned to newly-registered users
# This is a dictionary of lists, where the key is the realm that the list of roles applies to
# The key 0 implies not realm restricted
# The keys "organisation_id" and "site_id" can be used to indicate the user's "organisation_id" and "site_id"
#settings.auth.registration_roles = { 0: ["STAFF", "PROJECT_EDIT"]}
# Uncomment this to enable record approval
#settings.auth.record_approval = True
# Uncomment this and specify a list of tablenames for which record approval is required
#settings.auth.record_approval_required_for = ["project_project"]
# Uncomment this to request an image when users register
#settings.auth.registration_requests_image = True
# Uncomment this to direct newly-registered users to their volunteer page to be able to add extra details
# NB This requires Verification/Approval to be Off
# @ToDo: Extend to all optional Profile settings: Homepage, Twitter, Facebook, Mobile Phone, Image
#settings.auth.registration_volunteer = True
# Terms of Service to be able to Register on the system
# uses <template>/views/tos.html
settings.auth.terms_of_service = True
# Uncomment this to allow users to Login using Gmail's SMTP
#settings.auth.gmail_domains = ["gmail.com"]
# Uncomment this to allow users to Login using OpenID
#settings.auth.openid = True
# Uncomment this to enable presence records on login based on HTML5 geolocations
#settings.auth.set_presence_on_login = True
# Uncomment this and specify a list of location levels to be ignored by presence records
#settings.auth.ignore_levels_for_presence = ["L0", "L1", "L2", "L3"]
# Uncomment this to enable the creation of new locations if a user logs in from an unknown location. Warning: This may lead to many useless location entries
#settings.auth.create_unknown_locations = True

# L10n settings
# Languages used in the deployment (used for Language Toolbar & GIS Locations)
# http://www.loc.gov/standards/iso639-2/php/code_list.php
settings.L10n.languages = OrderedDict([
    ("en", "English"),
    ("it", "Italiano"),
])
# Default language for Language Toolbar (& GIS Locations in future)
settings.L10n.default_language = "en"
# Default timezone for users
settings.L10n.utc_offset = "UTC +0100"
# Uncomment these to use US-style dates in English (localisations can still convert to local format)
#settings.L10n.time_format = T("%H:%M:%S")
settings.L10n.date_format = T("%d/%m/%Y")
# Start week on Sunday
#settings.L10n.firstDOW = 0
# Number formats (defaults to ISO 31-0)
# Decimal separator for numbers (defaults to ,)
settings.L10n.decimal_separator = ","
# Thousands separator for numbers (defaults to space)
settings.L10n.thousands_separator = "."
# Default Country Code for telephone numbers
settings.L10n.default_country_code = +39
# Make last name in person/user records mandatory
settings.L10n.mandatory_lastname = True
# Configure the list of Religions
settings.L10n.religions = OrderedDict([("unknown", T("Unknown")),
                                       ("bahai", T("Bahai")),
                                       ("buddhist", T("Buddhist")),
                                       ("christian", T("Christian")),
                                       ("hindu", T("Hindu")),
                                       ("jewish", T("Jewish")),
                                       ("muslim", T("Muslim")),
                                       ("other", T("other"))
                                       ])
# Uncomment this to Translate CMS Series Names
#settings.L10n.translate_cms_series = True
# Uncomment this to Translate Layer Names
#settings.L10n.translate_gis_layer = True
# Uncomment this to Translate Location Names
settings.L10n.translate_gis_location = True

# Finance settings
settings.fin.currency_default = "EUR"
settings.fin.currencies = {
    "EUR": T("Euros"),
    "GBP": T("Great British Pounds"),
    "USD": T("United States Dollars"),
}

#settings.fin.currency_writable = False # False currently breaks things

# PDF settings
# Default page size for reports (defaults to A4)
#settings.base.paper_size = T("Letter")
# Location of Logo used in pdfs headers
#settings.ui.pdf_logo = "static/img/mylogo.png"

# GIS (Map) settings
# GeoNames username
settings.gis.geonames_username = "evass"
# Size of the Embedded Map
# Change this if-required for your theme
# NB API can override this in specific modules
#settings.gis.map_height = 400
#settings.gis.map_width = 700
# Restrict the Location Selector to just certain countries
# NB This can also be over-ridden for specific contexts later
# e.g. Activities filtered to those of parent Project
settings.gis.countries = ["IT"]
# Uncomment to pass Addresses imported from CSV to a Geocoder to try and automate Lat/Lon
#settings.gis.geocode_imported_addresses = "google"
# Hide the Map-based selection tool in the Location Selector
#settings.gis.map_selector = False
# Hide LatLon boxes in the Location Selector
#settings.gis.latlon_selector = False
# Use Building Names as a separate field in Street Addresses?
#settings.gis.building_name = False
# Use a non-default fillColor for Clustered points
#settings.gis.cluster_fill = "8087ff"
# Disable the label for clustered points
#settings.gis.cluster_label = False
# Use a non-default strokeColor for Clustered points
#settings.gis.cluster_stroke = "2b2f76"
# Use a non-default fillColor for Selected points
#settings.gis.select_fill = "ffdc33"
# Use a non-default strokeColor for Selected points
#settings.gis.select_stroke = "ff9933"
# Display Resources recorded to Admin-Level Locations on the map
# @ToDo: Move into gis_config?
# Uncomment to fall back to country LatLon to show resources, if nothing better available
#settings.gis.display_L0 = True
# Currently unused
#settings.gis.display_L1 = False
# Uncomemnt this to do deduplicate lookups on Imports via PCode (as alternative to Name)
#settings.gis.lookup_pcode = True
# Set this if there will be multiple areas in which work is being done,
# and a menu to select among them is wanted.
#settings.gis.menu = "Maps"
# Maximum Marker Size
# (takes effect only on display)
#settings.gis.marker_max_height = 35
#settings.gis.marker_max_width = 30
# Duplicate Features so that they show wrapped across the Date Line?
# Points only for now
# lon<0 have a duplicate at lon+360
# lon>0 have a duplicate at lon-360
#settings.gis.duplicate_features = True
# Uncomment to use CMS to provide Metadata on Map Layers
#settings.gis.layer_metadata = True
# Uncomment to show Clear Layers tool
#settings.gis.clear_layers = True
# Uncomment to hide the Geolocation control
#settings.gis.geolocate_control = False
# Uncomment to hide the WMS GetFeatureInfo control
#settings.gis.getfeature_control = False
# Uncomment to hide Layer Properties tool
#settings.gis.layer_properties = False
# Uncomment to hide the Base Layers folder in the LayerTree
#settings.gis.layer_tree_base = False
# Uncomment to hide the Overlays folder in the LayerTree
#settings.gis.layer_tree_overlays = False
# Uncomment to change the label of the Overlays folder in the LayerTree
#settings.gis.label_overlays = "Overlays"
# Uncomment to not expand the folders in the LayerTree by default
#settings.gis.layer_tree_expanded = False
# Uncomment to have custom folders in the LayerTree use Radio Buttons
#settings.gis.layer_tree_radio = True
# Uncomment to display the Map Legend as a floating DIV
settings.gis.legend = "float"
# Mouse Position: 'normal', 'mgrs' or None
#settings.gis.mouse_position = "mgrs"
# Uncomment to hide the Overview map
#settings.gis.overview = False
# Uncomment to hide the permalink control
#settings.gis.permalink = False
# Uncomment to disable the ability to add PoIs to the main map
#settings.gis.pois = False
# PoIs to export in KML/OSM feeds from Admin locations
#settings.gis.poi_resources = ["cr_shelter", "hms_hospital", "org_office"]
# Uncomment to hide the Save control, or set to "float"
#settings.gis.save = False
# Uncomment to hide the ScaleLine control
#settings.gis.scaleline = False
# Uncomment to modify the Simplify Tolerance
#settings.gis.simplify_tolerance = 0.001
# Uncomment to Hide the Toolbar from the main Map
#settings.gis.toolbar = False
# Uncomment to show Catalogue Layers in Map Widgets (e.g. Profile & Summary pages)
#settings.gis.widget_catalogue_layers = True
# Uncomment to show WMS Browser in Map Widgets (e.g. Profile & Summary pages)
# - NB This also requires the active gis_config to have one configured
#settings.gis.widget_wms_browser = True
# Uncomment to hide the Zoom control
#settings.gis.zoomcontrol = False

# Messaging Settings
# If you wish to use a parser.py in another folder than "default"
#settings.msg.parser = "mytemplatefolder"
# Uncomment to turn off enforcement of E.123 international phone number notation
#settings.msg.require_international_phone_numbers = False

# Use 'soft' deletes
#settings.security.archive_not_delete = False

# AAA Settings

# Security Policy
# http://eden.sahanafoundation.org/wiki/S3AAA#System-widePolicy
# 1: Simple (default): Global as Reader, Authenticated as Editor
# 2: Editor role required for Update/Delete, unless record owned by session
# 3: Apply Controller ACLs
# 4: Apply both Controller & Function ACLs
# 5: Apply Controller, Function & Table ACLs
# 6: Apply Controller, Function, Table ACLs and Entity Realm
# 7: Apply Controller, Function, Table ACLs and Entity Realm + Hierarchy
# 8: Apply Controller, Function, Table ACLs, Entity Realm + Hierarchy and Delegations
#
settings.security.policy = 7

# Ownership-rule for records without owner:
# True = not owned by any user (strict ownership, default)
# False = owned by any authenticated user
#settings.security.strict_ownership = False

# Audit
# - can be a callable for custom hooks (return True to also perform normal logging, or False otherwise)
# NB Auditing (especially Reads) slows system down & consumes diskspace
#settings.security.audit_read = True
#settings.security.audit_write = True

# Lock-down access to Map Editing
#settings.security.map = True
# Allow non-MapAdmins to edit hierarchy locations? Defaults to True if not set.
# (Permissions can be set per-country within a gis_config)
#settings.gis.edit_Lx = False
# Allow non-MapAdmins to edit group locations? Defaults to False if not set.
#settings.gis.edit_GR = True
# Note that editing of locations used as regions for the Regions menu is always
# restricted to MapAdmins.
# Uncomment to disable that LatLons are within boundaries of their parent
#settings.gis.check_within_parent_boundaries = False

# Enable this for a UN-style deployment
#settings.ui.cluster = True
# Enable Social Media share buttons
#settings.ui.social_buttons = True
# Enable this to show pivot table options form by default
#settings.ui.hide_report_options = False
# Uncomment to show created_by/modified_by using Names not Emails
#settings.ui.auth_user_represent = "name"
# Uncomment to restrict the export formats available
#settings.ui.export_formats = ["kml", "pdf", "rss", "xls", "xml"]
# Uncomment to include an Interim Save button on CRUD forms
#settings.ui.interim_save = True

# -----------------------------------------------------------------------------
# Shelters
# Uncomment to use a dynamic population estimation by calculations based on registrations  
settings.cr.shelter_population_dynamic = True
# Uncomment to activate the housing units management. 
settings.cr.shelter_housing_unit_management = True

# -----------------------------------------------------------------------------

# Events
# Make Event Types Hierarchical
#settings.event.types_hierarchical = True

# -----------------------------------------------------------------------------
# Evacuees
# Group Types
#settings.evr.group_types = {1: T("other"),
#                            2: T("Family"),
#                            3: T("Tourist group"),
#                            4: T("Society"),
#                            5: T("Company"),
#                            6: T("Convent"),
#                            7: T("Hotel"),
#                            8: T("Hospital"),
#                            9: T("Orphanage")
#                            }
# Uncomment to hide evacuees physical description in Evacuees page
settings.evr.physical_description = False
# Uncomment to hide Emergency Contacts in Person Contacts page
settings.pr.show_emergency_contacts = False
# Uncomment to link evacuees to Organisations
settings.evr.link_to_organisation= True
# -----------------------------------------------------------------------------
# Organisations
# Enable the use of Organisation Branches
settings.org.branches = True
# Make Facility Types Hierarchical
#settings.org.facility_types_hierarchical = True
# Enable the use of Organisation Groups & what their name is
#settings.org.groups = "Coalition"
#settings.org.groups = "Network"
# Enable the use of Organisation Regions
#settings.org.regions = True
# Make Organisation Regions Hierarchical
#settings.org.regions_hierarchical = True
# Make Services Hierarchical
#settings.org.services_hierarchical = True
# Set the length of the auto-generated org/site code the default is 10
#settings.org.site_code_len = 3
# Set the label for Sites
#settings.org.site_label = "Facility"
# Uncomment to show the date when a Site (Facilities-only for now) was last contacted
#settings.org.site_last_contacted = True
# Uncomment to use an Autocomplete for Site lookup fields
#settings.org.site_autocomplete = True
# Extra fields to show in Autocomplete Representations
#settings.org.site_autocomplete_fields = ["instance_type", "location_id$L1", "organisation_id$name"]
# Uncomment to hide inv & req tabs from Sites
#settings.org.site_inv_req_tabs = False
# Uncomment to add summary fields for Organisations/Offices for # National/International staff
#settings.org.summary = True
# Enable certain fields just for specific Organisations
# Requires a call to settings.set_org_dependent_field(field)
# empty list => disabled for all (including Admin)
#settings.org.dependent_fields = \
#    {#"<table name>.<field name>"  : ["<Organisation Name>"],
#     "pr_person_details.mother_name"             : [],
#     "pr_person_details.father_name"             : [],
#     "pr_person_details.company"                 : [],
#     "pr_person_details.affiliations"            : [],
#     "vol_volunteer.active"                      : [],
#     "vol_volunteer_cluster.vol_cluster_type_id"      : [],
#     "vol_volunteer_cluster.vol_cluster_id"          : [],
#     "vol_volunteer_cluster.vol_cluster_position_id" : [],
#     }
# Theme for the S3HierarchyWidget (folder in static/styles/jstree or relative to application)
settings.ui.hierarchy_theme = "default"
# -----------------------------------------------------------------------------
# Human Resource Management
# Uncomment to change the label for 'Staff'
#settings.hrm.staff_label = "Contacts"
# Uncomment to allow Staff & Volunteers to be registered without an email address
settings.hrm.email_required = False
# Uncomment to allow Staff & Volunteers to be registered without an Organisation
settings.hrm.org_required = False
# Uncomment to allow HR records to be deletable rather than just marking them as obsolete
#settings.hrm.deletable = True
# Uncomment to filter certificates by (root) Organisation & hence not allow Certificates from other orgs to be added to a profile (except by Admin)
#settings.hrm.filter_certificates = True
# Uncomment to allow HRs to have multiple Job Titles
settings.hrm.multiple_job_titles = True
# Uncomment to have each root Org use a different Job Title Catalog
#settings.hrm.org_dependent_job_titles = True
# Uncomment to hide the Staff resource
#settings.hrm.show_staff = False
# Uncomment to disable Staff experience
#settings.hrm.staff_experience = False
# Uncomment to enable Volunteer 'active' field
# - can also be made a function which is called to calculate the status based on recorded hours
#settings.hrm.vol_active = True
# Uncomment to define a Tooltip to show when viewing the Volunteer 'active' field
#settings.hrm.vol_active_tooltip = "A volunteer is defined as active if they've participated in an average of 8 or more hours of Program work or Trainings per month in the last year"
# Uncomment to disable Volunteer experience
#settings.hrm.vol_experience = False
# Uncomment to show the Organisation name in HR represents
#settings.hrm.show_organisation = True
# Uncomment to consolidate tabs into a single CV
#settings.hrm.cv_tab = True
# Uncomment to consolidate tabs into Staff Record
#settings.hrm.record_tab = True
# Uncomment to disable the use of Volunteer Awards
#settings.hrm.use_awards = False
# Uncomment to disable the use of HR Certificates
settings.hrm.use_certificates = False
# Uncomment to enable the use of Staff/Volunteer IDs
#settings.hrm.use_code = True
# Uncomment to disable the use of HR Credentials
#settings.hrm.use_credentials = False
# Uncomment to disable the use of HR Description
#settings.hrm.use_description = False
# Uncomment to enable the use of HR Education
#settings.hrm.use_education = True
# Uncomment to disable the use of HR ID
#settings.hrm.use_id = False
# Uncomment to disable the use of HR Skills
#settings.hrm.use_skills = False
# Uncomment to disable the use of HR Teams
settings.hrm.teams = False
# Uncomment to disable the use of HR Trainings
settings.hrm.use_trainings = False

#*****************************Frontpage settings*************************
# RSS feeds
settings.frontpage.rss = [
    {"title": "RSS News - Dipartimento della Protezione Civile ",
     "url": "http://www.protezionecivile.gov.it/jcms/do/jprss/Rss/Feed/show.action?id=12170&lang=it#"
    },
    {"title": "RSS Vigilanza Meteo - Dipartimento della Protezione Civile ",
     "url": "http://www.protezionecivile.gov.it/jcms/do/jprss/Rss/Feed/show.action?id=23573&lang=it#"
    },
    {"title": "RSS Previsioni Meteo - Dipartimento della Protezione Civile ",
     "url": "http://www.protezionecivile.gov.it/jcms/do/jprss/Rss/Feed/show.action?id=23575&lang=it#"
    },
    {"title": "RSS Comunicati Stampa - Dipartimento della Protezione Civile ",
     "url": "http://www.protezionecivile.gov.it/jcms/do/jprss/Rss/Feed/show.action?id=23577&lang=it#"
    },
    {"title": "Twitter - Croce Rossa Italia",
     # @crocerossa
     #"url": "https://search.twitter.com/search.rss?q=from%3Acrocerossa" # API v1 deprecated, so doesn't work, need to use 3rd-party service, like:
     "url": "http://www.rssitfor.me/getrss?name=@crocerossa"
     # Hashtag
     #url: "http://search.twitter.com/search.atom?q=%23eqnz" # API v1 deprecated, so doesn't work, need to use 3rd-party service, like:
     #"url": "http://api2.socialmention.com/search?q=protezionecivile&t=all&f=rss"
    },
#    {"title": "Twitter - Dipartimento della Protezione Civile",
#     # @protezionecivile
#     "url": "http://www.rssitfor.me/getrss?name=@protezionecivile"
#     # Hashtag
#     #url: "http://search.twitter.com/search.atom?q=%23eqnz" # API v1 deprecated, so doesn't work, need to use 3rd-party service, like:
#     "url": "http://api2.socialmention.com/search?q=protezionecivile&t=all&f=rss"
#    }
]
# -----------------------------------------------------------------------------
def customise_pr_person_resource(r, tablename):

    s3db = current.s3db
    table = r.resource.table

    # Disallow "unknown" gender and defaults to "male"
    evr_gender_opts = dict((k, v) for k, v in s3db.pr_gender_opts.items()
                                  if k in (2, 3))
    gender = table.gender
    gender.requires = IS_IN_SET(evr_gender_opts, zero=None)
    gender.default = 3

    if r.controller == "evr":
        # Hide evacuees emergency contacts
        settings.pr.show_emergency_contacts = False

        # Last name and date of birth mandatory in EVR module
        table.last_name.requires = IS_NOT_EMPTY(
                        error_message = T("Please enter a last name"))

        dob_requires = s3_date("dob",
                               future = 0,
                               past = 1320,
                               empty = False).requires
        dob_requires.error_message = T("Please enter a date of birth")
        table.date_of_birth.requires = dob_requires

        s3db.pr_person_details.place_of_birth.requires = IS_NOT_EMPTY(
                        error_message = T("Please enter a place of birth"))

    # Disable unneeded physical details
    pdtable = s3db.pr_physical_description
    hide_fields = [
        "race",
        "complexion",
        "height",
        "weight",
        "hair_length",
        "hair_style",
        "hair_baldness",
        "hair_comment",
        "facial_hair_type",
        "facial_hair_length",
        "facial_hair_color",
        "facial_hair_comment",
        "body_hair",
        "skin_marks",
        "medical_conditions"
    ]
    for fname in hide_fields:
        field = pdtable[fname]
        field.readable = field.writable = False

    # This set is suitable for Italy
    ethnicity_opts = ("Italian",
                      "Chinese",
                      "Albanese",
                      "Philippine",
                      "Pakistani",
                      "English",
                      "African",
                      "Other",
                      "Unknown",
                      )
    ethnicity_opts = dict((v, T(v)) for v in ethnicity_opts)

    ethnicity = pdtable.ethnicity
    ethnicity.requires = IS_EMPTY_OR(IS_IN_SET(ethnicity_opts,
                                               sort=True))
    ethnicity.represent = S3Represent(options=ethnicity_opts,
                                      translate=True)

    # Enable place of birth
    place_of_birth = s3db.pr_person_details.place_of_birth
    place_of_birth.readable = place_of_birth.writable = True

settings.customise_pr_person_resource = customise_pr_person_resource

def customise_pr_group_resource(r, tablename):
    
    messages = current.messages
    field = r.table.group_type
    pr_group_types = {1 : T("Family"),
                      2 : T("Tourist Group"),
                      3 : T("Relief Team"),
                      4 : T("other"),
                      5 : T("Mailing Lists"),
                      6 : T("Society"),
                      }
    field.represent = lambda opt: pr_group_types.get(opt, messages.UNKNOWN_OPT)
    field.requires = IS_IN_SET(pr_group_types, zero=None)

settings.customise_pr_group_resource = customise_pr_group_resource

# -----------------------------------------------------------------------------
def customise_event_event_resource(r, tablename):

    table = r.table
    table.exercise.default = True
    table.organisation_id.readable = table.organisation_id.writable = True
        
settings.customise_event_event_resource = customise_event_event_resource

# -----------------------------------------------------------------------------
def customise_project_location_resource(r, tablename):

    field = current.s3db.project_location.status_id
    field.readable = field.writable = True

settings.customise_project_location_resource = customise_project_location_resource

# -----------------------------------------------------------------------------
# Comment/uncomment modules here to disable/enable them
# @ToDo: Have the system automatically enable migrate if a module is enabled
# Modules menu is defined in modules/eden/menu.py
settings.modules = OrderedDict([
    # Core modules which shouldn't be disabled
    ("default", Storage(
        name_nice = T("Home"),
        restricted = False, # Use ACLs to control access to this module
        access = None,      # All Users (inc Anonymous) can see this module in the default menu & access the controller
        module_type = None  # This item is not shown in the menu
    )),
    ("admin", Storage(
        name_nice = T("Administration"),
        #description = "Site Administration",
        restricted = True,
        access = "|1|",     # Only Administrators can see this module in the default menu & access the controller
        module_type = None  # This item is handled separately for the menu
    )),
    ("appadmin", Storage(
        name_nice = T("Administration"),
        #description = "Site Administration",
        restricted = True,
        module_type = None  # No Menu
    )),
    ("errors", Storage(
        name_nice = T("Ticket Viewer"),
        #description = "Needed for Breadcrumbs",
        restricted = False,
        module_type = None  # No Menu
    )),
    ("sync", Storage(
        name_nice = T("Synchronization"),
        #description = "Synchronization",
        restricted = True,
        access = "|1|",     # Only Administrators can see this module in the default menu & access the controller
        module_type = None  # This item is handled separately for the menu
    )),
    ("translate", Storage(
        name_nice = T("Translation Functionality"),
        #description = "Selective translation of strings based on module.",
        module_type = None,
    )),
    ("gis", Storage(
        name_nice = T("Map"),
        #description = "Situation Awareness & Geospatial Analysis",
        restricted = True,
        module_type = 1,     # 6th item in the menu
    )),
    ("pr", Storage(
        name_nice = T("Person Registry"),
        #description = "Central point to record details on People",
        restricted = True,
        access = "|1|",     # Only Administrators can see this module in the default menu (access to controller is possible to all still)
        module_type = 10
    )),
    ("org", Storage(
        name_nice = T("Organizations"),
        #description = 'Lists "who is doing what & where". Allows relief agencies to coordinate their activities',
        restricted = True,
        module_type = 10
    )),
    # All modules below here should be possible to disable safely
    ("hrm", Storage(
        name_nice = T("Staff"),
        #description = "Human Resources Management",
        restricted = True,
        module_type = 10,
    )),
    ("vol", Storage(
        name_nice = T("Volunteers"),
        #description = "Human Resources Management",
        restricted = True,
        module_type = 10,
    )),
    ("doc", Storage(
        name_nice = T("Documents"),
        #description = "A library of digital resources, such as photos, documents and reports",
        restricted = True,
        module_type = 10,
    )),
    ("msg", Storage(
        name_nice = T("Messaging"),
        #description = "Sends & Receives Alerts via Email & SMS",
        restricted = True,
        # The user-visible functionality of this module isn't normally required. Rather it's main purpose is to be accessed from other modules.
        module_type = 2,
    )),
    ("cr", Storage(
        name_nice = T("Shelters"),
        #description = "Tracks the location, capacity and breakdown of victims in Shelters",
        restricted = True,
        module_type = 10
    )),
    ("evr", Storage(
         name_nice = T("Evacuees"),
         #description = "Evacuees Registry",
         restricted = True, # use Access Control Lists to see this module
         module_type = 7
    )),
    ("event", Storage(
        name_nice = T("Events"),
        #description = "Activate Events (e.g. from Scenario templates) for allocation of appropriate Resources (Human, Assets & Facilities).",
        restricted = True,
        module_type = 10,
    )),
])
