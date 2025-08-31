class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        rom = ''
        while num > 0:
            if num >= 1000:  # 1xxx 2xxx 3xxx
                num -= 1000
                rom += 'M'

            elif num >= 100:
                if num // 100 == 9:   # 9xx
                    num -= 900
                    rom += 'CM'
                elif num // 100 == 4: # 4xx
                    num -= 400
                    rom += 'CD'
                elif num >= 500:      # 5xx ~ 8xx
                    num -= 500
                    rom += 'D'
                else:                 # 1xx ~ 3xx
                    num -= 100
                    rom += 'C'

            elif num >= 10:
                if num // 10 == 9:    # 90
                    num -= 90
                    rom += 'XC'
                elif num // 10 == 4:  # 40
                    num -= 40
                    rom += 'XL'
                elif num >= 50:       # 50~80
                    num -= 50
                    rom += 'L'
                else:                 # 10~30
                    num -= 10
                    rom += 'X'

            else:  # 1 ~ 9
                if num == 9:
                    num -= 9
                    rom += 'IX'
                elif num == 4:
                    num -= 4
                    rom += 'IV'
                elif num >= 5:        # 5~8
                    num -= 5
                    rom += 'V'
                else:                 # 1~3
                    num -= 1
                    rom += 'I'

        return rom
