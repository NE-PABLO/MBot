from keyboardsKLAV import (
    get_main_keyboard,
    get_mechanics_keyboard,
    get_kinematics_keyboard,
    get_ravnoyskorenoe_keyboard,
    get_ravnomernoe_keyboard,
    get_svobodnoe_padenie_keyboard,
    get_ravnomernoe_dvizhenie_po_okruzhnosti_keyboard,
    get_dinamika_keyboard,
    get_zakony_sohraneniya_keyboard,
    get_statika_keyboard,
    get_mechanicheskie_kolebaniya_i_volny_keyboard,
    get_molekylarn_keyboard,
    get_thermodynamics_keyboard,
    get_electrodynamics_keyboard,
    get_electric_field_keyboard,
    get_zakon_postoinogo_toka_keyboard,
    get_magnetic_field_and_electromagnetic_induction_keyboard,
    get_electromagnetic_oscillations_and_waves_keyboard,
    get_optics_keyboard,
    get_quantum_physics_keyboard,
    get_nuclear_physics_keyboard,
)

# Импорты для раздела "Экзамены"
from keyboardsKLAV.экзамены import (
    get_exams_type_keyboard,
    get_ege_options_keyboard,
    get_ege_codificator_physics_sections_keyboard,
    # Механика
    get_ege_codificator_mechanics_topics_keyboard,
    get_ege_mechanics_kinematics_formulas_keyboard,
    get_ege_mechanics_dynamics_formulas_keyboard,
    get_ege_mechanics_statics_formulas_keyboard,
    get_ege_mechanics_conservation_laws_formulas_keyboard,
    get_ege_mechanics_oscillations_formulas_keyboard,
    # Молекулярная физика
    get_ege_codificator_molecular_physics_topics_keyboard,
    # get_ege_molecular_mkt_formulas_keyboard, # Пример, если будет такая функция
    # Термодинамика
    get_ege_codificator_thermodynamics_topics_keyboard,
    # get_ege_thermodynamics_internal_energy_formulas_keyboard, # Пример
    # Электродинамика
    get_ege_codificator_electrodynamics_topics_keyboard,
    # get_ege_electrodynamics_electrostatics_formulas_keyboard, # Пример
)

user_states = {}

previous_states = {
    'main': None,
    'search': 'main',
    'mechanics': 'main',
    'kinematics': 'mechanics',
    'ravnoyskorenoe': 'kinematics',
    'ravnomernoe': 'kinematics',
    'dinamika': 'mechanics',
    'svobodnoe_padenie': 'kinematics',
    'ravnomernoe_dvizhenie_po_okruzhnosti': 'kinematics',
    'zakony_sohraneniya': 'mechanics',
    'statika': 'mechanics',
    'mechanicheskie_kolebaniya_i_volny': 'main',
    'molekylarn': 'main',
    'thermodynamics': 'main',
    'electrodynamics': 'main',
    'electric_field': 'electrodynamics',
    'zakon_postoinogo_toka': 'electrodynamics',
    'magnetic_field_and_electromagnetic_induction': 'electrodynamics',
    'electromagnetic_oscillations_and_waves': 'electrodynamics',
    'optics': 'main',
    'quantum_physics': 'main',
    'nuclear_physics': 'main',

    # Состояния для раздела "Экзамены"
    'exams_type_selection': 'main',
    'ege_options': 'exams_type_selection',
    'oge_options': 'exams_type_selection',
    'ege_codificator_physics_sections': 'ege_options',
    
    # Механика (ЕГЭ Кодификатор)
    'ege_codificator_mechanics_topics': 'ege_codificator_physics_sections',
    'ege_mechanics_kinematics_formulas': 'ege_codificator_mechanics_topics',
    'ege_mechanics_dynamics_formulas': 'ege_codificator_mechanics_topics',
    'ege_mechanics_statics_formulas': 'ege_codificator_mechanics_topics',
    'ege_mechanics_conservation_laws_formulas': 'ege_codificator_mechanics_topics',
    'ege_mechanics_oscillations_formulas': 'ege_codificator_mechanics_topics',

    # Молекулярная физика (ЕГЭ Кодификатор)
    'ege_codificator_molecular_topics': 'ege_codificator_physics_sections',
    # 'ege_molecular_mkt_formulas': 'ege_codificator_molecular_topics', # Пример

    # Термодинамика (ЕГЭ Кодификатор)
    'ege_codificator_thermodynamics_topics': 'ege_codificator_physics_sections',
    # 'ege_thermodynamics_internal_energy_formulas': 'ege_codificator_thermodynamics_topics', # Пример

    # Электродинамика (ЕГЭ Кодификатор)
    'ege_codificator_electrodynamics_topics': 'ege_codificator_physics_sections',
    # 'ege_electrodynamics_electrostatics_formulas': 'ege_codificator_electrodynamics_topics', # Пример
}

