import discord
from discord.ext import commands
import requests
import socket

SECURITYTRAILS_API_KEY = "YOUR_SECURITYTRAILS_API_KEY" # https://securitytrails.com/

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

def fetch_subdomains(domain):
    """
    Fetch subdomains for a given domain using the SecurityTrails API.
    """
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {
        "Content-Type": "application/json",
        "APIKEY": SECURITYTRAILS_API_KEY,
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subdomains = data.get("subdomains", [])
            full_subdomains = [f"{sub}.{domain}" for sub in subdomains]
            return full_subdomains
        else:
            return f"Error: {response.json().get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error: {str(e)}"

def resolve_ip(subdomain):
    """
    Resolve the IP address of a given subdomain.
    """
    try:
        return socket.gethostbyname(subdomain)
    except socket.gaierror:
        return "IP not found"

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def subdomains(ctx, domain: str):
    """
    Command to fetch subdomains for a given domain and display them in an embed.
    """
    await ctx.send(f"Fetching subdomains for `{domain}`... This may take a moment.")
    subdomains = fetch_subdomains(domain)
    
    if isinstance(subdomains, list):
        if subdomains:
            embed = discord.Embed(
                title=f"Subdomains for {domain}",
                color=discord.Color.blue()
            )
            for subdomain in subdomains:
                ip_address = resolve_ip(subdomain)
                embed.add_field(name=subdomain, value=f"IP: {ip_address}", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"No subdomains found for `{domain}`.")
    else:
        await ctx.send(subdomains)

TOKEN = "try using skype token"
bot.run(TOKEN)
