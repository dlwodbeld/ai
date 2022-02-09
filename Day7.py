"""

#해쉬탐색법

선형 타색이나 이진 탐색의 전제 조건은 어떤 데이터가 어떤 요소(index)가 있는지
전혀 모르는 상태에서 검색을 시작한다는것이다.
그러나 해시 탐색법은 데이터의 '내용'과 저장한 곳의 '요소'를 미리 정할때
연계를 해서 극히(***) 짧은 시간 안에 탐색할 수 있도록 고안된 알고리즘이다.

24인 데이터는 첨자 24에 넣어두고 36데이터는 첨자 36에 넣어두는 것이다.
단지 2개의 데이터를 보관하는데 최소한 37의 요소의 배열이 필요하다.
낭비가 심해진다.

해시 탐색법의 특징은 나중에 데이터를 쉽게 찾도록 보관하는 단계에서 사전준비를 해두는것이 특징이다.

가장 알기 쉬운 방법은 데이터를 데이터의 숫자와 같은 방에 넣어두는것이다.
하지만 메모리의 불필요한 누수가 커진다.
따라서.

먼저 방을7개 준비한다. index 0 ~ index 6
0 1 2 3 4 5 6

11 15 23 26
11%7(index의 수) = 4
15%7            = 1
23 % 7          = 2
26 % 7          = 5
 0  1   2   3   4   5   6
    15  23      11  26

재대로 흩어진 상태가 되었다. 각각의 데이터를 나머지값과 같은 번호의 방에 저장한다.
데이터를 저장한 방의번호를 계산한 식은
해시값 -> 방 번호 = 데이터 % 방의갯수 <- 해시함수
11이라는 데이터를 찾아보자. 찾을떄도 저장할때 사용한 해시함수를 다시 사용한다.
저장할때의 계산식은 '데이터값%7' 이고 해시값은 4이며 인덱스 번호를 나타낸다.

따라서 해시 탐색법을 사용하면 단 한번의 계산으로 찾고자 하는 공을 찾을수있다.
검색 시간을 놀라울 정도로 단축시킬 수 있다는 큰 장점이 있다.
#해시 함수로 데이터를 보관하는 알고리즘
-해시 함수는 데이터의 저장소 첨자를 계산한다.
-저장소의 첨자가 겹치는 것을 '충돌'이라고한다.
-충돌이 발생하면 옆의 빈 요소에 데이터를 보관한다.

1.배열은 2개 준비한다.
-첫번째 배열은 데이터의 갯수만큼 준비한다.(임시배열) arrayD
0   1   2   3   4   5   6
12  25  36  20  30  8   42
-두번째 배열은 11개를 준비하여 0으로 초기화한다..(실제 저장될 배열) arrrayH
0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0  
arrayD 첫번째 요소부터 순차적으로 해시값을 계산하여 arrayH로 저장한다.
지금은 요소수가 11개이므로 11로 나눈 나머지를 계산하여 저장한다.

해시값 = arrayD데이터 % 11(해시함수)
첫번째 arrayD[0] = 12 를 해시함수에 넣어 계산하면 해시값은 1이 된다.
0   1   2   3   4   5   6   7   8   9   10
0   12  0   0   0   0   0   0   0   0   0
이미 다른 데이터가 할당되어 있는지 확인하여 비어있으면 대입한다.
왜 확인이필요하느냐는 다음에 자세히 나오지만 요소가 많으면 해시값이
즉, 나머지 값이 우연히 일치하는 경우가 많아 이미 데이터가 저장되어있을 가능성이 높다.
요소가 비어있는지 확인하려면 0이 있는지 확인하면 된다.


arrD[0] 이후의 데이터들도 마찬가지로 같은 절차를 사용하여 데이터들을 순차적으로 arrH로 저장한다.
따라서 반복구조를 사용한다.

종료 조건도 필요하다. i 의 최대값은 6 이므로 7이 되었을 때 반복을 종료하도록한다.
0   1   2   3   4   5   6
12  25  36  20  30  8   42

0   1   2   3   4   5   6   7   8   9   10
0   12  0   0   0   0   0   0   0   0   0

0   1   2   3   4   5   6   7   8   9   10
0   12  0   25   0   0   0   0   0   0   0

addD[2]의 데이터 35의 해시값은 3이다. 이비 데이터 25가 존재한다.
0   1   2   3   4   5   6   7   8   9   10
0   12  0   25   0   0   0   0   0   0   0
            -----이미 25가 들어가있어서 넣을수가 없다.
해시 탐색법에서는 이러한 해시값이 이미 존재하는것을 '충돌' synonym이라고한다.

이러한 충돌이 발생하는경우 즉 arrH[k] = 0이 아닌 NO 의 경우 처리를 생각해야하낟.
해결책은 간단하다. 바로 옆의 요소가 비어있으면 거기에 넣으면 된다.
arrH[k]옆의 요소는 arrH[k+1]이다. 

'''''충돌에 대하여''''''
충돌이 너무 자주 일어나면 추가적인 처리가 많이 필요하게 된다.
해시탐색법의 장점이 무색해진다.
충돌이 일어나지 않게 하려면 데이터가 많이 흩어지도록 해야한다.

요소가 많아질수록 충돌의 가능성은 적어지지만 메모리의 사용량이 늘어나고
알고리즘의 효율성이 떨어지게된다.
탐색 처리의 속도를 유지하는것과 가능한 메모리를 적게 사용하는 요소의 수는
일반적으로 저장 데이터 수의 1.5배에서 2배라고 알려져있다.

0   1   2   3   4   5   6
12  25  36  20  30  8   42

0   1   2   3   4   5   6   7   8   9   10
0   12  0   25  36  0   0   0   0   20  0

0   1   2   3   4   5   6   7   8   9   10
0   12  0   25  36  0   0   0   30  20  0
                                ㅁ<--8 충돌발생
                                    ㅁ<--8 충돌발생
                                        ㅁ<--8 충돌발생X
0   1   2   3   4   5   6   7   8   9   10
0   12  0   25  36  0   0   0   30  20  8
마지막 요소인 42는 해시값이 9이다. arrH[9]에 이미 데이터가 존재하고
arrH[10]에도 이미 데이터가 존재한다. 그리고 그 이상의 값은 없다.

좀더 간단한 방법을 사용해보자. k를 하나 증가시키는 처리 k + 1 -> k의
k+1을 arrH의 요소수로 나누어 그 나머지를 k에 대입하는 방법이다. 즉
(k+1)%11 -> k 를 사용한다.
k 값이 0 에서 10인경우에는 11로 나눌 필요가없지만 k 값이 10을 초과하는 경우의 처리를
별도로 준비하는것은 비효율적이다.
두 경우 모두 11로 나누는 처리를 거친값을 대입한다. k값이 0에서 10인 경우에는 이 과정을 거친 후에도
원래값과 같아서 문제가 없다.
k가 10넘어 11이 된다면 나머지가 0이 되서 (11%11 = 0)맨 앞 요소에 다시 할당할 수 있는 장소를 찾게된다.
만약,arrH[0]에도 이미 데이터가 있다면 k 12 12 % 11 = 1이 되어 바로 옆칸을 확인하는 처리를 진행하게된다.
언젠가는 빈칸을 발견하게 된다.
# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day7.drawio#R7V1tb6M4EP41SHsfWoHBxnxM0uxWpz3ppN7pbj%2BtCJCEK4krSrbN%2Ffqzg4Fg08bdvAxEtyvtwmAbd%2BaZ8bzY1HInq9cvefi0%2FI3FSWYhO3613DsLIT8g%2FF9B2JYEj9glYZGncUlyGsJD%2Bm8iiVWzTRonz62GBWNZkT61iRFbr5OoaNHCPGcv7WZzlrXf%2BhQuEo3wEIWZTv0rjYtlSaXIb%2Bj3SbpYVm92SFA%2BWYVVY%2FmTPC%2FDmL3skdyp5U5yxoryavU6STLBu4ovZb%2FPbzytJ5Yn68Kkw5cv6PGP6c2Nj34dY3sRh3%2Fesxs5yo8w28gfWE622FYc4PN%2BEpcxizar3bvGL8u0SB6ewkjQX7jcOW1ZrDJ%2B5%2FDLGdus4yT%2BOqsI8iVJXiSvb87eqXnCsZSwVVLkW95EdsCe5LjEEZZcfWmE4lScXu4JxJO0UOJgUY%2FcsIpfSG59gHPIgHNFzh5r2KA2kyq2rl4XQnFu5xl7iZZhXtxmjD19z9JV%2BharT8BO4veMna7GTq69dxYe2xbmd%2FaNhUi4Ej%2F9otixQGj3PX%2F%2BuHuucD4vEShZfQCuJ2BnxRbJTZdAs9M7jM58yVazzfNl%2BIPaDHKg%2BYMP84ePwheZ5CL8Ua0bOH8cEwbFfKWUtywvlmzB1mE2bajjRg1tfte0%2BcotnGTeP0lRbOWyH24K1sVa8aL3GcvnxTZ5lLzzE0k%2FpAjzRVK80y7oFlSeZGGR%2FmjP4%2BRsJxrXH%2FiEi5%2FH5jzNsgnLWL7r58ZhQueRWH12S9PeExLRZDY%2FizWskQuGZl9j6334vOSUhyTMo%2BVxy4fC4vk8IVEni2M%2FmNn2aViM7DaPPXAWG%2FhDwzIY1NBgOG9I6jIWg2ps3%2FlF%2FXTiiWoZbBsat45ucgeO28AUt3a3rC6D26ALt3v%2BvoW4B2IL3epw%2FR%2BPs9inX%2BIQPI71NW6bPA8cypUbfBDLLiSUq1mqNriKTe0drUIIVASmAJaCA1ZPPT0UHGLDcnX1FQ2esQae2KXNJaE%2BNFf0BJM1nVgj2%2BIC4xfB1Bpha3pnBVgQUUkcWYEnLiix6GRH8a2gfnpnjfnTsTX6bI2pJKoDjkX7gM%2BZZGLxmuX8qlzGpiOLL3YBaoZCVUdKRUdavX3kizHFUz69QMxQdqGaYA%2BIUk06zsLnNLrN2Cb%2BHoUZ%2F7%2FQFSlxYpz4XYoUEN8NyWkQ4viKgeoKGv0OxNCzIaYjh1biY1xiYizkqkiRllLkRFdcl83GE9kxoBJDo8nOi2kApaNjLBBXQ4nijjZXK3zHBRe%2BHlcpOh80Gjvi1iHYXXNZB1J7OSp4m44uqhilr%2BAIX2HPwnAzLvpggZ5yaBUP1yN93JK%2B25X9vKj0kR6d6H7JsDxp06gQ0W5ZXciVfjMsTIdRBmrbMQye%2BXSvLi1X7wI4iGQCiWTUFd4MMZXft1w%2Buj5Eu6aIxqCIfrNEnw4kZde3Ij3SI4zh5%2BwQNkSzA1ppdfUC95pBsJ4zON%2F%2BLfrf4ur22%2F6zu1c5eHm3lXcQInM9UAOki6yPeValMAtemXUN9vgNzMSY7uUod2mC4VUvLabvoRR4PYSvYVVZnytCqm%2BKVNAKFtKLh2ntwe3SVVmy%2FiS8vV96ZVzhq1iuC%2BIzvKbFnsvA777tPWkcBnFzDn%2Fh2ByR7Po7S%2FmrG%2BkSRbqY3FLbtj1KEXWq1b8ar1QpOUQjxVGeh9u9Zk%2BiwbP5SwlRdtEr7V16XHuEfQV05YwbCNYMPUKf9ex1s%2FLsrpCIySp592cNIvBrkN8fhbYvpdBH%2B%2FVmulXvAj%2BxDhPV51ZPwnys%2FXl00tWD%2FcdaJx97pJNYsVge%2FNkQvSrw2C6O1dXVsUWRuKgLc8GdLNFSu7MIaze19LrSXlLqUcqmoqRHdk%2BVqhy%2F3asHN7MpuyBRDkSdFV6tmC93HwRyWLkLQIx%2Fq6Hip6p9UavcdzxUCGkfW%2Bis3HmuDhVHtQSnO%2FhydTGEZ1rwwKAxhKenGYZVumshmYJHFh66OiCb1jk80Mywp9c5hlm5a6%2Fi8IA2OJM4MECb5s090Dyk15k3H1LhroVkH7wE7emJ3eHX7TzTVKUHet7J01OVfSwCtZ0J8KyGpyeEhg5X0w1tGBaueujarxpQC6gYfEsEvrrwDZuGbx7o7h6sh289LQG1EEvAy%2BsYBKDAFaCjUw3diVlHLQc4F6gAqS917APpY%2B1bJh9rT5wLVICwHsT2tQLUYk4AvwJdXZiKTcNUArr3Hx8KU%2FudQHRVswC%2FVRpf3bcNsGmQSkB3KmI9SB1iClGFNHzmBV9dHItN41iCQBF96GBWz3OIKpTh%2FQyiR7rDTyISZIhmDBrsEj3Yhd78b%2B1t%2Fd87CXD%2Bzf%2FGIitP4IKJDHUZoJ7lfTUf0AZPT5CO714M3MZ4pism6AFQoseRfcr8qlCFr1GQ6%2FvkqOk5FQy64cG%2FPhNhynjQhAfpPB%2FUv5S7ZirAt5KQHm3SvljO%2FejsXHd2Wj2gQC9x6kJ9qYMOHaPQvkPwwQ70EucuyFDOXWiOKvzhv%2Br3ZvRBpy928OLomMpQvaoS1an1GGsBz4Fa2KEO59HL6uNRnWcvPvHLsfNLk8A6RjfVj4Fj8VfQ2brYo5d%2FOvO3uz8nqq1pMAAPR3098%2FL%2FUY4%2BHOXALr5tf4YtOOdhDn7b%2FOajUs2bXx%2FlTv8D


"""