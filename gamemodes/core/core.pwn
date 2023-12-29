#include "core/atm.pwn"
#include "core/objects.pwn"
#include "core/helpers.pwn"

static Text:logo;

ShowProjectLogo(playerid)
{
	logo = TextDrawCreate(540.000000, 5.000000,"OpenRP");
    TextDrawAlignment(logo,0);
    TextDrawBackgroundColor(logo, -697958145);
    TextDrawFont(logo,1);
    TextDrawLetterSize(logo,0.333000,1.666666);
    TextDrawColor(logo, -88276737);
    TextDrawSetOutline(logo,1);
    TextDrawSetProportional(logo,1);
    TextDrawShowForPlayer(playerid, logo);
}