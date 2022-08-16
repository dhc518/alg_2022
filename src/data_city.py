class City:
  def __init__(self, name, x, y, index=0):
    self.name = name
    self.x, self.y = x, y
    self.index = index
  def __repr__(self):
    return f'{self.name}({self.index}:{self.x:3d},{self.y:3d})'
  def getName(self, **args):
    name = self.name
    if 'shows_city_index' in args and args['shows_city_index']:
      name = f'{self.index}.{name}'
    if 'shows_city_coord' in args and args['shows_city_coord']:
      name = f'{name}({self.x},{self.y})'
    if hasattr(self, 'weight'):
      name = f'{name} {self.weight})'
    return name
  @staticmethod
  def apply_index(cities):
    for i in range(len(cities)): 
      cities[i].index = i

five_letter_cities = [
  City("Clean", 1336, 536, 0),
  City("Prosy", 977, 860, 1),
  City("Rabbi", 6, 758, 2),
  City("Addle", 222, 261, 3),
  City("Smell", 1494, 836, 4),
  City("Quite", 905, 345, 5),
  City("Lives", 72, 714, 6),
  City("Cross", 23, 680, 7),
  City("Synth", 1529, 785, 8),
  City("Tweak", 1046, 426, 9),
  City("Medic", 1485, 514, 10),
  City("Glade", 660, 476, 11),
  City("Breve", 1586, 448, 12),
  City("Hotel", 1269, 576, 13),
  City("Toing", 398, 561, 14),
  City("Scorn", 617, 373, 15),
  City("Tweet", 1253, 403, 16),
  City("Zilch", 1289, 29, 17),
  City("React", 296, 659, 18),
  City("Fiche", 787, 278, 19),
  City("Stunt", 1123, 699, 20),
  City("Swing", 1113, 156, 21),
  City("Merry", 1002, 231, 22),
  City("Brine", 431, 53, 23),
  City("Miter", 126, 609, 24),
  City("Withy", 936, 432, 25),
  City("Brink", 1336, 404, 26),
  City("Madly", 1487, 104, 27),
  City("Spicy", 130, 498, 28),
  City("Cleft", 425, 506, 29),
  City("Cheep", 1511, 604, 30),
  City("Grief", 659, 683, 31),
  City("Links", 529, 850, 32),
  City("Write", 1345, 271, 33),
  City("Fixed", 434, 772, 34),
  City("Yobbo", 920, 848, 35),
  City("Grave", 868, 577, 36),
  City("Cress", 869, 678, 37),
  City("Ensue", 1209, 877, 38),
  City("Imply", 1544, 390, 39),
  City("Datum", 796, 235, 40),
  City("Quoit", 1281, 379, 41),
  City("Twain", 1220, 488, 42),
  City("Allow", 1192, 401, 43),
  City("Kiosk", 1131, 611, 44),
  City("Wheat", 1044, 133, 45),
  City("Birch", 1240, 519, 46),
  City("Flail", 1415, 72, 47),
  City("Thong", 190, 385, 48),
  City("Bongo", 528, 455, 49),
  City("Quilt", 800, 365, 50),
  City("Satyr", 1315, 172, 51),
  City("Alibi", 133, 245, 52),
  City("Auger", 442, 866, 53),
  City("Event", 218, 174, 54),
  City("Scowl", 206, 61, 55),
  City("Shelf", 928, 242, 56),
  City("Melon", 527, 416, 57),
  City("Scrap", 471, 625, 58),
  City("Drupe", 880, 13, 59),
  City("Nadir", 1163, 145, 60),
  City("Kudos", 1426, 806, 61),
  City("Pushy", 14, 429, 62),
  City("Bases", 742, 531, 63),
  City("Atone", 1037, 630, 64),
  City("Knife", 1025, 879, 65),
  City("Seise", 377, 257, 66),
  City("Odour", 614, 553, 67),
  City("Venom", 481, 676, 68),
  City("Filmy", 943, 53, 69),
  City("Barre", 88, 9, 70),
  City("Davit", 28, 271, 71),
  City("Smart", 952, 279, 72),
  City("Canon", 1426, 519, 73),
  City("Dixie", 699, 698, 74),
  City("Pease", 925, 716, 75),
  City("Adorn", 1132, 414, 76),
  City("Liver", 1371, 238, 77),
  City("Druid", 1389, 689, 78),
  City("Baked", 1573, 774, 79),
  City("Tulip", 915, 636, 80),
  City("Unzip", 941, 763, 81),
  City("Nervy", 1083, 385, 82),
  City("Hubby", 1297, 588, 83),
  City("Sweat", 764, 389, 84),
  City("Scald", 1536, 186, 85),
  City("Deity", 1098, 515, 86),
  City("Nutty", 1308, 65, 87),
  City("Mourn", 1111, 550, 88),
  City("Unbar", 566, 422, 89),
  City("Logic", 124, 105, 90),
  City("Stage", 620, 332, 91),
  City("Sisal", 784, 623, 92),
  City("Curvy", 182, 555, 93),
  City("Issue", 1413, 451, 94),
  City("Pilot", 1092, 660, 95),
  City("Wrote", 30, 217, 96),
  City("Quiff", 525, 148, 97),
  City("Willy", 1311, 887, 98),
  City("Plate", 1228, 353, 99),
  City("Nobel", 54, 68, 100),
  City("Chubb", 1155, 838, 101),
  City("Banjo", 467, 563, 102),
  City("Dirge", 86, 535, 103),
  City("Audit", 32, 630, 104),
  City("Rosin", 739, 766, 105),
  City("Scrag", 1386, 16, 106),
  City("Papal", 1565, 828, 107),
  City("Ducky", 868, 264, 108),
  City("Creed", 1301, 786, 109),
  City("Thief", 883, 415, 110),
  City("Pinko", 479, 534, 111),
  City("Hairy", 1101, 35, 112),
  City("Cobra", 671, 405, 113),
  City("Waken", 1478, 230, 114),
  City("Chime", 1343, 834, 115),
  City("Cower", 647, 97, 116),
  City("Whelp", 972, 447, 117),
  City("Milky", 327, 334, 118),
  City("Fauna", 716, 151, 119),
  City("Carob", 233, 411, 120),
  City("Locum", 486, 431, 121),
  City("Month", 1017, 381, 122),
  City("Check", 329, 830, 123),
  City("Dicey", 1286, 739, 124),
  City("Debit", 1528, 248, 125),
  City("Women", 216, 294, 126),
  City("Calve", 1306, 540, 127),
  City("Weepy", 204, 715, 128),
  City("Crash", 77, 120, 129),
  City("Durex", 97, 178, 130),
  City("Ovoid", 809, 28, 131),
  City("Aside", 354, 205, 132),
  City("Blame", 123, 551, 133),
  City("Stela", 248, 828, 134),
  City("Humph", 888, 139, 135),
  City("Amino", 594, 494, 136),
  City("Smash", 576, 702, 137),
  City("Sorry", 64, 218, 138),
  City("Muzzy", 1458, 739, 139),
  City("Camel", 1168, 460, 140),
  City("Sales", 1221, 19, 141),
  City("Biddy", 717, 594, 142),
  City("Indue", 1222, 414, 143),
  City("Jural", 1366, 204, 144),
  City("Tress", 1339, 366, 145),
  City("Egret", 179, 104, 146),
  City("Error", 1205, 547, 147),
  City("Ogive", 851, 719, 148),
  City("Frizz", 357, 152, 149),
  City("Quern", 1187, 204, 150),
  City("Divvy", 194, 886, 151),
  City("Style", 1137, 804, 152),
  City("Silky", 1592, 731, 153),
  City("Elver", 902, 886, 154),
  City("Strum", 1462, 398, 155),
  City("Sweep", 1437, 562, 156),
  City("Taste", 142, 403, 157),
  City("Largo", 794, 870, 158),
  City("There", 1036, 589, 159),
  City("Doric", 487, 266, 160),
  City("Slick", 610, 705, 161),
  City("Waive", 1536, 294, 162),
  City("Rejig", 729, 360, 163),
  City("Comet", 663, 136, 164),
  City("Punch", 347, 896, 165),
  City("Frill", 232, 751, 166),
  City("Dolby", 898, 597, 167),
  City("Saver", 1075, 694, 168),
  City("Brash", 1135, 268, 169),
  City("Sepoy", 195, 430, 170),
  City("Nippy", 842, 89, 171),
  City("Batty", 50, 190, 172),
  City("Unite", 1295, 460, 173),
  City("Promo", 1002, 705, 174),
  City("Towel", 692, 13, 175),
  City("Facia", 1581, 35, 176),
  City("Digit", 658, 26, 177),
  City("Ripen", 398, 445, 178),
  City("Sylph", 1177, 683, 179),
  City("Softy", 472, 391, 180),
  City("Radio", 159, 633, 181),
  City("Aback", 1490, 351, 182),
  City("Afore", 125, 772, 183),
  City("Sedan", 274, 798, 184),
  City("Ghyll", 698, 630, 185),
  City("Tying", 903, 794, 186),
  City("Mulch", 958, 209, 187),
  City("Caber", 174, 584, 188),
  City("Ghost", 82, 315, 189),
  City("Sheaf", 1547, 744, 190),
  City("Elfin", 1175, 361, 191),
  City("Squad", 340, 603, 192),
  City("Patch", 1057, 836, 193),
  City("Ester", 734, 281, 194),
  City("Roger", 145, 436, 195),
  City("Newel", 266, 193, 196),
  City("Tokay", 1296, 240, 197),
  City("Hydro", 1465, 190, 198),
  City("Tutti", 748, 109, 199),
  City("Infer", 76, 860, 200),
  City("Widow", 698, 437, 201),
  City("Hives", 1501, 417, 202),
  City("Inure", 831, 443, 203),
  City("Globe", 540, 553, 204),
  City("Cobol", 191, 679, 205),
  City("Annex", 514, 753, 206),
  City("Stout", 856, 367, 207),
  City("Ovary", 640, 761, 208),
  City("Wormy", 779, 427, 209),
  City("Pique", 57, 787, 210),
  City("Empty", 503, 478, 211),
  City("Snowy", 823, 569, 212),
  City("Oxbow", 104, 353, 213),
  City("Cinch", 21, 860, 214),
  City("Plumy", 434, 110, 215),
  City("Piety", 305, 46, 216),
  City("Craft", 1014, 149, 217),
  City("Fetch", 1121, 217, 218),
  City("Mosey", 699, 564, 219),
  City("Sense", 952, 696, 220),
  City("Tease", 1326, 324, 221),
  City("Handy", 625, 48, 222),
  City("Gismo", 1, 571, 223),
  City("Ditty", 1241, 896, 224),
  City("Coypu", 1270, 489, 225),
  City("Lunch", 1341, 118, 226),
  City("Screw", 338, 744, 227),
  City("Pager", 546, 626, 228),
  City("Ferry", 1564, 93, 229),
  City("Kinky", 331, 490, 230),
  City("Owlet", 1105, 440, 231),
  City("Guess", 912, 2, 232),
  City("Whisk", 465, 823, 233),
  City("Epoch", 287, 153, 234),
  City("Coney", 1433, 482, 235),
  City("Flour", 267, 525, 236),
  City("Spout", 328, 223, 237),
  City("Awoke", 639, 282, 238),
  City("Gnash", 467, 121, 239),
  City("Dinky", 701, 850, 240),
  City("Manic", 913, 385, 241),
  City("Nacho", 932, 469, 242),
  City("Rerun", 991, 780, 243),
  City("Serge", 1446, 442, 244),
  City("Flier", 1194, 849, 245),
  City("Waltz", 1570, 253, 246),
  City("Pubis", 1075, 761, 247),
  City("Shove", 1014, 822, 248),
  City("Bossa", 963, 410, 249),
  City("Swath", 376, 478, 250),
  City("Mousy", 526, 105, 251),
  City("Pivot", 1187, 769, 252),
  City("Frock", 1067, 16, 253),
  City("Muzak", 136, 23, 254),
  City("Bogie", 1272, 288, 255),
  City("Tenet", 1011, 428, 256),
  City("Impel", 77, 480, 257),
  City("Ahead", 1313, 206, 258),
  City("Stuck", 1294, 695, 259),
  City("Rural", 223, 495, 260),
  City("Judge", 321, 407, 261),
  City("Pommy", 644, 611, 262),
  City("Papaw", 1416, 714, 263),
  City("Senna", 273, 256, 264),
  City("Testa", 608, 437, 265),
  City("Slash", 564, 342, 266),
  City("Unity", 885, 53, 267),
  City("Roost", 1394, 512, 268),
  City("Dhoti", 1043, 319, 269),
  City("Solid", 1569, 196, 270),
  City("Dicky", 1223, 693, 271),
  City("Crier", 671, 644, 272),
  City("Seven", 590, 262, 273),
  City("Stick", 1531, 429, 274),
  City("Curse", 293, 756, 275),
  City("Haiku", 1026, 469, 276),
  City("Laver", 212, 609, 277),
  City("Amuse", 1281, 433, 278),
  City("Store", 711, 485, 279),
  City("Union", 961, 497, 280),
  City("Build", 1530, 535, 281),
  City("Knurl", 921, 319, 282),
  City("Rough", 706, 396, 283),
  City("Anion", 560, 268, 284),
  City("Nappy", 124, 215, 285),
  City("Solve", 821, 330, 286),
  City("Halal", 878, 185, 287),
  City("Assay", 414, 385, 288),
  City("Stile", 739, 642, 289),
  City("Bunny", 663, 566, 290),
  City("Ember", 38, 303, 291),
  City("Baron", 1470, 554, 292),
  City("Sauce", 531, 51, 293),
  City("Boost", 511, 517, 294),
  City("Spoof", 420, 632, 295),
  City("Ledge", 1365, 322, 296),
  City("Jolly", 768, 78, 297),
  City("Swift", 1539, 40, 298),
  City("Krone", 311, 793, 299),
  City("Fecal", 803, 156, 300),
  City("Badge", 359, 828, 301),
  City("Fusty", 889, 852, 302),
  City("Tumid", 1116, 292, 303),
  City("Leger", 1543, 872, 304),
  City("Waver", 768, 332, 305),
  City("Folly", 1396, 102, 306),
  City("Islam", 991, 57, 307),
  City("Squid", 1347, 652, 308),
  City("Fuzzy", 484, 16, 309),
  City("Hammy", 1552, 591, 310),
  City("Ducks", 354, 548, 311),
  City("Tongs", 217, 143, 312),
  City("Final", 1464, 9, 313),
  City("Foray", 454, 737, 314),
  City("Femme", 164, 868, 315),
  City("Groan", 1541, 121, 316),
  City("Vapid", 489, 882, 317),
  City("Iliac", 775, 24, 318),
  City("Crest", 1110, 786, 319),
  City("Skull", 143, 716, 320),
  City("Drive", 110, 470, 321),
  City("Melba", 351, 690, 322),
  City("Dingy", 1435, 126, 323),
  City("Wrack", 955, 825, 324),
  City("Emery", 616, 786, 325),
  City("Lucky", 1083, 107, 326),
  City("Savoy", 584, 748, 327),
  City("Trawl", 802, 501, 328),
  City("Zebra", 938, 130, 329),
  City("Tepid", 1360, 485, 330),
  City("Thick", 612, 91, 331),
  City("Objet", 270, 724, 332),
  City("Gouda", 1145, 750, 333),
  City("Sleep", 284, 104, 334),
  City("Downy", 134, 326, 335),
  City("Twine", 959, 557, 336),
  City("Penal", 1154, 553, 337),
  City("Owner", 504, 175, 338),
  City("Tangy", 852, 863, 339),
  City("Yield", 288, 898, 340),
  City("Mimic", 1111, 884, 341),
  City("Craze", 686, 512, 342),
  City("Dalai", 1049, 55, 343),
  City("Brand", 164, 823, 344),
  City("Wreak", 1599, 222, 345),
  City("Cameo", 301, 303, 346),
  City("Trump", 1034, 549, 347),
  City("Oakum", 568, 198, 348),
  City("Scrim", 38, 739, 349),
  City("Stray", 34, 898, 350),
  City("Clung", 259, 878, 351),
  City("Winch", 472, 321, 352),
  City("Brawl", 546, 718, 353),
  City("Crake", 471, 459, 354),
  City("Ducal", 1460, 59, 355),
  City("Gunny", 1364, 417, 356),
  City("Lapis", 411, 728, 357),
  City("Serum", 233, 680, 358),
  City("Split", 1115, 63, 359),
  City("Soggy", 1025, 31, 360),
  City("Fiend", 411, 137, 361),
  City("Taffy", 617, 890, 362),
  City("Crave", 1277, 630, 363),
  City("Lorry", 1528, 81, 364),
  City("Lurex", 1266, 348, 365),
  City("Seamy", 363, 413, 366),
  City("Polio", 607, 832, 367),
  City("Pools", 635, 511, 368),
  City("Jehad", 881, 522, 369),
  City("Cumin", 35, 542, 370),
  City("Hooch", 461, 595, 371),
  City("Humor", 428, 536, 372),
  City("Boron", 1322, 493, 373),
  City("Hippo", 1392, 627, 374),
  City("Axiom", 607, 407, 375),
  City("Spool", 355, 105, 376),
  City("Loyal", 179, 739, 377),
  City("Sumac", 47, 657, 378),
  City("Shalt", 437, 412, 379),
  City("Treat", 825, 205, 380),
  City("Taunt", 1415, 414, 381),
  City("Mayor", 964, 380, 382),
  City("Gripe", 1204, 586, 383),
  City("Hedge", 1028, 665, 384),
  City("Hajji", 1349, 745, 385),
  City("Spank", 266, 609, 386),
  City("Abaft", 1512, 150, 387),
  City("Hunch", 633, 162, 388),
  City("Swizz", 552, 486, 389),
  City("Bravo", 699, 342, 390),
  City("Nifty", 1057, 525, 391),
  City("Jihad", 992, 553, 392),
  City("Heart", 1155, 34, 393),
  City("Renal", 668, 263, 394),
  City("Curly", 782, 827, 395),
  City("Track", 14, 48, 396),
  City("Hello", 280, 851, 397),
  City("Creek", 1040, 699, 398),
  City("Maybe", 463, 52, 399),
  City("Resat", 237, 371, 400),
  City("Mealy", 809, 699, 401),
  City("Valid", 136, 372, 402),
  City("Aster", 1443, 777, 403),
  City("Umbra", 1380, 555, 404),
  City("April", 647, 197, 405),
  City("Ethos", 1205, 294, 406),
  City("Canal", 498, 349, 407),
  City("Fleck", 322, 152, 408),
  City("Could", 1160, 72, 409),
  City("Messy", 850, 153, 410),
  City("Honey", 1172, 803, 411),
  City("Litre", 943, 597, 412),
  City("Grist", 1365, 709, 413),
  City("Whore", 841, 396, 414),
  City("Paten", 1159, 398, 415),
  City("Mucus", 513, 609, 416),
  City("Whiff", 1194, 510, 417),
  City("Momma", 1591, 407, 418),
  City("Labor", 1201, 96, 419),
  City("Hobby", 836, 823, 420),
  City("Quake", 1228, 272, 421),
  City("Light", 1407, 208, 422),
  City("Crook", 1371, 156, 423),
  City("Gleam", 691, 296, 424),
  City("Bloom", 19, 370, 425),
  City("Cleat", 350, 50, 426),
  City("Pitta", 1159, 215, 427),
  City("Reign", 281, 357, 428),
  City("Twerp", 807, 744, 429),
  City("Aloft", 285, 425, 430),
  City("Abyss", 996, 500, 431),
  City("Decoy", 1420, 855, 432),
  City("Sperm", 309, 528, 433),
  City("Tilde", 996, 108, 434),
  City("Purge", 994, 333, 435),
  City("Debag", 813, 799, 436),
  City("Lousy", 863, 610, 437),
  City("Canst", 1012, 735, 438),
  City("Teeth", 855, 209, 439),
  City("Flood", 916, 214, 440),
  City("Borax", 121, 49, 441),
  City("Welch", 761, 232, 442),
  City("Ouija", 440, 218, 443),
  City("Salon", 707, 668, 444),
  City("Rebus", 1258, 800, 445),
  City("Pally", 522, 272, 446),
  City("Abbot", 1561, 419, 447),
  City("Poesy", 87, 400, 448),
  City("Stash", 682, 160, 449),
  City("Topee", 496, 807, 450),
  City("Fruit", 133, 180, 451),
  City("Yonks", 1564, 364, 452),
  City("Fatwa", 1511, 671, 453),
  City("Salty", 668, 72, 454),
  City("Shone", 800, 306, 455),
  City("Batch", 142, 281, 456),
  City("Apace", 1138, 457, 457),
  City("Usage", 502, 316, 458),
  City("Crime", 178, 327, 459),
  City("Catty", 1405, 760, 460),
  City("Phial", 867, 459, 461),
  City("Crone", 757, 474, 462),
  City("Appal", 381, 122, 463),
  City("Prank", 225, 340, 464),
  City("Plank", 592, 225, 465),
  City("Press", 1448, 622, 466),
  City("Virus", 168, 458, 467),
  City("Choir", 240, 93, 468),
  City("Dirty", 1407, 343, 469),
  City("Prise", 423, 177, 470),
  City("Chomp", 1216, 152, 471),
  City("Dower", 852, 506, 472),
  City("Phone", 394, 9, 473),
  City("Whale", 476, 89, 474),
  City("Bulky", 410, 841, 475),
  City("Thigh", 978, 744, 476),
  City("Shirk", 102, 816, 477),
  City("Scurf", 404, 271, 478),
  City("Worry", 1240, 49, 479),
  City("March", 732, 842, 480),
  City("Facer", 809, 115, 481),
  City("Soupy", 967, 621, 482),
  City("Shorn", 703, 883, 483),
  City("Piles", 980, 657, 484),
  City("Harem", 178, 212, 485),
  City("Olden", 1182, 611, 486),
  City("Ionic", 576, 148, 487),
  City("Genie", 1555, 152, 488),
  City("Mafia", 729, 443, 489),
  City("Bafta", 1118, 729, 490),
  City("Teddy", 864, 321, 491),
  City("Carib", 1488, 891, 492),
  City("Tabor", 402, 327, 493),
  City("Dogma", 568, 841, 494),
  City("Rider", 1485, 790, 495),
  City("Doggo", 1, 625, 496),
  City("Horse", 278, 388, 497),
  City("Blimp", 450, 265, 498),
  City("Slimy", 1399, 145, 499),
  City("Cloth", 246, 453, 500),
  City("Lease", 1151, 872, 501),
  City("Livid", 321, 184, 502),
  City("Tiara", 6, 107, 503),
  City("Tarty", 1514, 456, 504),
  City("Ocher", 944, 867, 505),
  City("Rondo", 1120, 114, 506),
  City("Bowie", 823, 56, 507),
  City("Crate", 876, 824, 508),
  City("Spick", 1426, 656, 509),
  City("Noose", 88, 251, 510),
  City("Seize", 744, 692, 511),
  City("Fiord", 1064, 481, 512),
  City("Music", 428, 671, 513),
  City("Front", 1351, 575, 514),
  City("Usury", 1264, 767, 515),
  City("Youth", 701, 238, 516),
  City("Jiffy", 1253, 95, 517),
  City("Gassy", 1248, 168, 518),
  City("Dolma", 1444, 237, 519),
  City("Trash", 553, 663, 520),
  City("Flora", 869, 889, 521),
  City("Newsy", 783, 899, 522),
  City("Weird", 597, 624, 523),
  City("Award", 211, 28, 524),
  City("Couch", 518, 378, 525),
  City("Bezel", 1560, 636, 526),
  City("Prowl", 55, 589, 527),
  City("Quirk", 2, 727, 528),
  City("Tench", 374, 768, 529),
  City("Brute", 1053, 207, 530),
  City("Salsa", 580, 391, 531),
  City("Exert", 205, 810, 532),
  City("Souse", 741, 197, 533),
  City("Khaki", 906, 86, 534),
  City("Dairy", 1477, 631, 535),
  City("Dumpy", 588, 867, 536),
  City("Venal", 180, 280, 537),
  City("Plain", 1069, 899, 538),
  City("Miser", 251, 150, 539),
  City("Squab", 1127, 660, 540),
  City("Sadhu", 1351, 25, 541),
  City("Borne", 351, 280, 542),
  City("Skiff", 162, 665, 543),
  City("Which", 1240, 847, 544),
  City("Going", 23, 147, 545),
  City("Femur", 1566, 488, 546),
  City("Chock", 274, 327, 547),
  City("Bract", 716, 743, 548),
  City("Prick", 214, 529, 549),
  City("Telly", 680, 795, 550),
  City("Hemal", 172, 784, 551),
  City("Whirr", 337, 660, 552),
  City("Offer", 735, 43, 553),
  City("Vaunt", 1525, 723, 554),
  City("Drawl", 762, 804, 555),
  City("Aware", 1480, 663, 556),
  City("Bidet", 1040, 264, 557),
  City("Lobar", 1219, 212, 558),
  City("Maple", 470, 193, 559),
  City("Moire", 250, 11, 560),
  City("Noise", 683, 763, 561),
  City("Vying", 1510, 639, 562),
  City("Parka", 1195, 56, 563),
  City("Donna", 105, 847, 564),
  City("Trice", 744, 570, 565),
  City("Drape", 1576, 698, 566),
  City("Train", 1495, 284, 567),
  City("Smite", 1098, 607, 568),
  City("Muggy", 650, 843, 569),
  City("Indie", 482, 718, 570),
  City("Viral", 1590, 805, 571),
  City("Flair", 1397, 278, 572),
  City("Weeny", 62, 623, 573),
  City("Clerk", 1198, 457, 574),
  City("Cigar", 411, 84, 575),
  City("Pipit", 1467, 590, 576),
  City("Unify", 432, 311, 577),
  City("Baulk", 997, 297, 578),
  City("Liege", 1097, 341, 579),
  City("Levee", 178, 172, 580),
  City("Capon", 156, 68, 581),
  City("Means", 1503, 551, 582),
  City("Twirp", 393, 617, 583),
  City("Elude", 668, 439, 584),
  City("Bream", 762, 664, 585),
  City("Bleep", 1297, 406, 586),
  City("Relax", 327, 72, 587),
  City("Prose", 1453, 270, 588),
  City("Hovel", 1586, 525, 589),
  City("Snail", 913, 169, 590),
  City("Mommy", 367, 664, 591),
  City("Uniat", 1468, 819, 592),
  City("Ethyl", 907, 754, 593),
  City("Vivid", 415, 802, 594),
  City("Abate", 1167, 115, 595),
  City("Erect", 1432, 886, 596),
  City("Motto", 694, 200, 597),
  City("Savor", 654, 377, 598),
  City("Busby", 1324, 602, 599),
  City("Tango", 375, 350, 600),
  City("Uncut", 1433, 373, 601),
  City("Snack", 1376, 807, 602),
  City("Slime", 532, 347, 603),
  City("Eagle", 799, 539, 604),
  City("Their", 51, 439, 605),
  City("Lisle", 199, 840, 606),
  City("Align", 25, 511, 607),
  City("Swiss", 945, 89, 608),
  City("Stoke", 1089, 823, 609),
  City("Nasal", 757, 144, 610),
  City("Queen", 1245, 618, 611),
  City("Lapse", 781, 589, 612),
  City("Marge", 319, 634, 613),
  City("Hades", 920, 566, 614),
  City("Vigil", 1179, 719, 615),
  City("Uvula", 985, 831, 616),
  City("Flaky", 1178, 324, 617),
  City("Adage", 381, 714, 618),
  City("Chain", 113, 741, 619),
  City("Obese", 1140, 6, 620),
  City("Therm", 319, 264, 621),
  City("Yukky", 14, 829, 622),
  City("Laird", 1503, 313, 623),
  City("Comma", 368, 873, 624),
  City("Evoke", 937, 523, 625),
  City("Fiber", 1483, 711, 626),
  City("Bread", 598, 187, 627),
  City("Nerve", 1292, 839, 628),
  City("Urban", 36, 92, 629),
  City("Tamil", 1241, 668, 630),
  City("Cycle", 1334, 786, 631),
  City("Newly", 524, 789, 632),
  City("Sappy", 175, 494, 633),
  City("Bitty", 1283, 122, 634),
  City("Least", 222, 205, 635),
  City("Torch", 279, 555, 636),
  City("Haste", 137, 685, 637),
  City("Nanny", 577, 112, 638),
  City("Bribe", 446, 3, 639),
  City("Human", 1295, 311, 640),
  City("Finch", 639, 660, 641),
  City("Broad", 175, 2, 642),
  City("Hymen", 1102, 186, 643),
  City("Dream", 1467, 485, 644),
  City("Blank", 1329, 692, 645),
  City("Slant", 1023, 345, 646),
  City("Dryly", 104, 289, 647),
  City("Lupus", 551, 131, 648),
  City("Terra", 829, 672, 649),
  City("Tutor", 901, 674, 650),
  City("Pedal", 219, 650, 651),
  City("Bough", 452, 156, 652),
  City("Abbey", 566, 586, 653),
  City("Picky", 531, 189, 654),
  City("Grime", 1508, 4, 655),
  City("Exult", 1376, 873, 656),
  City("Runny", 397, 882, 657),
  City("Bosom", 1253, 313, 658),
  City("Growl", 1025, 769, 659),
  City("Oasis", 1580, 311, 660),
  City("Sotto", 314, 709, 661),
  City("Bodge", 102, 144, 662),
  City("Brick", 387, 532, 663),
  City("Quire", 1149, 517, 664),
  City("Mushy", 209, 103, 665),
  City("Toxin", 261, 287, 666),
  City("Sever", 730, 83, 667),
  City("Stoic", 463, 490, 668),
  City("Sprig", 1069, 630, 669),
  City("Magic", 1401, 591, 670),
  City("Tubby", 822, 899, 671),
  City("Roman", 790, 55, 672),
  City("Fluid", 543, 221, 673),
  City("Blurt", 1176, 10, 674),
  City("Recto", 550, 767, 675),
  City("Title", 895, 443, 676),
  City("Jenny", 1447, 162, 677),
  City("Riven", 297, 824, 678),
  City("Fence", 86, 41, 679),
  City("Jelly", 800, 464, 680),
  City("Cubic", 1370, 365, 681),
  City("Quick", 313, 1, 682),
  City("Wroth", 1576, 573, 683),
  City("Friar", 82, 679, 684),
  City("Pinny", 1074, 281, 685),
  City("Tribe", 688, 119, 686),
  City("Pious", 1573, 891, 687),
  City("Xerox", 358, 631, 688),
  City("Tooth", 1074, 162, 689),
  City("Carat", 42, 410, 690),
  City("Spurn", 992, 5, 691),
  City("Worse", 210, 568, 692),
  City("Icing", 87, 604, 693),
  City("Kopek", 280, 463, 694),
  City("Cover", 634, 578, 695),
  City("Norse", 1032, 185, 696),
  City("Bacon", 621, 121, 697),
  City("Arris", 822, 280, 698),
  City("Sneak", 269, 68, 699),
  City("Crape", 502, 205, 700),
  City("Smoky", 1259, 714, 701),
  City("Lunge", 1459, 860, 702),
  City("Relay", 626, 247, 703),
  City("Jingo", 1358, 447, 704),
  City("Hurry", 1428, 9, 705),
  City("Renew", 672, 728, 706),
  City("Frame", 753, 601, 707),
  City("China", 286, 694, 708),
  City("Yacht", 387, 215, 709),
  City("Amity", 56, 361, 710),
  City("Flank", 113, 897, 711),
  City("Evict", 1075, 247, 712),
  City("Crazy", 550, 386, 713),
  City("Glint", 1324, 725, 714),
  City("Witty", 1219, 743, 715),
  City("Surly", 633, 2, 716),
  City("Cozen", 601, 582, 717),
  City("Craps", 59, 275, 718),
  City("Heavy", 507, 237, 719),
  City("Hover", 504, 646, 720),
  City("Satin", 410, 477, 721),
  City("Gross", 716, 313, 722),
  City("Horny", 1443, 340, 723),
  City("Nones", 1150, 585, 724),
  City("Reran", 30, 461, 725),
  City("Arrow", 598, 7, 726),
  City("Wreck", 199, 471, 727),
  City("Faddy", 995, 590, 728),
  City("Leery", 242, 42, 729),
  City("Prism", 1076, 451, 730),
  City("Honor", 1156, 628, 731),
  City("Baize", 1453, 305, 732),
  City("Vicar", 674, 896, 733),
  City("Cling", 1528, 360, 734),
  City("Scarp", 1536, 495, 735),
  City("Coach", 53, 13, 736),
  City("Squat", 79, 85, 737),
  City("Plaid", 535, 14, 738),
  City("Flout", 791, 196, 739),
  City("Fault", 1142, 369, 740),
  City("Udder", 43, 245, 741),
  City("Furry", 49, 833, 742),
  City("Nudge", 566, 69, 743),
  City("Fudge", 101, 440, 744),
  City("Huffy", 44, 122, 745),
  City("Bijou", 873, 647, 746),
  City("Grant", 1242, 467, 747),
  City("Image", 476, 237, 748),
  City("Sword", 565, 890, 749),
  City("Fatty", 305, 870, 750),
  City("Meths", 1306, 281, 751),
  City("Farce", 1477, 436, 752),
  City("Staff", 1397, 384, 753),
  City("Unsex", 58, 516, 754),
  City("Sherd", 445, 707, 755),
  City("Guest", 1064, 561, 756),
  City("Homey", 1593, 857, 757),
  City("Cheer", 567, 311, 758),
  City("Maria", 947, 2, 759),
  City("Forgo", 972, 149, 760),
  City("Decry", 853, 551, 761),
  City("Tough", 1009, 261, 762),
  City("Mambo", 1405, 43, 763),
  City("Wrest", 1504, 213, 764),
  City("Local", 1593, 339, 765),
  City("Lynch", 1365, 80, 766),
  City("Nasty", 853, 768, 767),
  City("Bigot", 1243, 126, 768),
  City("Hound", 1395, 176, 769),
  City("Ponce", 297, 605, 770),
  City("Stank", 1168, 289, 771),
  City("Cream", 99, 640, 772),
  City("Shaky", 1195, 238, 773),
  City("Bland", 389, 167, 774),
  City("Radii", 868, 110, 775),
  City("Smote", 1293, 93, 776),
  City("Zippy", 1270, 222, 777),
  City("Tunic", 1272, 668, 778),
  City("Helix", 524, 671, 779),
  City("Break", 884, 720, 780),
  City("Audio", 3, 339, 781),
  City("Guise", 976, 180, 782),
  City("Space", 1377, 839, 783),
  City("Small", 531, 304, 784),
  City("Amine", 1214, 182, 785),
  City("Admin", 817, 601, 786),
  City("Ducat", 891, 493, 787),
  City("Knell", 1138, 175, 788),
  City("Brace", 577, 541, 789),
  City("Saucy", 1099, 4, 790),
  City("Lupin", 458, 892, 791),
  City("Olive", 361, 447, 792),
  City("Whist", 627, 464, 793),
  City("Brain", 1170, 426, 794),
  City("Aglow", 8, 4, 795),
  City("Minim", 429, 600, 796),
  City("Irony", 81, 570, 797),
  City("Slurp", 1104, 482, 798),
  City("Sunny", 1059, 794, 799),
  City("Civil", 1524, 843, 800),
  City("Deter", 1113, 389, 801),
  City("Skirt", 344, 369, 802),
  City("Gooey", 81, 766, 803),
  City("Jammy", 648, 793, 804),
  City("Cease", 594, 674, 805),
  City("Jerry", 310, 123, 806),
  City("Shawl", 1074, 865, 807),
  City("Gamut", 892, 305, 808),
  City("Siege", 1221, 322, 809),
  City("Trite", 248, 569, 810),
  City("Force", 942, 663, 811),
  City("Manky", 510, 704, 812),
  City("Hoist", 1552, 5, 813),
  City("Glitz", 528, 882, 814),
  City("Laugh", 1363, 515, 815),
  City("Robin", 1498, 756, 816),
  City("Goner", 1588, 663, 817),
  City("Libra", 72, 156, 818),
  City("Allay", 782, 780, 819),
  City("Slake", 906, 266, 820),
  City("Chant", 1116, 580, 821),
  City("Fixer", 1002, 621, 822),
  City("Macho", 339, 859, 823),
  City("Canoe", 1219, 792, 824),
  City("Midst", 960, 321, 825),
  City("Dipso", 276, 29, 826),
  City("Maize", 1215, 628, 827),
  City("Tight", 1445, 687, 828),
  City("Shell", 378, 36, 829),
  City("Snipe", 1161, 248, 830),
  City("Mater", 525, 819, 831),
  City("Taupe", 1577, 122, 832),
  City("Shoot", 839, 13, 833),
  City("Trout", 953, 898, 834),
  City("Servo", 375, 306, 835),
  City("Blare", 496, 852, 836),
  City("Trews", 176, 248, 837),
  City("Blond", 1441, 93, 838),
  City("Still", 248, 635, 839),
  City("Taper", 261, 665, 840),
  City("Aegis", 967, 251, 841),
  City("Plush", 1106, 245, 842),
  City("Dwarf", 713, 781, 843),
  City("Prove", 504, 553, 844),
  City("Ounce", 377, 589, 845),
  City("Pagan", 158, 144, 846),
  City("Short", 828, 480, 847),
  City("Unman", 970, 28, 848),
  City("Cater", 1375, 774, 849),
  City("Woman", 1, 183, 850),
  City("Verve", 485, 766, 851),
  City("Gippy", 651, 316, 852),
  City("Croft", 1596, 491, 853),
  City("Blush", 438, 453, 854),
  City("Width", 74, 897, 855),
  City("Waged", 566, 800, 856),
  City("Gypsy", 572, 29, 857),
  City("Swung", 1032, 85, 858),
  City("Wader", 582, 454, 859),
  City("Grasp", 1320, 440, 860),
  City("Facet", 1306, 351, 861),
  City("Linen", 935, 350, 862),
  City("Eland", 1177, 889, 863),
  City("Peril", 311, 459, 864),
  City("Sahib", 840, 244, 865),
  City("Puppy", 1148, 327, 866),
  City("Mingy", 313, 577, 867),
  City("Thank", 1373, 603, 868),
  City("Clunk", 1548, 322, 869),
  City("Snick", 1590, 618, 870),
  City("Boule", 227, 886, 871),
  City("Spasm", 1243, 549, 872),
  City("Swoop", 657, 532, 873),
  City("Firry", 806, 411, 874),
  City("Panda", 1280, 874, 875),
  City("Taboo", 294, 232, 876),
  City("Knack", 414, 239, 877),
  City("Bimbo", 428, 344, 878),
  City("Imbed", 259, 770, 879),
  City("Clash", 1068, 358, 880),
  City("Polar", 1561, 542, 881),
  City("Pause", 1064, 600, 882),
  City("Leper", 398, 673, 883),
  City("Basso", 1489, 36, 884),
  City("Shire", 358, 3, 885),
  City("Filly", 1030, 503, 886),
  City("Prior", 463, 350, 887),
  City("Rumba", 1, 77, 888),
  City("Cheat", 381, 82, 889),
  City("Gutsy", 759, 742, 890),
  City("Provo", 741, 881, 891),
  City("Caret", 314, 374, 892),
  City("Magus", 1583, 164, 893),
  City("Dolor", 489, 143, 894),
  City("Shift", 140, 580, 895),
  City("Atoll", 1428, 287, 896),
  City("Demur", 720, 121, 897),
  City("Erase", 1295, 509, 898),
  City("Scots", 499, 54, 899),
  City("Opine", 1398, 308, 900),
  City("Tulle", 255, 495, 901),
  City("Miras", 27, 785, 902),
  City("Aisle", 1320, 2, 903),
  City("Adieu", 155, 541, 904),
  City("Knoll", 707, 535, 905),
  City("Bitch", 731, 6, 906),
  City("Yodel", 231, 784, 907),
  City("Legit", 1593, 78, 908),
  City("Hindi", 677, 829, 909),
  City("Every", 1079, 60, 910),
  City("Boric", 453, 653, 911),
  City("Lathe", 1552, 224, 912),
  City("Enemy", 827, 174, 913),
  City("Greed", 808, 85, 914),
  City("Awful", 824, 632, 915),
  City("Slice", 5, 303, 916),
  City("Easel", 635, 419, 917),
  City("Amiss", 1312, 140, 918),
  City("Thing", 167, 362, 919),
  City("Farsi", 402, 413, 920),
  City("Rusty", 615, 302, 921),
  City("Burin", 1495, 75, 922),
  City("Corny", 687, 45, 923),
  City("Tommy", 1245, 436, 924),
  City("Stead", 1599, 1, 925),
  City("Lunar", 855, 55, 926),
  City("Recce", 388, 817, 927),
  City("Death", 205, 233, 928),
  City("Magna", 591, 358, 929),
  City("Ideal", 463, 790, 930),
  City("Poste", 297, 492, 931),
  City("Nomen", 1552, 679, 932),
  City("Aloud", 673, 597, 933),
  City("Sarky", 1005, 201, 934),
  City("Stork", 998, 897, 935),
  City("Aries", 1466, 137, 936),
  City("Cufic", 1599, 287, 937),
  City("Moult", 732, 809, 938),
  City("Skint", 1181, 172, 939),
  City("Avail", 1227, 384, 940),
  City("Divot", 1204, 658, 941),
  City("Cissy", 1085, 723, 942),
  City("Cough", 799, 653, 943),
  City("Rouse", 467, 291, 944),
  City("Frisk", 660, 226, 945),
  City("Murky", 781, 126, 946),
  City("Slope", 1238, 583, 947),
  City("Genus", 174, 42, 948),
  City("Spree", 699, 82, 949),
  City("Patty", 554, 169, 950),
  City("Cello", 780, 707, 951),
  City("Moron", 886, 232, 952),
  City("Lento", 945, 173, 953),
  City("Sweet", 1127, 852, 954),
  City("Cryer", 361, 796, 955),
  City("Feast", 373, 380, 956),
  City("Loopy", 912, 37, 957),
  City("Funky", 1137, 487, 958),
  City("Snood", 1306, 652, 959),
  City("Thump", 1221, 73, 960),
  City("Combo", 1520, 899, 961),
  City("Stale", 1277, 59, 962),
  City("Whelm", 1215, 824, 963),
  City("Maser", 1340, 873, 964),
  City("Glare", 426, 893, 965),
  City("Buddy", 769, 516, 966),
  City("Primp", 1262, 12, 967),
  City("Floss", 1339, 237, 968),
  City("Crane", 1378, 654, 969),
  City("Ocean", 1509, 387, 970),
  City("Onset", 883, 384, 971),
  City("Baddy", 1051, 727, 972),
  City("Spiel", 1457, 525, 973),
  City("Shirt", 248, 222, 974),
  City("Curia", 946, 796, 975),
  City("Trunk", 6, 887, 976),
  City("Scamp", 16, 599, 977),
  City("Entry", 2, 254, 978),
  City("Carte", 199, 765, 979),
  City("Iraqi", 194, 633, 980),
  City("Chaos", 227, 854, 981),
  City("Crass", 443, 373, 982),
  City("Pesky", 2, 474, 983),
  City("Lotto", 132, 804, 984),
  City("Jesus", 1285, 190, 985),
  City("Shack", 110, 708, 986),
  City("Lover", 1248, 248, 987),
  City("Muddy", 1342, 186, 988),
  City("Liven", 500, 402, 989),
  City("Balmy", 1495, 178, 990),
  City("Donut", 1047, 395, 991),
  City("Lapel", 1371, 121, 992),
  City("Dippy", 446, 79, 993),
  City("Ratio", 1562, 63, 994),
  City("Gamma", 38, 708, 995),
  City("Knock", 259, 121, 996),
  City("Syrup", 1273, 544, 997),
  City("Neigh", 99, 503, 998),
  City("Washy", 660, 347, 999),
]

if __name__ == '__main__':
  # City.apply_index(five_letter_cities)
  print(f'{len(five_letter_cities)=}')
  print(f'Samples: {five_letter_cities[:30]}')

  cities = five_letter_cities[:100]
  # from vis import PlanarVisualizer as Visualizer
  from vis import Dummy as Visualizer
  vis = Visualizer('Cities Visualizer')
  vis.setup(vis.get_main_module())
  # for i in range(len(cities)):
  #   vis.set_city_level(i, i % vis.LEVELS_COUNT)
  vis.draw()
  vis.end()