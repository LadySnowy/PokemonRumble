from Pokemon import *;
from Move import *;

Charmander = Pokemon.Add("charmander");
Charmander.DisplayName = "Charmander";
Charmander.Animation = "Pokemon/charmander"
Charmander.HP = 39;
Charmander.Attack = 52;
Charmander.Defense = 43;
Charmander.SpecialAttack = 60;
Charmander.SpecialDefense = 50;
Charmander.Speed = 65;

Charmander.Width = .4;
Charmander.Height =  .6;
Charmander.Weight = 8.5;

Charmander.Move[0] = Move.Find("scratch");
Charmander.Move[1] = Move.Find("ember");
Charmander.Move[2] = Move.Find("flameburst");
Charmander.Move[3] = Move.Find("scaryface");

Charmander.SetMix("walk", "idle", 0.6);
Charmander.SetMix("walk", "jump", 0.2);

Charmander.SetMix("jump", "walk", 0.1);
Charmander.SetMix("jump", "idle", 0.1);

Charmander.SetMix("idle", "jump", 0.2);
Charmander.SetMix("idle", "walk", 0.4);

Charmander.SetMix("idle", "dead", 1);
Charmander.SetMix("walk", "dead", 1);
Charmander.SetMix("jump", "dead", 1);