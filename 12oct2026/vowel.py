words = "Hello world!123"
vowles_count = 0
vowles = ["a","e","i","o","u" ]
for i in vowles:
    vowles_count = vowles_count+words.count(i)
print(vowles_count)     