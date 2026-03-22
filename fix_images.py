#!/usr/bin/env python3
"""Replace all local images/ paths in index.html with appropriate Unsplash URLs."""

import re

# Maps image filename (or alt text keyword) -> Unsplash URL
# Key is the local filename (without path)
REPLACEMENTS = {
    # ── Breakfast / Brunch ──────────────────────────────────────────────────
    'tin_gmaps_0.jpg':           'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600&h=400&fit=crop',  # garden cafe brunch
    'fried_4023_bing_mass.jpg':  'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=600&h=400&fit=crop',  # fried egg sandwich
    'broder_38_final.jpg':       'https://images.unsplash.com/photo-1533920379810-6bed961503f1?w=600&h=400&fit=crop',  # Scandinavian brunch / eggs
    'sweedeedee_8622_bing_mass.jpg': 'https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?w=600&h=400&fit=crop',  # bakery pastries

    # ── Japanese ────────────────────────────────────────────────────────────
    'takibisnow_358_bing_mass.jpg':   'https://images.unsplash.com/photo-1547592180-85f173990554?w=600&h=400&fit=crop',  # Japanese outdoor/campfire
    'muratarestaurant_gmaps_1.jpg':   'https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600&h=400&fit=crop',  # sushi platter
    'afuri_auth_0.jpg':               'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&h=400&fit=crop',  # ramen bowl
    'tanaka_2060_bing_mass.jpg':      'https://images.unsplash.com/photo-1554433607-66b5efe9d304?w=600&h=400&fit=crop',  # katsu sandwich
    'yokai_auth_5.jpg':               'https://images.unsplash.com/photo-1559410545-0bdcd187e0a6?w=600&h=400&fit=crop',  # onigiri/musubi
    'nimblefish_1451_bing_mass.jpg':  'https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600&h=400&fit=crop',  # sashimi/omakase
    'nodoguro_gmaps_1.jpg':           'https://images.unsplash.com/photo-1617196034738-26c5f7c977ce?w=600&h=400&fit=crop',  # Japanese kaiseki
    'obon_gmaps_17.jpg':              'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600&h=400&fit=crop',  # Japanese set meal
    'wakitchenkuu_gmaps_1.jpg':       'https://images.unsplash.com/photo-1617196034092-87a40ef64840?w=600&h=400&fit=crop',  # Japanese small plates
    'tokyo_gmaps_19.jpg':             'https://images.unsplash.com/photo-1554433607-66b5efe9d304?w=600&h=400&fit=crop',  # Japanese sandwich
    'onigiri_gmaps_20.jpg':           'https://images.unsplash.com/photo-1559410545-0bdcd187e0a6?w=600&h=400&fit=crop',  # onigiri
    'soen_1591_bing_mass.jpg':        'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&h=400&fit=crop',  # shaved ice / kakigori
    'premium_auth_14.jpg':            'https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=600&h=400&fit=crop',  # matcha latte

    # ── Thai / SE Asian ──────────────────────────────────────────────────────
    'nongs.jpg':                  'https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=600&h=400&fit=crop',  # khao man gai
    'hat_6733_bing_mass.jpg':     'https://images.unsplash.com/photo-1562802378-063ec186a863?w=600&h=400&fit=crop',  # Thai fried chicken
    'eem_gmaps_7.jpg':            'https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=600&h=400&fit=crop',  # Thai BBQ
    'gadogado_gmaps_1.jpg':       'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&h=400&fit=crop',  # Indonesian gado gado
    'langbaan_gmaps_21.jpg':      'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=600&h=400&fit=crop',  # Thai fine dining
    'okchicken_gmaps_1.jpg':      'https://images.unsplash.com/photo-1562802378-063ec186a863?w=600&h=400&fit=crop',  # fried chicken
    'paadee_3810_bing_mass.jpg':  'https://images.unsplash.com/photo-1559847844-5315695dadae?w=600&h=400&fit=crop',  # Thai street food

    # ── Italian / Pizza ──────────────────────────────────────────────────────
    'nostrana_3327_bing_mass.jpg': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&h=400&fit=crop',  # wood-fired pizza
    'campana_gmaps_10.jpg':        'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600&h=400&fit=crop',  # Italian restaurant
    'luce_gmaps_1.jpg':            'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # Italian fine dining

    # ── French / European ────────────────────────────────────────────────────
    'st_yelp_4.jpg':               'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&h=400&fit=crop',  # French bakery boulangerie
    'jacqueline_6150_bing_mass.jpg': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French fine dining
    'stjack_gmaps_1.jpg':           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French bistro
    'murice_gmaps_1.jpg':           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French fine dining
    'cestsibon_gmaps_1.jpg':        'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French bistro
    'coquine_gmaps_1.jpg':          'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French neighborhood bistro
    'bergerac_9677_bing_mass.jpg':  'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French bistro

    # ── Korean ───────────────────────────────────────────────────────────────
    'han_8684_bing_mass.jpg':     'https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=600&h=400&fit=crop',  # Korean home cooking

    # ── African ──────────────────────────────────────────────────────────────
    'akadi_1510_bing_mass.jpg':   'https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=600&h=400&fit=crop',  # West African food

    # ── Asian noodles / misc ─────────────────────────────────────────────────
    'franks_auth_10.jpg':         'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&h=400&fit=crop',  # noodle bowl

    # ── Indian ───────────────────────────────────────────────────────────────
    'bollywood_2385_bing_mass.jpg': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=600&h=400&fit=crop',  # Indian street food

    # ── Russian / Eastern European ───────────────────────────────────────────
    'kachka_gmaps_35.jpg':        'https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&h=400&fit=crop',  # Russian/Eastern European food

    # ── Tex-Mex / Mexican ────────────────────────────────────────────────────
    'javelina_gmaps_36.jpg':      'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600&h=400&fit=crop',  # Tex-Mex
    'por_yelp_14.jpg':            'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600&h=400&fit=crop',  # tacos

    # ── Upscale / American ───────────────────────────────────────────────────
    'higgins_2306_bing_mass.jpg': 'https://images.unsplash.com/photo-1550966871-3ed3cdb51f3a?w=600&h=400&fit=crop',  # upscale restaurant plate

    # ── Casual American / Sandwiches ─────────────────────────────────────────
    'lardo_42_final.jpg':         'https://images.unsplash.com/photo-1553909489-cd47e0907980?w=600&h=400&fit=crop',  # pork sandwich
    'lottie_2213_bing_mass.jpg':  'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600&h=400&fit=crop',  # casual restaurant
    'cartopia_gmaps_44.jpg':      'https://images.unsplash.com/photo-1565123409695-7b5ef63a2efb?w=600&h=400&fit=crop',  # food carts/trucks
    'the_25_final.jpg':           'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600&h=400&fit=crop',  # restaurant

    # ── Sports Bar ───────────────────────────────────────────────────────────
    'the_bing_exterior.jpg':      'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=600&h=400&fit=crop',  # sports bar

    # ── Latin / Vietnamese fusion ─────────────────────────────────────────────
    'la_gmaps_24.jpg':            'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=600&h=400&fit=crop',  # Asian fusion
    'la_gmaps_104.jpg':           'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600&h=400&fit=crop',  # Mexican

    # ── Ice Cream / Sweets ───────────────────────────────────────────────────
    'saltandstraw.jpg':           'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&h=400&fit=crop',  # artisan ice cream scoops
    'pips_gmaps_46.jpg':          'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&h=400&fit=crop',  # mini donuts

    # ── Patisserie / Cakes ────────────────────────────────────────────────────
    'pix_yelp_16.jpg':            'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&h=400&fit=crop',  # French patisserie/fancy cake

    # ── Matcha / Tea ─────────────────────────────────────────────────────────
    'mako_9916_bing_mass.jpg':    'https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=600&h=400&fit=crop',  # matcha
    'project_yelp_17.jpg':        'https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=600&h=400&fit=crop',  # matcha

    # ── Donuts ────────────────────────────────────────────────────────────────
    'mikiko_1811_bing_mass.jpg':  'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&h=400&fit=crop',  # mochi donuts
    'bluestar.jpg':               'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&h=400&fit=crop',  # donuts
    'voodoo_58_final.jpg':        'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&h=400&fit=crop',  # Voodoo donuts

    # ── Custard / Cream Desserts ──────────────────────────────────────────────
    'cornet_9270_bing_mass.jpg':  'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&h=400&fit=crop',  # custard/cream puff

    # ── Pie / Bakery ─────────────────────────────────────────────────────────
    'lauretta_4984_bing_mass.jpg': 'https://images.unsplash.com/photo-1621743478914-cc8a86d7e7b5?w=600&h=400&fit=crop',  # fruit pie
    'papa_61_final.jpg':           'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&h=400&fit=crop',  # cake/dessert
    'kens_62_final.jpg':           'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&h=400&fit=crop',  # artisan bread/bakery
    'little_bing_exterior.jpg':    'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&h=400&fit=crop',  # bakery

    # ── Coffee ────────────────────────────────────────────────────────────────
    'barista_yelp_fixed.jpg':      'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&h=400&fit=crop',  # latte art
    'heart_5321_bing_mass.jpg':    'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&h=400&fit=crop',  # latte art pour
    'stumptown_bing_exterior.jpg': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&h=400&fit=crop',  # coffee
    'coava_4507_bing_mass.jpg':    'https://images.unsplash.com/photo-1541167760496-1628856ab772?w=600&h=400&fit=crop',  # coffee roastery interior
    'eyesore_gmaps_55.jpg':        'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600&h=400&fit=crop',  # quirky cafe interior
    'geekeasy_56_final.jpg':       'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600&h=400&fit=crop',  # anime cafe

    # ── Cafe ──────────────────────────────────────────────────────────────────
    'electrica_2761_bing_mass.jpg': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600&h=400&fit=crop',  # cafe interior

    # ── Shopping / Retail ────────────────────────────────────────────────────
    'muji_gmaps_68.jpg':            'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&h=400&fit=crop',  # minimalist store
    'kiriko_6886_bing_mass.jpg':    'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&h=400&fit=crop',  # handcrafted goods
    'kinokuniya_gmaps_70.jpg':      'https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=600&h=400&fit=crop',  # bookstore
    'the_5832_bing_mass.jpg':       'https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=600&h=400&fit=crop',  # specialty food/chocolate shop
    'hawthorne_6193_bing_mass.jpg': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&h=400&fit=crop',  # kitchen knives cutlery
    'kitchen_8213_bing_mass.jpg':   'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&h=400&fit=crop',  # kitchenware store
    'powells_2929_bing_mass.jpg':   'https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=600&h=400&fit=crop',  # Powell's Books
    'oblation_1709_bing_mass.jpg':  'https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=600&h=400&fit=crop',  # paper/stationery shop

    # ── Parks / Nature / Landmarks ───────────────────────────────────────────
    'portland_gmaps_76.jpg':        'https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=600&h=400&fit=crop',  # Japanese garden
    'sakura.jpg':                   'https://images.unsplash.com/photo-1522383225653-ed111181a951?w=600&h=400&fit=crop',  # cherry blossoms waterfront
    'forest_gmaps_78.jpg':          'https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&h=400&fit=crop',  # forest trail
    'pittock_gmaps_79.jpg':         'https://images.unsplash.com/photo-1509316785289-025f5b846b35?w=600&h=400&fit=crop',  # historic mansion
    'portland_gmaps_80.jpg':        'https://images.unsplash.com/photo-1565123409695-7b5ef63a2efb?w=600&h=400&fit=crop',  # Portland Saturday Market
    'mt_gmaps_81.jpg':              'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop',  # volcanic peak Mt Tabor
    'forest_7185_bing_mass.jpg':    'https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&h=400&fit=crop',  # forest park
    'oregon_gmaps_88.jpg':          'https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=600&h=400&fit=crop',  # zoo animals
    'portland_gmaps_89.jpg':        'https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=600&h=400&fit=crop',  # farmers market
    'portland_6212_bing_mass.jpg':  'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&h=400&fit=crop',  # flea market vintage
    'multnomah_5707_bing_mass.jpg': 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600&h=400&fit=crop',  # Multnomah Falls
    'silver_gmaps_128.jpg':         'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600&h=400&fit=crop',  # Silver Falls waterfall
    'mt_gmaps_127.jpg':             'https://images.unsplash.com/photo-1562124638-724e13052daf?w=600&h=400&fit=crop',  # Mt St Helens volcanic

    # ── Neighborhoods ────────────────────────────────────────────────────────
    'jade_7712_bing_mass.jpg':      'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=600&h=400&fit=crop',  # Jade District / dim sum
    'alberta_9935_bing_mass.jpg':   'https://images.unsplash.com/photo-1596300803969-24e6f2b8a9b0?w=600&h=400&fit=crop',  # street art / arts district

    # ── Day Trips / Gorge / Wine Country ────────────────────────────────────
    'columbia_gmaps_93.jpg':        'https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=600&h=400&fit=crop',  # Columbia River Gorge waterfall
    'wooden_gmaps_94.jpg':          'https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=600&h=400&fit=crop',  # tulip farm
    'wooden_gmaps_112.jpg':         'https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=600&h=400&fit=crop',  # tulip festival
    'mcminnville_gmaps_95.jpg':     'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=600&h=400&fit=crop',  # Oregon wine country vineyard
    'mcmenamins_gmaps_96.jpg':      'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=600&h=400&fit=crop',  # historic hotel McMenamins Edgefield
    'domaine_4427_bing_mass.jpg':   'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=600&h=400&fit=crop',  # winery/vineyard
    'crown_gmaps_121.jpg':          'https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=600&h=400&fit=crop',  # Columbia Gorge scenic viewpoint
    'pfriem_gmaps_122.jpg':         'https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&h=400&fit=crop',  # craft beer brewery
    'solstice_gmaps_123.jpg':       'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&h=400&fit=crop',  # wood-fired pizza
    'kickstand_gmaps_124.jpg':      'https://images.unsplash.com/photo-1541167760496-1628856ab772?w=600&h=400&fit=crop',  # coffee kitchen
    'sixth_4834_bing_mass.jpg':     'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # bistro dining
    'cicci_gmaps_126.jpg':          'https://images.unsplash.com/photo-1567206563114-c179afaa1931?w=600&h=400&fit=crop',  # gelato

    # ── Museums / Cultural ───────────────────────────────────────────────────
    'japanese_gmaps_85.jpg':        'https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=600&h=400&fit=crop',  # Japanese American heritage/museum
    'portland_2148_bing_mass.jpg':  'https://images.unsplash.com/photo-1580136579312-94651dfd596d?w=600&h=400&fit=crop',  # art museum
    'evergreen_gmaps_118.jpg':      'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&h=400&fit=crop',  # aviation museum

    # ── Bars / Nightlife ─────────────────────────────────────────────────────
    'sunflower_765_bing_mass.jpg':  'https://images.unsplash.com/photo-1583623025817-d180a2221d0a?w=600&h=400&fit=crop',  # sake bar
    'victoria_5771_bing_mass.jpg':  'https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=600&h=400&fit=crop',  # bar interior

    # ── Hotels ───────────────────────────────────────────────────────────────
    'ace_2665_bing_mass.jpg':       'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&h=400&fit=crop',  # boutique hotel
    'old_11_bing_mass.jpg':         'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&h=400&fit=crop',  # Georgian restaurant/historic

    # ── Olympia, WA ──────────────────────────────────────────────────────────
    'olympia_2995_bing_mass.jpg':   'https://images.unsplash.com/photo-1474906157786-261c788e0c54?w=600&h=400&fit=crop',  # oysters/seafood Olympia
    'cynara_gmaps_99.jpg':          'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # fine dining
    'uptown_gmaps_100.jpg':         'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&h=400&fit=crop',  # restaurant interior
    'encore_gmaps_101.jpg':         'https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=600&h=400&fit=crop',  # chocolates and teas
    'archibald_gmaps_102.jpg':      'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&h=400&fit=crop',  # boutique home goods
    'bucks_gmaps_103.jpg':          'https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=600&h=400&fit=crop',  # spice shop
    'mcmenamins_723_bing_mass.jpg': 'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=600&h=400&fit=crop',  # McMenamins historic
    'cecilia_gmaps_106.jpg':        'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # upscale restaurant
    'ondus_gmaps_107.jpg':          'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # waterfront dining
    'nostra_gmaps_109.jpg':         'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600&h=400&fit=crop',  # Italian trattoria
    'fort_1193_bing_mass.jpg':      'https://images.unsplash.com/photo-1501854140801-50d01698950b?w=600&h=400&fit=crop',  # historic fort
    'vancouver_gmaps_111.jpg':      'https://images.unsplash.com/photo-1483193722442-5422d99849bc?w=600&h=400&fit=crop',  # waterfront park
    'bistro_gmaps_114.jpg':         'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # French bistro McMinnville
    'okta_gmaps_115.jpg':           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',  # farm-to-table restaurant
    'la_gmaps_116.jpg':             'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600&h=400&fit=crop',  # La Rambla tapas
    'grounded_gmaps_117.jpg':       'https://images.unsplash.com/photo-1541167760496-1628856ab772?w=600&h=400&fit=crop',  # coffee/brunch restaurant
    'red_gmaps_119.jpg':            'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&h=400&fit=crop',  # market/deli

    # ── Chelsea Farms ────────────────────────────────────────────────────────
    'chelsea_gmaps_97.jpg':         'https://images.unsplash.com/photo-1474906157786-261c788e0c54?w=600&h=400&fit=crop',  # oyster bar
}


def fix_images(html_path: str) -> None:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    replaced = 0
    not_found = []

    def replace_src(m: re.Match) -> str:
        nonlocal replaced
        full_tag = m.group(0)
        filename = m.group(1)  # e.g. "tin_gmaps_0.jpg"

        if filename in REPLACEMENTS:
            new_tag = full_tag.replace(f'src="images/{filename}"',
                                       f'src="{REPLACEMENTS[filename]}"')
            replaced += 1
            return new_tag
        else:
            not_found.append(filename)
            return full_tag

    # Match src="images/FILENAME" inside img tags
    new_content = re.sub(r'<img\b[^>]*\bsrc="images/([^"]+)"[^>]*>', replace_src, content)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Replaced {replaced} images.")
    if not_found:
        print(f"\nNOT in replacement dict ({len(not_found)}):")
        for n in sorted(set(not_found)):
            print(f"  {n}")
    else:
        print("All images/ paths replaced successfully.")


if __name__ == '__main__':
    import os
    html_path = os.path.join(os.path.dirname(__file__), 'index.html')
    fix_images(html_path)
