initialEnergy = 2
initialExperience = 4
energy = [1]
experience = [3]

min_energy = [sum(energy[:i+1]) for i in range(len(energy))]
min_exp = [experience[i] - sum(experience[:i]) for i in range(len(experience))]

delta_en = max(0, (max(min_energy) - initialEnergy + 1))
delta_exp = max(0, max(min_exp) - initialExperience + 1)

print(delta_en + delta_exp)

# print(min_energy[-1] + initialEnergy, min_exp[-1] - initialExperience)

