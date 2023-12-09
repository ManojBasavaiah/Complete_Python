dict={
    1:"January",
    2:"Febraury",
    "Mar":"March",
    4:"April",
    5:"May"
}
print(dict[2])#it returns value in key 2
print(dict.get(10))#throws None
print(dict.get(10, "Not a valid key"))# returns Not a valid key as default