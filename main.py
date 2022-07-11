# This is a sample Python script.
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://ubaporanga.esus.versatecnologia.com.br/')
    print("Página de login encontrada")
    #browser.close()
    page.click('text=Usuário')
    page.fill('input[name="username"]', '08716719646')
    page.fill('input[name="password"]', 'saude2022')
    page.click("[data-testid='LoginForm\.access-button']")
    page.click("button.css-1jy51ie")
    page.wait_for_url("http://ubaporanga.esus.versatecnologia.com.br/lista-atendimento")
    print("Login feito com sucesso")
    time.sleep(1)
    page.locator("button.css-adiyg2").nth(0).click()
    time.sleep(1)
    print("Ficha de atendimento individual acessada com sucesso")
    page.frame_locator("iframe").locator("div:nth-child(2) > .botao-lateral").click()
    page.wait_for_url("http://ubaporanga.esus.versatecnologia.com.br/lista-atendimento/atendimento/23882?iframeUrl=%2Fpec%2Fuser%2Fatendimento%2Fsoap%3FZHBiPTY4MSZkcGM9MTUwMTAmcGVjQmFja0xpbms9TDJ4cGMzUmhMV0YwWlc1a2FXMWxiblJ2JmNpZGFkYW9JZD0xMDUxNCZwcmVBdGVuZGltZW50bz0wJmF0ZW5kUHJvZklkPTMxODgxJmF0ZW5kaW1lbnRvSWQ9MjM4ODImaXNWaXN1YWxpemFyUHJvbnR1YXJpbz0wJnJlYWRPbmx5PTAmbE5EaEhXPTEmMlFLVlNZPTEwJk8zekJZUj0xMTU1JkpyUXJDMT0xJlliZ3ZLYz0zMTg4MSY3enZ3Vzc9MA%3D%3D")
    print("SOAP acessado com sucesso")

    #adicionar cid10 de renovação de prescrição
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1051\"]").click()
    # Fill input[name="ext-comp-1051"]
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1051\"]").fill("z760")
    time.sleep(1)
    page.keyboard.press("Enter")
    page.wait_for_url("http://ubaporanga.esus.versatecnologia.com.br/lista-atendimento/atendimento/23882?iframeUrl=%2Fpec%2Fuser%2Fatendimento%2Fsoap%3FZHBiPTY4MSZkcGM9MTUwMTAmcGVjQmFja0xpbms9TDJ4cGMzUmhMV0YwWlc1a2FXMWxiblJ2JmNpZGFkYW9JZD0xMDUxNCZwcmVBdGVuZGltZW50bz0wJmF0ZW5kUHJvZklkPTMxODgxJmF0ZW5kaW1lbnRvSWQ9MjM4ODImaXNWaXN1YWxpemFyUHJvbnR1YXJpbz0wJnJlYWRPbmx5PTAmbE5EaEhXPTEmMlFLVlNZPTEwJk8zekJZUj0xMTU1JkpyUXJDMT0xJlliZ3ZLYz0zMTg4MSY3enZ3Vzc9MA%3D%3D")
    print("CID10 z760 selecionado")
    buttons = page.locator("role=button")
    # ...
    confirmar_button = buttons.filter(has_text="Confirmar").nth(3)
    confirmar_button.click()
    page.screenshot(path="example.png")
# Press the green button in the gutter to run the script.
