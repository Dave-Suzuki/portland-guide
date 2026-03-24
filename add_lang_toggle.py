#!/usr/bin/env python3
"""
Add Japanese/English language toggle to Portland Guide index.html.
One-pass transformation using regex.
"""

import re

INPUT = '/Users/daves/portland-guide/index.html'

with open(INPUT, 'r', encoding='utf-8') as f:
    html = f.read()

# =============================================================================
# 1. Nav items
# =============================================================================
nav_map = {
    'レストラン': 'Restaurants',
    'スイーツ': 'Sweets',
    'カフェ': 'Cafes',
    'ショッピング': 'Shopping',
    '観光': 'Sights',
    'イベント': 'Events',
    '周辺': 'Nearby',
    '道中': 'En Route',
    '行程': 'Itinerary',
}

for ja, en in nav_map.items():
    html = html.replace(
        f'\n     {ja}\n    ',
        f'\n     <span class="lang-ja">{ja}</span><span class="lang-en" style="display:none">{en}</span>\n    '
    )

# =============================================================================
# 2. Section headers (.st elements) - h2 tags with Japanese text
# =============================================================================

# レスト<em>ラン</em>
html = html.replace(
    '<h2 class="st">\n      レスト\n      <em>\n       ラン\n      </em>\n     </h2>',
    '<h2 class="st"><span class="lang-ja">レスト<em>ラン</em></span><span class="lang-en" style="display:none">Restau<em>rants</em></span></h2>'
)

# スイーツ<em>・デザート</em>
html = html.replace(
    '<h2 class="st">\n     スイーツ\n     <em>\n      ・デザート\n     </em>\n    </h2>',
    '<h2 class="st"><span class="lang-ja">スイーツ<em>・デザート</em></span><span class="lang-en" style="display:none">Sweets<em> &amp; Desserts</em></span></h2>'
)

# カフェ<em>・コーヒー</em>
html = html.replace(
    '<h2 class="st">\n      カフェ\n      <em>\n       ・コーヒー\n      </em>\n     </h2>',
    '<h2 class="st"><span class="lang-ja">カフェ<em>・コーヒー</em></span><span class="lang-en" style="display:none">Cafes<em> &amp; Coffee</em></span></h2>'
)

# ショッ<em>ピング</em>
html = html.replace(
    '<h2 class="st">\n     ショッ\n     <em>\n      ピング\n     </em>\n    </h2>',
    '<h2 class="st"><span class="lang-ja">ショッ<em>ピング</em></span><span class="lang-en" style="display:none">Shop<em>ping</em></span></h2>'
)

# 観光<em>スポット</em>
html = html.replace(
    '<h2 class="st">\n      観光\n      <em>\n       スポット\n      </em>\n     </h2>',
    '<h2 class="st"><span class="lang-ja">観光<em>スポット</em></span><span class="lang-en" style="display:none">Sight<em>seeing</em></span></h2>'
)

# イベント<em>・3月</em>
html = html.replace(
    '<h2 class="st">\n     イベント\n     <em>\n      ・3月\n     </em>\n    </h2>',
    '<h2 class="st"><span class="lang-ja">イベント<em>・3月</em></span><span class="lang-en" style="display:none">Events<em> · March</em></span></h2>'
)

# 周辺<em>デイトリップ</em>
html = html.replace(
    '<h2 class="st">\n      周辺\n      <em>\n       デイトリップ\n      </em>\n     </h2>',
    '<h2 class="st"><span class="lang-ja">周辺<em>デイトリップ</em></span><span class="lang-en" style="display:none">Nearby<em> Day Trips</em></span></h2>'
)

# I-5 道中<em>スポット</em>
html = html.replace(
    '<h2 class="st">\n     I-5 道中\n     <em>\n      スポット\n     </em>\n    </h2>',
    '<h2 class="st"><span class="lang-ja">I-5 道中<em>スポット</em></span><span class="lang-en" style="display:none">I-5 En Route<em> Stops</em></span></h2>'
)

# おすすめ<em>行程</em>
html = html.replace(
    '<h2 class="st">\n      おすすめ\n      <em>\n       行程\n      </em>\n     </h2>',
    '<h2 class="st"><span class="lang-ja">おすすめ<em>行程</em></span><span class="lang-en" style="display:none">Suggested<em> Itinerary</em></span></h2>'
)

# =============================================================================
# 3. Sub-section labels (.sl elements)
# =============================================================================
sl_map = {
    '🌅 朝食 &middot; ブランチ': '🌅 Breakfast &middot; Brunch',
    '🍣 日本食 &middot; 和食': '🍣 Japanese &middot; Washoku',
    '🌶️ タイ料理 &middot; アジア料理': '🌶️ Thai &middot; Asian Cuisine',
    '🍝 イタリアン &middot; フレンチ': '🍝 Italian &middot; French',
    '🦪 シーフード': '🦪 Seafood',
    '🍙 おにぎり &middot; サンドイッチ': '🍙 Onigiri &middot; Sandwiches',
    '🍳 レストラン・食事（和食・アジア系） (追加分)': '🍳 Restaurants (Japanese &amp; Asian, More)',
    '🍽️ レストラン・食事（洋食・その他） (追加分)': '🍽️ Restaurants (Western &amp; Other, More)',
    '🇯🇵 日本系セレクト': '🇯🇵 Japanese Picks',
    '🧂 食材 &middot; キッチン用品': '🧂 Food &middot; Kitchen',
    '📖 本 &middot; 雑貨': '📖 Books &middot; Goods',
}

for ja, en in sl_map.items():
    html = html.replace(
        f'<div class="sl">\n      {ja}\n     </div>',
        f'<div class="sl"><span class="lang-ja">{ja}</span><span class="lang-en" style="display:none">{en}</span></div>'
    )
    html = html.replace(
        f'<div class="sl">\n     {ja}\n    </div>',
        f'<div class="sl"><span class="lang-ja">{ja}</span><span class="lang-en" style="display:none">{en}</span></div>'
    )

# =============================================================================
# 4. Card descriptions (.cd elements) - wrap content with lang spans
# =============================================================================

