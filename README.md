># https://github.com/moslog/exam-app

# Exam App with Python

This logic notebook generator was built with python.


```shell
pip3 install examapp
```

```shell
RUN_FILE=/tmp/run.py
printf 'import examapp; examapp.run()' > $RUN_FILE
python3 $RUN_FILE
```

# MAINTAINER NOTE

This is `examapp` folder tree.

<pre>
.
├── __init__.py
├── app
│   ├── __init__.py
│   ├── assets
│   │   ├── _RAW
│   │   │   ├── A
│   │   │   │   ├── LogicPuzzleExamPDF_p001-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p002-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p003-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p004-1.png
│   │   │   │   └── LogicPuzzleExamPDF_p005-1.png
│   │   │   ├── B
│   │   │   │   ├── LogicPuzzleExamPDF_p006-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p007-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p008-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p009-1.png
│   │   │   │   └── LogicPuzzleExamPDF_p010-1.png
│   │   │   ├── C
│   │   │   │   ├── LogicPuzzleExamPDF_p011-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p012-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p013-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p014-1.png
│   │   │   │   └── LogicPuzzleExamPDF_p015-1.png
│   │   │   ├── D
│   │   │   │   ├── LogicPuzzleExamPDF_p016-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p017-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p018-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p019-1.png
│   │   │   │   └── LogicPuzzleExamPDF_p020-1.png
│   │   │   ├── E
│   │   │   │   ├── LogicPuzzleExamPDF_p021-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p022-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p023-1.png
│   │   │   │   ├── LogicPuzzleExamPDF_p024-1.png
│   │   │   │   └── LogicPuzzleExamPDF_p025-1.png
│   │   │   ├── encoder.py
│   │   │   └── resizer.sh
│   │   ├── __init__.py
│   │   ├── qA.b64
│   │   ├── qB.b64
│   │   ├── qC.b64
│   │   ├── qD.b64
│   │   ├── qE.b64
│   │   ├── template.ipynb
│   │   └── template.json
│   ├── lang
│   │   └── __init__.py
│   ├── main.py
│   └── worker
│       ├── __init__.py
│       ├── date.py
│       ├── image.py
│       ├── notebook.py
│       └── writer.py
└── folder_tree.txt
</pre>

Use resizer to resize Image.
