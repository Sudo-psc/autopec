#!/usr/bin/env venv
# -*- encoding: utf-8 -*-

import time
import cv2
#from pyclick import HumanClicker
from playwright.sync_api import Playwright, sync_playwright, expect
import numpy as np
import pyautogui
import os
has = "120"
had = "80"
_Z760 = cv2.imread('./images/_Z760.jpg')
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = browser.new_page()
    context.set_default_navigation_timeout(60000)
    page.goto('http://ubaporanga.esus.versatecnologia.com.br/')
    print("Página de login encontrada")
    page.click('text=Usuário')
    page.fill('input[name="username"]', '08716719646')
    page.fill('input[name="password"]', 'saude2022')
    page.click("[data-testid='LoginForm\.access-button']")
    page.click("button.css-1jy51ie")
    page.wait_for_url("http://ubaporanga.esus.versatecnologia.com.br/lista-atendimento")
    print("Login feito com sucesso")
    page.wait_for_timeout(1000)
    page.locator("button.css-adiyg2").nth(1).click()
    page.wait_for_timeout(1000)
    print("Ficha de atendimento individual acessada com sucesso")
    page.frame_locator("iframe").locator("div:nth-child(2) > .botao-lateral").click()
    print("SOAP acessado com sucesso")
    page.wait_for_timeout(1000)
    form_has = page.frame_locator("iframe").locator('input[name="ext-comp-1033"]')
    form_has.wait_for()
    form_has.fill(has)
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1033\"]").press("Tab")
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1034\"]").fill(had)
    page.wait_for_timeout(1000)
    print(f"Pressão arterial preenchida em 120x80")
    # adicionar cid10 de renovação de prescrição
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1051\"]").click()
    # Fill input[name="ext-comp-1051"]
    page.frame_locator("iframe").locator("input[name=\"ext-comp-1051\"]")
    page.keyboard.type("z760")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(5000)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    pyautogui.locateOnScreen(_Z760)
    pyautogui.click()
    page.wait_for_timeout(1000)
    print("CID10 z760 selecionado")
    page.frame_locator("iframe").locator("button", has_text="Confirmar").nth(1).click()
    print("CID confirmado")
    page.wait_for_timeout(1000)
    page.frame_locator("iframe").locator("button", has_text="Finalizar Atendimento").click()
    #page.check(has_text="Alta do episódio")
    page.wait_for_timeout(3000)
    page.frame_locator("iframe").locator('input[name="ext-comp-1088"]').click()
    page.wait_for_timeout(4000)
    page.frame_locator("iframe").locator("button", has_text="Finalizar Atendimento").click()
    print(f"Atendimento finalizado com sucesso!")

    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)