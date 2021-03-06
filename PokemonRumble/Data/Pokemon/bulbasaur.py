from Pokemon import *;
from Move import *;

Bulbasaur = Pokemon.Add("bulbasaur");
Bulbasaur.DisplayName = "Bulbasaur";
Bulbasaur.Animation = "Pokemon/bulbasaur"
Bulbasaur.HP = 45;
Bulbasaur.Attack = 49;
Bulbasaur.Defense = 49;
Bulbasaur.SpecialAttack = 65;
Bulbasaur.SpecialDefense = 65;
Bulbasaur.Speed = 45;

Bulbasaur.Width = .8;
Bulbasaur.Height = .5;
Bulbasaur.Weight = 6.9;
 

Bulbasaur.Move[0] = Move.Find("tackle");
Bulbasaur.Move[1] = Move.Find("leechseed");
Bulbasaur.Move[2] = Move.Find("razorleaf");
Bulbasaur.Move[3] = Move.Find("growl");

Bulbasaur.AddAnimationAlias("tackle", "jump");

Bulbasaur.SetMix("walk", "idle", 0.6);
Bulbasaur.SetMix("walk", "jump", 0.2);
Bulbasaur.SetMix("walk", "leech_seed", 0.2);

Bulbasaur.SetMix("jump", "walk", 0.1);
Bulbasaur.SetMix("jump", "idle", 0.1);

Bulbasaur.SetMix("idle", "jump", 0.2);
Bulbasaur.SetMix("idle", "walk", 0.4);
Bulbasaur.SetMix("idle", "leech_seed", 0.2);

Bulbasaur.SetMix("leech_seed", "walk", 0.2);
Bulbasaur.SetMix("leech_seed", "idle", 0.2);

Bulbasaur.SetMix("idle", "dead", 1);
Bulbasaur.SetMix("walk", "dead", 1);
Bulbasaur.SetMix("jump", "dead", 1);
Bulbasaur.SetMix("leech_seed", "dead", 1);