from base64 import b64decode
import gmpy2
from gmpy2 import mpz
    
ct_flag = 168983021050194662907347201039749624334018305584798256427720234124687821499395153666390978224123298918650634666841336215550941474908921504095575522484700762067500300201770813754829834860160379274218770917011877045290003477941302777813275645827206600893285719668345249109813679100084706805720168329085007460782758007631921415991130486336549188707306230007353731584103743813111361459484156963062467048197197784810987963388806994701719303631086277446332883140767381754531663295830972211329105775590652807896831672045317944698499044717185109826331263880742325176680908085034848658912023592648249382891372815445801584298287992828154303674087879270324463534956976827234471775121783290239009610907010692103067119513346334795530035771747412847347120082250073224717326793195524127752589373772626833205363604302639063635063996415315888154448995128765393322388321625946368324726141912626645511763404366795018372293647789834156882923072714664271870314071506418704226734896563104570538567980078337244458172631785939014466923005417866126704924791729165171531020167761114422832610750889880212549083080919034851061540724772271068277519622721577352309031522022990966077946684626551648566922286118455793868426448507509969246763503205450415229166128868262374270433823914083135853611348754790042896850400037036078943481037029591751435527838487767759703254954134229279382128505339771942811232183179324375703003487364882411643123422010647423419537093092163611143374933991502051487028721063828140540797627411190600418848793637130963264043958897739685803844856463467219915446689941443195410679671915108299521536705829795667865126907180818179606796124412234143954194229060132357439825166137484697470009741077449374837876631241307182909142818216964447612968861464917204471081536547594481906566969835621087706426552708335112106752437623180812787011119108520518113476820756523580517417664743444598781664253726493605734080576470136378017824266607707602794322314564739611667725979766149068325618251309363617350092478679672838776745774768096061989974314899776410940843282422564062639451710651297839173566860316082037172966805574120179204323299078516571816489502165074702263171285117524631376780841893836404494381605058369671539959153028135418837129114267589853903495053270331078676448622434565520870415108801955282036801892341920205470380253963930375401654404073122091516670058700314442302292468233055983750002150749236750630122078148153508547871467800779213993359670944862435962042407861090208806
ct_hint = 3770672017221666816547861884439510290426446279267117656622687976669224914154937491591708478700747291255630586997511263014063062329221017589839096130409321271857421737741894244523075696932433133055734486784305603444758661781833216286494985788703920075575212550879937169200718544335877301359963735183929596161600493933645442460209489926141345737659163670263068011422124424806066933653655217711225048051622117634748597992455153029066999024544303796850868649791972229004870301892150145420544466658351485771466322308260133814894463108888766354453279468671214677882021149801242838437172684385845118444591123846908843913529
n = 18079000622302757068313223467559503885444484811432370681542887670223985604322380165551132889005500224033439395788283539701492362755956703789715734272250642596464879368184603738250220649894056759441935382494235639534468058869514437515092553110849383978953664827723763071485824603999595511662175735145982424328132632347176363357754648339055768543289001800113359615677141748527641961884018026049387569551478900395530038347856807695757211729029109884701713272108083167091312271141341497920718111276034626027406128669233942317585914040960811257625273380372197211004981994917515678650353119179145759650513707894772159605087
n1 = 432392930987450813283722533691710471639791473905431411294422812680756059949490692752875940898283336354461864884367734026785241346129070442248412780693537140560773322402969517700925527579740683508840314300447096080073192208933558154937691810086107491733836827299512462259912221275201109718958299074633000499623440421040143963104420051385605854252248867123433634295390585186828253120863809228241733292139298105094701347702544088317801642266242067133482727786530822718765087789363482995507281709424162756711939795927271454560739347412817394971294525699507322243012757524776508763041144277237805450059749429275583978526920254876287602685393371308963777741407781687881759517910815475529722022156196422492207441469630389516583012482349342676487037424824491336214500358408341603133648118963532274769154562712459317724710468787266997127544995452621261999638308703482143237827695610582427901997818556478678622692719873547639783786326267655086073215766478090203819268036774156269115051885820643961995346825139596078343240305269625072013892835377846140920835534830699221086011664740822794506801515773509685918509255970874660577412413013082901402223037135209213424501835949006236665465839172104928609091664832148404799835006667798625083702202233
n2 = 587352203597414738591602713648322506709565023811865128539829977150224842443109789355241067780017557104203309185211099135760720695098526516430906191145034700195064161116661384068714724405712616476833138349553353734476857313002892535857021132384816143833829866569863544074617198598282028775798047967026029343917720715255092190528673897767786453437854894610296870427263732300925481202747236911016359813167755521534063290783769619808097218066693838752922206907922674956938342136820654120249471093055362841354147216981044807020436226076763925791202952569937084670667847784401517249827854202767823304216269817447354378269105404140948569082723117786248795393077859592887105486252114651174710576137604711606470660779841115268338281243239981393025380799851069654268516883518918597754310300053889061850266635223448855158538878839417198847586851106236199204072636513222521518089791514487352894811239525040518309171371155737270659319157101985569038982203950699018204316900116409532944173129092666933080754152634367412154805344844650121402577506547775707418297375596096498761267790555591843196092275779436130993153083074335542175482544324719067295252900579350697746523113159284088954469553795143934184248871730394281841625405936476833478684660181
n3 = 253966940835424110371060934444877624479916684708798201066188695233344349658054455953310223468546217796100695697931776242638869923048439359017623186526474782867338459263498253894522156946712877312310784382916007656025170459852692814578570957396256618824238440005703177519684618193701564950636936578841798939325772718756674176234987466402497837152072953633430876253858464509875749285845605449118532758629626201703196843330034246655914307672394001399614749044648825030177219478148650516436631938238511364477497365150865792302483787675901527767328295365965920054900565794136202347779920351827502929543603141235195334612780481680242180896195453515002702724802848207569700570221971365301454942213417215146736183562533267171349711241863062266258176279809656026231955226364711510691175143961821961538996349805318412205295819319820491530447387214896368780283586802952216236930589182914655321771763585708140369159536084376528398484195831953437176062578639887047945357635059754739907561665205203281144212342426974849555557179398189601043212541232215802310269023864792307707421294737959517088991710020002288313084327010723688324739322015568710153316881501545927957631699484417864491625131009890130841647565846849747590501229509874563111792909186529299459498603767514124650454823290451105677800120537941346486558376642860815481803588774038808664372144839016416321886654468598462737403431337976447939405360691389869468755793006036447453013095749767052012048757729582274392578791289856240675643306612232207304045160677435091951341939961624595613632981654956099078098012141779955916210630792851114511358314111107705581439477416066001852682599750333993536646651542369777516191909394426662740795081556067697605461397031682916836365748327360301315644451857264781645126013044438517874696729838735370775019619467284546083451110591844170567129083381610546323583279971866683988314790970561772059299398282152905686450814954253636840711226443746268939223715380642705606578926428605889585075837835227973738667854844699633094087335324374704037117933576183449223872696690444525398999104906905626930008419442296775907723357533708516202675947929180938276011173829421533614467941392579125540796746745022921082245660937608000104680753586023491241913641568804988306091316699862320344921277599214913874270523741369508751270726206273560239470231209244308298415829253422757314384515566661465572350284548940660177853719277052716232230083362429181983803204614875578166843318523381630816379446304944384173

