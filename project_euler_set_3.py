"""
Here is a gathering of the problems + solutions 11 - 15 of projecteuler.
To run individual functions without running docstring tests, paste
if __name__ == "__main__": and then the specific function to do so.
"""
import time
from datetime import timedelta

# Largest Product in a Grid
# Problem 11
# In the 20 x 20 grid below, four numbers along a diagonal line
# have been marked in red.
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# The product of these numbers is 26 * 63 * 78 * 14 = 1788696
# What is the greatest product of four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

def largest_product_of_the_grid():
    """
    This function calculates the greatest product of four adjacent numbers in
    any direction (up, down, left, right, or diagonally) in a 20x20 grid
    of integers.

    The grid is represented as a list of lists where each sublist contains
    20 numbers as strings.
    The function scans the grid in the following directions to find the product
    of four adjacent numbers:

    - Diagonally from top left to bottom right
    - Diagonally from top right to bottom left
    - Horizontally
    - Vertically

    It keeps track of the maximum product found across all directions and
    returns it as the result.
    During the scanning process, it prints the details of the numbers being
    multiplied, the intermediate products, and the maximum product found.

    Returns:
        None: The function prints the maximum product and details about each
        scan, but it does not return a value.
    """

    data = [
        ['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08'],
        ['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00'],
        ['81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65'],
        ['52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91'],
        ['22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80'],
        ['24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50'],
        ['32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70'],
        ['67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21'],
        ['24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72'],
        ['21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95'],
        ['78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92'],
        ['16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57'],
        ['86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58'],
        ['19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40'],
        ['04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66'],
        ['88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69'],
        ['04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36'],
        ['20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16'],
        ['20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54'],
        ['01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']
    ]

    max_value = 0
    scanner = list()
    scanner_values = list()
    scanner_dict = []
    product = 1
    for o in range(20):
        for p in range(19, -1, -1):
            # diagonal left scanner
            if o <= 16 and p >= 4:
                for q in range(4):
                    print(f'q: {q}')
                    product *= int(data[o + q][p - q])
                    scanner.append(data[o + q][p - q])
                max_value = max(max_value, product)
                scanner_values.append(scanner)
                scanner_dict.append((product, scanner))
                print(f'diagonal left scanner: {scanner}')
                product = 1
                scanner = []
                print(f'scanner_values: {scanner_values}')

    for i in range(20):
        for j in range(20):
            # horizontal scanner
            if j <= 16:

                for k in range(4):
                    print(f'k: {k}')
                    product *= int(data[i][j+k])
                    scanner.append(data[i][j+k])
                max_value = max(max_value, product)
                scanner_dict.append((product, scanner))
                product = 1
                scanner_values.append(scanner)
                print(f'horizontal scanner: {scanner}')
                scanner = []
                print(f'scanner_values: {scanner_values}')

            # vertical scanner
            if j <= 16:
                for l in range(4):
                    print(f'l: {l}')
                    product *= int(data[j + l][i])
                    scanner.append(data[j + l][i])
                max_value = max(max_value, product)
                scanner_dict.append((product, scanner))
                product = 1
                scanner_values.append(scanner)
                print(f'vertical scanner: {scanner}')
                scanner = []
                print(f'scanner_values: {scanner_values}')

            # diagonal right scanner
            if i <= 16 and j <= 16:
                for m in range(4):
                    print(f'm: {m}')
                    product *= int(data[i + m][j+m])
                    scanner.append(data[i + m][j+m])
                max_value = max(max_value, product)
                scanner_dict.append((product, scanner))
                product = 1
                scanner_values.append(scanner)
                print(f'diagonal right scanner: {scanner}')
                scanner = []
                print(f'scanner_values: {scanner_values}')

    print(f'max_values: {max_value}')
    print(scanner_dict)
    print(len(scanner_dict))
# -----------------------------------------------------------------------------

# Highly Divisible Triangular Number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1,3,6,10,15,21,28,36,45,55,...
# Let us list the factors of the first seven triangle numbers:
#
#                       1:1
#                       3:1,3
#                       6:1,2,3,6
#                       10_1,2,5,10
#                       15:1,3,5,15
#                       21:1,3,7,21
#                       28:1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred
# divisors?

