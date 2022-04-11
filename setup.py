from setuptools import setup

setup(
    name="auth0-integration",
    use_scm_version=True,
    license="BSD",
    description="Django auth0 integration for custom account management.",
    author="Jacco Broeren",
    author_email="jaccobroeren@freedom.nl",
    url="https://github.com/F2210/auth0_integration",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Django",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.7",
    install_requires=["django>=4.0", "python-jose", "sentry_sdk"],
    setup_requires=["setuptools_scm"],
    zip_safe=False,
    include_package_data=True,
)