e = 65537

diff_xy = int(b64decode("MTgwOTE5Njk0MzYwNDUzNTM4NzA0MzQzMDI2MzUwNTA5MjY1ODYyNjg2NTUyODgxMjYwOTY1MjY5MTU0NzYwNjAyMjI3MzM2Nzg0MDEwMzk0NDE2MDg2OTc2NDU4MTM0MTQxMjUzMDk3NDg2MzI3NTY4NzMyNzkyNDg3Nzk5NTMwMzQ4OTIzMDg0NDIzNTE0OTc4MzM3NTExODk1NTQ0MjMyOTA2Nzc0ODY1Njc2ODMzODQ5MjczMjk2OTQwNzE3Nzk2NzA4Mzg4NTM3MDc5ODA4NTU0ODM1NjQzNDk2MDE1Nzc3NDA4MTMyMDg4NzE0NTQwNDkyNTAzOTk0NjMxODc0ODA2MjQ5MTM2MjM0OTAyNDU5MjM0ODY1NTQwNzU0MDkwMjM0NDM0MTc0NDExMzM1NTQ=").decode())


sum_xy = gmpy2.iroot(diff_xy**2+4*n, 2)
assert sum_xy[1]

sum_xy = sum_xy[0]
x = gmpy2.divexact(diff_xy + sum_xy, 2)
y = x - diff_xy

