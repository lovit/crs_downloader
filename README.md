# Congressional Research Service Reports downloader

Congressional Research Service Reports 에서 제공하는 pdf 형식의 reports 를 다운로드 받는 Python script 입니다.

```python
python download.py --debug --directory ./output/ --sleep 1.0
```

위 스크립트는 output 폴더에 각 주제별로의 reports 를 저장합니다.

`homesec-IN10890.pdf` 파일은 `homesec` category 의 `IN10890.pdf` 파일입니다.

Category code 와 설명은 아래와 같습니다.

| Category name | Category code |
| --- | --- |
| General National Security Topics | natsec |
| Defense Primers | natsec |
| Middle East | mideast |
| Foreign Policy and Regional Affairs | row |
| Secrecy and Information Policy | secrecy |
| Intelligence | intel |
| Homeland Security | homesec |
| Nuclear Weapons and Arms Control | nuke |
| Conventional Weapons Systems | weapons |
| Terrorism | terror |
| Miscellaneous Topics | misc |

