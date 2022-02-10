"""
정렬 알고리즘 sortalgoritihms

데이터를 오름차순 또는 내림차순으로 나열하는 알고리즘
겁색엔진 엑셀,워드.....이미 많이 사용하고있다.

#단순 선택법 - 정렬되지 않은 데이터 중 가장 작은 데이터를 선택하여 맨 앞부터 순서대로 정렬해 나가는 알고리즘
                선택정렬,선택법,단순선택법

0   1   2   3   4   <-index번호
12  13  11  14  10


먼저 가장작은 숫자의 공을 첫번째 공과 교환한다.
-----------1---------------
12  13  11  14  10

10  13  11  14  12
-------------2-----------
10  13  11  14  12

10  11  13  14  12
-------------3-----------
10  11  13  14  12

10  11  12  14  13
-------------4-----------
10  11  12  14  13

10  11  12  13  14
단순 선택법의 정렬.

잠정적인 최소값의 인덱스를 저장하는 변수 indexMin을 준비한다.
그때그때 마다의 최소값의 첨자를 저장할 변수 indexMin을 만든다.
arr[indexMin]와 요소들의 비교처라는 같은 절차의 반복이다. i 는 0에서 4까지 순차적으로 변하면서 반복된다.
이 변화는 구조의 첨자는 변수 k로 나타내보자.

잠정 최소값과 비교하는 욧의 첨자를 변수 k로 치환하여 반복구조로 만들었다.
이대로라면 k에 무한루프가 발생된다. 반복구조는 언제나 종료조건이 필수이다.

i 가 0 일ㄸ k 는 1부터 4까지 변하게 된다. k는 5가 되는일은 절대 없다.
따라서 종료조건은 k<5

최소값과 arr[i]의 데이터를 교환


#단순교환법 Bubble Sort
인접한 데이터를 교환하는 처리를 반복한다.

0   1   2   3   4 index
5   3   4   1   2 data

5   3   4   1   2 --- 이미 정렬된 상태임에 따라 정렬할 필요가 없다.
            -   -
5   3   4   1   2   ---정렬이 되지않은 상태임에따라 교환한다.
        -   -
5   3   1   4   2

5   3   1   4   2   ---정렬이 되지않은 상태임에따라 교환한다.
    -   -
5   1   3   4   2

5   1   3   4   2   ---정렬이 되지않은 상태임에따라 교환한다.
-   -
1 | 5   3   4   2   1은 정렬이 완전히 끝난 상태로 확정되었다.
1 | 5   3   2   4
1 | 5   2   3   4
1 | 2 | 5   3   4
1 | 2 | 3 | 5   4
1 | 2 | 3 | 4 | 5 |   모든 정렬이 완전히 이루어졌다.

#단순 교환법 bubble sort 알고리즘

1.오른쪽 끝부터 순서대로 인접한 공 2개를 오름차순 정렬한다.
2.왼쪽 끝 칸부터 순서대로 들어갈 공을 확정시켜나간다.

0   1   2   3   4 index
5   3   4   1   2 data

오른쪽 끝 인접한 공 2개
오른쪽 요소 i   arr[i]
왼쪽 요소 i-1   arr[i-1]

정렬이 이미 되어있는 상태인지의 여부를 확인하려면 '왼쪽요소가 오른쪽 요소보다 작은 가??'
arr[i-1] < arr[i]

여기까지는 순조롭게 비교와 교환처리가 진행된다.
마지막에 i -1이 0이 되고 i 가 1이 되면
이미 확정된 arr[0] 과 arr[1]을 비교하게된다. 이것은 쓸데없는 낭비가 된다.
그러면 어디를 수정해야할까...       i > 0 조건식이 문제로 보인다.
따라서......
arr[1]를 확정하는 반복처리부터는 i > 0를 i > 1로 바꿔야한다.
반복할때마다 i > 0, i > 1, i > 2.......와 같이 늘려가도록 변화하는 처리를 추가하자.

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day8.drawio#R7V1Lc%2BO4Ef41rEoO4yJIAgSOku1NDrupVCapfVy2ZEm2FcvmlCyvPXvIbw9foEg0KMImwQYlz2FKpkiKRD%2FQ34fuhhdePr79bbf4dv9TslpvvcBfvXnhlRcEPOTp%2F9mB78UBGkXFgbvdZlUcIocDXzd%2FrsuDfnn0ZbNaPzdO3CfJdr%2F51jy4TJ6e1st949hit0tem6fdJtvmr35b3K3Bga%2FLxRYe%2FXmz2t%2BXrxXEh%2BN%2FX2%2Fu7uUvEyaKbx4X8uTyTZ7vF6vktXYovPbCy12S7ItPj2%2BX6202dnJciut%2BaPm2erDd%2BmlvckGwvHvc%2Fudfq%2Fuvv%2FOX3%2F599w%2F%2Ftz%2B%2FBEEpjj8W25fylcvH3X%2BXY7BepUNS%2Fpns9vfJXfK02F4fjs53ycvTap39kJ%2F%2BdTjnxyT5lh4k6cH%2Frvf776V8Fy%2F7JD10v3%2Fclt8%2B73fJw%2Foy2Sa7%2FDdDP%2F%2BXflM8TfYIre9dHnpOXnbL9ZGXlfqz2N2t90cHhVTySfV6nTyu97vv6ZW79Xax3%2FzRfJJFqWF31XkHIaQfSjm8QyYESCRVZCCUVJ2%2BZR9XyfLlMR%2BK%2Bev9Zr%2F%2B%2Bm2RD8Jrao7NMb4phPTjjTxQ%2Fs56t1%2B%2FHR9cOBTyAiLVu7RvIlh54PVgLtVJ9zVTiXxL4xd0a3ShbtKgA0UXy5F9fLvLXNrF7TZ5Xd4vdvuLbarOv283j5u20R5gRFkcNwaUYg8nIVAhnxIMJ7F%2B2%2Bx%2FqX3%2BNbvVBS3%2Funor75z%2F8V3%2B8ZSOwS%2BHE7M%2Ff61%2Fd7gs%2F0teN6DbCQ3dDmeoXodAu%2FmezryIcj7I9tfaN3o5Dy2vHmIoL%2F1nskl%2FueYpY3HBCA15VPzPG2Ye%2BYr9FupS3kSRbfVUHxd3CIS98TK3whaPmSPb7vMx9SMg%2F9198njz8tw93diYXcIA2xvCcGn9tIJGst2mAep6lEHizSGK0YcoZGfoNKgVpxFG%2FkVU%2BxdGDVkHzMxpzHa7xffaad%2ByE56P%2FqwSg5D67cD5UdDvfPkeB60rnnhQj0f1Hi%2F75Be%2BL3N4Ut41h1dpJhnFnlWDjiKCbNAMjNzXVNH2Lnk9gu30YjBGGWijc9%2BjV%2F8rPkbpR%2B%2F60ptFnkhfjuVz7E2K7NhdPtumX82pJy6zD2ksyNMPMy%2B9gchunH%2Fre%2FPr%2FCDPPmMrqiICji0CDkRQG7RLT1x52SP6x8Y5%2BxB680sonYM0veu5x6%2ByC4qbpnK9Tm8d5Ufm3ozm1%2Fv5vdKf8bNvhfAEd01gBB2payAHqlOhtIm90b0KgWF6oYjkbNxKNbh4QtBQpEM7FnJKjgUfpREY7BXjHJyN3UQ%2BdthIYNw4uN0Ep2Q3EXoIRdrC2PBs7IbiR0UjBLLhKdkNQw8RQhingUEagQMrfnOYtdJyGbt7sdTXi2qkVQsBBv7A6uD7FhDM%2Buia6sZ6%2F4CaKoevW1P7ruoPwqXK4Ngq1ynHBMzjm9Odx4GtcewAOIQoZOq2ZppC03c5pF8CCExYGDyA2kw6gAKInWHbijSNY7Yy9ihVqTh4owLxWO6yUxWluYr53uyyWrR%2FunkukpD8L7napdqZnsJz7eaZmhcqnyroLNdFHmZam56WwmhB%2Bw337Wa7raXv3d6u2XLpaRL7VrG4qSX29RJQ6DfVWGiiK66RV2zN42ug28Q9Pjf0%2BCFqzmQAB16bz7JdP%2F0ldeB%2Fhco%2BYlpLFKmRCjYqkEvMZ5WyEYieGqsP%2BKmPkrNBFV9IuZIOrp6v8l7vPH%2BUnI3gGLx3KWlDNWmKvgQSakKHaU9FoTHQ55hTkXxMRykpMPngU1LQyKeuqaYwOQxQNVVfaeIuS6SCDL5c60HGDacRHQhkqAYToi8QRdDDTN1gAlPX3jdm62cwGpLik1g6ZiwR%2BtJc9CmzyZGBkWY59VNmjstshCy5U5MZum9sS5NzNQC0IAUHyLcR8uQQLQclaHfQ1tpS61y1NSfk5oB1jpCNd27W6R5KoCeXwBeZJvBR1AS%2BCJJ%2FGVv6pVq5uytX7jbpyL79tHlyLoDAzz6lMPRG6twwoP7Kvifd%2Bou68Exh8Dad5iiDi2vwxVQ1e5JbWj1VK9Lj6PhqqHo%2BZ8fPb3sPuxXvbVmgebWZJjsi%2BzaeV56WXkFnO2KahHudLejJJXRS44TOANXLwpWqQzxQLq3iJwHAinh0hQ1aPEAwSQ%2FA0dEg1aHBHObxArhdZ0gtkJ9TFF9BxOzDzBNRDR9WsE6L9CuESTMYWN2TF3eYy4TOeYYti%2FtnWZ55uqeIc4Q4z%2FEnL89JYWOGGenhnJm8Q3q3DG%2BmH4onLDJHowsg%2FQ6Zq63zbhbPm%2BVFko7W78vFdpu87AfQikjJdGI6bsfXaIUaOwzXIOXkMhiY6bzA%2BnZL69d1BZJquNG3DLFHjr7ZIKVNnTl%2FptH3UAEsg9P%2Bg27W0uSujzhLsVAZJXRCgMFpf%2Br%2ByLSJJosw%2FRHTtFV0L05VFVagA6v4FBksFhnqbIyKrWIY0p7nHNrXc%2BjnUCaaxkaIakUDUViMKD%2FkNyuNuy8gTdLLDinFoKkXkPRhEpBU9Z3ERwf57OSKzhg1ne1RuX8G6cAHh6f5GD0HItYUZk9cU5mppsaomgpXqVyqSVE1laH7VFkhfEKaGptqKmrvBgYZHcfzAYDyopPU8cktU8WBofLGuHQk5F1KNa2c7YNz%2Bkp8fIU9xx0DeqtqK95slp83hM3Tb%2F3av6B5%2B6GgqIp5wd5kygVx3PMCLkaArjFk9x7qhu27Uo0OTBy%2F1XcMl8jK3Nc6sC%2FH8hV%2FBEWza0Mkl%2FjwutufXEQq%2B7N1b4yFOqlzCFpfK02t5W%2B7prKhj66yMByausqaLkPFqHXKvG3bgE3dy2r8r2sqzNFVeNCqxrq7KC7Oyjf8j5d%2BHPJ5aqk76VUz0d7W7UMpPMtt8rIaMIdHlXRANJJmGklLjRhe0hrQDDvoHWuf11SCWeDxKfbUIz5tBo%2B6bIZRm%2BoRR%2FYoHnIeMaWNSTAISnwvgCNqvrroyG8nRG3FOEaCO4e0tsNbJcNsVuyafW7QI8xyNeHzw3q%2FvC8vXy2e76ufGmKWUfZSJjqmS%2BfLQmptmjFYrH3XkLcPbaswbA55tX2GbISn6claKXQjOdfe%2FCF30XKfXnRgt2oZYHVPTT4uLIeEEv6ulGDDYnziTWh4o6zAAGKJyzyQzbHEjOW1Aa0jKWfUHBZY91EDCCYGWViGcuHW5KLJhTgGIjubO0xZOmr3VNMtb%2B1J5%2BSoK2GajSoYplsXkLo6y2xUYScbVbQ1Lxh4BVD9HVpinTb82PZcVuGjgLyCg%2BUlIKag6L3exMklmAhTQkagEvtCk8fnXn0J0FiGvoW9gEzH9AtMhDlUQ80%2BFZ8VJsP4jjbuFZRpKvcYaFIHJG8cHZ%2FVwQXyyexO622pJtOoMAHeMw6wvWclxtOZ8ImcJ7tnfNSK0uo5dUlnYN8vl5LQgB5H6OsdhESo0860mOCS4DXZxgLXQjRF11U0jF%2FcAuxAu6I%2Bsj8%2FuRV14pvWDJYeFU9dIXh2vMIFenIf3ZP7mqbZU9dg0wot4qOSENWDOl3mApSWO6C0sFmzo%2BHHoHptD%2FY2Kl1IQ9yMkBEqXQD2Fl2QOGA9L0hfTNFECxia%2BBBEu1nrAu3cAZhhAJdH3XBWqQdC7%2FdD5Duc0PRNjAPQYqjRpm%2FSuuuLk6VYAszj6NpLTi%2F4JMbBJ8ENPgkMPp0sx1LVFn%2BbgDRWOT21NV4CI6htLaoHnVpJlqrG%2BE3YCY7WYqOo3kGDIYAJfUVwljKCRMcOC4L0O1%2B%2Bh12YFMBI380N6kEUJQvyEe0Y8vbXTyto22Pmb%2FtKJqoD7f1IYJBtZblkpFElcrdbrDbpgMoTn5KnTDrP94tV8lp6vrvt4vm5%2FDx0tjDxlWRubZmwrqyHqokRAwqpZRPHc0znrrq3VAJCz%2BcmwYmXunHeLHVjOrZ73FI3EmjwxvmVngglB4qapvNYNAYIRmqtB1LxkMwplQXtV2VbARHmriyVEDlsPcKD%2FJLi2sK%2FidzRXXqz2OPQrTXj8O5eBPoppWE9DYEBeRfsvyLvcspqmcmGEHqkVJ76sWEcYW2TEhK6slWdNyAsksx2NwEQ4hIAcgrEz0BG3imwFNngSFYNOggLFFMaCMmGikMn1D8OTcEF8snsYtMQYtOSX%2FpybAPANv50zBRYZcmTROgtKkkYgNF0oN5YHagQn54LP6vt3%2BMMTcsy%2B7vNnmKFKYMHpgum1Y6eBgBcBj5xE2rC7KmHW8aL3CFqyVH1oOpGjU3g6ZzWUvR%2BEaXg3EleAWPkwEpqBEMrbOo6VMNfB0KBCMZMkivISZ%2BZn%2B%2BQWjQxlJRCekT4kim9bPZJhFuoyr1XtVuoloTG3Jv9cCA0ZsVerfPswywnNIQvf%2F0ya%2BrHiezuV9AdIruJKtr%2BG6FOmd5QcxJJlWFWVzZtmyd7ygaXk6SOUSDuYgdcJsmr66y9o9z1tib0Qg%2FjXF3nmb6VmlMwYJ8qUfc%2F6m5iVBeAjawSMGadPuMV9e3PoicpqLrySUfe7JVEMGQ7U4ZsLBHH6hLDUPs%2FqLFIF0MGLpBP1nZB66vYpdQifcPRCVBqEVdnbHxKTa6RfDJFRk6hhKvd0Lu3%2B%2BgpVrjs6xJTBC0BnymKpsYUdSsh7Vtla%2Br41TClsCR7YYpmUXsMr%2FVBDwR7xbMbRpmn6S5%2FG%2BT5D0MqQbG39OBKABbU4nBkJaAG9Uuo07sDVTLUjS5xxolaFW4ectamgbHDxO0zIx8U1tU0I9w%2Bs%2Ff7c%2BZsmIYDHDs12qCnZ%2B2dG6PtQMEIdaNcD9kRGS80U9x2PhSSdirGzq1jkeP7Iar93DAUB5a1KFz6mz5fSu20n4jl6j4aX0ohzj5TvnQsEdviSzlRdamDLwUXdPGlra9ily%2BlkNeYCF%2FKYmXAHOBLYzeaZowTrzA7%2FFEc8gsRxSHjUbbVXaCk6UeG1a%2BDWQiDMnWJLGUxbw6QA1klDCJVl2OUEaYlQwq0%2B058dPXXJG2cHTRjxtCM4SZVMgjNBueIbMzdDjA%2BrLXpklvdlsDYOcDfsE%2F%2BRpq%2BkZPALXRjkESwzN%2FYUHsH2BgmMLT8I%2BkRI1mAncVEEASFllA%2BjLY6NlVmtO8F4XtpgXAUWoAdyxDJm2H3bJijuOrVYs1vta6aLfn65taSD3FgDTaGWAmJIxzCRxisXYzEBEaqyGwnHMSupDJ%2FhOsdZ36I%2B65btXCtVM0XC%2FyLnDtiIaExl3uyjQWZ45btLtTtAzS9N8bkTx3Msot1NYFVwdE860HDedm6ZN5WcDT3ZjRrdaIpOCqqCmmt6uQyqyjJyoiusk4pRWkJz29YNldpdr05lJbAm1fFKdU9ax%2FEdfYW8Cpw5AIoxYeqVvLmO0OXrYR%2BtjXHyGUrXM0nDDUb1mv1lKhc2YCKCpdNkFf2eqGBAVMODWYBO7UTgRAXvLZwIKvNpNpU%2FRXHmgY4DJGnMvufgj7AFFRLOymHILOzAwSCC%2BST2cV0sWZr2oHDkjZ1aVewASaIQJ0gOD4zFJ984cxHRT2QzzAutentXXoqgsVSGzesLcZfuuEBirV90HLs9invtgjZh7TbyrgdPleAQuZ4ZK6GQ4Q%2BofB9SEfK%2By5FtYg4VILxFp8xViwuIeMkybmDo2m4mYPXMa0ss0LqceOGU7wv9dtzltBv6wniX83OiB%2BNf0fJU%2BcgTx0%2FEZKzqThTFwrHuXHmQG933VOsmn1Fh4pmrVgCPqXNIQA4bNOogdrYQ0bxs4kEKnHWdB7%2BUecx0gxrZ8kUhuGW0ioIAf2YO7IeWh%2FNLkPGIavv6JaqYBccB5IARQBGDwtUTRSZi77Jwy32F0b%2BhdzUXioM2LzCNuYWn5hbjoQdzE3CFHSLqBV0R4bufTiJTzkjxm3QLUxBdxljoiEGYR90DzGfpt4QeEgH8mHEJ4x%2Bj1EYw%2BjeHrinWN2G0VprcKCsUDiUbu8ALuzv2t8TLhpmz7wbG1K%2F%2Fcfa4OHRJ7QKESvKxn2IGGnGKELPjAh8iBIxrHokC7VTX6zXf8P0puFMARbGu8Rsamcxgp6sEGg2VcZFRb73EVTUs8mlHXMzLtPuaZY9XSDExQ91TCQbrWgiwXExEWl3MogTCESUk2%2BBFfgjMn9jt8EKfJh4ep5tsEYVs61WWHl1FdCpjnZY2ou6WmIdfS3LYX53ibyjbbH0VBZ6RkhAIHBy2WmPZKMf7QukvdvYvYHScNoJmaK2%2FUjtyDMLOlMv2VOzelogRN4u9gbSOjD8%2FkCpybVNCW71B9KOH356QDoJfTqL0gUYOQvUHs%2FVg06qR5BW9fH7BKXPgKHpzvYJSt2RnRArAC0NbK1ahKDmsKPm87CA8vEr5NvYhT7k2OLkEK1%2FbBk6fjOf6k0c2nWYEEWNAh%2FfIcqp%2F1gsIPtarJLly2P%2Bsl2jdVNo4Y83Aw4fpc3%2Bwxbj0PTPXZLs6%2BacNfT4KVmtszP%2BDw%3D%3D




"""
#475
def xyz():
  a = 56
  xyz()
print(a)