"""
#이진 탐색법 Binary Search

탐색 대상 데이터들이 미리 오름차순 또는 내림차순으로 정렬되어있어야만 한다.
탐색하는 범위를 절반씩 추려나가면서 탐색을 한다.

0   1   2   3   4   5   6   index
11  13  17  19  23  29  31  data

0   1   2   3   4   5   6   step 1 가운데 인덱스 즉 3을 열어서 확인한다.
            19              찾고있는 17이 아니다. 그런데 정렬되어있다는 전제조건이 있으므로 이후의 모든 데이터는 절대 찾고있는 17이 될수 없다.

0   1   2                   step2 새로운 범위의 가운데 인덱스 즉 1을 열어 확인한다.
    13                          찾고있는 17이 아니다. 그런데 정렬되어있다는 전제조건이 있으므로 이전의 이후의 모든 데이터는 절대 찾고있는 17이 될수 없다.
2                           step3 마지막 요소만 남게 되었지만 찾고있는 17이 아예 없는경우도 발생할수있으므로
17                                처리해 주어야하지만 지금은 마지막 index 2가 착조있는 17이므로 검색을 종료한다.

#이진 탐색법의 알고리즘
1.가운데 요소를 선택하는 처리(인텍스의 평균을 계산하여 구한다.)
2.가운데 데이터와 찾는 데이터를 비교하는 처리
3.탐색 범위를 절반으로 줄이는 처리

#요소의 갯수가 짝수일때는 어떻게 해야할까!!!!
0   1   2   3   4   5
11  13  17  19  23  29

요소의 갯수가 짝수일때는 가운데 요소가 2개라는 것을 알수있다.
이경우 어느쪽을 선택해야 한다고 정해진 것은 없다. 단지 둘 중하나만 선택하면 된다.
따라서 같은 공식으로 계싼해 보면 (0+5) / 2 = 2.5
소수를 정수화하는 방법으로는
1.반올림
2.올림
3.버림
하지만 재일 간단한 방법은 3.버림이 재일 쉬운 처리방법이다.
정수형 변수에 넣기만하면 자동으로 소수부분은 잘려 나가기 때문이다.
쉽게 정수 부분만 얻을 수 있게된다.

#해시 탐색법
데이터의 '내용'과 저장한 곳의 '요소'를 연계해두어 극히(***)짧은 시간안에 검색할 수 있도록 고안된 알고리즘


해시값 = 데이터 % 저장공간의 수 <-해시 함수
미리 해시 함수를 사용하여 데이터를 저장하는 장소를 정해서 검색시간을 놀라울 정도로 단축 시킬수있다.

#해시 탐색 알고리즘
1.해시함수를 통해 데이터를 저장하는 알고리즘
2.해시함수를 통해 데이터를 검색하는 알고리즘

배열을 2개 사용한다.
정렬 전에 준비된 데이터의 배열과 데이터를 저장할 배열을 준비한다.
데이터를 저장할 배열의 수는 데이터 갯수의 1.5배에서 2배로 준비하는것이 좋다.
검색 속도와 메모리 효율 면에서 적당 크기는 1.5배에서 2배로 알려져있다.

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=%ED%95%B4%EC%8B%9C%ED%83%90%EC%83%89%EB%B2%95.drawio#R3Vzdc%2BI2EP9rNHP30IxtWUZ%2BxECbmaYzN81Mr3k0WIAbgzghEuhfX8mWsS0R4hR8ikkeIq0lf%2BzHT6vdVQAcrfa%2FsXiz%2FIMmJAOek%2BwBHAPPcx2IxR9JORQU5CnCgqWJGlQRHtN%2FSTlTUXdpQraNgZzSjKebJnFG12sy4w1azBh9bQ6b06z51E28IAbhcRZnJvV7mvBlQcXeoKLfk3SxLJ%2FsBmFxZRWXg9WXbJdxQl9rJDgBcMQo5UVrtR%2BRTDKv5Esx79c3rh5fjJE1bzPhx%2F39X%2Fz38XfsPgSLwY8%2FH777h19c9R0vcbZTX6zelh9KFpBEcER1KeNLuqDrOJtU1IjR3Toh8jmO6FVjHijdCKIriP8Qzg9KvPGOU0Fa8lWmrhbPlA968%2BMUaUt3bEbOfBFUShKzBeFnxg2OIhC6S%2BiKcHYQ8xjJYp6%2BNN8jVkq0OI6r%2BCwaitUfYDt0DLavqQ3Gk33K%2F661n%2BSt7pDqjffqznnnoDoWhFXc0Jq0DGGlQBpbEK8El6OM50xxMrL%2BIiDnqyFHtqSr6U68VfS6TDl53MQ5U14FYjalMU%2BzbEQzyvJ5cI5nZDYT9C1n9JnUrkwx8lElixfCONmfl4bJPDXB85UyHrT%2Ba4V3bgliyxrWleOuzm8PGQw%2FiDWg37gUtFV1eKGq51OHjMWH2oANTdd8W7vzN0moKYHXVAJfX0zeGQ99RxN78QaVEhw%2F5QK9wJ8ENW2ohWcTAQOD8QLoAIqeARpLKJQkhYbr6XZT4KFjiKZfQOg7toHQNRW%2B5%2Bo%2BaKnugU1tN33i51LJ5Z5iLBQ%2FVYovl6ozC%2F%2BR8%2B7HdR7JX0mna16jFz%2BnbCHIf7qxBejZtoWbM4WwpSlc6g9cxPXQ4Hp6NIUT%2BH4z%2Bu4GtvXdNXcdZJ2YOp9l6WZLPszuJCZ4fnJJDWaYTOdXYiv0m0sqts5WU6N7jiOu3xJIQptAUr5lje%2BP4o153xRawwn7%2BmzulcFkDEIEIh9MRgBHIBxJyBZEDEHo5EQIcAgmEYg8OfKqMD6fe6dd9SSYBuhKcA1RE1fcE2IIAlMMQWchi4ENFCmjd1XE7ql2pfPoXS2MfUGowogtQKdpY8dYQ3mLAunUrEpwH415uPp%2BLzgf8xhcNFwLz3cUITHjyumJnTnwosKFKyV9Cy4c1sRjffcO3U%2FhatRAIhfCESbuHO8sUsjON8JSwQ3COkCPMp33nt%2FiWomIIl9zXd8xdx21tPEd2bupYjFj94aabZfxRjYTOtutckm9Z9rTQu0epm%2B5W4jgxD9l09ibwmvZtP%2F5jNquDdtJ0xXA1flCD3E3Cz3UtEhLVrw%2FHv8MU%2FYMU66ijl9EM3K%2F5ks3cm9p1fZ1HbAeaPTMZIcNk7%2Bm%2BbZOs1%2Fq0F%2FGeDPilS9mzTRTMwJ%2FM3agQ451M4A3FyiDbc2gCFpaqzYxzaCPkbKBViHgWtfo8sY3pNFtQ78QWdVoM%2FYro5CRA6KJbIRjgH2J75OhJIZe3hb0CcBIhimHDhheOUxpFex12%2FCsb2vQCRH13DZQS9vwreZFoBm%2FP7r9zbjdHtxwvYFhEdYTK8gMrVgqQvw%2FUX7BdnaoTZLdp%2Fq1alre66K2t21pG7Raio3MfXd%2FSrH7JGZkdXMJT5Yw3hu7y70Jqp%2B6aFEHTt969bZv7l%2F67kq0rVosDjtZU%2FETZ3mEFy2cZ1y608KLlo2R9LelBx6CEEsHGw9BKDzAID%2FKMGWitZCtZ1UjgHF%2BowGIcOma5xNkKUEA8KjhrOMoH583hv7dDTspyHqRGDSrIvtXJBbAJlsD6xCGTKe89wcN%2FNb1plZrr5G5Ttt2u%2B3k3C7elp7ObQU6hrUsrrlWmss3w8pVmqtvJ0b0BQFaXxAQtGkqlk6RXryzeKOA64208bXT06H2HOScT0%2Fr43%2FK2TtkBs%2Bb6em8qMxzyiS1bN5SnhrrxYL2A1R9OxHT%2Ffap5ZKnVwEXAHOxHevPKftv2XEQnh3fkR2b6%2B9e5V2kRhebu4Hc1snNnaDf%2BJ7uqAy6P9SBXYtu9e8%2BCoFW%2FzQFTv4D


#단순 선택법
1.탐색 범위의 최소값을 찾는 처리
2. 찾을 최소값을 맨 앞의 요소와 교환하는 처리

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=%EB%8B%A8%EC%88%9C%EC%84%A0%ED%83%9D%EB%B2%95.drawio#R3Vtbk6o4EP41qdp92C0gCcKj17Nn65yq3ZqHPfOIEpQjEgvjqPvrN4FwDTq44mR0pmomaRIC3V9%2Fne4ogOPN8UvibVffqU8iYBn%2BEcAJsCzTgA7%2FJySnTIItKVgmoS8HlYKX8F%2BSz5TSfeiTXW0gozRi4bYuXNA4JgtWk3lJQg%2F1YQGN6qtuvSVRBC8LL1Kl%2F4Q%2BW2VSxxqU8j9IuFzlK5u2m13ZePlg%2BSa7lefTQ0UEpwCOE0pZ1tocxyQSysv1ks2bnblaPFhCYtZlwnr%2F5%2BA1jI%2F237NhErjTr5uvwW9QPtybF%2B3lG8unZadcBcTnGpFdmrAVXdLYi6aldJTQfewTsY7Be%2BWYb5RuudDkwp%2BEsZM0r7dnlItWbBPJq9maYqGzLydFO7pPFuTCG%2BXAYV6yJOzSQLcwAkcvoRvCkhOfmJDIY%2BFb%2FUk8CaNlMa7UNG9IZV%2BheFNVfMi7acswFBuUGhbqOqxCRl62XqqIA3e8ujaDMIrGNKJJOhcGWPwKOY1ZRZ79cPmOJXRNKlfs9KewyxtJGDletoyqRznBQvJtJAGYtuwfSncycx9ZVVwpn9e%2F6s2nw7zVFfNGu60%2BCPOWovgX%2FshM1X4UcX4nVyPd94gTLFoRvXDIPLgPoh3tgIYqoKcj4IzA0AHTMXAc4I4FuYg2AkPemAAHAnciho0s4OJ%2BCScIrEWrGXx7buOeiAViVCeWFjNwElPMYN%2FNDE6LGcZghIX2hept4PDGEIwM4GaXDDCaphJHtM%2FbwLjaBqY7m80GXL5MPD8kNeKf8EvTmWAtfreQCf0hsYIXhcuYdyISsH5sNDDrrgKxaqTCcFUjYfNeVoLPx%2F5uR%2FY%2FZ6yPYX%2Fs6tAzOYbsR6X9Km71O5a9yVHeOe2c8k7M3%2FdHOVB0X6vXymlpL5%2Bnw6ZQ7y7WVZwp3cVatrcR%2FBRlPGJEJP6FZ2O%2FqhS3opv5fnd9iHEWpD3EzB2MsNEPfTUjfdHXFuqtlnxNxA8eY9Ko7rrATWO%2BiOqOCO9DGwzHvYYWPwhIcF1k6SOUNGyBrLZ432IL824BH6r72QcPJUWJ5d1QAnXSjqXG8JDr8Pg9jIscOryA%2BUfPoWEb9j%2BUh2BLyvHg0IddoY%2B0Ql9V%2FLqKeRl44%2Flum4VeYIm%2FpmKd5%2FEGZGj3BqQY5UR2j%2B4QqKtD2DodwlZ3RDHVofo808jTiS6ZRu%2FmusEKcupfNORLl1UWo%2B5sg6YTZfCQs0pbDpPEO1WGbcWA3fl1rMY62GicZrwzPn%2BuEkrZE5TAKnRyA%2Fmqfs6zGoBHa4AnT5z3IO0lTog%2FC8P%2B3%2BJAQQ8FJbxWiOP%2B9GB3ZfNBHzxyrfs3acaGl93%2FnfH3cX9bTTv0hpoHK2p1xiDSm13aV7J8djXNQDc8A8WTB6d7rP2IFqom0OFnfWJ%2F0JV%2FtRZ088e8VFlZq%2FB%2BmlzS1r%2FTcXRGFF27k1tB322XgJql4J6Sl%2BY6Drq8ezHxbePz97hvsqOe7axlPSmlgWcuKQ20R0Dc8mGCx46AsOuRJtL6ISWowl7s75q63628rWj6dLHfpLp4D%2FDzzBbf5ueO1TBxfNSGdMeaw76QXuztGtSjD%2Bn5jSsKJ7Gvgv1TfyasqVZX%2BwkNUnH84ASCup7QIK0nNEg9oTkUe2eZKrbmiA8bPVGzGKP9QAarnPLo4O96GoOwVvCfq5CHsnZS9YI8sXxuZ9CeUeKn%2B8Qjwl2dQevRJFIPLVqQL33i8MQ%2B8AnSKS2Q11xVuRn93aodxTfceq6qoDN76rNVEvO28Y0v0N2nqoLUynb4rFWVJg3cM9fk3fKrlJmxyi%2Bkwul%2F

#단순 교환법 Bubble Sort
인접한 2개의 데이터를 교환하는 처리를 반복하여 저넻를 정렬한다.
속도가 느린 알고리즘

알고리즘
1.오른쪽 끝 요소부터 차례로 인접한 데이터를 오름차순 정렬하여 교환한다.
2.왼쪽 끝부터 순서대로 하나씩 데이터를 정렬하여 확정시킨다.

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=%EB%8B%A8%EC%88%9C%EC%84%A0%ED%83%9D%EB%B2%95%2F%EA%B5%90%ED%99%98%EB%B2%95.drawio#R5R1dj6M28NcgtQ9XYWzAPOZr26vupFb70NtHEpyELoGIkEvSX18DBhIbEucC68DtSrt4sGMz3zMeEw1ONsffY3e7%2Fhp5JNAM3TtqcKoZBtAhpv9SyCmHmAYDrGLfY50qwKv%2FHylGMuje98juomMSRUHiby%2BBiygMySK5gLlxHB0uuy2j4HLWrbsiAuB14QYi9B%2FfS9Y5FBt2Bf%2BD%2BKt1MTOwnPzOxi06syfZrV0vOpyB4EyDkziKkvxqc5yQIEVegZd83EvD3XJhMQkTmQHv%2Bz%2FtNz88Wn%2B%2FjOKlM%2Fu8%2Bbz8BNnivrvBnj0xW21yKlBAPIoR1oziZB2totANZhV0HEf70CPpPDptVX2%2BRNGWAgEF%2FkuS5MTI6%2B6TiILWySZgd%2FM504kaH46BdtE%2BXpArT1QwTuLGK5Jc6%2BiURKDcS6INSeITHRiTwE3875crcRkbrcp%2BFabpBUP2HYgHIuJ92syudF2gQYXhFF2HtZ%2BQ162bIeJABe8Sm0s%2FCCZREMXZWLg0098UHoXJGTz%2FofBdEkfv5OyOlf2UdPlO4oQcr1NGxCMbYCD2NEwBAIu1D5U4gUJG1meiVIxrH%2FVgcDxvyPK8Xk%2BrD%2BJ5Q0D8K11yImI%2FCKh%2BJ3dzuucSvFzUcvQCk%2FmyG47Gyhkaigw9G2t4rI2wNptoGGvOJFUus5E2NjWHXkw1x9EcnHYbG5pjtqtwlktjUUsGz5pbZkuKBQB4SQejhg5Uiwl0sDqjA66hwyRD%2BSSjg6XhSUYEXXPyW7o2nmUQnF43E0G%2FmwjAeXl5sSl8FbueTy40%2F5Temr2kaot%2Bmp%2Bk%2BEPpDG7gr0LaCMgyaYdINrikETRFIpW%2B3jmRTNAVleDw1L8jqf6biPUx6t90VOCZHP3k29n1W%2FpRv5msNT2yT84ap6IR0uf9VnVMm2%2Fn96phWasYp4KmUK0b6wjClLmxhuVuUv0U5HpED0j4Cw3HfhVV3DrazPe7%2B20MXpB6GzPHJjL1dtQXb%2BrLtjJbb9QEbDVmfZKZ9cy%2BjyxtNGnVtHjLJVneZ1naMCUcLVCtva%2BhBejM4EPRoe25KSlzLDdNCVSpdgzRhvsUh8evflgG0f4Vnu97EA3reP9D9RCsiTl6zvpQlvWRUtYXEf9%2BzvPM8Ibz3TY3vZqR%2FgUCdYYjDUhXLg1IIMqJ7PouEEhWICyVAmGJHlEYqUB9EWkU4YRMpNE6uR6gAhv6V%2BTTqUthg%2FqlsNm8EOXswUZVtBzFsXs667ZNO%2Bya5zG4eUyd28640b9YV8VK%2BQoqxipx8oDyFeWcRjWaOX7XzOmA4x6kPMcJzWfRsD%2BaHCjVQ6kS3s4UR%2FfqwZLV5nYbeuRe8efVjAWvi%2F%2BN%2Ft2IvyWGHWpNTc%2BSWtI8iNRGl9adWj6%2Fm0WgGxqBmtOeq3tT%2BR4tFEmgQs7a5H1bVv8qTegWy7yWWXkX2XswsaSl3tPBKi2KKu%2FkUaaX8xIQnwpuKXjh58HouvcCzMf6F8%2FRbbAj7u28s3xSpgaGnFKylVtAs6aYoN8WEMpuaSKlVUpQZPvUv%2BNxv1u72%2FTSixb7TYaLWww%2Fz2nxZd60rWYS7KE6TsfGHLbF6aVvx6kedZxefPAZwknoicz%2B1EVhPFod5Ts0SOTjnisQJLtDg5Tu0CBxh%2BZQ%2Bs4sVKyNEXtrPRGfjFG%2BIWOKOqXvzC%2B7G4NMpczflCH3We7kXAqKwHLYwqA8ojQHV%2FGITFlhULo1icRNixrOZzJxGLAMPEE4pYTlFWdVHuZ%2BuWxHWXnfclYFNfjUjVkS8Fh%2F7gRdN1kVJGa2%2FaFmVXg1oD7WtOqOaNQelaHXSBtlNbUYas60z0dloIUuGV31SRlrcLGpLXvs1DZUeiS2GBcNPDYF4Ok2N%2B3B%2BeO2Icv9SjMzxTJ%2F3uBUkAZLuUm2B1dJbsumamylqRq7MVUz8OhUEAJbebLeEd3%2B4VcsP8z%2BDWFd6d%2FyJ8Vajk8B4CbCNwPOhpV1GnHaYhZqsBEnAA7%2Fcgblov1E9Tz6h4l2N5knQbSFELUt0YZW%2FUTdSqqYGxpsxQ3gs4gQKpfU4XmiskWnWGnRqS0WnfbxxUAAcEoDKPcrsZhqUHVs5geOLLQpCbgjg8RVZtq4K4PEOTbmrZJRfkCxssYBhnV1QDcmD4tB6E95etPGkpraVlocaYv7Jyxn8AlcPxzTv1MxwOBeMGaqV%2BeDKwq2ZYuCsdJKjmKZta%2FrbD7k21%2FvnHdloPJdEyymMfpXJgx0LoBVXyeMRee7%2F%2B%2BuwLInTR%2F2Cx%2BLOMXt2P4fKC4PyXd%2FoFiezK3kox7OIn3IuS3cVGHEHLMVc8xqjnH2yx9DyvcuHTF66bvilPXHHEOl4sTX%2FDF9yI6YoX5D42lexdIi3zuGrCVRmil1RGetP%2BmSJ3gDiTSZHTUOg465sOvGW7CEAdxJ8m48jAKLwj7VMN5%2BJepc5Ud4nMEVzDqyrjtWWiTl1L8LiMd9X0%2BDC%2FmILkv0abP6uqNcF1VfGgVn%2FwM%3D






"""