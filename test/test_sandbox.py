import allure
import pytest
import time
def test_click_en_enviar(sandbox_page):
    sandbox_page.navigate_sandbox()
    #sandbox_page.click_enviar()
    sandbox_page.click_boton_id_dinamico()
    elemento_texto_oculto =sandbox_page.wait_for_element(sandbox_page.HIDDEN_TEXT_LABEL)
    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    assert (
            texto_esperado in elemento_texto_oculto.text
    ),"El texto esperado no coincide"

def test_boton_id_dinamico_hover(sandbox_page):
    sandbox_page.navigate_sandbox()
    button_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)
    color_before_hover = button_id_dinamico.value_of_css_property("background-color")
    sandbox_page.hover_over_dynamic_id_button()
    color_after_hover = button_id_dinamico.value_of_css_property("background-color")
    assert color_before_hover != color_after_hover

def test_elegir_checkbox_by_id(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox_by_id()

def test_elegir_checkbox_by_xpath(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox_by_xpath()

def test_elegir_checkbox_by_dinamic_word(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox_by_dinamic_word("Pasta")

def test_radio_button(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_radio_button_by_dinamic_word("Si")

def test_elegir_checkbox_by_dinamic_word_new(sandbox_page):
    sandbox_page.navigate_new_page()
    time.sleep(5)
    sandbox_page.select_checkbox_by_dinamic_word_new("Checkbox")
    #sandbox_page.unselect_checkbox_by_dinamic_word_new("Checkbox")
    time.sleep(5)

@pytest.mark.dropdown
def test_elegir_operacion_dropdown(sandbox_page):
    sandbox_page.navigate_dropdowns()
    sandbox_page.selec_operation('minus')

@pytest.mark.dropdown
def test_operation_dropdown_options(sandbox_page):
    sandbox_page.navigate_dropdowns()
    options =sandbox_page.get_operation_options()
    expectedoptions = ['plus', 'times', 'minus','divide']
    assert all(
        option in options for option in expectedoptions
        ),"No todas las opciones esperadas estan presentes en el select"

@pytest.mark.popup
def test_popup_title(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_popup()
    popup_title_text =sandbox_page.get_popup_title_text()
    expected_popup_title_text = "Popup de ejemplo"

    assert (expected_popup_title_text in popup_title_text
            ),f"EL textop del popup es incorrecto '{popup_title_text}' en su lugar"

@pytest.mark.cell
def test_valor_celda_dinamica(sandbox_page):
    sandbox_page.navigate_sandbox()
    valor_inicial=sandbox_page.get_cell_value_dinamic(2,3)
    sandbox_page.reload_page()
    valor_post_carga=sandbox_page.get_cell_value_dinamic(2,3)
    assert (
            valor_inicial != valor_post_carga
    ), f"el valor de la celda no cambio, el valor es {valor_inicial}"

@allure.epic("Interfaz Web")
@allure.feature("Tabla estatica")
@allure.story("Comportamiento de tablas")
@allure.issue("IS-145")
@allure.link("https://github.com/jrramirezglz/web")
@pytest.mark.cell
def test_valor_celda_estatica(sandbox_page):
    with allure.step("Navega a la pagina"):
        sandbox_page.navigate_sandbox()
    with allure.step("carga el valor de la tabla"):
        valor_inicial=sandbox_page.get_cell_value_static(2,3)
    with allure.step("recarga la pagina"):
        sandbox_page.reload_page()
    with allure.step("carga el nuevo valor de la tabla"):
        valor_post_carga=sandbox_page.get_cell_value_static(2,3)
    assert (
            valor_inicial == valor_post_carga
    ), f"el valor de la celda no cambio, el valor es {valor_inicial}"