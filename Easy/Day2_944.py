def minDeletionSize(strs):
    lenstr = len(strs[0])
    sumstr = len(strs)
    count = 0

    for i in range(lenstr):
        minchar = strs[0][i]
        for j in range(1, sumstr):
            if minchar > strs[j][i]:
                count += 1
                break
            else:
                minchar = strs[j][i]
    return count


if __name__ == "__main__":
    strs = ["cba", "daf", "ghi"]
    print(minDeletionSize(strs))
