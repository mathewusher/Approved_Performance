# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class ApHubsPartNumbers(models.Model):
    beginning_year = models.IntegerField(blank=True, null=True)
    ending_year = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=13, blank=True)
    model = models.CharField(max_length=26, blank=True)
    fitment_notes = models.CharField(max_length=46, blank=True)
    ap_kit_number = models.CharField(max_length=8, blank=True)
    class Meta:
        managed = False
        db_table = 'AP_Hubs_Part_Numbers'

class AmazonListings(models.Model):
    item_sku = models.CharField(max_length=10, blank=True)
    external_product_id = models.CharField(max_length=10, blank=True)
    external_product_id_type = models.CharField(max_length=4, blank=True)
    gtin_exemption_reason = models.CharField(max_length=10, blank=True)
    related_product_id = models.CharField(max_length=10, blank=True)
    related_product_id_type = models.CharField(max_length=10, blank=True)
    item_name = models.CharField(max_length=111, blank=True)
    manufacturer = models.CharField(max_length=20, blank=True)
    part_number = models.CharField(max_length=7, blank=True)
    feed_product_type = models.CharField(max_length=8, blank=True)
    item_type = models.CharField(max_length=28, blank=True)
    product_subtype = models.CharField(max_length=10, blank=True)
    product_description = models.CharField(max_length=1977, blank=True)
    brand_name = models.CharField(max_length=20, blank=True)
    update_delete = models.CharField(max_length=6, blank=True)
    item_package_quantity = models.CharField(max_length=2, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    product_tax_code = models.CharField(max_length=9, blank=True)
    product_site_launch_date = models.CharField(max_length=10, blank=True)
    merchant_release_date = models.CharField(max_length=10, blank=True)
    restock_date = models.CharField(max_length=10, blank=True)
    map_price = models.CharField(max_length=10, blank=True)
    list_price = models.CharField(max_length=6, blank=True)
    standard_price = models.CharField(max_length=5, blank=True)
    sale_price = models.CharField(max_length=10, blank=True)
    sale_from_date = models.CharField(max_length=10, blank=True)
    sale_end_date = models.CharField(max_length=10, blank=True)
    condition_type = models.CharField(max_length=3, blank=True)
    condition_note = models.CharField(max_length=82, blank=True)
    quantity = models.CharField(max_length=3, blank=True)
    fulfillment_latency = models.CharField(max_length=10, blank=True)
    max_aggregate_ship_quantity = models.CharField(max_length=10, blank=True)
    offering_can_be_gift_messaged = models.CharField(max_length=10, blank=True)
    offering_can_be_giftwrapped = models.CharField(max_length=10, blank=True)
    is_discontinued_by_manufacturer = models.CharField(max_length=10, blank=True)
    missing_keyset_reason = models.CharField(max_length=10, blank=True)
    delivery_schedule_group_id = models.CharField(max_length=10, blank=True)
    item_volume_unit_of_measure = models.CharField(max_length=10, blank=True)
    item_volume = models.CharField(max_length=10, blank=True)
    item_weight_unit_of_measure = models.CharField(max_length=10, blank=True)
    item_weight = models.CharField(max_length=10, blank=True)
    item_length_unit_of_measure = models.CharField(max_length=2, blank=True)
    item_length = models.CharField(max_length=2, blank=True)
    item_height = models.CharField(max_length=2, blank=True)
    item_width = models.CharField(max_length=2, blank=True)
    website_shipping_weight_unit_of_measure = models.CharField(max_length=2, blank=True)
    website_shipping_weight = models.CharField(max_length=5, blank=True)
    item_display_diameter_unit_of_measure = models.CharField(max_length=10, blank=True)
    item_display_diameter = models.CharField(max_length=10, blank=True)
    style_keywords1 = models.CharField(max_length=26, blank=True)
    style_keywords2 = models.CharField(max_length=24, blank=True)
    style_keywords3 = models.CharField(max_length=10, blank=True)
    style_keywords4 = models.CharField(max_length=10, blank=True)
    style_keywords5 = models.CharField(max_length=10, blank=True)
    bullet_point1 = models.CharField(max_length=204, blank=True)
    bullet_point2 = models.CharField(max_length=371, blank=True)
    bullet_point3 = models.CharField(max_length=244, blank=True)
    bullet_point4 = models.CharField(max_length=232, blank=True)
    bullet_point5 = models.CharField(max_length=244, blank=True)
    specific_uses_keywords1 = models.CharField(max_length=26, blank=True)
    specific_uses_keywords2 = models.CharField(max_length=10, blank=True)
    specific_uses_keywords3 = models.CharField(max_length=10, blank=True)
    specific_uses_keywords4 = models.CharField(max_length=10, blank=True)
    specific_uses_keywords5 = models.CharField(max_length=10, blank=True)
    target_audience_keywords1 = models.CharField(max_length=10, blank=True)
    target_audience_keywords2 = models.CharField(max_length=10, blank=True)
    target_audience_keywords3 = models.CharField(max_length=10, blank=True)
    thesaurus_attribute_keywords1 = models.CharField(max_length=10, blank=True)
    thesaurus_attribute_keywords2 = models.CharField(max_length=10, blank=True)
    thesaurus_attribute_keywords3 = models.CharField(max_length=10, blank=True)
    thesaurus_attribute_keywords4 = models.CharField(max_length=10, blank=True)
    thesaurus_attribute_keywords5 = models.CharField(max_length=10, blank=True)
    generic_keywords1 = models.CharField(max_length=48, blank=True)
    generic_keywords2 = models.CharField(max_length=50, blank=True)
    generic_keywords3 = models.CharField(max_length=48, blank=True)
    generic_keywords4 = models.CharField(max_length=100, blank=True)
    generic_keywords5 = models.CharField(max_length=43, blank=True)
    catalog_number = models.CharField(max_length=7, blank=True)
    thesaurus_subject_keywords1 = models.CharField(max_length=10, blank=True)
    thesaurus_subject_keywords2 = models.CharField(max_length=11, blank=True)
    thesaurus_subject_keywords3 = models.CharField(max_length=11, blank=True)
    thesaurus_subject_keywords4 = models.CharField(max_length=10, blank=True)
    thesaurus_subject_keywords5 = models.CharField(max_length=10, blank=True)
    platinum_keywords1 = models.CharField(max_length=6, blank=True)
    platinum_keywords2 = models.CharField(max_length=10, blank=True)
    platinum_keywords3 = models.CharField(max_length=10, blank=True)
    platinum_keywords4 = models.CharField(max_length=10, blank=True)
    platinum_keywords5 = models.CharField(max_length=10, blank=True)
    main_image_url = models.CharField(max_length=56, blank=True)
    other_image_url1 = models.CharField(max_length=49, blank=True)
    other_image_url2 = models.CharField(max_length=50, blank=True)
    other_image_url3 = models.CharField(max_length=50, blank=True)
    other_image_url4 = models.CharField(max_length=49, blank=True)
    other_image_url5 = models.CharField(max_length=49, blank=True)
    other_image_url6 = models.CharField(max_length=50, blank=True)
    other_image_url7 = models.CharField(max_length=50, blank=True)
    other_image_url8 = models.CharField(max_length=61, blank=True)
    swatch_image_url = models.CharField(max_length=10, blank=True)
    fulfillment_center_id = models.CharField(max_length=10, blank=True)
    parent_child = models.CharField(max_length=10, blank=True)
    parent_sku = models.CharField(max_length=10, blank=True)
    relationship_type = models.CharField(max_length=10, blank=True)
    variation_theme = models.CharField(max_length=10, blank=True)
    legal_disclaimer_description = models.CharField(max_length=482, blank=True)
    prop_65 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement1 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement2 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement3 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement4 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_description = models.CharField(max_length=10, blank=True)
    country_of_origin = models.CharField(max_length=10, blank=True)
    abpa_partslink_number1 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number2 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number3 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number4 = models.CharField(max_length=10, blank=True)
    exterior_finish = models.CharField(max_length=10, blank=True)
    color_name = models.CharField(max_length=10, blank=True)
    color_map = models.CharField(max_length=10, blank=True)
    oe_manufacturer = models.CharField(max_length=10, blank=True)
    part_interchange_info = models.CharField(max_length=10, blank=True)
    department_name1 = models.CharField(max_length=10, blank=True)
    department_name2 = models.CharField(max_length=10, blank=True)
    department_name3 = models.CharField(max_length=10, blank=True)
    department_name4 = models.CharField(max_length=10, blank=True)
    department_name5 = models.CharField(max_length=10, blank=True)
    model_name = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number1 = models.CharField(max_length=90, blank=True)
    oem_equivalent_part_number2 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number3 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number4 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number5 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number1 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number2 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number3 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number4 = models.CharField(max_length=10, blank=True)
    part_type_id = models.CharField(max_length=10, blank=True)
    is_memorabilia = models.CharField(max_length=10, blank=True)
    is_autographed = models.CharField(max_length=10, blank=True)
    size_name = models.CharField(max_length=10, blank=True)
    size_map = models.CharField(max_length=10, blank=True)
    special_size_type = models.CharField(max_length=10, blank=True)
    material_type = models.CharField(max_length=10, blank=True)
    viscosity = models.CharField(max_length=10, blank=True)
    auto_part_position_id = models.CharField(max_length=10, blank=True)
    orientation = models.CharField(max_length=10, blank=True)
    control_type = models.CharField(max_length=10, blank=True)
    is_foldable = models.CharField(max_length=10, blank=True)
    heating_element_type = models.CharField(max_length=10, blank=True)
    lens_curvature = models.CharField(max_length=10, blank=True)
    included_components = models.CharField(max_length=10, blank=True)
    light_type = models.CharField(max_length=10, blank=True)
    special_features1 = models.CharField(max_length=27, blank=True)
    special_features2 = models.CharField(max_length=19, blank=True)
    special_features3 = models.CharField(max_length=9, blank=True)
    special_features4 = models.CharField(max_length=20, blank=True)
    special_features5 = models.CharField(max_length=10, blank=True)
    special_features6 = models.CharField(max_length=10, blank=True)
    special_features7 = models.CharField(max_length=10, blank=True)
    special_features8 = models.CharField(max_length=10, blank=True)
    external_testing_certification1 = models.CharField(max_length=9, blank=True)
    external_testing_certification2 = models.CharField(max_length=10, blank=True)
    external_testing_certification3 = models.CharField(max_length=10, blank=True)
    external_testing_certification4 = models.CharField(max_length=10, blank=True)
    external_testing_certification5 = models.CharField(max_length=10, blank=True)
    light_source_type = models.CharField(max_length=10, blank=True)
    operation_mode = models.CharField(max_length=10, blank=True)
    auto_part_profile = models.CharField(max_length=10, blank=True)
    pulley_type = models.CharField(max_length=10, blank=True)
    number_of_grooves = models.CharField(max_length=10, blank=True)
    warranty_description = models.CharField(max_length=253, blank=True)
    lifestyle1 = models.CharField(max_length=10, blank=True)
    lifestyle2 = models.CharField(max_length=10, blank=True)
    lifestyle3 = models.CharField(max_length=10, blank=True)
    lifestyle4 = models.CharField(max_length=10, blank=True)
    lifestyle5 = models.CharField(max_length=10, blank=True)
    fabric_type1 = models.CharField(max_length=10, blank=True)
    fabric_type2 = models.CharField(max_length=10, blank=True)
    fabric_type3 = models.CharField(max_length=10, blank=True)
    inner_material_type = models.CharField(max_length=10, blank=True)
    outer_material_type = models.CharField(max_length=10, blank=True)
    sole_material = models.CharField(max_length=10, blank=True)
    closure_type = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type1 = models.CharField(max_length=206, blank=True)
    compatible_with_vehicle_type2 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type3 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type4 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type5 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type6 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type7 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type8 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type9 = models.CharField(max_length=10, blank=True)
    minimum_height_recommendation_unit_of_measure = models.CharField(max_length=10, blank=True)
    minimum_height_recommendation = models.CharField(max_length=10, blank=True)
    maximum_height_recommendation_unit_of_measure = models.CharField(max_length=10, blank=True)
    maximum_height_recommendation = models.CharField(max_length=10, blank=True)
    waist_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    waist_size = models.CharField(max_length=10, blank=True)
    inseam_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    inseam_length = models.CharField(max_length=10, blank=True)
    sleeve_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    sleeve_length = models.CharField(max_length=10, blank=True)
    neck_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    neck_size = models.CharField(max_length=10, blank=True)
    chest_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    chest_size = models.CharField(max_length=10, blank=True)
    cup_size = models.CharField(max_length=10, blank=True)
    shoe_width = models.CharField(max_length=10, blank=True)
    heel_height_unit_of_measure = models.CharField(max_length=10, blank=True)
    heel_height = models.CharField(max_length=10, blank=True)
    heel_type = models.CharField(max_length=10, blank=True)
    shaft_height_unit_of_measure = models.CharField(max_length=10, blank=True)
    shaft_height = models.CharField(max_length=10, blank=True)
    belt_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    belt_length_derived = models.CharField(max_length=10, blank=True)
    belt_width_unit_of_measure = models.CharField(max_length=10, blank=True)
    belt_width_derived = models.CharField(max_length=10, blank=True)
    item_diameter_derived = models.CharField(max_length=10, blank=True)
    voltage = models.CharField(max_length=10, blank=True)
    wattage = models.CharField(max_length=10, blank=True)
    amperage_unit_of_measure = models.CharField(max_length=10, blank=True)
    amperage = models.CharField(max_length=10, blank=True)
    mfg_warranty_description_type = models.CharField(max_length=68, blank=True)
    item_diameter_unit_of_measure = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'Amazon_Listings'

class AmazonOrderReport(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    amazonorderid = models.CharField(db_column='AmazonOrderID', max_length=25, blank=True) # Field name made lowercase.
    amazonsessionid = models.CharField(db_column='AmazonSessionID', max_length=25, blank=True) # Field name made lowercase.
    orderdate = models.CharField(db_column='OrderDate', max_length=25, blank=True) # Field name made lowercase.
    orderposteddate = models.CharField(db_column='OrderPostedDate', max_length=25, blank=True) # Field name made lowercase.
    buyeremailaddress = models.CharField(db_column='BuyerEmailAddress', max_length=100, blank=True) # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=50, blank=True) # Field name made lowercase.
    buyerphonenumber = models.CharField(db_column='BuyerPhoneNumber', max_length=25, blank=True) # Field name made lowercase.
    fulfillmentmethod = models.CharField(db_column='FulfillmentMethod', max_length=15, blank=True) # Field name made lowercase.
    fulfillmentservicelevel = models.CharField(db_column='FulfillmentServiceLevel', max_length=15, blank=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True) # Field name made lowercase.
    addressfieldone = models.CharField(db_column='AddressFieldOne', max_length=50, blank=True) # Field name made lowercase.
    addressfieldtwo = models.CharField(db_column='AddressFieldTwo', max_length=50, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True) # Field name made lowercase.
    stateorregion = models.CharField(db_column='StateOrRegion', max_length=25, blank=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=25, blank=True) # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=10, blank=True) # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=25, blank=True) # Field name made lowercase.
    amazonorderitemcode = models.CharField(db_column='AmazonOrderItemCode', max_length=25) # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=250, blank=True) # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=25, blank=True) # Field name made lowercase.
    producttaxcode = models.CharField(db_column='ProductTaxCode', max_length=25, blank=True) # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=10, blank=True) # Field name made lowercase.
    itemamount = models.DecimalField(db_column='ItemAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    shippingtype = models.CharField(db_column='ShippingType', max_length=25, blank=True) # Field name made lowercase.
    shippingamount = models.DecimalField(db_column='ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    itemtaxtype = models.CharField(db_column='ItemTaxType', max_length=25, blank=True) # Field name made lowercase.
    itemtaxamount = models.DecimalField(db_column='ItemTaxAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    shippingtaxtype = models.CharField(db_column='ShippingTaxType', max_length=25, blank=True) # Field name made lowercase.
    shippingtaxamount = models.DecimalField(db_column='ShippingTaxAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    itemfeetype = models.CharField(db_column='ItemFeeType', max_length=25, blank=True) # Field name made lowercase.
    itemfeeamount = models.DecimalField(db_column='ItemFeeAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotionclaimcode = models.CharField(db_column='PromotionClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid = models.CharField(db_column='MerchantPromotionID', max_length=75, blank=True) # Field name made lowercase.
    promotiontype = models.CharField(db_column='PromotionType', max_length=25, blank=True) # Field name made lowercase.
    promotionamount = models.DecimalField(db_column='PromotionAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotionshippingtype = models.CharField(db_column='PromotionShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotionshippingamount = models.DecimalField(db_column='PromotionShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion2claimcode = models.CharField(db_column='Promotion2ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid2 = models.CharField(db_column='MerchantPromotionID2', max_length=75, blank=True) # Field name made lowercase.
    promotion2type = models.CharField(db_column='Promotion2Type', max_length=25, blank=True) # Field name made lowercase.
    promotion2amount = models.DecimalField(db_column='Promotion2Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion2shippingtype = models.CharField(db_column='Promotion2ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion2shippingamount = models.DecimalField(db_column='Promotion2ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion3claimcode = models.CharField(db_column='Promotion3ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid3 = models.CharField(db_column='MerchantPromotionID3', max_length=75, blank=True) # Field name made lowercase.
    promotion3type = models.CharField(db_column='Promotion3Type', max_length=25, blank=True) # Field name made lowercase.
    promotion3amount = models.DecimalField(db_column='Promotion3Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion3shippingtype = models.CharField(db_column='Promotion3ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion3shippingamount = models.DecimalField(db_column='Promotion3ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion4claimcode = models.CharField(db_column='Promotion4ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid4 = models.CharField(db_column='MerchantPromotionID4', max_length=75, blank=True) # Field name made lowercase.
    promotion4type = models.CharField(db_column='Promotion4Type', max_length=25, blank=True) # Field name made lowercase.
    promotion4amount = models.DecimalField(db_column='Promotion4Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion4shippingtype = models.CharField(db_column='Promotion4ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion4shippingamount = models.DecimalField(db_column='Promotion4ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    earliestshipdate = models.CharField(db_column='EarliestShipDate', max_length=25, blank=True) # Field name made lowercase.
    latestshipdate = models.CharField(db_column='LatestShipDate', max_length=25, blank=True) # Field name made lowercase.
    earliestdeliverydate = models.CharField(db_column='EarliestDeliveryDate', max_length=25, blank=True) # Field name made lowercase.
    latestdeliverydate = models.CharField(db_column='LatestDeliveryDate', max_length=25, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'Amazon_Order_Report'

class Customer(models.Model):
    customerid = models.IntegerField(db_column='customerID', primary_key=True) # Field name made lowercase.
    buyeremailaddress = models.CharField(db_column='BuyerEmailAddress', max_length=100, blank=True) # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=50, blank=True) # Field name made lowercase.
    buyerphonenumber = models.CharField(db_column='BuyerPhoneNumber', max_length=25, blank=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True) # Field name made lowercase.
    addressfieldone = models.CharField(db_column='AddressFieldOne', max_length=50, blank=True) # Field name made lowercase.
    addressfieldtwo = models.CharField(db_column='AddressFieldTwo', max_length=50, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True) # Field name made lowercase.
    stateorregion = models.CharField(db_column='StateOrRegion', max_length=25, blank=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=25, blank=True) # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=10, blank=True) # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=25, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'Customer'

class DmbPartNumbers(models.Model):
    item_sku = models.CharField(max_length=11, blank=True)
    external_product_id = models.CharField(max_length=10, blank=True)
    external_product_id_type = models.CharField(max_length=10, blank=True)
    gtin_exemption_reason = models.CharField(max_length=10, blank=True)
    related_product_id = models.CharField(max_length=10, blank=True)
    related_product_id_type = models.CharField(max_length=10, blank=True)
    item_name = models.CharField(max_length=125, blank=True)
    manufacturer = models.CharField(max_length=20, blank=True)
    part_number = models.CharField(max_length=8, blank=True)
    feed_product_type = models.CharField(max_length=8, blank=True)
    item_type = models.CharField(max_length=28, blank=True)
    product_subtype = models.CharField(max_length=10, blank=True)
    product_description = models.CharField(max_length=1985, blank=True)
    brand_name = models.CharField(max_length=20, blank=True)
    update_delete = models.CharField(max_length=6, blank=True)
    item_package_quantity = models.CharField(max_length=1, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    product_tax_code = models.CharField(max_length=9, blank=True)
    product_site_launch_date = models.CharField(max_length=1, blank=True)
    merchant_release_date = models.CharField(max_length=1, blank=True)
    restock_date = models.CharField(max_length=1, blank=True)
    map_price = models.CharField(max_length=1, blank=True)
    list_price = models.CharField(max_length=6, blank=True)
    standard_price = models.CharField(max_length=5, blank=True)
    sale_price = models.CharField(max_length=1, blank=True)
    sale_from_date = models.CharField(max_length=1, blank=True)
    sale_end_date = models.CharField(max_length=1, blank=True)
    condition_type = models.CharField(max_length=3, blank=True)
    condition_note = models.CharField(max_length=82, blank=True)
    quantity = models.CharField(max_length=3, blank=True)
    fulfillment_latency = models.CharField(max_length=1, blank=True)
    max_aggregate_ship_quantity = models.CharField(max_length=1, blank=True)
    offering_can_be_gift_messaged = models.CharField(max_length=1, blank=True)
    offering_can_be_giftwrapped = models.CharField(max_length=1, blank=True)
    is_discontinued_by_manufacturer = models.CharField(max_length=1, blank=True)
    missing_keyset_reason = models.CharField(max_length=1, blank=True)
    delivery_schedule_group_id = models.CharField(max_length=1, blank=True)
    item_volume_unit_of_measure = models.CharField(max_length=1, blank=True)
    item_volume = models.CharField(max_length=1, blank=True)
    item_weight_unit_of_measure = models.CharField(max_length=2, blank=True)
    item_weight = models.CharField(max_length=5, blank=True)
    item_length_unit_of_measure = models.CharField(max_length=2, blank=True)
    item_length = models.CharField(max_length=2, blank=True)
    item_height = models.CharField(max_length=2, blank=True)
    item_width = models.CharField(max_length=2, blank=True)
    website_shipping_weight_unit_of_measure = models.CharField(max_length=2, blank=True)
    website_shipping_weight = models.CharField(max_length=5, blank=True)
    item_display_diameter_unit_of_measure = models.CharField(max_length=1, blank=True)
    item_display_diameter = models.CharField(max_length=1, blank=True)
    style_keywords1 = models.CharField(max_length=26, blank=True)
    style_keywords2 = models.CharField(max_length=1, blank=True)
    style_keywords3 = models.CharField(max_length=1, blank=True)
    style_keywords4 = models.CharField(max_length=1, blank=True)
    style_keywords5 = models.CharField(max_length=1, blank=True)
    bullet_point1 = models.CharField(max_length=206, blank=True)
    bullet_point2 = models.CharField(max_length=103, blank=True)
    bullet_point3 = models.CharField(max_length=212, blank=True)
    bullet_point4 = models.CharField(max_length=165, blank=True)
    bullet_point5 = models.CharField(max_length=48, blank=True)
    specific_uses_keywords1 = models.CharField(max_length=26, blank=True)
    specific_uses_keywords2 = models.CharField(max_length=24, blank=True)
    specific_uses_keywords3 = models.CharField(max_length=1, blank=True)
    specific_uses_keywords4 = models.CharField(max_length=1, blank=True)
    specific_uses_keywords5 = models.CharField(max_length=1, blank=True)
    target_audience_keywords1 = models.CharField(max_length=1, blank=True)
    target_audience_keywords2 = models.CharField(max_length=1, blank=True)
    target_audience_keywords3 = models.CharField(max_length=1, blank=True)
    thesaurus_attribute_keywords1 = models.CharField(max_length=1, blank=True)
    thesaurus_attribute_keywords2 = models.CharField(max_length=1, blank=True)
    thesaurus_attribute_keywords3 = models.CharField(max_length=1, blank=True)
    thesaurus_attribute_keywords4 = models.CharField(max_length=1, blank=True)
    thesaurus_attribute_keywords5 = models.CharField(max_length=1, blank=True)
    generic_keywords1 = models.CharField(max_length=61, blank=True)
    generic_keywords2 = models.CharField(max_length=50, blank=True)
    generic_keywords3 = models.CharField(max_length=39, blank=True)
    generic_keywords4 = models.CharField(max_length=100, blank=True)
    generic_keywords5 = models.CharField(max_length=43, blank=True)
    catalog_number = models.CharField(max_length=8, blank=True)
    thesaurus_subject_keywords1 = models.CharField(max_length=10, blank=True)
    thesaurus_subject_keywords2 = models.CharField(max_length=11, blank=True)
    thesaurus_subject_keywords3 = models.CharField(max_length=11, blank=True)
    thesaurus_subject_keywords4 = models.CharField(max_length=10, blank=True)
    thesaurus_subject_keywords5 = models.CharField(max_length=1, blank=True)
    platinum_keywords1 = models.CharField(max_length=6, blank=True)
    platinum_keywords2 = models.CharField(max_length=1, blank=True)
    platinum_keywords3 = models.CharField(max_length=1, blank=True)
    platinum_keywords4 = models.CharField(max_length=1, blank=True)
    platinum_keywords5 = models.CharField(max_length=1, blank=True)
    main_image_url = models.CharField(max_length=58, blank=True)
    other_image_url1 = models.CharField(max_length=52, blank=True)
    other_image_url2 = models.CharField(max_length=54, blank=True)
    other_image_url3 = models.CharField(max_length=54, blank=True)
    other_image_url4 = models.CharField(max_length=54, blank=True)
    other_image_url5 = models.CharField(max_length=48, blank=True)
    other_image_url6 = models.CharField(max_length=10, blank=True)
    other_image_url7 = models.CharField(max_length=10, blank=True)
    other_image_url8 = models.CharField(max_length=61, blank=True)
    swatch_image_url = models.CharField(max_length=1, blank=True)
    fulfillment_center_id = models.CharField(max_length=1, blank=True)
    parent_child = models.CharField(max_length=1, blank=True)
    parent_sku = models.CharField(max_length=1, blank=True)
    relationship_type = models.CharField(max_length=1, blank=True)
    variation_theme = models.CharField(max_length=1, blank=True)
    legal_disclaimer_description = models.CharField(max_length=482, blank=True)
    prop_65 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement1 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement2 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement3 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_statement4 = models.CharField(max_length=10, blank=True)
    cpsia_cautionary_description = models.CharField(max_length=10, blank=True)
    country_of_origin = models.CharField(max_length=10, blank=True)
    abpa_partslink_number1 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number2 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number3 = models.CharField(max_length=10, blank=True)
    abpa_partslink_number4 = models.CharField(max_length=10, blank=True)
    exterior_finish = models.CharField(max_length=10, blank=True)
    color_name = models.CharField(max_length=10, blank=True)
    color_map = models.CharField(max_length=10, blank=True)
    oe_manufacturer = models.CharField(max_length=10, blank=True)
    part_interchange_info = models.CharField(max_length=10, blank=True)
    department_name1 = models.CharField(max_length=10, blank=True)
    department_name2 = models.CharField(max_length=10, blank=True)
    department_name3 = models.CharField(max_length=10, blank=True)
    department_name4 = models.CharField(max_length=10, blank=True)
    department_name5 = models.CharField(max_length=10, blank=True)
    model_name = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number1 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number2 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number3 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number4 = models.CharField(max_length=10, blank=True)
    oem_equivalent_part_number5 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number1 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number2 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number3 = models.CharField(max_length=10, blank=True)
    hollander_interchange_number4 = models.CharField(max_length=10, blank=True)
    part_type_id = models.CharField(max_length=10, blank=True)
    is_memorabilia = models.CharField(max_length=10, blank=True)
    is_autographed = models.CharField(max_length=10, blank=True)
    size_name = models.CharField(max_length=10, blank=True)
    size_map = models.CharField(max_length=10, blank=True)
    special_size_type = models.CharField(max_length=10, blank=True)
    material_type = models.CharField(max_length=10, blank=True)
    viscosity = models.CharField(max_length=10, blank=True)
    auto_part_position_id = models.CharField(max_length=10, blank=True)
    orientation = models.CharField(max_length=10, blank=True)
    control_type = models.CharField(max_length=10, blank=True)
    is_foldable = models.CharField(max_length=10, blank=True)
    heating_element_type = models.CharField(max_length=10, blank=True)
    lens_curvature = models.CharField(max_length=10, blank=True)
    included_components = models.CharField(max_length=10, blank=True)
    light_type = models.CharField(max_length=10, blank=True)
    special_features1 = models.CharField(max_length=27, blank=True)
    special_features2 = models.CharField(max_length=19, blank=True)
    special_features3 = models.CharField(max_length=9, blank=True)
    special_features4 = models.CharField(max_length=20, blank=True)
    special_features5 = models.CharField(max_length=10, blank=True)
    special_features6 = models.CharField(max_length=10, blank=True)
    special_features7 = models.CharField(max_length=10, blank=True)
    special_features8 = models.CharField(max_length=10, blank=True)
    external_testing_certification1 = models.CharField(max_length=10, blank=True)
    external_testing_certification2 = models.CharField(max_length=10, blank=True)
    external_testing_certification3 = models.CharField(max_length=10, blank=True)
    external_testing_certification4 = models.CharField(max_length=10, blank=True)
    external_testing_certification5 = models.CharField(max_length=10, blank=True)
    light_source_type = models.CharField(max_length=10, blank=True)
    operation_mode = models.CharField(max_length=10, blank=True)
    auto_part_profile = models.CharField(max_length=10, blank=True)
    pulley_type = models.CharField(max_length=10, blank=True)
    number_of_grooves = models.CharField(max_length=10, blank=True)
    warranty_description = models.CharField(max_length=10, blank=True)
    lifestyle1 = models.CharField(max_length=10, blank=True)
    lifestyle2 = models.CharField(max_length=10, blank=True)
    lifestyle3 = models.CharField(max_length=10, blank=True)
    lifestyle4 = models.CharField(max_length=10, blank=True)
    lifestyle5 = models.CharField(max_length=10, blank=True)
    fabric_type1 = models.CharField(max_length=10, blank=True)
    fabric_type2 = models.CharField(max_length=10, blank=True)
    fabric_type3 = models.CharField(max_length=10, blank=True)
    inner_material_type = models.CharField(max_length=10, blank=True)
    outer_material_type = models.CharField(max_length=10, blank=True)
    sole_material = models.CharField(max_length=10, blank=True)
    closure_type = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type1 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type2 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type3 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type4 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type5 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type6 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type7 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type8 = models.CharField(max_length=10, blank=True)
    compatible_with_vehicle_type9 = models.CharField(max_length=10, blank=True)
    minimum_height_recommendation_unit_of_measure = models.CharField(max_length=10, blank=True)
    minimum_height_recommendation = models.CharField(max_length=10, blank=True)
    maximum_height_recommendation_unit_of_measure = models.CharField(max_length=10, blank=True)
    maximum_height_recommendation = models.CharField(max_length=10, blank=True)
    waist_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    waist_size = models.CharField(max_length=10, blank=True)
    inseam_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    inseam_length = models.CharField(max_length=10, blank=True)
    sleeve_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    sleeve_length = models.CharField(max_length=10, blank=True)
    neck_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    neck_size = models.CharField(max_length=10, blank=True)
    chest_size_unit_of_measure = models.CharField(max_length=10, blank=True)
    chest_size = models.CharField(max_length=10, blank=True)
    cup_size = models.CharField(max_length=10, blank=True)
    shoe_width = models.CharField(max_length=10, blank=True)
    heel_height_unit_of_measure = models.CharField(max_length=10, blank=True)
    heel_height = models.CharField(max_length=10, blank=True)
    heel_type = models.CharField(max_length=10, blank=True)
    shaft_height_unit_of_measure = models.CharField(max_length=10, blank=True)
    shaft_height = models.CharField(max_length=10, blank=True)
    belt_length_unit_of_measure = models.CharField(max_length=10, blank=True)
    belt_length_derived = models.CharField(max_length=10, blank=True)
    belt_width_unit_of_measure = models.CharField(max_length=10, blank=True)
    belt_width_derived = models.CharField(max_length=10, blank=True)
    item_diameter_derived = models.CharField(max_length=10, blank=True)
    voltage = models.CharField(max_length=10, blank=True)
    wattage = models.CharField(max_length=10, blank=True)
    amperage_unit_of_measure = models.CharField(max_length=10, blank=True)
    amperage = models.CharField(max_length=10, blank=True)
    mfg_warranty_description_type = models.CharField(max_length=10, blank=True)
    item_diameter_unit_of_measure = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'DMB_Part_Numbers'

class FullCatalogFitment(models.Model):
    id = models.CharField(db_column='ID', max_length=5, blank=True) # Field name made lowercase.
    make = models.CharField(db_column='MAKE', max_length=13, blank=True) # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=27, blank=True) # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=4, blank=True) # Field name made lowercase.
    position = models.CharField(db_column='POSITION', max_length=14, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='APPLICATION', max_length=97, blank=True) # Field name made lowercase.
    ap_kit_num = models.CharField(db_column='AP KIT NUM', max_length=8, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    key = models.CharField(db_column='KEY', max_length=144, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FULL CATALOG FITMENT'

class Orders(models.Model):
    orderid = models.IntegerField(db_column='orderID', primary_key=True) # Field name made lowercase.
    amazonorderid = models.CharField(db_column='AmazonOrderID', max_length=25, blank=True) # Field name made lowercase.
    amazonsessionid = models.CharField(db_column='AmazonSessionID', max_length=25, blank=True) # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True) # Field name made lowercase.
    orderposteddate = models.CharField(db_column='OrderPostedDate', max_length=25, blank=True) # Field name made lowercase.
    fulfillmentmethod = models.CharField(db_column='FulfillmentMethod', max_length=15, blank=True) # Field name made lowercase.
    fulfillmentservicelevel = models.CharField(db_column='FulfillmentServiceLevel', max_length=15, blank=True) # Field name made lowercase.
    amazonorderitemcode = models.CharField(db_column='AmazonOrderItemCode', max_length=25) # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=250, blank=True) # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=25, blank=True) # Field name made lowercase.
    producttaxcode = models.CharField(db_column='ProductTaxCode', max_length=25, blank=True) # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=10, blank=True) # Field name made lowercase.
    itemamount = models.DecimalField(db_column='ItemAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    shippingtype = models.CharField(db_column='ShippingType', max_length=25, blank=True) # Field name made lowercase.
    shippingamount = models.DecimalField(db_column='ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    itemtaxtype = models.CharField(db_column='ItemTaxType', max_length=25, blank=True) # Field name made lowercase.
    itemtaxamount = models.DecimalField(db_column='ItemTaxAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    shippingtaxtype = models.CharField(db_column='ShippingTaxType', max_length=25, blank=True) # Field name made lowercase.
    shippingtaxamount = models.DecimalField(db_column='ShippingTaxAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    itemfeetype = models.CharField(db_column='ItemFeeType', max_length=25, blank=True) # Field name made lowercase.
    itemfeeamount = models.DecimalField(db_column='ItemFeeAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotionclaimcode = models.CharField(db_column='PromotionClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid = models.CharField(db_column='MerchantPromotionID', max_length=75, blank=True) # Field name made lowercase.
    promotiontype = models.CharField(db_column='PromotionType', max_length=25, blank=True) # Field name made lowercase.
    promotionamount = models.DecimalField(db_column='PromotionAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotionshippingtype = models.CharField(db_column='PromotionShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotionshippingamount = models.DecimalField(db_column='PromotionShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion2claimcode = models.CharField(db_column='Promotion2ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid2 = models.CharField(db_column='MerchantPromotionID2', max_length=75, blank=True) # Field name made lowercase.
    promotion2type = models.CharField(db_column='Promotion2Type', max_length=25, blank=True) # Field name made lowercase.
    promotion2amount = models.DecimalField(db_column='Promotion2Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion2shippingtype = models.CharField(db_column='Promotion2ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion2shippingamount = models.DecimalField(db_column='Promotion2ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion3claimcode = models.CharField(db_column='Promotion3ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid3 = models.CharField(db_column='MerchantPromotionID3', max_length=75, blank=True) # Field name made lowercase.
    promotion3type = models.CharField(db_column='Promotion3Type', max_length=25, blank=True) # Field name made lowercase.
    promotion3amount = models.DecimalField(db_column='Promotion3Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion3shippingtype = models.CharField(db_column='Promotion3ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion3shippingamount = models.DecimalField(db_column='Promotion3ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion4claimcode = models.CharField(db_column='Promotion4ClaimCode', max_length=25, blank=True) # Field name made lowercase.
    merchantpromotionid4 = models.CharField(db_column='MerchantPromotionID4', max_length=75, blank=True) # Field name made lowercase.
    promotion4type = models.CharField(db_column='Promotion4Type', max_length=25, blank=True) # Field name made lowercase.
    promotion4amount = models.DecimalField(db_column='Promotion4Amount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    promotion4shippingtype = models.CharField(db_column='Promotion4ShippingType', max_length=25, blank=True) # Field name made lowercase.
    promotion4shippingamount = models.DecimalField(db_column='Promotion4ShippingAmount', max_digits=25, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    earliestshipdate = models.CharField(db_column='EarliestShipDate', max_length=25, blank=True) # Field name made lowercase.
    latestshipdate = models.CharField(db_column='LatestShipDate', max_length=25, blank=True) # Field name made lowercase.
    earliestdeliverydate = models.CharField(db_column='EarliestDeliveryDate', max_length=25, blank=True) # Field name made lowercase.
    latestdeliverydate = models.CharField(db_column='LatestDeliveryDate', max_length=25, blank=True) # Field name made lowercase.
    customerid = models.ForeignKey(Customer, db_column='customerID') # Field name made lowercase.
    sbc_xml_generated = models.IntegerField()
    tracking_number_received = models.IntegerField()
    account_number = models.ForeignKey('MfgToAccountNumber', db_column='account_number')
    po_number = models.CharField(max_length=50, blank=True)
    tracking_number = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'Orders'

class TrackingNumbers(models.Model):
    po_number = models.ForeignKey(Orders, db_column='po_number', blank=True, null=True)
    tracking_number = models.CharField(max_length=50, blank=True)
    detail_line_type = models.CharField(max_length=10, blank=True)
    account_number = models.CharField(max_length=25, blank=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cost_parts = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sbc_reference_number = models.CharField(unique=True, max_length=25)
    date = models.CharField(max_length=8, blank=True)
    clerk_codes = models.CharField(max_length=25, blank=True)
    shipping_type = models.CharField(max_length=25, blank=True)
    customerid = models.ForeignKey(Customer, db_column='customerID', blank=True, null=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'Tracking_Numbers'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_migrations'

class MfgToAccountNumber(models.Model):
    mfg = models.CharField(max_length=3)
    account_number = models.CharField(max_length=25)
    marketplace = models.CharField(max_length=25)
    sold_to_company_name = models.CharField(max_length=25, blank=True)
    sold_to_street_address = models.CharField(max_length=100, blank=True)
    sold_to_city = models.CharField(max_length=50, blank=True)
    sold_to_state = models.CharField(max_length=2, blank=True)
    sold_to_zip_code = models.CharField(max_length=10, blank=True)
    sold_to_phone_number = models.CharField(max_length=20, blank=True)
    #id = models.BigIntegerField(db_column='ID') # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)
    class Meta:
        managed = True
        db_table = 'mfg_to_account_number'

class ZipCodes(models.Model):
    zip = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=8, blank=True)
    primary_city = models.CharField(max_length=27, blank=True)
    acceptable_cities = models.CharField(max_length=255, blank=True)
    unacceptable_cities = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    county = models.CharField(max_length=39, blank=True)
    timezone = models.CharField(max_length=28, blank=True)
    area_codes = models.CharField(max_length=21, blank=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    world_region = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=2, blank=True)
    decommissioned = models.IntegerField(blank=True, null=True)
    estimated_population = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=124, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'zip_codes'

