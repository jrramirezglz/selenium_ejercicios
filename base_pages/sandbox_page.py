from selenium.webdriver.common.by import By
from .base_page import BasePage


class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH,"//button[contains(text(),'Enviar')]")
    DYNAMIC_ID_BUTTON = (By.XPATH,"//button[contains(text()"
                                  ",'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]")
    HIDDEN_TEXT_LABEL = (By.XPATH,"//p[contains(text(),'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]")
    CHECKBOX_BUTTON = (By.ID, 'checkbox-0')
    CHECKBOX_HAMBURGUESA = (By.XPATH, "//label[contains(.,'Hamburguesa')]/preceding-sibling::input[@type = 'checkbox']")
    CALCULADORA_DROPDOWN =(By.ID, 'function')
    MOSTRAR_BOTON_POP_UP=(By.XPATH, "//button[@type='button' and contains(@class,'btn-primary')and text()='Mostrar popup']")
    POP_TITLE=(By.ID,"contained-modal-title-vcenter")

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def navigate_new_page(self):
        self.navigate_to(
            "https://testpages.eviltester.com/styled/reference/input.html"
        )

    def navigate_dropdowns(self):
        self.navigate_to(
            "https://testpages.eviltester.com/styled/calculator"
        )

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)

    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)

    def navigate_in_page(self, element):
        self.hover_over_element(element)

    def select_checkbox_by_id(self):
        self.select_element(self.CHECKBOX_BUTTON)

    def select_checkbox_by_xpath(self):
        self.select_element(self.CHECKBOX_HAMBURGUESA)

    def select_checkbox_by_dinamic_word(self,label_text):
        assert label_text in ["Pizza", "Hamburguesa","Pasta","Helado", "Torta"], "La opcion tiene que ser SI o NO"
        checkbox_locator =(
            By.XPATH,
            f"//label[contains(.,'{label_text}')]/preceding-sibling::input[@type = 'checkbox']",
        )
        self.select_element(checkbox_locator)

    def select_radio_button_by_dinamic_word(self,option):
        assert option in ["Si", "No"], "La opcion tiene que ser SI o NO"
        radio_button_locator =(
            By.XPATH,
            f"//label[@class='form-check-label' and contains(text(),'{option}')]",
        )
        self.select_element(radio_button_locator)

    def select_checkbox_by_dinamic_word_new(self,label_text):
        assert label_text in ["Checkbox"], "La opcion tiene que ser Home"
        checkbox_locator =(
            By.XPATH,
            f"//label[contains(.,'{label_text}')]/following-sibling::input[@type = 'checkbox']",
        )
        self.select_element(checkbox_locator)

    def unselect_checkbox_by_dinamic_word_new(self,label_text):
        assert label_text in ["Checkbox"], "La opcion tiene que ser Home"
        checkbox_locator =(
            By.XPATH,
            f"//label[contains(.,'{label_text}')]/following-sibling::input[@type = 'checkbox']",
        )
        self.unselect_checkbox(checkbox_locator)

    def selec_operation(self,operation):
        self.selec_from_dropdown_by_visible_text(self.CALCULADORA_DROPDOWN,operation)

    def get_operation_options(self):
        return self.get_select_option(self.CALCULADORA_DROPDOWN)

    def click_boton_popup(self):
        self.navigate_in_page(self.MOSTRAR_BOTON_POP_UP)
        self.click(self.MOSTRAR_BOTON_POP_UP)


    def get_popup_title_text(self):
        return self.wait_for_element(self.POP_TITLE).text

    def get_cell_value_dinamic(self, fila, columna):
        #celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}/td[{columna}]]"
        celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}]/td[{columna}]"

        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None

    def get_cell_value_static(self, fila, columna):
        #celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}/td[{columna}]]"
        celda_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{fila}]/td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None