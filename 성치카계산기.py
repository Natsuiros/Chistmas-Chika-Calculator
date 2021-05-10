import os
print('본 계산기는 프린세스 커넥트 마이너 갤러리에서 제작하였습니다.')
Chara_Star=int(input("성급 입력 : "))
Chara_def=int(input("방어력 입력 : "))
Chara_hp=int(input("hp입력 : "))
Chara_Lv=int(input("UB 레벨 입력 : "))
Chara_Rank=int(input("랭크 입력 : "))
Boss_Damage=int(input('보스 유버 데미지 : '))
if Chara_Star==3 : 
                Seirei_hp=round(243.7+((Chara_Lv+Chara_Rank)*38.68))
elif Chara_Star==4 : 
                Seirei_hp=round(278.6+((Chara_Lv+Chara_Rank)*48.34))
elif Chara_Star==5 : 
                Seirei_hp=round(313.4+((Chara_Lv+Chara_Rank)*58.02))
else : print(f'성급 똑바로 써라 게이야')
if Chara_Star==3 : 
                Seirei_def=round(4.46+((Chara_Lv+Chara_Rank)*0.7))
elif Chara_Star==4 : 
                Seirei_hp=round(5.1+((Chara_Lv+Chara_Rank)*0.87))
elif Chara_Star==5 : 
                Seirei_hp=round(5.74+((Chara_Lv+Chara_Rank)*1.05))
main_damage=int(Chara_hp-(Boss_Damage/(0.01*Chara_def+1)))
Seirei_damage=int(Seirei_hp-(Boss_Damage/(0.01*Seirei_def+1)))
if main_damage>0 and Seirei_damage<0 :
                print(f'연구 가능성 존재')
else : print(f'불가능 돌아가셈.')
os.system("pause");