# Dictionary mapping card names to English translations
# Key = exact Japanese text inside .cd (stripped), Value = English translation
translations = {
    # Restaurants - Breakfast/Brunch
    'ポートランド最有名の犬フレンドリーパティオ。ワンコ専用メニューあり。Guy Fieri訪問歴あり。週末は予約推奨。':
        "Portland's most famous dog-friendly patio. Dog-specific menu available. Featured by Guy Fieri. Reservations recommended on weekends.",

    '朝食サンドの名店。Mississippi店にはヒートランプ付き犬フレンドリーパティオが2つ。フルバーも充実。':
        "A beloved breakfast sandwich spot. The Mississippi location has two dog-friendly heated patios. Full bar available.",

    # Japanese food
    'Snow Peak本社ビル内の薪火和食。炉端焼き・ラーメン・オマカセ。日本酒充実。Dining Month $55コースあり。火曜定休。':
        "Wood-fired Japanese cuisine inside Snow Peak's HQ. Robatayaki, ramen, and omakase. Extensive sake selection. Portland Dining Month $55 course available. Closed Tuesdays.",

    '1988年創業の老舗寿司バー。毎日変わる黒板メニューにPNWの新鮮魚介が並ぶ。ポートランド日本食の定番。':
        "A classic sushi bar established in 1988. Daily blackboard menu featuring fresh PNW seafood. A staple of Portland's Japanese dining scene.",

    '柚子塩ラーメンで名高い阿夫利のポートランド店。居酒屋スタイルで日本酒・クラフトビールとともに。':
        "Portland outpost of AFURI, famous for yuzu salt ramen. Izakaya-style dining with sake and craft beer.",

    # Thai / Asian
    'タイチキンライス一品勝負の神話的名店。紙包みを広げる儀式から始まる至福のランチ。桜の公園でのピクニックに最高。 Google ★4.6（2,379件）':
        "A legendary spot that does one thing: Thai chicken rice. The ritual of unwrapping the paper is half the joy. Perfect for a cherry blossom picnic. Google ★4.6 (2,379 reviews)",

    '南タイ式フライドチキン専門。チキン＋パンダンロティ＋スティッキーライスの組み合わせが王道。帰り道のテイクアウトにも。 Google ★4.6（1,352件）':
        "Southern Thai-style fried chicken specialist. The classic combo: chicken + pandan roti + sticky rice. Great for takeout on the way home. Google ★4.6 (1,352 reviews)",

    'タイBBQ×カクテルバーの革命的コラボ。スモーキーな豚バラKrapaoと白いカリーが看板。広いパティオで犬連れに最適。 Google ★4.6（2,755件）':
        "A revolutionary mashup of Thai BBQ and cocktail bar. Signature smoky pork belly krapao and white curry. Spacious patio — ideal for dogs. Google ★4.6 (2,755 reviews)",

    'インドネシア料理の傑作。Keith Lee 10点満点、James Beard候補。ライステーブル4コースで大胆なフレーバーを体験。 Google ★4.6（809件）':
        "A masterpiece of Indonesian cuisine. Keith Lee gave it a perfect 10; James Beard nominee. The 4-course rijsttafel delivers bold, complex flavors. Google ★4.6 (809 reviews)",

    # Italian / French
    '2005年創業の殿堂入り薪窯ピザ＆パスタ。「ポートランドのネグローニの聖地」とも。日曜定休。 Google ★4.5（1,952件）':
        "An institution since 2005 — wood-fired pizza and pasta. Also known as Portland's negroni mecca. Closed Sundays. Google ★4.5 (1,952 reviews)",

    '今ポートランドで最も話題のパスタ専門店。自家製パスタのBoar Pappardelle・Tortelli di Zuccaは必食。月火定休。 Google ★4.7（724件）':
        "Currently Portland's hottest pasta destination. Must-try: house-made Boar Pappardelle and Tortelli di Zucca. Closed Mon–Tue. Google ★4.7 (724 reviews)",

    '本格フレンチベーカリー。早朝から焼きたてのバゲット・クロワッサンが揃う。火曜朝の旅立ちに最適。':
        "Authentic French bakery. Fresh-baked baguettes and croissants from early morning. Perfect for a Tuesday morning departure.",

    'ミシシッピ地区のスクラッチイタリアン。自家製パスタとフォカッチャが看板で「世界中で食べた中で最高のパスタ」とのレビューも。オープンキッチンのカウンター席が人気。チョコレートブディーノも絶品。グルテンフリー対応あり。要予約。 Google ★4.6（460件）':
        "Scratch Italian in the Mississippi District. House-made pasta and focaccia earn raves as \"the best pasta I've eaten anywhere in the world.\" Open-kitchen counter seats are popular. Chocolate budino is a must. Gluten-free options available. Reservations required. Google ★4.6 (460 reviews)",

    '2025年夏オープンのSE Division地区の注目新店。予約不可・ウォークインのみで行列必至のブカティーニとラヴィオリ。ペペロンチーニマティーニは必飲。温かみのあるモダンな雰囲気。6名以上のみ予約可。Portland Monthly「Best New Italian」選出。 Google ★4.6（172件）':
        "A buzzy new arrival on SE Division since summer 2025. Walk-ins only (no reservations except 6+), with lines for the bucatini and ravioli. Don't skip the pepperoncini martini. Portland Monthly's \"Best New Italian.\" Google ★4.6 (172 reviews)",

    'ウォーターフロントのアルゼンチン＆南米料理。28日ドライエイジドリブアイの薪焼きとボーンマロウが看板。ロモ・サルタード（ペルー風牛肉炒め）やエンパナーダなどタパスも充実。ハッピーアワーが大人気で100件以上のレビューで言及。OpenTableで予約可。 Google ★4.7（2,372件）':
        "Argentine and South American cuisine on the waterfront. Signature 28-day dry-aged rib-eye over wood fire and bone marrow. Tapas like lomo saltado and empanadas. Happy hour is wildly popular. Reserve via OpenTable. Google ★4.7 (2,372 reviews)",

    # Seafood
    '当日水揚げの生牡蠣が17–18時は$1のハッピーアワー。Wes Anderson「Life Aquatic」をモチーフにした可愛い内装。要予約。 Google ★4.8（951件）':
        "Daily-caught raw oysters for $1 during happy hour 5–6 PM. Adorable Wes Anderson \"Life Aquatic\"-inspired interior. Reservations required. Google ★4.8 (951 reviews)",

    # Onigiri / Sandwiches
    '大阪スタイルのカツサンド専門。自家製ミルクブレッドに分厚いカツ。海老サンドも人気。旅の弁当にも◎。 Google ★4.3（724件）':
        "Osaka-style katsu sandwich specialist. Thick-cut katsu on house-made milk bread. The shrimp sandwich is also a hit. Great road-trip bento. Google ★4.3 (724 reviews)",

    'ポートランド最古参のおにぎり・ムスビ専門店。コシヒカリ使用、日本×ハワイアンフュージョンスタイル。 Google ★4.8（164件）':
        "Portland's longest-standing onigiri/musubi specialist. Made with koshihikari rice in a Japanese-Hawaiian fusion style. Google ★4.8 (164 reviews)",

    # Added Asian section
    '12席カウンターのみの江戸前オマカセ（$125）。地元PNWの魚介と日本直送素材を一貫ずつ握る。自家〆の鯖と玉子焼きが特に評判。シェフが一つ一つ丁寧に解説してくれる。火〜金はアラカルトも可。 Google ★4.6（462件）':
        "12-seat counter-only Edomae omakase ($125). Each piece features local PNW seafood alongside ingredients direct from Japan. House-cured mackerel and tamagoyaki are standouts. Chef explains each piece. À la carte available Tue–Fri. Google ★4.6 (462 reviews)",

    'James Beard候補のシェフRyan Roadhouseによる創作オマカセ。6〜8週ごとにテーマが変わり、村上春樹やジブリ、ツインピークスなどの世界観を11コースで表現する「ルールなしの懐石」。2025年にダウンタウンの美しいボザール建築に移転。予約必須。 Google ★4.8（194件）':
        "Creative omakase by James Beard-nominated chef Ryan Roadhouse. Themes change every 6–8 weeks, weaving Murakami, Ghibli, Twin Peaks, and more into 11 courses of \"kaiseki without rules.\" Moved to a beautiful Beaux-Arts building downtown in 2025. Reservations required. Google ★4.8 (194 reviews)",

    'OregonLive読者投票ベストヴィーガン1位。発芽玄米おにぎり（味噌漬け豆腐、柚子かぼちゃなど）が看板。Ota Tofuの油揚げを使ったうどんも人気。日本人オーナー夫妻が営むほっとする味。 Google ★4.7（846件）':
        "OregonLive readers' #1 best vegan. Signature sprouted brown rice onigiri with fillings like miso-marinated tofu and yuzu kabocha. Udon with Ota Tofu aburaage is also popular. Cozy home cooking from a Japanese couple. Google ★4.7 (846 reviews)",

    '日本人シェフが営む地元密着の和食店。ランチの定食メニューが充実。焼き魚、生姜焼き、天ぷらなど家庭的な味わいで在住日本人のリピーターが多い。 Google ★4.7（566件）':
        "A neighborhood Japanese restaurant run by a Japanese chef. Generous teishoku lunch sets. Grilled fish, ginger pork, tempura — the kind of home-style flavors that keep resident Japanese returning. Google ★4.7 (566 reviews)",

    '黒ニンニク味噌カツサンドなど、日本式サンドのフードカート。\n         Google ★4.9（924件）':
        "A food cart specializing in Japanese-style sandwiches including a black garlic miso katsu sando. Google ★4.9 (924 reviews)",

    'コシヒカリ使用のオーダーメイドおにぎり専門店。日本×ハワイアンフュージョンの具材が独創的。平日ランチのみの営業で売り切れ次第終了。SE地区で移転先を要確認。 Google ★4.4（51件）':
        "Custom-made onigiri using koshihikari rice with creative Japanese-Hawaiian fusion fillings. Weekday lunch only — sells out fast. Confirm current SE location. Google ★4.4 (51 reviews)",

    '2024年James Beard受賞のタイ料理最高峰。バンコク出身シェフによる完全予約制の隠れ家。木〜日のディナーのみ。毎回テーマが変わるコースでタイの地方料理を深く掘り下げる。PaaDeeの奥にある秘密の扉の先。 Google ★4.6（441件）':
        "The pinnacle of Thai cuisine — 2024 James Beard Award winner. Hidden-door reservation-only spot by a Bangkok-born chef. Thu–Sun dinner only. Each menu explores a different region of Thailand. Enter through the secret door at the back of PaaDee. Google ★4.6 (441 reviews)",

    'Eemチームが手がけるカオソイ（北タイカレーラーメン）の専門店。チキン＋パンダンロティ＋スティッキーライスのセットが定番。帰りのテイクアウトにも最適。':
        "From the Eem team: a khao soi (Northern Thai curry noodle) specialist. The classic set of chicken + pandan roti + sticky rice is the move. Great for takeout on the way home.",

    'タイ全土の家庭料理をカバー。ランチの定食メニューがコスパ抜群でテイクアウトに最適。パパイヤサラダとラープが人気。Eemの姉妹店。 Google ★4.5（853件）':
        "Covers home-style cooking from across Thailand. Lunch sets are excellent value and perfect for takeout. Papaya salad and larb are favorites. Sister restaurant to Eem. Google ★4.5 (853 reviews)",

    'ベトナム料理。レモングラスチキンのバインミーとベルミセリボウルが看板。緑豊かなウィリアムズ通りの居心地いいダイニング。':
        "Vietnamese cuisine. Signature lemongrass chicken banh mi and vermicelli bowls. Comfortable dining on the leafy Williams Ave corridor.",

    'ハノイのカウザイ通りをイメージした北ベトナム料理店。メニューが「詳細なマニュアル」のような冊子で楽しい。ブン、フォー、串焼き肉、鴨のグリルとバラエティ豊か。 Google ★4.6（390件）':
        "Northern Vietnamese restaurant inspired by Hanoi's Cầu Giấy street. The menu is a booklet — fun to read. Wide variety: bun, pho, skewered meats, grilled duck. Google ★4.6 (390 reviews)",

    '韓国家庭料理。テーブルで作るインスタントラーメンのパフォーマンスが名物。フライドチキンとビビンバも人気。金〜月のディナーのみ営業の予約困難店。 Google ★4.5（790件）':
        "Korean home cooking. The tableside instant ramen performance is the star attraction. Fried chicken and bibimbap are also hits. Dinner only Fri–Mon — hard to get a table. Google ★4.5 (790 reviews)",

    '西アフリカ料理の先駆的レストラン。ジョロフライスとスモーキーなピーナッツシチューが看板。エチオピアのインジェラも。温かいホスピタリティで常連が多い。水〜日のディナー営業。 Google ★4.7（1,091件）':
        "A pioneering West African restaurant. Signature jollof rice and smoky peanut stew. Ethiopian injera also available. Warm hospitality keeps regulars coming back. Dinner Wed–Sun. Google ★4.7 (1,091 reviews)",

    '毎日店内で手打ちする麺が名物。Food NetworkのDDDにも出演。ビーフ手打ち麺とイカの塩コショウ揚げが鉄板。ポーク骨付きポテトスープも人気。$10前後で大盛り、コスパ最強。':
        "Famous for hand-pulled noodles made fresh daily. Featured on Food Network's Diners, Drive-Ins and Dives. The beef hand-pulled noodles and salt-pepper squid are classics. Pork bone potato soup is also popular. Generous portions around $10 — unbeatable value.",

    'インドのストリートフード専門。カティロール（パラタ巻き）とポークヴィンダルーが看板。バダパヴ（スパイシーポテトフライのバーガー）も必食。カウンターで注文してテーブルで待つスタイル。ベジ・ヴィーガンの選択肢も豊富。 Google ★4.4（1,474件）':
        "Indian street food specialist. Signature kati rolls (paratha wraps) and pork vindaloo. Don't skip the vada pav (spicy potato fritter burger). Order at the counter and wait at your table. Plenty of veg and vegan options. Google ★4.4 (1,474 reviews)",

    '2025年末オープンの手打ち麺＆点心の新店。蘭州ビーフヌードルスープと幅広ピリ辛ヌードルが看板。自家製の麺は太さを選べる。小籠包や焼き餃子も人気。パールディストリクトの新星。$20〜30。イートイン・テイクアウト・宅配。':
        "New hand-pulled noodle and dim sum spot opened late 2025. Signature Lanzhou beef noodle soup and wide spicy noodles. House-made noodles in your choice of thickness. Xiao long bao and pan-fried dumplings also popular. A Pearl District newcomer. $20–30. Dine-in, takeout, or delivery.",

    'ハワイアン＆フィリピン料理のプレートランチ。ポケナチョス、肉ジュン（韓国風薄切り牛肉フライ）、カルビ、ポークカレーカツが人気。ロコモコの「May-Jah Moco Special」は常連の定番。イロコスエンパナーダも予約必須。アイランドコミュニティに愛される活気ある店。量たっぷり。 Google ★4.6（981件）':
        "Hawaiian and Filipino plate lunches. Favorites: poke nachos, meat jun (Korean-style thin fried beef), kalbi, and pork curry katsu. The \"May-Jah Moco Special\" loco moco is a regular's staple. Ilocos empanadas sell out fast. A lively, community-loved spot with generous portions. Google ★4.6 (981 reviews)",

    # Added Western section
    'ダウンタウンのUmpqua Plaza内にある地中海デリ。ギロピタプレートとオクトパスプレートが看板で「ポートランド最高のレストランに匹敵する味がカジュアル価格」とレビュー。サーモンプレートもボリューム満点。朝7時から営業でコーヒーも好評。$10〜20でコスパ抜群。 Google ★4.6（201件）':
        "Mediterranean deli inside downtown's Umpqua Plaza. Signature gyro pita plate and octopus plate are praised as \"flavors rivaling Portland's best restaurants at casual prices.\" Salmon plate is also generous. Open from 7 AM — coffee is great too. Excellent value at $10–20. Google ★4.6 (201 reviews)",

    '地元民の隠れ家的カジュアルイタリアン。ゴルゴンゾーラ×ハニーのニョッキやアサリのスパゲッティが絶品。$2アンティパスティとワインリストも充実。予約不可・毎日16〜22時。 Google ★4.6（730件）':
        "A locals' hidden gem for casual Italian. Gorgonzola-honey gnocchi and clam spaghetti are outstanding. $2 antipasti and an excellent wine list. No reservations — daily 4–10 PM. Google ★4.6 (730 reviews)",

    'フランス南西部出身シェフが営む本格ビストロ。ウッドストック地区の隠れ家。ステーキフリットとコックオヴァンが人気。火〜土ディナーのみ。 Google ★4.6（423件）':
        "Authentic bistro run by a chef from southwestern France. A hidden gem in the Woodstock neighborhood. Steak frites and coq au vin are the draws. Dinner Tue–Sat only. Google ★4.6 (423 reviews)",

    '14年以上愛されるリヨン風カジュアルフレンチ。NW 23rd通り。鴨のコンフィとムール貝が定番。バーエリアはウォークインで気軽に使える。':
        "Beloved casual Lyonnais French for over 14 years. On NW 23rd Ave. Duck confit and mussels are the standards. The bar area welcomes walk-ins.",

    'フランス×スカンジナビアの白を基調にしたランチェット。Bon Appétit「全米ベストレストラン2014」選出。名物の黒胡椒チーズケーキは花びらを飾った芸術品。ノルウェー風スモーブロー（オープンサンド）やビステイヤも人気。水〜土10:00–16:00のランチのみ営業。':
        "A white-toned French-Scandinavian luncheonette. Bon Appétit's \"Best New Restaurant in America 2014.\" The signature black pepper cheesecake adorned with flowers is a work of art. Norwegian-style smørbrød and basteeya are also beloved. Lunch only, Wed–Sat 10 AM–4 PM.",

    'パリのビストロに瞬間移動したかのような名店。':
        "A restaurant so authentic it feels like teleporting straight to a Paris bistro.",

    'ロシア・東欧料理のパイオニア。ベラルーシ系アメリカ人シェフBonnie Moralesの家庭の味。シベリア式ペリメニ（肉入り水餃子）をバターとスメタナで。ウサギの土鍋煮込みとボルシチも必食。 Google ★4.6（2,729件）':
        "A pioneer of Russian and Eastern European cuisine. Belarusian-American chef Bonnie Morales's home cooking. Siberian pelmeni (meat dumplings) with butter and smetana. Rabbit braised in a clay pot and borscht are also musts. Google ★4.6 (2,729 reviews)",

    'バイソンやエルクなどPNWのジビエを使ったネイティブアメリカン料理。先住民の伝統食材を現代的に再解釈する唯一無二の存在。NW Davis St。要チェック。 Google ★4.7（250件）':
        "Native American cuisine using PNW game like bison and elk. A one-of-a-kind restaurant reinterpreting Indigenous traditional ingredients in a modern way. NW Davis St. Worth checking out. Google ★4.7 (250 reviews)",

    '1994年創業、オレゴンのファームトゥテーブルの先駆者。シェフGreg HigginsはJames Beard受賞。名物の"ホールピッグプレート"はロイン・ソーセージ・リブ・ベリーの豚尽くし。季節で変わるメニューとワインリストも秀逸。バーエリアはカジュアルに利用可。\n         Google ★4.5（1,342件）':
        "Pioneer of Oregon's farm-to-table movement since 1994. Chef Greg Higgins is a James Beard Award winner. The signature \"whole pig plate\" is a glorious spread of loin, sausage, ribs, and belly. Seasonal menu and wine list are both excellent. Bar area is casual walk-in. Google ★4.5 (1,342 reviews)",

    'スカンジナビア料理のブランチ人気店。スウェーデン式パンケーキとNord（スモークサーモンプレート）が看板。エッグス・ベネディクトも定番。週末は行列必至。SE Clinton St. Google ★4.7（1,393件）':
        "A popular Scandinavian brunch spot. Signature Swedish pancakes and the Nord smoked salmon plate. Eggs Benedict is also a classic. Expect a line on weekends. SE Clinton St. Google ★4.7 (1,393 reviews)",

    '絶品フレンチと、朝営業のマーケットのクッキーが有名。 Google ★4.7（860件）':
        "Renowned for excellent French cuisine and the morning market's legendary cookies. Google ★4.7 (860 reviews)",

    '女性スポーツの試合だけを流す世界唯一のスポーツバー。サッカー、バスケ、テニスの試合観戦をしながら地元クラフトビールとパブフード。子連れフレンドリー。NE Broadway. Google ★4.4（601件）':
        "The world's only sports bar that exclusively shows women's sports. Watch soccer, basketball, and tennis with local craft beer and pub food. Family-friendly. NE Broadway. Google ★4.4 (601 reviews)",

    'メキシコ・ユカタン半島スタイルのタコス専門店。カルニタスとポークアルパストールが看板で常に行列。フレッシュサルサバーで自分好みにカスタマイズ。ミシシッピ店とホーソン店あり。':
        "Yucatán-style taco specialist. Carnitas and pork al pastor are the signatures — always a line. Customize at the fresh salsa bar. Locations on Mississippi and Hawthorne.",

    'ポークチョップサンドの殿堂。自家製ソースが決め手のダーティフライとファットボーイ・サンドが人気。SE Hawthorne店は行列覚悟。 Google ★4.4（1,257件）':
        "The temple of pork chop sandwiches. Dirty fries with house-made sauce and the Fat Boy sandwich are favorites. Expect a wait at the SE Hawthorne location. Google ★4.4 (1,257 reviews)",

    'NE Albertaの地元民御用達サンドイッチ＆コーヒー店。ローストターキーのサンドとメニュー看板のコーヒー＆ティーが人気。 Google ★4.7（306件）':
        "A neighborhood sandwich and coffee staple on NE Alberta. Roast turkey sandwich and the coffee & tea menu are highlights. Google ★4.7 (306 reviews)",

    '深夜まで営業するSE Hawthorneのフードカートポッド。ピロシキ、タコス、クレープなど多国籍の屋台が集まる。バー帰りの〆に最適。 Google ★4.6（1,692件）':
        "A late-night food cart pod on SE Hawthorne open until midnight. International carts: piroshki, tacos, crepes, and more. Perfect for a post-bar bite. Google ★4.6 (1,692 reviews)",

    # Sweets
    'ポートランド生まれのクリエイティブアイスクリーム。ハニーラベンダー・ペア&ブルーチーズなど季節限定フレーバーが自由すぎる。試食し放題。':
        "Portland-born creative ice cream. Wild seasonal flavors like honey lavender and pear & blue cheese. Unlimited tasting encouraged.",

    '注文を受けてから揚げるミニドーナツ×チャイの専門店。チャイフライトで好みを探す楽しさ。':
        "Mini doughnuts fried to order, paired with artisan chai. Try the chai flight to find your favorite.",

    'フランス修業シェフの本格パティスリー。深夜もPix-O-Matic自販機でケーキが買える唯一無二の存在。\n       Google ★4.3（1,121件）':
        "An authentic pâtisserie by a French-trained chef. Unique in the world: the Pix-O-Matic vending machine lets you buy cake at 3 AM. Google ★4.3 (1,121 reviews)",

    'オレゴン唯一の本格抹茶ソフトクリーム専門店。宇治産抹茶使用の濃厚なドリンク・スイーツが揃う。 Google ★4.7（530件）':
        "Oregon's only dedicated matcha soft-serve specialist. Rich drinks and sweets made with Uji matcha. Google ★4.7 (530 reviews)",

    '米粉グルテンフリーのモチモチドーナツ。ゆずFunfetti・抹茶・黒ゴマなど日本感覚のフレーバーが豊富。 Google ★4.8（565件）':
        "Gluten-free mochi donuts made with rice flour. Japanese-inspired flavors: yuzu funfetti, matcha, black sesame, and more. Google ★4.8 (565 reviews)",

    'ブリオッシュ生地の大人向けドーナツ。ヘーゼルナッツ・コーヒーグレーズなど洗練されたフレーバーが揃う。 Google ★4.4（3,650件）':
        "Grown-up doughnuts made with brioche dough. Sophisticated flavors like hazelnut and coffee glaze. Google ★4.4 (3,650 reviews)",

    'ポートランド初のマルチロースターカフェ。全米の厳選ロースターの豆を日替わりで提供し、Stumptown一強だった街のコーヒーシーンを変えた存在。オーナーはNWバリスタチャンピオン3回優勝のBilly Wilson。ラテアートも見事。犬連れOK。':
        "Portland's first multi-roaster café. Daily-rotating beans from the country's best roasters — the shop that changed the city's coffee scene beyond Stumptown alone. Owner Billy Wilson is a three-time NW Barista Champion. Latte art is excellent. Dog-friendly.",

    '日本とメキシコにルーツを持つオーナーのおしゃれなカフェ。 Google ★4.6（180件）':
        "A stylish café from an owner with Japanese and Mexican roots. Google ★4.6 (180 reviews)",

    '2025年オープンの大行列マッチャ専門カフェ。\n       Google ★4.4（186件）':
        "Matcha-specialty café that opened in 2025 to long lines. Google ★4.4 (186 reviews)",

    '2026年オープン予定。店内で抹茶を挽く超話題店。 Google ★4.4（69件）':
        "Opening in 2026. The highly anticipated café where matcha is stone-ground in-house. Google ★4.4 (69 reviews)",

    'サンルームに植えられた2026年オープンの最新カフェ。\n       Google ★4.8（687件）':
        "A brand-new 2026 café with a plant-filled sunroom interior. Google ★4.8 (687 reviews)",

    'ポートランド初のアニメテーマカフェ。抹茶アフォガート、ベトナム式練乳＆塩キャラメルコーヒー、プーアル茶の香港ミルクティーなど創作ドリンクが充実。アニメフィギュアの展示や上映会も。ヴィーガンオプション豊富。 Google ★4.6（136件）':
        "Portland's first anime-themed café. Creative drinks include matcha affogato, Vietnamese condensed milk & salted caramel coffee, and pu-erh Hong Kong milk tea. Anime figure displays and screening events. Lots of vegan options. Google ★4.6 (136 reviews)",

    '季節のフルーツを使った芸術的なかき氷（春〜秋営業）。 Google ★4.7（40件）':
        "Artistic shaved ice using seasonal fruit. Open spring through fall. Google ★4.7 (40 reviews)",

    '奇抜でカラフルなポートランド名物のドーナツ。 Google ★4.4（19,402件）':
        "Portland's iconic wacky, colorful doughnuts. Google ★4.4 (19,402 reviews)",

    '卵黄12個を使った濃厚フローズンカスタード。 Google ★4.4（130件）':
        "Rich frozen custard made with 12 egg yolks. Google ★4.4 (130 reviews)",

    '21年・7,000個のパイを焼いてきた職人のパイ専門店。サクサクのバタークラストが最大の特徴。タルトチェリーパイとソルテッドハニーパイが人気。バターミルクビスケット＆グレイビーも朝食の定番。':
        "A master pie shop with 21 years and 7,000+ pies baked. The flaky butter crust is the star. Tart cherry pie and salted honey pie are the favorites. Buttermilk biscuits & gravy are a breakfast classic.",

    '1978年創業、ポートランドのデザート界を支える老舗。 Google ★4.5（2,168件）':
        "A Portland dessert institution since 1978. Google ★4.5 (2,168 reviews)",

    '全米トップクラスの天然酵母カントリーブレッド。':
        "Country bread from natural sourdough starter, among the best in the country.",

    'ヨーロッパの製パン技術とPNWの食材を融合した名ベーカリー。バゲットの完璧なクラストとクロワッサンのバター層が絶品。ベーコンエッグチーズ・クレセントが朝食の人気No.1。オレゴン産の地粉を地元製粉所で挽いて使用。 Google ★4.5（412件）':
        "An acclaimed bakery blending European technique with PNW ingredients. Perfect baguette crust and croissant layers. The bacon egg cheese crescent is the #1 breakfast pick. Uses Oregon-grown grain milled locally. Google ★4.5 (412 reviews)",

    'ブルーベリーマフィンが人気の朝食カフェ。 Google ★4.4（747件）':
        "A breakfast café beloved for its blueberry muffins. Google ★4.4 (747 reviews)",

    'チーズの名前だけど実は絶品ソフトクリーム＆サンデーの店。バナナプディングサンデーが一番人気で「今まで食べた中で最高のソフトクリーム」とレビュー多数。チョコの帽子がのった可愛い盛り付け。甘さ控えめで量もたっぷり。チーズプレートやスナックメニューもあり。':
        "Don't let the name fool you — it's actually a stellar soft-serve and sundae shop. The banana pudding sundae is #1, with reviews calling it \"the best soft-serve I've ever had.\" Adorable chocolate hat presentation. Not too sweet, very generous portions. Cheese plates and snacks also available.",

    # Cafes
    'サードウェーブコーヒームーブメントの発祥地。シングルオリジンへの真剣な姿勢が世界を変えた。本店限定ブレンドをぜひ。\n        Google ★4.4（1,868件）':
        "The birthplace of the third-wave coffee movement. Their serious commitment to single-origin changed the world. Try the flagship-exclusive blend. Google ★4.4 (1,868 reviews)",

    '倉庫を改装した美しい空間。豆へのこだわりが強く、日本のコーヒーメディアにも頻出する名店。\n        Google ★4.5（703件）':
        "A beautifully converted warehouse space. Their obsessive attention to beans earns frequent coverage in Japanese coffee media. Google ★4.5 (703 reviews)",

    '工場を改装した天井の高い美しい空間。壁面を覆う植物が印象的。豆の品質も最高峰。 Google ★4.6（1,649件）':
        "A stunning converted factory with soaring ceilings. The wall of plants is striking, and the bean quality is top-tier. Google ★4.6 (1,649 reviews)",

    # Shopping
    '西海岸最大の無印良品（11,000 sq ft）。ロボットバリスタ「Jarvis」が常駐。日本仕様の文具・アロマ・家具が消費税ゼロで揃う。\n        Google ★4.5（961件）':
        "The West Coast's largest MUJI (11,000 sq ft). Robot barista \"Jarvis\" is on staff. Japanese-spec stationery, aromatherapy, and furniture — all tax-free. Google ★4.5 (961 reviews)",

    '古い着物地をリメイクしたバッグ・クッション・テキスタイル。「もったいない」精神が宿る唯一無二の店。Mizuba Tea Co.（宇治産抹茶）も取扱。\n        Google ★4.7（262件）':
        "Bags, cushions, and textiles remade from vintage kimono fabric. A one-of-a-kind shop imbued with the spirit of mottainai (waste-not). Also carries Mizuba Tea Co. (Uji matcha). Google ★4.7 (262 reviews)",

    '日本語雑誌・書籍・文房具・フィギュア・ガチャが揃う。日本の最新カルチャーをアメリカでキャッチできる貴重な場所。\n        Google ★4.7（1,027件）':
        "Japanese magazines, books, stationery, figures, and gacha machines. A rare place to catch up on the latest Japanese culture in America. Google ★4.7 (1,027 reviews)",

    '全米最大クラスのクラフト塩コレクション＋アルティザンチョコ＋ビターズ。壁一面のチョコレートは圧巻。お土産の宝庫。\n        Google ★4.8（42件）':
        "One of the largest craft salt collections in the US, plus artisan chocolate and bitters. The wall of chocolate is jaw-dropping. A treasure trove for souvenirs. Google ★4.8 (42 reviews)",

    'ナイフ専門店。研ぎサービスも。日本製包丁のセレクションが充実。消費税ゼロなのでシアトルより断然お得。\n        Google ★4.1（68件）':
        "A knife specialty shop with sharpening services. Excellent selection of Japanese knives. Tax-free Oregon makes it far cheaper than Seattle. Google ★4.1 (68 reviews)",

    '1975年創業のポートランド老舗キッチンストア。全米Top25にも選ばれた地元密着の名店。\n        Google ★4.4（185件）':
        "Portland's beloved kitchen store since 1975. Named to the Top 25 kitchen stores in the US. Google ★4.4 (185 reviews)",

    '一棟まるごと本で埋め尽くされた迷宮。新刊と古書が同じ棚に並ぶ天国。カフェ内蔵。地図を持って3時間迷うべし。\n        Google ★4.9（37,723件）':
        "An entire city block of books — a labyrinthine paradise where new and used books share the same shelves. Café inside. Bring a map and plan to wander for three hours. Google ★4.9 (37,723 reviews)",

    '手製紙・活版印刷カード・文房具の専門店。ギフト包装も美しく、旅の記念品やお土産に最適。\n        Google ★4.8（273件）':
        "Handmade paper, letterpress cards, and stationery specialist. Beautiful gift wrapping makes it ideal for travel souvenirs. Google ★4.8 (273 reviews)",

    # Sights
    '「日本国外で最も美しい日本庭園」と称される本格派。盆栽テラスと茶室あり。月曜は12時オープンに注意。要予約推奨。\n        Google ★4.5（7,741件）':
        "Acclaimed as \"the most authentic Japanese garden outside of Japan.\" Bonsai terrace and tea house on site. Note: Monday opening is noon. Reservations recommended. Google ★4.5 (7,741 reviews)",

    'ウォーターフロントの桜並木が3月下旬〜4月上旬に満開。Nong\'sのテイクアウトでピクニックに最適。入場無料。\n        Google ★4.6（230件）':
        "The waterfront cherry trees peak from late March to early April. Perfect for a Nong's takeout picnic. Free admission. Google ★4.6 (230 reviews)",

    '5,200エーカーの都市森林。苔むした石造りの廃墟「Witch\'s Castle」まで短いトレイルで到達可能。朝の散歩に最適。':
        "5,200 acres of urban forest. A short trail leads to the moss-covered stone ruins of Witch's Castle. Perfect for a morning walk.",

    'Mt. Hood・Mt. St. Helens・Mt. Rainierなど5火山と市街が一望できる丘の上の歴史的邸宅。庭園・展望台は無料。\n        Google ★4.7（8,147件）':
        "A historic hilltop mansion with panoramic views of five volcanoes — Mt. Hood, Mt. St. Helens, Mt. Rainier, and more — plus the city. Gardens and viewpoint are free. Google ★4.7 (8,147 reviews)",

    '3月から始まるウォーターフロントの屋外マーケット。地元アーティスト・クラフト作家が一堂に集結。犬連れ歓迎。\n        Google ★4.5（4,833件）':
        "An outdoor waterfront market that kicks off in March. Local artists and craftspeople gather each weekend. Dogs welcome. Google ★4.5 (4,833 reviews)",

    '市内に実在する火山の丘公園。ドッグオフリースエリアあり。見晴らしもよく、地元犬連れ民の聖地。':
        "A park built on an actual volcano within city limits. Off-leash dog area available. Great views — a pilgrimage spot for local dog owners.",

    '200種以上の日本酒が楽しめるサケバー。\n        Google ★5.0（62件）':
        "A sake bar with over 200 varieties of Japanese sake. Google ★5.0 (62 reviews)",

    '広々とした犬連れ歓迎パティオがある人気バー。\n        Google ★4.6（1,212件）':
        "A popular bar with a spacious dog-friendly patio. Google ★4.6 (1,212 reviews)",

    'ポートランドブームの象徴的ホテル。\n        Google ★4.3（1,186件）':
        "The iconic hotel that helped put Portland on the map. Google ★4.3 (1,186 reviews)",

    'オレゴンの日系アメリカ人の歴史博物館。\n        Google ★4.8（128件）':
        "Museum dedicated to the history of Japanese Americans in Oregon. Google ★4.8 (128 reviews)",

    '新設パビリオンが話題の美術館。\n        Google ★4.6（6,243件）':
        "An art museum currently buzzing about its newly built Mark Rothko Pavilion. Google ★4.6 (6,243 reviews)",

    '5,200エーカーの都市森林と石造りの廃墟。':
        "5,200 acres of urban forest with mossy stone ruins.",

    '犬連れ入園も可能な動物園。\n        Google ★4.5（24,075件）':
        "A zoo that welcomes dogs as well as visitors. Google ★4.5 (24,075 reviews)",

    '土曜開催のポートランドを象徴する市場。\n        Google ★4.8（1,102件）':
        "Portland's iconic Saturday farmers market. Google ★4.8 (1,102 reviews)",

    '毎月最終日曜開催の巨大フリーマーケット。':
        "A giant flea market held on the last Sunday of every month.",

    'アジア系食文化が集まる注目のローカルエリア。':
        "A local neighborhood hub for Asian food culture and community.",

    '毎月最終木曜の路上アートフェス。':
        "A street art festival held on the last Thursday of every month.",

    # Daytrip
    '東方向。Multnomah Falls（30分）→ Hood River（1時間）の王道ルート。pFriem Brewery・Solstice Pizza・KickStand Coffee、すべて犬連れOK。':
        "Head east. The classic route: Multnomah Falls (30 min) → Hood River (1 hr). pFriem Brewery, Solstice Pizza, and KickStand Coffee are all dog-friendly.",

    '40エーカーの圧巻チューリップ畑。現在開催中（〜4/26）。乗り物・食べ物・ワインテイスティングも充実。Mt. Hood眺望も美しい。\n        Google ★4.7（5,720件） Google ★4.6（1,384件）':
        "40 acres of breathtaking tulips — open now through 4/26. Rides, food, and wine tasting on site. Stunning views of Mt. Hood. Google ★4.7 (5,720 reviews)",

    '南西45分。Bistro Maison（本格フレンチ）、Okta（2024年JBAファイナリスト）、Willamette Valleyのピノノワールワイナリーめぐり。':
        "45 minutes southwest. Bistro Maison (classic French), Okta (2024 JBA finalist), and a tour of Willamette Valley pinot noir wineries.",

    '東20分。歴史的農場を再生したリゾート施設。広大な敷地で犬の散歩も◎。複数のバー・レストランがあり近場のエスケープに最適。':
        "20 minutes east. A resort built on a historic farm property. Vast grounds great for dog walks. Multiple bars and restaurants — perfect for a quick getaway.",

    'I-5沿い最高の穴場。絶品オイスターバー。\n        Google ★4.6（1,254件）':
        "The best hidden gem along I-5. An outstanding oyster bar. Google ★4.6 (1,254 reviews)",

    'ビール旧工場跡地のクラフトエリア。':
        "A craft district built on the grounds of a former beer factory.",

    '地中海フュージョン。\n        Google ★4.4（404件）':
        "Mediterranean fusion cuisine. Google ★4.4 (404 reviews)",

    '地元定番のアメリカングリル。\n        Google ★4.5（1,187件）':
        "A local staple American grill. Google ★4.5 (1,187 reviews)",

    'チョコと紅茶のスペシャルティストア。\n        Google ★4.8（371件）':
        "A specialty store for artisan chocolate and tea. Google ★4.8 (371 reviews)",

    '香水・ギフトのユニークなブティック。\n        Google ★4.7（334件）':
        "A unique boutique for perfume and gifts. Google ★4.7 (334 reviews)",

    '歴史あるスパイス専門店。':
        "A historic specialty spice shop.",

    '1997年創業の絶品メキシカン。\n        Google ★4.7（1,362件）':
        "Outstanding Mexican food since 1997. Google ★4.7 (1,362 reviews)",

    '歴史的建物を再生したパブ。\n        Google ★4.4（1,819件）':
        "A pub housed in a beautifully restored historic building. Google ★4.4 (1,819 reviews)",

    'ユニークなコンセプトレストラン。\n        Google ★4.7（1,250件）':
        "A restaurant with a unique concept. Google ★4.7 (1,250 reviews)",

    'コロンビア川を望む絶景レストラン。\n        Google ★4.3（166件）':
        "A restaurant with a spectacular view of the Columbia River. Google ★4.3 (166 reviews)",

    '珍しいジョージア（国）料理店。\n        Google ★4.6（220件）':
        "A rare restaurant serving cuisine from the country of Georgia. Google ★4.6 (220 reviews)",

    '旬の食材を使った地元イタリアン。\n        Google ★4.4（332件）':
        "Local Italian restaurant using seasonal ingredients. Google ★4.4 (332 reviews)",

    'Vancouver, WAのナポリ風ピッツェリア。「ナポリで食べたピザと同じ食感」と月2回通うファンも。本格窯焼きピザと自家製パスタ。サービスの温かさも好評。テイクアウトOK。\n        Google ★4.5（836件）':
        "A Neapolitan-style pizzeria in Vancouver, WA with fans who come twice a month saying it tastes like pizza in Naples. Authentic wood-fired pizza and house-made pasta. Warm service. Takeout available. Google ★4.5 (836 reviews)",

    '歴史的砦跡。犬の散歩に最適。':
        "Historic fort ruins. Great for dog walks.",

    '川沿いの新公園。\n        Google ★4.7（6,523件）':
        "A new riverside park. Google ★4.7 (6,523 reviews)",

    '40エーカーの絶景チューリップ畑。':
        "40 acres of stunning tulip fields.",

    'ウィラメットバレーの有名ワイナリー群。':
        "Renowned wineries of the Willamette Valley.",

    '本格フレンチビストロ。':
        "An authentic French bistro.",

    'ミシュランシェフによるテイスティングメニュー。':
        "A tasting menu by a Michelin-recognized chef.",

    'スペイン料理・タパス。':
        "Spanish cuisine and tapas.",

    'ファームトゥテーブルの地元密着店。':
        "A locally focused farm-to-table restaurant.",

    '航空宇宙博物館。':
        "An aviation and space museum.",

    'ワインカントリーの定番ランチスポット。':
        "The go-to lunch spot in wine country.",

    'オレゴン最大の滝。':
        "Oregon's largest waterfall.",

    '峡谷を一望できる展望台。':
        "A viewpoint overlooking the Columbia River Gorge.",

    '川沿いの犬フレンドリーなブルワリー。':
        "A dog-friendly brewery right on the river.",

    '薪窯ピザの人気店。\n        Google ★4.5（2,565件）':
        "A popular wood-fired pizza spot. Google ★4.5 (2,565 reviews)",

    'アウトドアパティオのあるカフェ＆レストラン。':
        "A café and restaurant with an outdoor patio.",

    'サステナブルな地元食材のビストロ。':
        "A bistro focused on sustainable local ingredients.",

    'イタリアンジェラート店。\n        Google ★4.4（94件）':
        "An Italian gelato shop. Google ★4.4 (94 reviews)",

    'セントヘレンズ山のビジターセンター。':
        "The visitor center for Mt. St. Helens.",

    '10本の滝を巡る州立公園。\n        Google ★4.9（10,242件）':
        "A state park featuring a trail of 10 waterfalls. Google ★4.9 (10,242 reviews)",
}

