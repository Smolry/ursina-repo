from ursina import*
from ursina.prefabs.first_person_controller import*

app=Ursina()
model=Entity(model='cube',color=color.white33,texture="shore",scale=2,position=(1,9,1))#standard position=1,9,1
sphere=Entity(parent=model,model="sphere",color=color.white66,position=(0,0,-5),texture="shore",scale=3)#standard position=1,10,1
#mark20=Entity(model="res/IronMan.obj",color=color.white10,texture="white_cube",scale=0.005,position=(5,1,5))

map=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]



for i in range(10):
    for j in range(10):
        if i==0 or i==9 or j==0 or j==9:
            map[i][j]=1

for x in range(10):
    for z in range(10):
        if map[x][z]==0:
           Entity(model="plane",scale=3,color=color.white66,texture="brick",position=(x,0,z) ,collider="mesh")#(standard position=x,0,z)
        else:
            Entity(model="cube",scale=1,color=color.white66,texture="brick",position=(x,map[x][z],z),collider="mesh")#(standard position= x,map[x][z],z)


#player=FirstPersonController(x=5,y=10,z=5)
EditorCamera()


def update():
    model.rotation_y+=50*time.dt
    #if player.y<0:
     #   player.position=(5,10,5)





app.run()