tot_xy = (x-1)*(y-1)

d_hint = gmpy2.invert(e, tot_xy)
print(bytes.fromhex(hex(pow(ct_hint, d_hint, n))[2:]).decode("utf-8"))
# https://pastebin.com/Ss2RBhVN

diff_pq = 1242254675415543503766895259645948956714565032314250524137831358209708821235656498568430715669433767267932849541878017070288450179946709465045989670967018664210510249524337371370194547615415463025339620947231767209068732717430495760349314268551548766308784014198416595085792538559604304511204343591110575966133411683494405581283707510216996645953704755030009685705598286875623318644696137632011886800339620903367486743178531224878773137291025036671073484661382147243850459058814557865200213432899144037919525943152724499373048644942059816246177492327411881290878242343351064106920857862403657075984791138952343067648
sum_rq = 42586529994337243194594377547592760240086486028023740254425823469718813679975915502231955918323718835882222049323701867968652256315221185961367892844011306331592144711636470848175554548789329171719808343017960868421271177298276565596919161553043629866916804224794067993887169815975501872828652912660595467444117226917978816760167520113510193812597514339079391849704994946666438188636725168245833136374679832893838578803430257564660326875785366074158859721507370632997652618843009207468965641349574727141875293709085091812931425610936131487776887932443004650024160535276113074323157342494176103553301253459146310813328
sum_rp = 41344275318921699690827482287946811283371920995709489730287992111509104858740259003663525202654285068614289199781823850898363806135274476496321903173044287667381634462112133476805360001173913708694468722070729101212202444580846069836569847284492081100608020210595651398801377277415897568317448569069484891477983815234484411178883812603293197166643809584049382163999396659790814869992029030613821249574340211990471092060251726339781553738494341037487786236845988485753802159784194649603765427916675583103955767765932367313558376965994071671530710440115592768733282292932762010216236484631772446477316462320193967745680

sum_pq = gmpy2.iroot(diff_pq**2+4*n1, 2)

assert sum_pq[1]

sum_pq = sum_pq[0]

p = gmpy2.divexact(diff_pq + sum_pq, 2)
q = p - diff_pq

r = gmpy2.divexact(sum_rq + sum_rp - sum_pq, 2)
s = gmpy2.divexact(n2, r)

assert p*q == n1
assert r*s == n2

# calculate ϕ(n3) trivially by ϕ(ab)=ϕ(a)⋅ϕ(b)
tot_pq = (p-1)*(q-1)
tot_rs = (r-1)*(s-1)

tot_flag = gmpy2.mul(tot_pq, tot_rs)


d_flag = gmpy2.invert(mpz(e), mpz(tot_flag))
print(bytes.fromhex(hex(pow(ct_flag, d_flag, n3))[2:]).decode("utf-8"))
# zh3r0{Y0u_h4v3_b34ten_RSA}





