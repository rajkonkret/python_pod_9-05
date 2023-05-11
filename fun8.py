def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print('a, b', a, b)
    print('c, d', c, d)
    print('args', args)
    print('kwargs', kwargs)

allparams(1, 2)  # przekazane argumenty pozycyjnie
allparams(1, 2, 3)
# TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
# / - oddzielenie argumentów pozycyjnych od nazwanych
# po użyciu /, a i b muszą byc przekazane pozycyjnie, c może byc jako nazwa
# allparams(b=1, a=4, c=7) - tak nie zadziałą dla  /
# gdy chcemy przekazac *args to c musi byc pozycyjnie
allparams(1, 2, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# d musi byc przekazane po nazwie
allparams(1, 2, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, d=100)
allparams(1, 2, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, d=100, e=18, a=9, b=89, h='/home')
allparams(4, 5, 67, 3, 4, 5, 6, zone='/zone')