state_keyboards = {
    'main': lambda: get_main_keyboard(),
    'mechanics': lambda: get_mechanics_keyboard(),
    'kinematics': lambda: get_kinematics_keyboard(),
    'ravnoyskorenoe': lambda: get_ravnoyskorenoe_keyboard(),
    'ravnomernoe': lambda: get_ravnomernoe_keyboard(),
    'dinamika': lambda: get_dinamika_keyboard(),
    'svobodnoe_padenie': lambda: get_svobodnoe_padenie_keyboard(),
    'ravnomernoe_dvizhenie_po_okruzhnosti': lambda: get_ravnomernoe_dvizhenie_po_okruzhnosti_keyboard(),
    'zakony_sohraneniya': lambda: get_zakony_sohraneniya_keyboard(),
    'statika': lambda: get_statika_keyboard(),
    'mechanicheskie_kolebaniya_i_volny': lambda: get_mechanicheskie_kolebaniya_i_volny_keyboard(),
    'molekylarn': lambda: get_molekylarn_keyboard(),
    'thermodynamics': lambda: get_thermodynamics_keyboard(),
    'electrodynamics': lambda: get_electrodynamics_keyboard(),
    'electric_field': lambda: get_electric_field_keyboard(),
    'zakon_postoinogo_toka': lambda: get_zakon_postoinogo_toka_keyboard(),
    'magnetic_field_and_electromagnetic_induction': lambda: get_magnetic_field_and_electromagnetic_induction_keyboard(),
    'electromagnetic_oscillations_and_waves': lambda: get_electromagnetic_oscillations_and_waves_keyboard(),
    'optics': lambda: get_optics_keyboard(),
    'quantum_physics': lambda: get_quantum_physics_keyboard(),
    'nuclear_physics': lambda: get_nuclear_physics_keyboard(),

    # Клавиатуры для раздела "Экзамены"
    'exams_type_selection': lambda: get_exams_type_keyboard(),
    'ege_options': lambda: get_ege_options_keyboard(),
    'ege_codificator_physics_sections': lambda: get_ege_codificator_physics_sections_keyboard(),

    # Механика (ЕГЭ Кодификатор)
    'ege_codificator_mechanics_topics': lambda: get_ege_codificator_mechanics_topics_keyboard(),
    'ege_mechanics_kinematics_formulas': lambda: get_ege_mechanics_kinematics_formulas_keyboard(),
    'ege_mechanics_dynamics_formulas': lambda: get_ege_mechanics_dynamics_formulas_keyboard(),
    'ege_mechanics_statics_formulas': lambda: get_ege_mechanics_statics_formulas_keyboard(),
    'ege_mechanics_conservation_laws_formulas': lambda: get_ege_mechanics_conservation_laws_formulas_keyboard(),
    'ege_mechanics_oscillations_formulas': lambda: get_ege_mechanics_oscillations_formulas_keyboard(),

    # Молекулярная физика (ЕГЭ Кодификатор)
    'ege_codificator_molecular_topics': lambda: get_ege_codificator_molecular_physics_topics_keyboard(),
    # 'ege_molecular_mkt_formulas': lambda: get_ege_molecular_mkt_formulas_keyboard(), # Пример

    # Термодинамика (ЕГЭ Кодификатор)
    'ege_codificator_thermodynamics_topics': lambda: get_ege_codificator_thermodynamics_topics_keyboard(),
    # 'ege_thermodynamics_internal_energy_formulas': lambda: get_ege_thermodynamics_internal_energy_formulas_keyboard(), # Пример

    # Электродинамика (ЕГЭ Кодификатор)
    'ege_codificator_electrodynamics_topics': lambda: get_ege_codificator_electrodynamics_topics_keyboard(),
    # 'ege_electrodynamics_electrostatics_formulas': lambda: get_ege_electrodynamics_electrostatics_formulas_keyboard(), # Пример
}

user_state_stack = {}

def collect_search_keywords():
    keywords = []
    for state_func in state_keyboards.values():
        keyboard = state_func()
        if keyboard is not None and hasattr(keyboard, 'keyboard'):
            for row in keyboard.keyboard:
                for button in row:
                    # Исключаем системные кнопки и кнопки верхнего уровня навигации экзаменов
                    excluded_texts = ['Назад', 'Главное меню', 'Поиск', '🎤 Ваш мега-коммент', 'Экзамены', 'ЕГЭ', 'ОГЭ', 'Кодификатор ЕГЭ']
                    # Также исключаем общие названия разделов кодификатора, если они не являются конечными узлами для поиска
                    if button.text not in excluded_texts and not button.text.endswith('(ЕГЭ Кодификатор)'):
                        if button.text not in keywords:
                            keywords.append(button.text)
    return list(set(keywords))

SEARCH_KEYWORDS = collect_search_keywords()

