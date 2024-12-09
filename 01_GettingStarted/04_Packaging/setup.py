from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Nếu có dependencies, thêm vào đây
    entry_points={
        'console_scripts': [
            'run-mypackage = main:main',  # Tạo lệnh để chạy package
        ],
    },
    python_requires='>=3.6',  # Đảm bảo phiên bản Python tối thiểu
)