def highly_divisible_triangular_number():
    """
    Finds the first triangular number that has over 500 divisors.

    A triangular number is generated by adding consecutive natural
    numbers (e.g., 1, 3, 6, 10, ...).
    The function calculates the divisors of each triangular number and
    tracks the maximum number of divisors encountered so far.
    It continues to generate new triangular numbers until it finds
    one that has at least 500 divisors.

    The function works as follows:
    - Iteratively generates triangular numbers by summing consecutive
        natural numbers.
    - For each triangular number, it finds all its divisors by checking numbers
        up to its square root.
    - Stores information in a tuple:
        (index, triangular number, number of divisors, list of divisors).
    - Stops when a triangular number has more than or equal to 500 divisors.

    Prints:
        - The maximum number of divisors found so far.
        - The list of triangular numbers along with their divisors when a
            solution is found.

    Returns:
        None
    """
    max_no_divisors = 0
    temp_divisors = list()
    number = 1
    j = 1
    triangle_numbers = list()
    while True:

        for i in range(1, int(number**0.5)+1):
            if number % i == 0:
                temp_divisors.append(i)
                temp_divisors.append(number // i )

        temp_divisors.sort(reverse=False)
        no_divisors = len(temp_divisors)
        tup = (j, number, no_divisors, temp_divisors)
        triangle_numbers.append(tup)
        max_no_divisors = max(no_divisors, max_no_divisors)
        print(f'max_no_divisors: {max_no_divisors}')
        no_divisors = 0
        temp_divisors = list()
        j += 1
        number += j

        if max_no_divisors >= 500:
            print(f'max_no_divisors: {max_no_divisors}')
            print(triangle_numbers)
            break
# -----------------------------------------------------------------------------

# Large Sum
# Problem 13
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690

def large_sum():
    """
    Computes the approximate sum of a set of 50-digit numbers by summing only
    the first 12 digits of each number. This approximation is sufficient to
    determine the first ten digits of the final sum.

    The function processes the numbers as follows:
    1. A single large number (`num`) is split into multiple 50-digit substrings.
       Each substring represents one number from the original input.
    2. For each 50-digit number, only the first 12 digits are extracted,
       converted to an integer, and added to the running total (`result`).
       This works because the leading digits of large numbers dominate the
       sum's significant figures.
    3. The final result is printed, which is the sum of these approximations.

    Note:
        - This approach relies on the observation that for very large numbers,
          the first ten digits of the full sum can be accurately determined
          from the leading 12 digits of each number.

    Example:
        If the numbers are:
        [12345678901234567890, 98765432109876543210],
        only the first 12 digits are used:
        [123456789012, 987654321098].
        The sum of these approximations is:
        123456789012 + 987654321098 = 1111111110110.
    """
    num = 37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690
    result = 0
    num_arr = list()
    for i in range(0, len(str(num)), 50):
        num_arr.append(str(num)[i:i+50])

    for fifty in num_arr:
        fifty_cent = int(str(fifty)[:12])
        result += fifty_cent

    print(f'result: {result}')
# -----------------------------------------------------------------------------

# Longest Collatz Sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
# n --> n/2 (even numbers)
# n --> 3*n + 1 (odd numbers)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is
# thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def longest_collatz_sequence():
    """
    Finds the number under 1,000,000 that produces the longest Collatz sequence.

    The Collatz sequence is defined as follows:
    - Start with any positive integer `n`.
    - If `n` is even, the next term is `n / 2`.
    - If `n` is odd, the next term is `3n + 1`.
    - Repeat this process until `n` becomes 1.

    The function performs the following steps:
    1. Iterates through all integers from 1 to 1,000,000.
    2. For each number, computes its Collatz sequence and tracks the length of
        the sequence.
    3. Stores the sequence details
        (length, final number, and the sequence representation) in a set
        `globes` to maintain uniqueness.
    4. Keeps track of the number that produces the longest sequence and the
        length of this sequence.
    5. Prints the following results:
       - The total number of unique sequences stored in `globes`.
       - The length of the longest Collatz sequence.
       - The number that generates the longest sequence.

    Notes:
        - The function prints the full sequence for each number as part of its
            processing,represented as a string with arrows ("-->") indicating
            transitions.
        - This implementation calculates the sequence for every number
            independently and does not use memoization for optimization.

    Example Output:
        no. of numbers are tested: 1000000
        max_chain_length: 525
        number with longest chain: 837799
    """
    max_chain_length = 0
    max_number = 0
    globes = set()
    for num in range(1, 1000001):
        counter = 1
        number = num
        result = str(number) + '-->'
        while True:
            if number % 2 == 0:
                number = int(number / 2)
                if number == 1:
                    result += str(number)
                else:
                    result += str(number) + '-->'
            else:
                number = int(3 * number + 1)
                result += str(number) + '-->'
            counter += 1

            if number == 1:
                globes.add((counter, number, result))
                if counter > max_chain_length:
                    max_chain_length = counter
                    max_number = num
                break

    print(f'no. of numbers are tested: {len(globes)}')
    print(f'max_chain_length: {max_chain_length}')
    print(f'number with longest chain: {max_number}')
# -----------------------------------------------------------------------------

# Lattice Pace
# Problem 15
# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# recursive
def lattice_paths(n, m):
    """
    Calculates the number of possible paths in an n x m grid
    to move from the top-left corner to the bottom-right corner,
    allowing only movements to the right and downward.

    This implementation uses recursion and is inefficient for larger
    values of n and m due to repeated calculations of intermediate values.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.

    Returns:
        int: Total number of possible paths.

    Example:
        >>> lattice_paths(2, 2)
        6
    """
    if n == 0 or m == 0:
        return 1
    return lattice_paths(n-1, m) + lattice_paths(n, m-1)

# dynamic programming
def lattice_paths2(n, m):
    """
    Calculates the number of possible paths in an n x m grid
    to move from the top-left corner to the bottom-right corner,
    allowing only movements to the right and downward.

    This implementation uses dynamic programming to store intermediate
    results, significantly improving computational efficiency.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.

    Returns:
        int: Total number of possible paths.

    Example:
        >>> lattice_paths2(2, 2)
        6
        >>> lattice_paths2(3, 3)
        20
    """
    grid = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        grid[i][0] = 1
    for j in range(m + 1):
        grid[0][j] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[n][m]


if __name__ == "__main__":
    #largest_product_of_the_grid()
    start_time = time.perf_counter()
    #highly_divisible_triangular_number()
    #large_sum()
    #longest_collatz_sequence()
    #print(lattice_paths(17,17)) # 2333606220 Job took:  0:05:29.210534
    #print(lattice_paths2(20,20)) #137846528820Job took:  0:00:00.000082
    duration = timedelta(seconds=time.perf_counter()-start_time)
    print('Job took: ', duration)
    pass