# Now apply translations to .cd elements using regex
# Match <div class="cd"> ... </div> and wrap content
def replace_cd(match):
    content = match.group(1)
    content_stripped = content.strip()

    # Look up translation
    en = translations.get(content_stripped)
    if en:
        return f'<div class="cd"><span class="lang-ja">{content_stripped}</span><span class="lang-en" style="display:none">{en}</span></div>'
    else:
        # Try to find partial match by stripping whitespace variations
        for ja_key, en_val in translations.items():
            if content_stripped == ja_key.strip():
                return f'<div class="cd"><span class="lang-ja">{content_stripped}</span><span class="lang-en" style="display:none">{en_val}</span></div>'
        # No translation found - still wrap it (lang-en will be empty)
        print(f"WARNING: No translation for: {repr(content_stripped[:80])}")
        return f'<div class="cd"><span class="lang-ja">{content_stripped}</span><span class="lang-en" style="display:none">[Translation pending]</span></div>'

# Match .cd divs - content can be multiline
cd_pattern = re.compile(r'<div class="cd">(.*?)</div>', re.DOTALL)
html = cd_pattern.sub(replace_cd, html)

# =============================================================================
# 5. Toggle button + JS
# =============================================================================
toggle_html = '''<div id="lang-toggle" onclick="toggleLang()" style="position:fixed;top:12px;right:16px;z-index:200;cursor:pointer;background:rgba(0,0,0,0.6);color:white;padding:6px 12px;border-radius:20px;font-size:14px;backdrop-filter:blur(8px);">🇯🇵 日本語</div>
<script>
function toggleLang(){
  const btn=document.getElementById('lang-toggle');
  const isJa=btn.textContent.includes('日本語');
  document.querySelectorAll('.lang-ja').forEach(el=>el.style.display=isJa?'none':'');
  document.querySelectorAll('.lang-en').forEach(el=>el.style.display=isJa?'':'none');
  btn.textContent=isJa?'🇺🇸 English':'🇯🇵 日本語';
}
</script>'''

html = html.replace('</body>', toggle_html + '\n</body>')

# =============================================================================
# Write output
# =============================================================================
with open(INPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! Language toggle added successfully.")
