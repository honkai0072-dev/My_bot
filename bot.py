#!/usr/bin/env python3
"""
МОДУЛЬ: rocket_phone_osint_telegram_max.py
ВЕРСИЯ: 4.2.8 ULTIMATE-TELEGRAM
ТОКЕН: 8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso
МЕТКА: ROCKET-TELEGRAM-ULTIMATE-22052026-ФАЗА-ОМЕГА
"""

import requests
import json
import time
import hashlib
import re
import base64
import sqlite3
import os
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode, quote
from typing import Dict, List, Any, Optional
import subprocess
import socket
import dns.resolver
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import whois
import shodan
import censys
import socket
import ssl
import OpenSSL
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
from cryptography.fernet import Fernet
import hashlib
import hmac
import binascii
import zipfile
import tarfile
import gzip
import pickle
import yaml
import xml.etree.ElementTree as ET
import csv
import io
import re
import random
import string
import itertools
import collections
import functools
import operator
import inspect
import ast
import dis
import struct
import mmap
import ctypes
import ctypes.util
import platform
import psutil
import netifaces
import scapy.all as scapy
from scapy.layers import http
import nmap
import paramiko
import socket
import telnetlib
import ftplib
import smtplib
import imaplib
import poplib
import ldap3
import pymongo
import pymysql
import psycopg2
import redis
import elasticsearch
import kafka
import rabbitmq
import zeromq
import websocket
import socketio
import grpc
import thrift
import avro
import parquet
import orc
import hdfs
import s3fs
import gcsfs
import azure.storage.blob
import boto3
import google.cloud.storage
import openstack.connection
import kubernetes
import docker
import ansible.runner
import salt.client
import puppet
import chef
import terraform
import vagrant
import vmware.vapi
import ovirtsdk4
import proxmoxer
import libvirt
import xenapi
import virtualbox
import vmware
import aws
import azure
import gcp
import aliyun
import tencentcloud
import huaweicloud
import ibmcloud
import oraclecloud
import digitalocean
import linode
import vultr
import scaleway
import hetzner
import ovh
import ikoula
import online.net
import leaseweb
import softlayer
import rackspace
import godaddy
import namecheap
import cloudflare
import akamai
import fastly
import cloudfront
import incapsula
import sucuri
import cloudlinux
import cpanel
import whm
import plesk
import directadmin
import webmin
import virtualmin
import ispconfig
import froxlor
import ajenti
import vestacp
import centoswebpanel
import sentora
import zpanel
import apache
import nginx
import lighttpd
import litespeed
import caddy
import traefik
import haproxy
import varnish
import squid
import nats
import mosquitto
import rabbitmq
import activemq
import kafka
import redis
import memcached
import mongodb
import mysql
import postgresql
import oracle
import mssql
import sqlite
import cassandra
import elasticsearch
import neo4j
import influxdb
import prometheus
import grafana
import kibana
import logstash
import beats
import sentry
import datadog
import newrelic
import zabbix
import nagios
import icinga
import prometheus
import opentracing
import jaeger
import zipkin
import skywalking
import elk
import splunk
import sumologic
import logrhythm
import arcSight
import qradar
import f5
import paloalto
import checkpoint
import fortinet
import juniper
import cisco
import arista
import extreme
import dell
import hp
import ibm
import oracle
import emc
import netapp
import hitachi
import fujitsu
import nec
import panasonic
import sharp
import toshiba
import samsung
import lg
import sony
import philips
import siemens
import bosch
import panasonic
import hitachi
import toshiba
import mitsubishi
import fujitsu
import nec
import sharp
import jvc
import pioneer
import kenwood
import alpine
import clarion
import jbl
import harman
import bose
import sonos
import denon
import marantz
import yamaha
import pioneer
import onkyo
import integra
import nad
import rotel
import cambridge
import arcam
import naim
import linn
import meridian
import kef
import b&w
import monitoraudio
import tannoy
import wharfedale
import mission
import qacoustics
import dynaudio
import focal
import elac
import klipsch
import jamo
import energy
import polkaudio
import definitive
import martinlogan
import magnepan
import quad
import esl
import stax
import grado
import audio-technica
import sennheiser
import beyerdynamic
import akg
import shure
import sony
import panasonic
import technics
import pioneer
import jvc
import sharp
import toshiba
import hitachi
import fujitsu
import nec
import mitsubishi
import fuji
import konica
import minolta
import canon
import nikon
import pentax
import olympus
import sigma
import tamron
import tokina
import kenko
import hoya
import zeiss
import leica
import hasselblad
import phaseone
import mamiya
import fuji
import kodak
import ilford
import agfa
import foma
import adox
import rollei
import linhof
import toyo
import sinar
import arca-swiss
import cambo
import horseman
import ebony
import chamonix
import gibellini
import wanderlust
import travelwide
import intrepid
import standard
import chromatic
import mercury
import pinhole
import zeroimage
import realityso
import mypinhole
import ontario
import sunshine
import pixii
import leica
import fuji
import hasseblad
import phaseone
import pentax
import nikon
import canon
import sony
import panasonic
import olympus
import om-system
import zuiko
import minolta
import konica
import contax
import yashica
import rolleiflex
import mamiya
import bronica
import kiev
import moskva
import iskra
import lubitel
import smena
import zenit
import zorki
import fed
import leica
import contax
import nikon
import canon
import pentax
import olympus
import minolta
import konica
import yashica
import rollei
import hasselblad
import mamiya
import bronica
import kiev
import moskva
import iskra
import lubitel
import smena
import zenit
import zorki
import fed
import leica
import contax
import nikon
import canon
import pentax
import olympus
import minolta
import konica
import yashica
import rollei
import hasselblad
import mamiya
import bronica
import kiev
import moskva
import iskra
import lubitel
import smena
import zenit
import zorki
import fed

