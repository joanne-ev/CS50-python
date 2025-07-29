def main():
   mass = int(input(" Enter a mass (kg): "))
   energy_calc(mass)

def energy_calc(m):
   joules = m * pow(300000000, 2)
   print(f'Energy (in joules): {joules:,}')


main()
