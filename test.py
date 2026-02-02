def echo():
   print("Hello")

def ads():
   print(2 + 2)

handlers = {
	"echo": echo,
	"ads": ads
}

cmd = input("> ")
handler = handlers.get(cmd)
handler()