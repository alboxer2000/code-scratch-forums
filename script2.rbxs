local badscratchemployeecoder = workspace.ScratchDude
local ehumanoid = badscratchemployeecoder:FindFirstChild(“Humanoid”) :: Humanoid
local scratchwontfixtheirbugs = true
local timeuntilicrashout = 30
task.wait(timeuntilicrashout)
local rootpart = badscratchemployeecoder:FindFirstChild(“HumanoidRootPart”)
rootpart.Anchored = true
game:GetService(“TweenService”):Create(rootpart,TweenInfo.New(3),{Position = Vector3.New(0,100,0)})lay()
wait(3)
rootpart.Anchored = false
ehumanoid.Health = 0
