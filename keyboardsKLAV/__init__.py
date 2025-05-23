from .меню import get_main_keyboard
from .механика import get_mechanics_keyboard
from .кинематика import get_kinematics_keyboard
from .прямолинейное_равноускоренное_движение import get_ravnoyskorenoe_keyboard
from .прямолинейное_равномерное_движение import get_ravnomernoe_keyboard
from .свободное_падение import get_svobodnoe_padenie_keyboard
from .движение_по_окружности import get_ravnomernoe_dvizhenie_po_okruzhnosti_keyboard
from .динамика import get_dinamika_keyboard
from .законы_сохранения_в_механике import get_zakony_sohraneniya_keyboard
from .статика import get_statika_keyboard
from .механические_колебания_и_волны import get_mechanicheskie_kolebaniya_i_volny_keyboard
from .молекулярная_физика import get_molekylarn_keyboard
from .термодинамика import get_thermodynamics_keyboard
from .электродинамика import get_electrodynamics_keyboard
from .электрическое_поле import get_electric_field_keyboard
from .законы_постоянного_тока import get_zakon_postoinogo_toka_keyboard
from .магнитное_поле_и_электромагнитная_индукция import get_magnetic_field_and_electromagnetic_induction_keyboard
from .электромагнитные_колебания_и_волны import get_electromagnetic_oscillations_and_waves_keyboard
from .оптика import get_optics_keyboard
from .квантовая_физика import get_quantum_physics_keyboard
from .ядерная_физика import get_nuclear_physics_keyboard

# Добавляем импорты для клавиатур раздела "Экзамены"
from .экзамены import (
    get_exams_type_keyboard,
    get_ege_options_keyboard,
    get_ege_codificator_physics_sections_keyboard,
    get_ege_codificator_mechanics_topics_keyboard
    # TODO: Добавить импорты для других клавиатур по мере их создания
)

