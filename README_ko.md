## 이 리포지토리에 대하여

이 리포지토리는 Satanarious가 만든 [TransparentFlyoutsConfig](https://github.com/Satanarious/TransparentFlyoutsConfig)의 포크입니다. <br>
저는 한국어 지원을 추가하기 위해 Satanarious의 [번역 기여 가이드](https://github.com/Satanarious/TransparentFlyoutsConfig#translation-contribution)를 참고해 만들었습니다. <br>

이하 내용은 오리지널 리포지토리의 README입니다.

---
<br>

<img src="Screenshots/banner.png">
<img src="Screenshots/language_and_description_spread.png" align="right" width=450>

**Translucent Flyouts Config GUI**는 Windows 10/11용 [Translucent Flyouts](https://github.com/ALTaleX531/TranslucentFlyouts)와 함께 사용하는 애플리케이션으로, windows32 스타일 컨텍스트 메뉴에 대한 다양한 사용자 커스터마이징을 가능하게 합니다.

목차:

- [설치 지침](#설치-지침)
- [사용 지침](#사용-지침)
- [번역 기여](#번역-기여)
- [추가 예정 기능](#추가-예정-기능)
- [의존성 (Dependencies)](#의존성-(Dependencies))
- [면책 조항](#면책-조항)
- [라이선스](#라이선스)

## 설치 지침

> 최신 버전의 [Translucent Flyouts](https://github.com/ALTaleX531/TranslucentFlyouts/releases/latest)를 이미 설치한 상태여야합니다.

- [최신 릴리즈](https://github.com/Satanarious/TransparentFlyoutsConfigGUI/releases/latest)를 다운로드합니다.
- 모든 파일을 디랙토리/폴더 형태로 압축 해제하세요.
- `TranslucentFlyoutsConfig.exe` 파일을 실행하세요.

## 사용 지침

<img src="Screenshots/all_tabs_spread.png" align="right" width=300>

- 설정의 맨 오른쪽에 있는 초기화 버튼을 마우스 왼쪽 버튼으로 클릭하면 값이 기본값으로 재설정됩니다.
- 설정의 맨 오른쪽에 있는 초기화 버튼을 마우스 오른쪽 버튼으로 클릭하면 값이 마지막으로 지정된 값으로 재설정됩니다.
- 색상 선택기를 사용해 색상과 투명도 값을 선택합니다.
- 매개변수 라벨을 클릭하면 사용 가능한 값과 해당 설명을 볼 수 있습니다.
- 모든 변경사항은 해당 섹션의 적용 버튼을 누름과 동시에 적용됩니다.
- 우상단읜 닫기 버튼 옆에 있는 설정 아이콘을 클릭해 언어를 변경할 수 있습니다.

## 번역 기여

이 프로젝트에 추가할 수 있는 언어를 기여할 수 있습니다. 번역에 기여하기 전 [이 번역 파일](Translations/hi-in.json)을 참고하세요.

처음 기여하는 경우 다음 단계를 따르세요:

- 리포지토리를 포크합니다.
- `LanguageCode-CountryCode.json` 이름 규칙을 사용하여 [Translations 디랙토리](Translations/)에 파일을 생성합니다. (파일 이름은 전부 소문자여야 합니다)
- [hi-in.json](Translations/hi-in.json)의 모든 것을 복사하고 새 파일에 붙여넣습니다.
- 각 영어에 대한 힌디어 번역을 지우고 기여 할 언어로 번역합니다.

> 주의: `<code>`로 끝나는 문장과 `</code>`로 시작하는 문장이 있으니, 없애지 않도록 주의하십시오. 그렇지 않으면 코드가 망가질 것입니다.
> 해당 문장:
>
> - `"Uses the corresponding value in the global tab as the <code>"`
> - `"</code> value."`

한 발자국 더 나아가 파이썬으로 수정할 것이라면, 이것을 참고하세요:

- Open [Data/enum.py](Data/enums.py) and add an additional value to the class ` Languages`.
- Open [Data/paths.py](Data/paths.py) and under class `Translations` add the path to you translation path in the exact as mentioned there for the previously mentioned language(s).
- Open [Data/translations.py](Data/translations.py) and under class `TranslationModel`, under method `_fetch()`, find a dictionary `translationPath` and add another pair in the format `LanguageEnum:LanguageJSONPathVariable`
- Open [Widget/settings_widget.py](Widget/settings_widget.py) and under method `__init__` you will find a line which says `self.languageComboBox.addItems` with a list of language names in their own languages. Add one for the one you are adding.

> 참고 1: 번역 파일만을 작성할 것이라면, 제가 풀 리퀘스트를 받아 두번째 작업을 수행하겠습니다. 그러나 두번째 작업도 해주시면 감사하겠습니다.

> 참고 2: 현재 글꼴이 지원되지 않는 언어에 대해서는 글꼴을 수정하지 않겠습니다. 나중에 더 많은 글꼴을 추가하겠습니다.

## 추가 예정 기능

[추적기 (tracker)](https://github.com/users/Satanarious/projects/2/views/2)를 통해 자세한 내용을 확인하세요.
<img src="Screenshots/theme_tease.png" align=right width=50%>

- [x] 번역 지원
- [x] 더 나은 파라미터 설명
- [ ] 미지원 언어를 위한 글꼴 추가
- [ ] 인앱 테마 지원
- [ ] Translucent Flyouts의 내부 기능 지원:
  - [ ] 다시 시작
  - [ ] 정지
  - [ ] 설치
  - [ ] 삭제
- [ ] UI 애니메이션
- [ ] 적용 전 빠른 미리보기를 위한 미리보기 창
- [ ] 최신 버전의 Translucent Flyouts 설치 및 업데이트
- [ ] Microsoft Store 및/또는 Winget에 추가

## 의존성 (Dependencies)

### [TranslucentFlyouts](https://github.com/ALTaleX531/TranslucentFlyouts)

An application that makes most of the win32 popup menus translucent/transparent on Windows 10/11, providing more options to tweak it to meet your need.

### [PyQT6](https://www.riverbankcomputing.com/software/pyqt/)

PyQt is a set of Python bindings for The Qt Company's Qt application framework and runs on all platforms supported by Qt including Windows, macOS, Linux, iOS and Android. Documentations can be found [here](https://doc.qt.io/qtforpython-6/).

### [PyInstaller](https://pyinstaller.org/en/stable/)

PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.7 and newer, and correctly bundles many major Python packages such as numpy, matplotlib, PyQt, wxPython, and others.

### [VColorPicker](https://github.com/nlfmt/pyqt-colorpicker)

VColorPicker is a simple visual Color Picker with a modern UI created with Qt to easily get color input from the user.

### [Tick icon by Freepik - Flaticon](https://www.flaticon.com/free-icons/tick)

The Tick icon included in the application, which appears when the user clicks the apply button is designed by Freepik - Flaticon

## 면책 조항

This application contains everything necessary to be known and understood about configuring the appearance of context menus without the need to refer to the previously mentioned Config file.

> Note: This application just serves as a GUI to eliminate any kind of registry editing, required by the previously mentioned application to configure the appearnce of context menus. This is not a standalone application and is required to be used alongside [Translucent Flyouts](https://github.com/ALTaleX531/TranslucentFlyouts)

Take a look at the [Config File](https://github.com/ALTaleX531/TranslucentFlyouts/blob/master/CONFIG.md) which provides description as well as methods to configure various aspects of the windows32 style context menus. Though some features are restricted to Windows 11 due to the absence of Mica on Windows 10.

## 라이선스

이 소프트웨어는 GNU GPL v3.0 라이선스에 따라 라이선스가 부여됩니다.<br>
자세한 내용은 전용 [라이선스](https://github.com/Satanarious/TransparentFlyoutsConfig/blob/master/LICENSE) 파일에서 제공됩니다.
