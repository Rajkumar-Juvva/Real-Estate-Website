BEDROOM_CHOICES = (
        ('1RK', '1RK'),
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
        ('6BHK', '6BHK'),
        ('7BHK', '7BHK'),
        ('8BHK', '8BHK'),
        ('9BHK', '9BHK'),
        ('10BHK', '10BHK')
    )
BATHROOM_CHOICES = [(i, str(i)) for i in range(11)]

FLOOR_CHOICES = [(i,str(i)) for i in range(1,151)]
TOTAL_FLOOR_CHOICES = [(i,str(i)) for i in range(1,26)]

AREA_UNITS_CHOICES = (
        ('sq ft', 'sq ft'),
        ('sq mt', 'sq mt')
    )
VASTU_EXIT_CHOICES = (
        ('East', 'East'),
        ('West', 'West'),
        ('North', 'North'),
        ('South', 'South')
    )

INTERIORS_CHOICES = (
        ('Empty', 'Empty / Unfurnished'),
        ('Semi', 'Semi Furnished'),
        ('Fully', 'Fully Furnished')
    )

KITCHEN_CHOICES = (
        ('Empty', 'Empty'),
        ('Shelves', 'Shelves'),
        ('Modular', 'Modular')
    )
PANTRY_CHOICES=[(i, str(i)) for i in range(11)]

SALE_CHOICES = (
        ('new', 'New'),
        ('resale', 'Resale')
    )
PARKING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12')
    )
CERTIFICATION_CHOICES = (
        ('occupation_certificate', 'Occupation Certificate'),
        ('commencement_certificate', 'Commencement Certificate')
    )

POSSESSION_CHOICES = [
        ('ready_to_move', 'Ready To Move'),
        ('under_construction', 'Under Construction'),
    ]

AMENITIES_CHOICES = [
        ('SWIMMING_POOL', 'Swimming Pool'),
        ('GYM', 'Gym'),
        ('GARDEN', 'Garden'),
        ('ELEVATOR', 'Elevator'),
        ('VISITOR_PARKING', 'Visitor Parking'),
        ('WATER_HARVESTING', 'Water Harvesting'),
        ('SEWAGE_TREATMENT', 'Sewage Treatment'),
        ('INTERCOM', 'Intercom'),
        ('STAND_ALONE', 'Stand Alone'),
        ('GATED_COMPLEX', 'Gated Complex'),
    ]
AMENITIES_CHOICES_COMMERCIAL_OFFICE = [
        ('ELEVATOR', 'Elevator'),
        ('VISITOR_PARKING', 'Visitor Parking'),
        ('WATER_CONNECTION', 'Water Connection'),
        ('SEWAGE_TREATMENT', 'Sewage Treatment'),
        ('INTERCOM', 'Intercom'),
        ('SERVICE_ELEVATOR', 'Service Elevator'),
        ('SECURITY', 'Security'),
    ]
AMENITIES_CHOICES_SHOP = [
        ('VISITOR_PARKING', 'Visitor Parking'),
        ('WATER_HARVESTING', 'Water Harvesting'),
        ('SEWAGE_TREATMENT', 'Sewage Treatment'),
        ('INTERCOM', 'Intercom'),
        ('GARBAGE_DISPOSAL', 'Garbage Disposal'),
        ('SECURITY', 'Security'),
    ]
AMENITIES_CHOICE_COTTAGE = [
    ('VISITOR_PARKING', 'Visitor Parking'),
    ('INDEPENDENT', 'Independent'),
    ('GATED_COMMUNITY', 'Gated Community'),
    ('WATER_HARVESTING', 'Water Harvesting'),
    ('SEWAGE_TREATMENT', 'Sewage Treatment'),
    ('INTERCOM', 'Intercom'),
]
OTHER_FEATURES_CHOICES = [
        ('PIPE_GAS', 'Pipe Gas'),
        ('PET_FRIENDLY', 'Pet Friendly'),
        ('BACHELOR_FRIENDLY', 'Bachelor Friendly'),
        ('FAMILY_ONLY', 'Family Only'),
        ('WORKING_PROFESSIONALS', 'Working Professionals'),
        ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'),
        ('THREE_PHASE_CONNECTION', 'Three Phase Connection'),
        ('JODI', 'Jodi'),
        ('EXCLUSIVE_VIEWS', 'Exclusive Views'),
]
OTHER_FEATURES_CHOICES_COMMERCIAL_OFFICE = [
        ('MEZANINE', 'Mezanine'),
        ('ROAD_FACING', 'Road Facing'),
        ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'),
        ('THREE_PHASE_CONNECTION', 'Three Phase Connection'),
        ('FIRE_EXIT', 'Fire Exit'),
        ('PILLARLESS', 'Pillarless'),
        ('JODI', 'Jodi'),
    ]

OTHER_FEATURES_CHOICES_SHOP = [
        ('ROAD_TOUCH', 'Road Touch'),
        ('JODI', 'Jodi'),
        ('MEZANINE', 'Mezanine'),
        ('BASEMENT','Basement'),
        ('ROAD_FACING', 'Road Facing'),
        ('WATER_CONNECTION', 'Water Connection'),
        ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'),
        ('THREE_PHASE_CONNECTION', 'Three Phase Connection'),
        ('FIRE_EXIT', 'Fire Exit'),
        ('PILLARLESS', 'Pillarless'),
        ('GAS_PIPELINE', 'Gas Pipeline'),
    ]
OTHER_FEATURES_CHOICES_COTTAGE = [
    ('PET_FRIENDLY', 'Pet Friendly'),
    ('BACHELOR_FRIENDLY', 'Bachelor Friendly'),
    ('WORKING_PROFESSIONALS', 'Working Professionals'),
    ('FAMILY_ONLY', 'Family Only'),
    ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'),
    ('THREE_PHASE_CONNECTION', 'Three Phase Connection'),
    ('PIPE_GAS', 'Pipe Gas'),
    ('ROAD_TOUCH', 'Road Touch'),
    ('JODI', 'Jodi'),
]

PROPERTY_STATUS_CHOICES = [
        ('to_confirm', 'To Confirm'),
        ('active', 'Active'),
        ('sold', 'Sold'),
    ]

LEAD_STATUS_CHOICES = (
    ('uncontacted', 'Uncontacted'),
    ('contacted', 'Contacted'),
    ('follow_up', 'Follow up'),
    ('field_visit', 'Field Visit'),
    ('cold', 'Cold'),
    ('won', 'Won'),
)

labels = ( ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),)

PROPERTY_UTILITY_CHOICES = (
        ('Agricultural', 'Agricultural'),
        ('Commercial', 'Commercial'),
        ('Educational', 'Educational'),
        ('Hospital', 'Hospital'),
        ('Industrial', 'Industrial'),
        ('Lodging / Hotel', 'Lodging / Hotel'),
        ('Recreational', 'Recreational'),
        ('Residential', 'Residential'),
        ('Restaurant / Dinner', 'Restaurant / Dinner'),
)
CONTACT_LABELS = (
    ('client', 'Client'),
    ('brokers_estate_agents', 'Brokers/Estate Agents'),
    ('developers', 'Developers'),
    ('maintenance', 'Maintenance'),
    ('it_support', 'IT Support'),
    ('legal', 'Legal'),
    ('others', 'Others'),
)

OPEN_SPACE_CHOICES = (
('Terrace', 'Terrace'),
('Balcony', 'Balcony'),
('Deck', 'Deck'),
('Lawn', 'Lawn'),
)

