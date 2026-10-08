import vpython as vp

scene = vp.canvas(title="Spring Mass Oscillator", width=1600, height=900,center=vp.vector(0,0,0),resizable=True)
pos_graph=vp.graph(title="Position Vs Time ",xtitle="Time(s)",ytitle="Position(m)",width=800,height=400,fast=False)
wall=vp.box(pos=vp.vector(-4,0,0),size=vp.vector(0.2,2,2))
block=vp.box(pos=vp.vector(3,0,0),size=vp.vector(1,1,1),color=vp.color.cyan)
spring=vp.helix(pos=wall.pos,axis=block.pos-wall.pos,radius=0.3,thickness=0.015,coils=15,color=vp.color.orange)
floor=vp.box(pos=vp.vector(0,-0.55,0),size=vp.vector(12,0.1,4),color=vp.color.green)

x_curve=vp.gcurve(color=vp.color.red,label="x(t)",graph=pos_graph)
m=1.0
k=5.0
dt=0.01
x0=0
x=block.pos.x
v=0.0
t=0
while True:
    vp.rate(100)
    a=(-k*(x-x0)/m)
    v=v+(a*dt)
    x=x+(v*dt)
    t=t+dt
    block.pos.x=x
    spring.axis=vp.vector(block.pos.x-wall.pos.x,0,0)
    x_curve.plot(t,x)

    