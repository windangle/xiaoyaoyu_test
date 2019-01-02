#——————————过滤器示例——————————
#敏感词过滤器第一部分
def text_create(name,msg):
	test_path = 'd://Test/'
	full_path = test_path + name +'.txt'
	file = open(full_path,'a')
	file.write(msg+'\n')
	file.close()
	print('Done')
	
text_create('hello','hello world')	#A test
	
#敏感词过滤器第二部分
def text_filter(word,censored_word='lame',changed_word='Awesome'):
	return word.replace(censored_word,changed_word)

print(text_filter('Python is lame!'))	#A test

#敏感词过滤器Main部分
def censor_text_create(name,msg):
	clear_text=text_filter(msg)
	text_create(name,clear_text)

#启动程序
censor_text_create('JustDoIt',"I think U R lame~!!!")

#——————————批量创建目录文件——————————
file_path = "d://Test/TestDocumen/"
for create_doc in range(1, 11):
    file = open(file_path+str(create_doc)+".txt", "w")
    file.close()
	
#——————————猜大小练习——————————
#摇骰子
def yaoshaizi(count = 3):
    import random
    point = []
    for point_count in (0,count):
        point.append(random.randrange(1, 7))
    return point

#算骰子点数
def suandianshu(point):
    point_sum = 0
    for point_count in point:
        point_sum = point_sum + point_count
    return point_sum

#启动程序
print('<<<<<GAME START!>>>>>')
user_chose = input('Chose Big or Small:')
user_chose_big = user_chose.lower() == "big"
user_chose_small = user_chose.lower() == "small"
print('<<<<<ROLE THE DICE!>>>>>')
role_dice = yaoshaizi()
dice_sum = suandianshu(role_dice)
num_small = 1*len(role_dice) <= dice_sum <= 1*len(role_dice)
num_big = 4*len(role_dice) <= dice_sum <= 6*len(role_dice)
if (user_chose_big and num_big) or (user_chose_small and num_small):
    print("The points are",role_dice,".You Win!")
else:
    print("The points are", role_dice, ".You Lose!")

#——————————算词频——————————
import string

path = 'd://Test/Walden-new.txt'
with open(path,'r',encoding='utf-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}
    for word in sorted(counts_dict,key=lambda x: counts_dict[x], reverse = True):
        print('{} -- {} times'.format(word,counts_dict[word]))

#——————————类的示例——————————
class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = ['High Fructose Corn Syrup','Carbonated Water','Phosphoric Acid','Natural flavors','Caffeine']

    def __init__(self,logo_name):
        self.logo_name = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

class CaffineFree(CocaCola):
    caffeine = 0
    ingredients = ['High Fructose Corn Syrup','Carbonated Water','Phosphoric Acid','Natural flavors','Caramel Color']

coke_a = CaffineFree('Cocacola-Free')

coke_a.drink()

#——————————类的实践——————————
# coding=gbk
import random

ln_path = 'D://Program Files/Account/first_name.txt'
fn_path = 'D://Program Files/Account/last_name.txt'
fn = []
ln1 = []	#单字名
ln2 = []	#双字名
with open(fn_path,'r',encoding='utf-8') as f:
	for line in f.readlines():
		fn.append(line.split('\n')[0])	#如果这里看不明白不妨试试对其中的一行使用split方法看看会返回什么结果
fn_set = set(fn)
print(fn)
print('='*50)	#分割线
with open(ln_path,'r',encoding='utf-8') as f:
	for line in f.readlines():
		if len(line.split('\n')[0]) == 1:
			ln1.append(line.split('\n')[0])
		else:
			ln2.append(line.split('\n')[0])
ln1_set = set(ln1)
print(ln1_set)
print('='*50)	#分割线
ln2_set = set(ln2)
print(ln2_set)

class FakeUser:
    def fake_name(self,one_world = False, two_word = False):
        if one_world:
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_word:
            full_name = random.choice(fn) + random.choice(ln2)
        else:
            full_name = random.choice(fn) + random.choice(ln1 + ln2)
        print(full_name)

    def fake_gender(self):
        gender = random.choice(['男','女','未知'])
        print(gender)

class SnsUser(FakeUser):
    def get_followers(self,few = True, a_lot = False):
        if few:
            followers = random.randrange(1,50)
        elif a_lot
            followers = random.randrange(200,10000)
        print(followers)

user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_b.get_followers(few = True)
