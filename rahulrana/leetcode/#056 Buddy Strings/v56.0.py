class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        a_list = list(a)
        b_list = list(b)
        length = len(a)
        if a_list == b_list:
            for i in range(length):
                for j in range(i+1, length):
                    if a_list[i] == a_list[j]:
                        return True
        diff_chars = []
        for i in range(length):
            if a_list[i] != b_list[i]:
                diff_chars.append(i)
        if len(diff_chars)!= 2:
            return False
        else:
            one = diff_chars[0]
            two = diff_chars[1]
            temp = a[one]
            a_list[one] = a_list[two]
            a_list[two] = temp
            if a_list != b_list:
                return False
        return True