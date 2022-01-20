# Wordle helper (just for fun)

usage: `./python wordle.py presentchars absentchars`

example: `./python wordle.py pro aeos`

> `> ['rinse']`

bonus:
> `chmod +x /path/to/wordle.py`

add this to your .profile

`wordle () { /path/to/wordle.py $1 $2; }`

then `source ~/profile`

now `wordle bort chile`