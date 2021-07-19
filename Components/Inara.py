import datetime, json, requests, re
from Components.Logging import Logging
from discord import Embed
from discord.ext import commands
from os import getenv, getcwd
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv(f'{getcwd()}/config.env')


class Inara(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=['Get_Commander', 'cmdr'])
    async def Get_Cmdr(self, ctx, cmdr_name):
        params = {
            'header': {
                'appName': 'RogueBot',
                'appVersion': re.search('\d+$', requests.get('https://api.github.com/repos/thijnmens/RogueBot/commits?per_page=1').links['last']['url']).group(),
                'isBeingDeveloped': True,
                'APIkey': str(getenv('INARAKEY')),
                'commanderName': 'Thijnmens',
                'commanderFrontierID': '8017135'
            },
            'events': [
                {
                    'eventName': 'getCommanderProfile',
                    'eventTimestamp': str(datetime.datetime.now().strftime('%Y-%m-%d' + 'T' + '%H:%M:%S' + 'Z')),
                    'eventData': {
                        'searchName': cmdr_name
                    }
                }
            ]
        }
        params = json.dumps(params)
        response = requests.post(url='https://inara.cz/inapi/v1/', data=params)
        data = response.json()
        inaraPage = requests.get(url=data['events'][0]['eventData']['inaraURL']).text
        soup = BeautifulSoup(inaraPage, "lxml")
        InaraRank = soup.find('span', class_='major bigger')

        # Combat Rank
        Combat = int(data['events'][0]['eventData']['commanderRanksPilot'][0]['rankValue'])
        CombatProgress = str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][0]['rankProgress'])*100))
        if (Combat == 0):
            Combat = 'Harmless'
        elif (Combat == 1):
            Combat = 'Mostly Harmless'
        elif (Combat == 2):
            Combat = 'Novice'
        elif (Combat == 3):
            Combat = 'Competent'
        elif (Combat == 4):
            Combat = 'Expert'
        elif (Combat == 5):
            Combat = 'Master'
        elif (Combat == 6):
            Combat = 'Dangerous'
        elif (Combat == 7):
            Combat = 'Deadly'
        elif (Combat == 8):
            Combat = 'Elite'
        else:
            Combat = "Unkown, please report"
            Logging.warning('Combat rank unknown, set to None')

        # Trading Rank
        Trading = int(data['events'][0]['eventData']['commanderRanksPilot'][1]['rankValue'])
        TradingProgress = str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][1]['rankProgress'])*100))
        if (Trading == 0):
            Trading = 'Penniless'
        elif (Trading == 1):
            Trading = 'Mostly Penniless'
        elif (Trading == 2):
            Trading = 'Peddler'
        elif (Trading == 3):
            Trading = 'Dealer'
        elif (Trading == 4):
            Trading = 'Merchant'
        elif (Trading == 5):
            Trading = 'Broker'
        elif (Trading == 6):
            Trading = 'Entrepreneur'
        elif (Trading == 7):
            Trading = 'Tycoon'
        elif (Trading == 8):
            Trading = 'Elite'
        else:
            Trading = "Unkown, please report"
            Logging.warning('Trading rank unknown, set to None')
        
        # Exploration Rank
        Exploration = int(data['events'][0]['eventData']['commanderRanksPilot'][2]['rankValue'])
        ExplorationProgress = str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][2]['rankProgress'])*100))
        if (Exploration == 0):
            Exploration = 'Aimless'
        elif (Exploration == 1):
            Exploration = 'Mostly Aimless'
        elif (Exploration == 2):
            Exploration = 'Scout'
        elif (Exploration == 3):
            Exploration = 'Surveyor'
        elif (Exploration == 4):
            Exploration = 'Trailblazer'
        elif (Exploration == 5):
            Exploration = 'Pathfinder'
        elif (Exploration == 6):
            Exploration = 'Ranger'
        elif (Exploration == 7):
            Exploration = 'Pioneer'
        elif (Exploration == 8):
            Exploration = 'Elite'
        else:
            Exploration = "Unkown, please report"
            Logging.warning('Exploration rank unknown, set to None')
        
        # CQC Rank
        CQC = int(data['events'][0]['eventData']['commanderRanksPilot'][3]['rankValue'])
        CQCProgress = str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][3]['rankProgress'])*100))
        if (CQC == 0):
            CQC = 'Helpless'
        elif (CQC == 1):
            CQC = 'Mostly Helpless'
        elif (CQC == 2):
            CQC = 'Amateur'
        elif (CQC == 3):
            CQC = 'Semi Professional'
        elif (CQC == 4):
            CQC = 'Professional'
        elif (CQC == 5):
            CQC = 'Champion'
        elif (CQC == 6):
            CQC = 'Hero'
        elif (CQC == 7):
            CQC = 'Legend'
        elif (CQC == 8):
            CQC = 'Elite'
        else:
            CQC = "Unkown, please report"
            Logging.warning('CQC rank unknown, set to None')
        
        # Empire Rank
        try:
            Empire = int(data['events'][0]['eventData']['commanderRanksPilot'][4]['rankValue'])
            EmpireProgress = str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][4]['rankProgress'])*100))
        except Exception:
            Empire = 0
        if (Empire == 0):
            Empire = 'None'
        elif (Empire == 1):
            Empire = 'Outsider'
        elif (Empire == 2):
            Empire = 'Serf'
        elif (Empire == 3):
            Empire = 'Master'
        elif (Empire == 4):
            Empire = 'Squire'
        elif (Empire == 5):
            Empire = 'Knight'
        elif (Empire == 6):
            Empire = 'Lord'
        elif (Empire == 7):
            Empire = 'Baron'
        elif (Empire == 8):
            Empire = 'Viscount'
        elif (Empire == 9):
            Empire = 'Count'
        elif (Empire == 10):
            Empire = 'Earl'
        elif (Empire == 11):
            Empire = 'Marquis'
        elif (Empire == 12):
            Empire = 'Duke'
        elif (Empire == 13):
            Empire = 'Prince'
        elif (Empire == 14):
            Empire = 'King'
        else:
            Empire = "Unkown, please report"
            Logging.warning('Empire rank unknown, set to None')
        
        # Federation Rank
        try:
            Federation = int(data['events'][0]['eventData']['commanderRanksPilot'][5]['rankValue'])
            FederationProgress= str(int(float(data['events'][0]['eventData']['commanderRanksPilot'][5]['rankProgress'])*100))
        except Exception:
            Federation = 0
        if (Federation == 0):
            Federation = 'None'
        elif (Federation == 1):
            Federation = 'Recruit'
        elif (Federation == 2):
            Federation = 'Cadet'
        elif (Federation == 3):
            Federation = 'Midshipman'
        elif (Federation == 4):
            Federation = 'Petty Officer'
        elif (Federation == 5):
            Federation = 'Chief Petty Officer'
        elif (Federation == 6):
            Federation = 'Warrant Officer'
        elif (Federation == 7):
            Federation = 'Ensign'
        elif (Federation == 8):
            Federation = 'Lieutenant'
        elif (Federation == 9):
            Federation = 'Lieutenant Commander'
        elif (Federation == 10):
            Federation = 'Post Commander'
        elif (Federation == 11):
            Federation = 'Post Captain'
        elif (Federation == 12):
            Federation = 'Rear Admiral'
        elif (Federation == 13):
            Federation = 'Vice Admiral'
        elif (Federation == 14):
            Federation = 'Admiral'
        else:
            Federation = "Unkown, please report"
            Logging.warning('Federation rank unknown, set to None')

        embed = Embed(
            title=f"Cmdr {data['events'][0]['eventData']['commanderName']}",
            url=data['events'][0]['eventData']['inaraURL'],
            description=data['events'][0]['eventData']['preferredGameRole'],
            color=0xff0000
        )
        embed.add_field(
            name="**Ranks**",
            value=f"`{InaraRank}`",
            inline=False
        )
        embed.add_field(
            name="Combat",
            value=f"`{Combat} | {CombatProgress}%`",
            inline=True
        )
        embed.add_field(
            name="Trading",
            value=f"`{Trading} | {TradingProgress}%`",
            inline=True
        )
        embed.add_field(
            name="Exploration",
            value=f"`{Exploration} | {ExplorationProgress}%`",
            inline=True
        )
        embed.add_field(
            name="CQC",
            value=f"`{CQC} | {CQCProgress}%`",
            inline=True
        )
        embed.add_field(
            name="Empire",
            value=f"`{Empire} | {EmpireProgress}%`",
            inline=True
        )
        embed.add_field(
            name="Federation",
            value=f"`{Federation} | {FederationProgress}%`",
            inline=True
        )
        if "commanderSquadron" in data['events'][0]['eventData']:
            embed.add_field(
                name="‎",
                value="‎",
                inline=False
            )
            embed.add_field(
                name="‎**Squadron**",
                value=f"[{data['events'][0]['eventData']['commanderSquadron']['squadronName']}]({data['events'][0]['eventData']['commanderSquadron']['inaraURL']})",
                inline=False
            )
            embed.add_field(
                name="Rank",
                value=f"`{data['events'][0]['eventData']['commanderSquadron']['squadronMemberRank']}`",
                inline=True,
                #url=data['events'][0]['eventData']['commanderSquadron']['inaraURL']
            )
            embed.add_field(
                name="Members",
                value=f"`{data['events'][0]['eventData']['commanderSquadron']['squadronMembersCount']}`",
                inline=True
            )
        embed.add_field(
            name="‎",
            value="‎",
            inline=False
        )
        embed.set_thumbnail(url=data['events'][0]['eventData']['avatarImageURL'])
        embed.set_footer(text='This code is ruined by ThiJNmEnS#6669')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Inara(bot))