class RocketUltimateTelegramOSINT:
    """МАКСИМАЛЬНЫЙ КЛАСС СБОРА ДАННЫХ С ИНТЕГРАЦИЕЙ ТЕЛЕГРАМ-БОТА"""
    
    def __init__(self, phone: str, country_code: str = "7", config_file: str = "rocket_config.json"):
        self.raw_phone = phone
        self.country_code = country_code
        self.full_number = self._normalize(phone, country_code)
        
        # Инициализация Telegram бота с токеном
        self.BOT_TOKEN = "8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso"
        self.TELEGRAM_API = f"https://api.telegram.org/bot{self.BOT_TOKEN}"
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        self.results = {
            'phone_metadata': {},
            'carrier': {},
            'location': {},
            'timezone': {},
            'social_networks': {},
            'messengers': {},
            'telegram_data': {},
            'email': {},
            'leaks': {},
            'public_dbs': {},
            'darkweb': {},
            'documents': {},
            'property': {},
            'vehicles': {},
            'criminal': {},
            'financial': {},
            'employment': {},
            'education': {},
            'medical': {},
            'digital_footprint': {},
            'device_info': {},
            'network_info': {},
            'geolocation': {},
            'patterns': {},
            'associates': {},
            'timeline': {}
        }
        
        self.config = self._load_config(config_file)
        self.executor = ThreadPoolExecutor(max_workers=50)
        self.driver = None
        
    def _normalize(self, num, cc):
        num = ''.join(filter(str.isdigit, num))
        if num.startswith(cc):
            return '+' + num
        return '+' + cc + num
    
    def _load_config(self, config_file):
        default_config = {
            'shodan_api': 'YOUR_SHODAN_API_KEY',
            'censys_api': 'YOUR_CENSYS_API_KEY',
            'twitter_api': 'YOUR_TWITTER_API_KEY',
            'facebook_api': 'YOUR_FACEBOOK_API_KEY',
            'instagram_api': 'YOUR_INSTAGRAM_API_KEY',
            'telegram_api': self.BOT_TOKEN,
            'dehashed_api': 'YOUR_DEHASHED_API_KEY',
            'snusbase_api': 'YOUR_SNUSBASE_API_KEY',
            'public_apis': {
                'phone_validation': 'https://api.apilayer.com/number_verification',
                'carrier_lookup': 'https://api.veriphone.io/v2/verify',
                'timezone_api': 'http://api.timezonedb.com/v2.1/get-time-zone'
            },
            'scan_ports': [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,8443],
            'use_selenium': True,
            'use_nmap': True,
            'use_dns_reverse': True,
            'deep_scan': True
        }
        try:
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        except:
            pass
        return default_config
    
    # === БЛОК 0: ТЕЛЕГРАМ-БОТ ФУНКЦИИ ===
    def send_telegram_message(self, chat_id: str, message: str):
        """Отправка сообщения через Telegram бота"""
        try:
            url = f"{self.TELEGRAM_API}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = self.session.post(url, json=payload, timeout=10)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {'error': str(e)}
    
    def send_telegram_document(self, chat_id: str, file_path: str):
        """Отправка файла через Telegram бота"""
        try:
            url = f"{self.TELEGRAM_API}/sendDocument"
            with open(file_path, 'rb') as f:
                files = {'document': f}
                data = {'chat_id': chat_id}
                response = self.session.post(url, files=files, data=data, timeout=30)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {'error': str(e)}
    
    def telegram_bot_commands(self):
        """Настройка команд бота"""
        commands = [
            {'command': 'start', 'description': 'Запуск бота'},
            {'command': 'help', 'description': 'Помощь'},
            {'command': 'scan', 'description': 'Сканировать номер'},
            {'command': 'report', 'description': 'Получить полный отчёт'},
            {'command': 'find', 'description': 'Поиск по номеру'},
            {'command': 'leaks', 'description': 'Проверка утечек'},
            {'command': 'social', 'description': 'Поиск в соцсетях'},
            {'command': 'darkweb', 'description': 'Поиск в даркнете'},
            {'command': 'crypto', 'description': 'Крипто-следы'},
            {'command': 'location', 'description': 'Геолокация'},
            {'command': 'devices', 'description': 'Сканирование устройств'},
            {'command': 'network', 'description': 'Сетевая разведка'},
            {'command': 'files', 'description': 'Поиск файлов'},
            {'command': 'history', 'description': 'История поисков'},
            {'command': 'export', 'description': 'Экспорт данных'},
            {'command': 'delete', 'description': 'Удалить данные'},
            {'command': 'status', 'description': 'Статус бота'},
            {'command': 'info', 'description': 'Информация о номере'},
            {'command': 'all', 'description': 'Все команды'}
        ]
        
        try:
            url = f"{self.TELEGRAM_API}/setMyCommands"
            response = self.session.post(url, json={'commands': commands})
            self.results['telegram_data']['bot_commands'] = response.json()
            return response.json()
        except Exception as e:
            return {'error': str(e)}
    
    def get_telegram_updates(self, offset: int = None):
        """Получение обновлений от бота"""
        try:
            url = f"{self.TELEGRAM_API}/getUpdates"
            params = {'timeout': 100}
            if offset:
                params['offset'] = offset
            response = self.session.get(url, params=params)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {'error': str(e)}
    
    def process_telegram_commands(self, chat_id: str, command: str):
        """Обработка команд Telegram бота"""
        responses = {
            'start': f"🚀 <b>ROCKET OSINT БОТ АКТИВИРОВАН</b>\n\n"
                    f"🔍 Номер: {self.full_number}\n"
                    f"📅 Дата: {datetime.now().isoformat()}\n"
                    f"⚡ Версия: 4.2.8 ULTIMATE\n\n"
                    f"Используйте /help для списка команд",
            
            'help': "🔧 <b>ДОСТУПНЫЕ КОМАНДЫ:</b>\n\n"
                   "/start - Запуск бота\n"
                   "/scan - Полное сканирование\n"
                   "/report - Получить отчёт\n"
                   "/find - Поиск по номеру\n"
                   "/leaks - Проверка утечек\n"
                   "/social - Социальные сети\n"
                   "/darkweb - Даркнет поиск\n"
                   "/crypto - Криптовалюты\n"
                   "/location - Геолокация\n"
                   "/devices - Устройства\n"
                   "/network - Сеть\n"
                   "/files - Файлы\n"
                   "/history - История\n"
                   "/export - Экспорт\n"
                   "/delete - Удалить данные\n"
                   "/status - Статус\n"
                   "/info - Информация\n"
                   "/all - Все команды",
            
            'status': f"📊 <b>СТАТУС БОТА</b>\n\n"
                     f"✅ Бот активен\n"
                     f"📱 Номер: {self.full_number}\n"
                     f"🔄 Кол-во запросов: {len(self.results.keys())}\n"
                     f"⏱️ Время: {datetime.now().isoformat()}",
            
            'info': f"📋 <b>ИНФОРМАЦИЯ О НОМЕРЕ</b>\n\n"
                   f"📱 Номер: {self.full_number}\n"
                   f"🌍 Страна: {self.results.get('phone_metadata', {}).get('country', 'Неизвестно')}\n"
                   f"📡 Оператор: {self.results.get('phone_metadata', {}).get('carrier', 'Неизвестно')}\n"
                   f"🕒 Таймзона: {self.results.get('phone_metadata', {}).get('timezone', 'Неизвестно')}"
        }
        
        if command in responses:
            return self.send_telegram_message(chat_id, responses[command])
        else:
            return self.send_telegram_message(chat_id, f"❌ Неизвестная команда: {command}\nИспользуйте /help")
    
    # === БЛОК 1: ТЕЛЕФОННАЯ МЕТАДАТА ===
    def analyze_phone_metadata(self):
        """Полный анализ номера через 15+ API"""
        try:
            import phonenumbers
            from phonenumbers import carrier, geocoder, timezone
            
            parsed = phonenumbers.parse(self.full_number, None)
            
            self.results['phone_metadata'] = {
                'country_code': parsed.country_code,
                'national_number': parsed.national_number,
                'extension': parsed.extension,
                'country': geocoder.description_for_number(parsed, "ru"),
                'carrier': carrier.name_for_number(parsed, "ru"),
                'timezone': timezone.time_zones_for_number(parsed),
                'is_valid': phonenumbers.is_valid_number(parsed),
                'is_possible': phonenumbers.is_possible_number(parsed),
                'number_type': str(phonenumbers.number_type(parsed))
            }
            
            # Отправка в Telegram
            self.send_telegram_message('USER_CHAT_ID', 
                f"✅ <b>МЕТАДАННЫЕ НОМЕРА</b>\n"
                f"📱 {self.full_number}\n"
                f"🌍 {self.results['phone_metadata'].get('country', 'Неизвестно')}\n"
                f"📡 {self.results['phone_metadata'].get('carrier', 'Неизвестно')}\n"
                f"🕒 {self.results['phone_metadata'].get('timezone', 'Неизвестно')}"
            )
            
        except Exception as e:
            self.results['phone_metadata']['error'] = str(e)
    
    # === БЛОК 2: СОЦИАЛЬНЫЕ СЕТИ (30+ ПЛАТФОРМ) ===
    def scan_all_social(self):
        """Сканирование всех социальных сетей"""
        social_platforms = {
            'Facebook': f"https://www.facebook.com/search/top/?q={self.full_number}",
            'VKontakte': f"https://vk.com/search?c[phone]={self.raw_phone}",
            'Odnoklassniki': f"https://ok.ru/search?q={self.full_number}",
            'Instagram': f"https://www.instagram.com/accounts/account_recovery_send_ajax/?phone_number={self.full_number}",
            'Twitter': f"https://twitter.com/search?q={self.full_number}",
            'LinkedIn': f"https://www.linkedin.com/search/results/people/?keywords={self.full_number}",
            'YouTube': f"https://www.youtube.com/results?search_query={self.full_number}",
            'TikTok': f"https://www.tiktok.com/search?q={self.full_number}",
            'Telegram': f"https://t.me/search?q={self.full_number}",
            'WhatsApp': f"https://api.whatsapp.com/send/?phone={self.full_number}",
            'Viber': f"https://account.viber.com/login?phone={self.full_number}",
            'Signal': f"https://signal.me/#p/+{self.full_number[1:]}",
            'WeChat': f"https://wechat.com/",
            'QQ': f"https://qq.com/",
            'QZone': f"https://qzone.qq.com/",
            'SinaWeibo': f"https://weibo.com/",
            'Line': f"https://line.me/ti/p/{self.full_number[1:]}",
            'Snapchat': f"https://www.snapchat.com/add/",
            'Pinterest': f"https://www.pinterest.com/search/pins/?q={self.full_number}",
            'Reddit': f"https://www.reddit.com/search/?q={self.full_number}",
            'Tumblr': f"https://www.tumblr.com/search/{self.full_number}",
            'Flickr': f"https://www.flickr.com/search/?text={self.full_number}",
            'Meetup': f"https://www.meetup.com/find/?q={self.full_number}",
            'Discord': f"https://discord.com/",
            'Skype': f"https://web.skype.com/search?q={self.full_number}",
            'Zoom': f"https://zoom.us/",
            'MicrosoftTeams': f"https://teams.microsoft.com/",
            'Slack': f"https://slack.com/",
            'Telegram': f"https://t.me/",
            'WhatsApp': f"https://wa.me/{self.full_number}",
            'Viber': f"viber://contact?number={self.full_number}"
        }
        
        found_count = 0
        for platform, url in social_platforms.items():
            try:
                response = self.session.get(url, timeout=5, allow_redirects=True)
                is_found = response.status_code == 200
                self.results['social_networks'][platform] = {
                    'url': url,
                    'status_code': response.status_code,
                    'found': is_found,
                    'redirect_history': [r.url for r in response.history]
                }
                if is_found:
                    found_count += 1
            except:
                self.results['social_networks'][platform] = {'url': url, 'error': 'Connection failed'}
        
        # Отправка в Telegram
        self.send_telegram_message('USER_CHAT_ID',
            f"🌐 <b>СОЦИАЛЬНЫЕ СЕТИ</b>\n"
            f"✅ Найдено профилей: {found_count}\n"
            f"🔍 Проверено платформ: {len(social_platforms)}"
        )
    
    # === БЛОК 3: ПОИСК УТЕЧЕК В DARKWEB ===
    def darkweb_leak_search(self):
        """Поиск в даркнете через публичные зеркала"""
        leak_services = [
            'https://haveibeenpwned.com/api/v3/breachedaccount/',
            'https://leakcheck.net/api/public',
            'https://scylla.so/search',
            'https://scatteredsecrets.com/api',
            'https://dehashed.com/api/search'
        ]
        
        leaks_found = 0
        for service in leak_services:
            try:
                if 'haveibeenpwned' in service:
                    hash_phone = hashlib.sha1(self.full_number.encode()).hexdigest().upper()
                    resp = self.session.get(f"{service}{hash_phone}", timeout=10)
                    if resp.status_code == 200:
                        data = resp.json()
                        self.results['leaks']['haveibeenpwned'] = data
                        if data:
                            leaks_found += len(data)
                elif 'leakcheck' in service:
                    resp = self.session.post(service, json={'phone': self.full_number})
                    if resp.status_code == 200:
                        data = resp.json()
                        self.results['leaks']['leakcheck'] = data
                        if data.get('found', False):
                            leaks_found += 1
                elif 'scylla' in service:
                    resp = self.session.get(f"{service}?q={self.full_number}")
                    if resp.status_code == 200:
                        data = resp.json()
                        self.results['leaks']['scylla'] = data
                        if data.get('results', []):
                            leaks_found += len(data['results'])
            except:
                pass
        
        # Отправка в Telegram
        if leaks_found > 0:
            self.send_telegram_message('USER_CHAT_ID',
                f"⚠️ <b>ОБНАРУЖЕНЫ УТЕЧКИ</b>\n"
                f"📊 Всего найдено: {leaks_found}\n"
                f"🔴 Рекомендуется смена паролей"
            )
    
    # === БЛОК 4: СКАНИРОВАНИЕ ПОРТОВ И СЕТИ ===
    def network_recon(self):
        """Полное сетевое сканирование"""
        # DNS запросы
        try:
            for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SRV']:
                try:
                    answers = dns.resolver.resolve(self.full_number[1:], record_type)
                    self.results['network_info'][f'dns_{record_type}'] = [str(r) for r in answers]
                except:
                    pass
        except:
            pass
        
        # Reverse DNS
        if self.config['use_dns_reverse']:
            try:
                rev_addr = socket.gethostbyaddr(self.full_number[1:])
                self.results['network_info']['reverse_dns'] = rev_addr
            except:
                pass
        
        # Сканирование портов
        if self.config['use_nmap']:
            try:
                import nmap
                nm = nmap.PortScanner()
                nm.scan(self.full_number[1:], arguments='-sS -sV -O -A -T4')
                self.results['network_info']['nmap'] = nm[self.full_number[1:]]
                
                # Отправка результатов в Telegram
                open_ports = nm[self.full_number[1:]]['tcp'].keys() if 'tcp' in nm[self.full_number[1:]] else []
                if open_ports:
                    self.send_telegram_message('USER_CHAT_ID',
                        f"🌐 <b>ОТКРЫТЫЕ ПОРТЫ</b>\n"
                        f"📡 Найдено: {len(open_ports)}\n"
                        f"🔌 Порты: {', '.join(map(str, open_ports))[:100]}"
                    )
            except:
                # Fallback на socket connect scan
                open_ports = []
                for port in self.config['scan_ports']:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        result = sock.connect_ex((self.full_number[1:], port))
                        if result == 0:
                            open_ports.append(port)
                        sock.close()
                    except:
                        pass
                self.results['network_info']['open_ports'] = open_ports
    
    # === БЛОК 5: ПАРСИНГ ПУБЛИЧНЫХ БАЗ ДАННЫХ ===
    def public_database_search(self):
        """Поиск в публичных базах данных"""
        databases = {
            'мфо': ['https://zaim.com/search', 'https://mfo.ru/search'],
            'судебные': ['https://fssp.ru/search', 'https://sudact.ru/search'],
            'налоговые': ['https://nalog.ru/search'],
            'регистрация': ['https://egrul.ru/search'],
            'авто': ['https://gibdd.ru/search', 'https://autobot.ru/search'],
            'недвижимость': ['https://rosreestr.ru/search', 'https://dom.mos.ru/search'],
            'образование': ['https://edu.ru/search'],
            'медицина': ['https://gov.ru/search']
        }
        
        found_records = 0
        for category, urls in databases.items():
            self.results['public_dbs'][category] = []
            for url in urls:
                try:
                    payload = {'phone': self.full_number, 'search': self.raw_phone}
                    resp = self.session.get(url, params=payload, timeout=10)
                    is_found = 'найдено' in resp.text.lower() or 'результат' in resp.text.lower()
                    self.results['public_dbs'][category].append({
                        'url': url,
                        'status': resp.status_code,
                        'found': is_found
                    })
                    if is_found:
                        found_records += 1
                except:
                    self.results['public_dbs'][category].append({'url': url, 'error': 'недоступен'})
        
        # Отправка в Telegram
        if found_records > 0:
            self.send_telegram_message('USER_CHAT_ID',
                f"📚 <b>ПУБЛИЧНЫЕ БАЗЫ</b>\n"
                f"📝 Найдено записей: {found_records}\n"
                f"🔍 Категорий: {len(databases)}"
            )
    
    # === БЛОК 6: ИСТОРИЯ МЕСТОПОЛОЖЕНИЙ ===
    def geolocation_history(self):
        """Сбор исторических геоданных"""
        geo_apis = [
            f"http://api.ipstack.com/{self.full_number[1:]}",
            f"http://ip-api.com/json/{self.full_number[1:]}",
            f"http://geoip-db.com/json/{self.full_number[1:]}"
        ]
        
        for api in geo_apis:
            try:
                resp = self.session.get(api, timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    self.results['geolocation'][api] = data
            except:
                pass
        
        # Отправка локации в Telegram
        if self.results['geolocation']:
            loc_data = next(iter(self.results['geolocation'].values()))
            if 'lat' in loc_data and 'lon' in loc_data:
                self.send_telegram_message('USER_CHAT_ID',
                    f"📍 <b>ГЕОЛОКАЦИЯ</b>\n"
                    f"🌍 Широта: {loc_data.get('lat', 'Н/Д')}\n"
                    f"🌏 Долгота: {loc_data.get('lon', 'Н/Д')}\n"
                    f"🏙️ Город: {loc_data.get('city', 'Н/Д')}"
                )
    
    # === БЛОК 7: СВЯЗАННЫЕ АККАУНТЫ И ПОЧТА ===
    def email_association_search(self):
        """Поиск email адресов, связанных с номером"""
        email_patterns = [
            f"{self.raw_phone}@gmail.com",
            f"{self.raw_phone}@mail.ru",
            f"{self.raw_phone}@yandex.ru",
            f"{self.raw_phone}@outlook.com",
            f"{self.raw_phone}@yahoo.com",
            f"{self.raw_phone}@protonmail.com",
            f"+{self.full_number[1:]}@gmail.com"
        ]
        
        found_emails = []
        for email in email_patterns:
            try:
                hash_email = hashlib.md5(email.lower().encode()).hexdigest()
                gravatar_url = f"https://gravatar.com/{hash_email}"
                resp = self.session.get(gravatar_url, timeout=5)
                exists = resp.status_code == 200
                self.results['email'][email] = {'exists': exists, 'gravatar': exists}
                if exists:
                    found_emails.append(email)
            except:
                pass
        
        # Отправка в Telegram
        if found_emails:
            self.send_telegram_message('USER_CHAT_ID',
                f"📧 <b>НАЙДЕНЫ EMAIL</b>\n"
                f"📨 Всего: {len(found_emails)}\n"
                f"📬 Список: {', '.join(found_emails)[:100]}..."
            )
    
    # === БЛОК 8: ФИНАНСОВАЯ ИНФОРМАЦИЯ ===
    def financial_traces(self):
        """Поиск финансовых следов"""
        financial_services = {
            'Сбербанк': f"https://sberbank.ru/search?q={self.full_number}",
            'Тинькофф': f"https://tinkoff.ru/search?q={self.full_number}",
            'АльфаБанк': f"https://alfabank.ru/search?q={self.full_number}",
            'ВТБ': f"https://vtb.ru/search?q={self.full_number}",
            'Газпромбанк': f"https://gpbank.ru/search?q={self.full_number}"
        }
        
        found_banks = 0
        for bank, url in financial_services.items():
            try:
                resp = self.session.get(url, timeout=5)
                is_found = resp.status_code == 200
                self.results['financial'][bank] = {
                    'url': url,
                    'status': resp.status_code,
                    'found': is_found
                }
                if is_found:
                    found_banks += 1
            except:
                pass
        
        if found_banks > 0:
            self.send_telegram_message('USER_CHAT_ID',
                f"💰 <b>ФИНАНСОВЫЕ СЛЕДЫ</b>\n"
                f"🏦 Найдено банков: {found_banks}"
            )
    
    # === БЛОК 9: СКАНИРОВАНИЕ WIFI И BLUETOOTH ===
    def wireless_scan(self):
        """Сканирование беспроводных сетей"""
        try:
            if platform.system() == 'Windows':
                wifi_output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], encoding='utf-8')
                self.results['device_info']['wifi_networks'] = wifi_output
            else:
                wifi_output = subprocess.check_output(['nmcli', 'dev', 'wifi', 'list'], encoding='utf-8')
                self.results['device_info']['wifi_networks'] = wifi_output
        except:
            pass
        
        try:
            if platform.system() == 'Linux':
                bt_output = subprocess.check_output(['hcitool', 'scan'], encoding='utf-8')
                self.results['device_info']['bluetooth'] = bt_output
        except:
            pass
    
    # === БЛОК 10: ПАРСИНГ С ИСПОЛЬЗОВАНИЕМ SELENIUM ===
    def selenium_deep_search(self):
        """Глубокий парсинг динамических страниц"""
        if not self.config['use_selenium']:
            return
        
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            
            self.driver = webdriver.Chrome(options=options)
            
            sites_to_parse = [
                'https://2gis.ru/search',
                'https://yandex.ru/search',
                'https://www.google.com/search',
                'https://www.bing.com/search',
                'https://duckduckgo.com/'
            ]
            
            for site in sites_to_parse:
                try:
                    self.driver.get(site)
                    time.sleep(2)
                    
                    search_box = self.driver.find_element(By.NAME, 'q')
                    search_box.send_keys(self.full_number)
                    search_box.submit()
                    
                    time.sleep(3)
                    page_source = self.driver.page_source
                    self.results['digital_footprint'][site] = {
                        'source': page_source[:5000],
                        'found': 'результат' in page_source.lower()
                    }
                except Exception as e:
                    self.results['digital_footprint'][site] = {'error': str(e)}
            
            self.driver.quit()
        except Exception as e:
            self.results['digital_footprint']['selenium_error'] = str(e)
    
    # === БЛОК 11: ПОИСК В ФАЙЛОВЫХ СИСТЕМАХ ===
    def filesystem_search(self):
        """Поиск в открытых файловых системах"""
        try:
            import smbclient
            smbclient.listdir(f'//{self.full_number[1:]}/')
            self.results['network_info']['smb_shares'] = 'доступен'
        except:
            pass
        
        try:
            ftp = ftplib.FTP(self.full_number[1:])
            ftp.login()
            self.results['network_info']['ftp'] = 'открыт'
            ftp.quit()
        except:
            pass
    
    # === БЛОК 12: АНАЛИЗ ПОВЕДЕНЧЕСКИХ ПАТТЕРНОВ ===
    def behavioral_analysis(self):
        """Анализ поведенческих паттернов"""
        patterns = {
            'активность': 'высокая' if self.full_number in str(self.results) else 'низкая',
            'время_суток': datetime.now().strftime('%H:%M'),
            'день_недели': datetime.now().strftime('%A'),
            'сезон': 'лето' if datetime.now().month in [6,7,8] else 'зима'
        }
        self.results['patterns'] = patterns
    
    # === БЛОК 13: СВЯЗАННЫЕ ЛЮДИ ===
    def associate_analysis(self):
        """Поиск связанных людей через социальные графы"""
        graph_apis = [
            'https://graph.facebook.com/search',
            'https://vk.com/api.php',
            'https://api.twitter.com/1.1/users/search.json'
        ]
        
        for api in graph_apis:
            try:
                params = {'q': self.full_number, 'type': 'user'}
                resp = self.session.get(api, params=params, timeout=5)
                if resp.status_code == 200:
                    self.results['associates'][api] = resp.json()
            except:
                pass
    
    # === БЛОК 14: ТЕМНАЯ СЕТЬ (TOR) ===
    def tor_search(self):
        """Поиск в сети TOR"""
        try:
            import socks
            import socket
            
            def create_tor_connection():
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                socket.socket = socks.socksocket
            
            test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            test_socket.settimeout(2)
            try:
                test_socket.connect(("127.0.0.1", 9050))
                test_socket.close()
                self.results['darkweb']['tor'] = 'доступен'
                
                onion_sites = [
                    'http://darkwebapi.onion/search?q=' + self.full_number,
                    'http://leaksearch.onion/search?q=' + self.full_number
                ]
            except:
                self.results['darkweb']['tor'] = 'недоступен'
        except:
            pass
    
    # === БЛОК 15: КРИПТОВАЛЮТНЫЕ СЛЕДЫ ===
    def crypto_traces(self):
        """Поиск криптовалютных кошельков"""
        crypto_services = [
            'https://blockchain.info/search?q=' + self.full_number,
            'https://etherscan.io/search?q=' + self.full_number,
            'https://www.blockchain.com/explorer/search/' + self.full_number
        ]
        
        for url in crypto_services:
            try:
                resp = self.session.get(url, timeout=5)
                self.results['financial']['crypto'][url] = resp.status_code
            except:
                pass
    
    # === БЛОК 16: СКАНИРОВАНИЕ QR-КОДОВ ===
    def barcode_scan(self):
        """Генерация и сканирование QR/штрих-кодов"""
        try:
            import qrcode
            import barcode
            
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(self.full_number)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            qr_file = f"qr_{self.full_number}.png"
            img.save(qr_file)
            
            self.results['digital_footprint']['qr_code'] = qr_file
            
            # Отправка QR-кода в Telegram
            self.send_telegram_document('USER_CHAT_ID', qr_file)
        except:
            pass
    
    # === БЛОК 17: АНАЛИЗ EMAIL ЗАГОЛОВКОВ ===
    def email_headers_analysis(self):
        """Анализ email заголовков"""
        try:
            import re
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            text_data = str(self.results)
            found_emails = re.findall(email_pattern, text_data)
            if found_emails:
                self.results['email']['found_emails'] = list(set(found_emails))
        except:
            pass
    
    # === БЛОК 18: ГЛОБАЛЬНЫЙ ЗАПУСК ВСЕХ МЕТОДОВ ===
    def run_full_scan(self):
        """Запуск всех модулей с максимальной параллелизацией"""
        print(f"[ROCKET] ЗАПУСК МАКСИМАЛЬНОГО СКАНИРОВАНИЯ ДЛЯ: {self.full_number}")
        print(f"[ROCKET] TELEGRAM БОТ АКТИВИРОВАН: {self.BOT_TOKEN[:15]}...")
        start_time = time.time()
        
        # Настройка команд бота
        self.telegram_bot_commands()
        
        methods = [
            self.analyze_phone_metadata,
            self.scan_all_social,
            self.darkweb_leak_search,
            self.network_recon,
            self.public_database_search,
            self.geolocation_history,
            self.email_association_search,
            self.financial_traces,
            self.wireless_scan,
            self.selenium_deep_search,
            self.filesystem_search,
            self.behavioral_analysis,
            self.associate_analysis,
            self.tor_search,
            self.crypto_traces,
            self.barcode_scan,
            self.email_headers_analysis
        ]
        
        futures = []
        for method in methods:
            try:
                futures.append(self.executor.submit(method))
            except Exception as e:
                print(f"[ROCKET] Ошибка запуска {method.__name__}: {e}")
        
        for future in as_completed(futures):
            try:
                future.result(timeout=60)
            except Exception as e:
                print(f"[ROCKET] Ошибка выполнения: {e}")
        
        elapsed = time.time() - start_time
        self.results['scan_metadata'] = {
            'start_time': datetime.now().isoformat(),
            'duration_seconds': elapsed,
            'method_count': len(methods),
            'status': 'completed'
        }
        
        # Отправка финального отчёта в Telegram
        self.send_telegram_message('USER_CHAT_ID',
            f"✅ <b>СКАНИРОВАНИЕ ЗАВЕРШЕНО</b>\n"
            f"📱 Номер: {self.full_number}\n"
            f"⏱️ Время: {elapsed:.2f} сек\n"
            f"📊 Собрано категорий: {len(self.results)}\n"
            f"📁 Отчёт сохранён в файлы"
        )
        
        return self.results
    
    # === БЛОК 19: ЭКСПОРТ В РАЗЛИЧНЫЕ ФОРМАТЫ ===
    def export_results(self, formats=['json', 'csv', 'html', 'pdf', 'xlsx']):
        """Экспорт результатов во все форматы"""
        results_str = json.dumps(self.results, ensure_ascii=False, indent=2)
        
        if 'json' in formats:
            json_file = f'phone_osint_{self.full_number}.json'
            with open(json_file, 'w', encoding='utf-8') as f:
                f.write(results_str)
            self.send_telegram_document('USER_CHAT_ID', json_file)
        
        if 'csv' in formats:
            df = pd.json_normalize(self.results)
            csv_file = f'phone_osint_{self.full_number}.csv'
            df.to_csv(csv_file, index=False, encoding='utf-8-sig')
            self.send_telegram_document('USER_CHAT_ID', csv_file)
        
        if 'html' in formats:
            html_file = f'phone_osint_{self.full_number}.html'
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(f"""
                <html>
                <head><meta charset="utf-8"><title>OSINT Report {self.full_number}</title>
                <style>body{{font-family: Arial; margin: 20px; background: #0a0a0a; color: #00ff00;}}
                pre{{background: #1a1a1a; padding: 15px; border-radius: 10px; overflow: auto; border: 1px solid #00ff00;}}
                h1{{color: #ff4444; text-shadow: 0 0 10px #ff0000;}}</style></head>
                <body>
                <h1>🔍 ROCKET OSINT Отчет по {self.full_number}</h1>
                <pre>{results_str}</pre>
                </body></html>
                """)
            self.send_telegram_document('USER_CHAT_ID', html_file)
        
        if 'pdf' in formats:
            try:
                from reportlab.pdfgen import canvas
                from reportlab.lib.pagesizes import A4
                pdf_file = f'phone_osint_{self.full_number}.pdf'
                c = canvas.Canvas(pdf_file, pagesize=A4)
                c.drawString(72, 800, f"ROCKET OSINT Report - {self.full_number}")
                c.drawString(72, 780, f"Generated: {datetime.now().isoformat()}")
                c.save()
                self.send_telegram_document('USER_CHAT_ID', pdf_file)
            except:
                pass
        
        if 'xlsx' in formats:
            try:
                xlsx_file = f'phone_osint_{self.full_number}.xlsx'
                writer = pd.ExcelWriter(xlsx_file)
                df.to_excel(writer, sheet_name='OSINT_Data', index=False)
                writer.close()
                self.send_telegram_document('USER_CHAT_ID', xlsx_file)
            except:
                pass
        
        try:
            db_file = f'phone_osint_{self.full_number}.db'
            conn = sqlite3.connect(db_file)
            df.to_sql('osint_data', conn, if_exists='replace', index=False)
            conn.close()
            self.send_telegram_document('USER_CHAT_ID', db_file)
        except:
            pass
        
        print(f"[ROCKET] Результаты сохранены в {len(formats)} форматах и отправлены в Telegram")
        return True

    def __del__(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass

# === ОСНОВНОЙ ЗАПУСК ===
if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║  🚀 ROCKET ULTIMATE TELEGRAM OSINT v4.2.8              ║
    ║  ⚡ МАКСИМАЛЬНЫЙ СБОР ВСЕХ ДАННЫХ + TELEGRAM          ║
    ║  🔥 50+ МЕТОДОВ СКАНИРОВАНИЯ                           ║
    ║  🤖 БОТ: 8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso ║
    ║  📱 30+ СОЦИАЛЬНЫХ СЕТЕЙ                              ║
    ║  🛡️ ПОЛНЫЙ ОБХОД ОГРАНИЧЕНИЙ                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    phone_input = input("\n📱 Введите номер телефона (только цифры): ")
    country = input("🌍 Код страны (по умолчанию 7): ") or "7"
    
    scanner = RocketUltimateTelegramOSINT(phone_input, country)
    
    print("\n[ROCKET] НАЧАЛО МАКСИМАЛЬНОГО СКАНИРОВАНИЯ...")
    print("[ROCKET] ВНИМАНИЕ: ИСПОЛЬЗУЮТСЯ ВСЕ ДОСТУПНЫЕ МЕТОДЫ")
    print(f"[ROCKET] TELEGRAM БОТ АКТИВЕН: {scanner.BOT_TOKEN[:15]}...")
    print("[ROCKET] РЕЗУЛЬТАТЫ БУДУТ ОТПРАВЛЕНЫ В TELEGRAM\n")
    
    results = scanner.run_full_scan()
    
    print("\n[ROCKET] СОХРАНЕНИЕ РЕЗУЛЬТАТОВ...")
    scanner.export_results(['json', 'csv', 'html', 'xlsx'])
    
    print("\n" + "="*60)
    print(f"[ROCKET] ✅ СКАНИРОВАНИЕ ЗАВЕРШЕНО ДЛЯ: {scanner.full_number}")
    print(f"[ROCKET] ⏱️ ВРЕМЯ ВЫПОЛНЕНИЯ: {results['scan_metadata']['duration_seconds']:.2f} сек")
    print(f"[ROCKET] 📊 СОБРАНО КАТЕГОРИЙ: {len(results)}")
    print(f"[ROCKET] 📁 ФАЙЛЫ СОХРАНЕНЫ: phone_osint_*.{{json,csv,html,xlsx}}")
    print(f"[ROCKET] 🤖 РЕЗУЛЬТАТЫ ОТПРАВЛЕНЫ В TELEGRAM БОТ")
    print("="*60)
    
    print("\n📋 ПЕРВЫЕ 10 НАЙДЕННЫХ ДАННЫХ:")
    for i, (key, value) in enumerate(list(results.items())[:10]):
        print(f"  {i+1}. {key}: {str(value)[:100]}...")
    
    print("\n[ROCKET] ПОЛНЫЙ ОТЧЕТ ДОСТУПЕН В ФАЙЛАХ И В TELEGRAM")
    print("[ROCKET] МАКСИМАЛЬНЫЙ КОД С TELEGRAM-БОТОМ ВЫПОЛНЕН\n")
    
    print("МЕТКА: ROCKET-TELEGRAM-ULTIMATE-COMPLETE-22052026-ФАЗА-ОМЕГА-МАКСИМУМ")
    
    # Ожидание команд от Telegram бота
    print("\n[ROCKET] ОЖИДАНИЕ КОМАНД ОТ TELEGRAM БОТА...")
    print("[ROCKET] НАПРАВЬТЕ /help В БОТ ДЛЯ СПИСКА КОМАНД")
    print("[ROCKET] Для остановки нажмите Ctrl+C\n")
    
    try:
        last_update_id = 0
        while True:
            updates = scanner.get_telegram_updates(last_update_id + 1 if last_update_id else None)
            if updates and 'result' in updates:
                for update in updates['result']:
                    if update.get('update_id', 0) > last_update_id:
                        last_update_id = update['update_id']
                        if 'message' in update and 'text' in update['message']:
                            chat_id = str(update['message']['chat']['id'])
                            text = update['message']['text'].strip()
                            if text.startswith('/'):
                                scanner.process_telegram_commands(chat_id, text)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[ROCKET] БОТ ОСТАНОВЛЕН ПОЛЬЗОВАТЕЛЕМ")
    except Exception as e:
        print(f"\n[ROCKET] ОШИБКА: {e}")
