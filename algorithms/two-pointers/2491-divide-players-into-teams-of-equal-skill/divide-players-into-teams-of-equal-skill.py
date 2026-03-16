class Solution:
    def dividePlayers(self, skill) -> int:
        skill.sort()
        n = len(skill)
        total_equal_skill = (int(sum(skill) / (n/2)))
        
        l, r = 0, len(skill) - 1
        total_chem = 0
        
        while l < r:
            total = skill[l] + skill[r]
            if total == total_equal_skill:
                total_chem += (skill[l] * skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return total_chem