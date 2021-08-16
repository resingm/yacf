"""
This file implements a few primitive tests for the configuration framework.

Since the framework itself is quite simple, I skipped elaborate testes and just
implemented one integration test.
"""

# standard lib
import traceback
from typing import Union

# first party
from yacf import Configuration

_default = {
    "a": {
        "string_0": "test",
        "int_0": 0,
        "int_1": 1,
        "int_2": -1,
        "bool_0": False,
        "bool_1": True,
    },
    "b": {
        "int_arr": [0, 1, 2],
        "bool_arr": [False, True],
        "string_arr": ["", "filled"],
    },
    "c": {
        "empty": {},
        "c_a": {
            "parent": "c",
            "section": "a",
        },
        "c_b": {
            "parent": "c",
            "section": "b",
        },
    },
}


def assert_section_a(cfg: Union[Configuration, dict]):
    # Regular access
    assert _default.get("a").get("string_0") == cfg.get("a").get("string_0")
    assert _default.get("a").get("int_0") == cfg.get("a").get("int_0")
    assert _default.get("a").get("int_1") == cfg.get("a").get("int_1")
    assert _default.get("a").get("int_2") == cfg.get("a").get("int_2")
    assert _default.get("a").get("bool_0") == cfg.get("a").get("bool_0")
    assert _default.get("a").get("bool_1") == cfg.get("a").get("bool_1")

    # dot access
    assert _default.get("a").get("string_0") == cfg.get("a.string_0")
    assert _default.get("a").get("int_0") == cfg.get("a.int_0")
    assert _default.get("a").get("int_1") == cfg.get("a.int_1")
    assert _default.get("a").get("int_2") == cfg.get("a.int_2")
    assert _default.get("a").get("bool_0") == cfg.get("a.bool_0")
    assert _default.get("a").get("bool_1") == cfg.get("a.bool_1")

    # attribute access
    if isinstance(cfg, Configuration):
        assert _default.get("a").get("string_0") == cfg.a.string_0
        assert _default.get("a").get("int_0") == cfg.a.int_0
        assert _default.get("a").get("int_1") == cfg.a.int_1
        assert _default.get("a").get("int_2") == cfg.a.int_2
        assert _default.get("a").get("bool_0") == cfg.a.bool_0
        assert _default.get("a").get("bool_1") == cfg.a.bool_1


def assert_section_b(cfg: Union[Configuration, dict]):
    # Regular access
    assert _default.get("b").get("int_arr") == cfg.get("b").get("int_arr")
    assert _default.get("b").get("bool_arr") == cfg.get("b").get("bool_arr")
    assert _default.get("b").get("string_arr") == cfg.get("b").get("string_arr")

    # dot access
    assert _default.get("b").get("int_arr") == cfg.get("b.int_arr")
    assert _default.get("b").get("bool_arr") == cfg.get("b.bool_arr")
    assert _default.get("b").get("string_arr") == cfg.get("b.string_arr")

    # attribute access
    if isinstance(cfg, Configuration):
        assert _default.get("b").get("int_arr") == cfg.b.int_arr
        assert _default.get("b").get("bool_arr") == cfg.b.bool_arr
        assert _default.get("b").get("string_arr") == cfg.b.string_arr


def assert_section_c(cfg: Union[Configuration, dict]):
    # Regular access
    assert _default.get("c").get("empty") == cfg.get("c").get("empty")
    assert _default.get("c").get("c_a").get("parent") == cfg.get("c").get("c_a").get(
        "parent"
    )
    assert _default.get("c").get("c_a").get("section") == cfg.get("c").get("c_a").get(
        "section"
    )
    assert _default.get("c").get("c_b").get("parent") == cfg.get("c").get("c_b").get(
        "parent"
    )
    assert _default.get("c").get("c_b").get("section") == cfg.get("c").get("c_b").get(
        "section"
    )

    # dot access
    assert _default.get("c").get("empty") == cfg.get("c.empty")
    assert _default.get("c").get("c_a").get("parent") == cfg.get("c.c_a.parent")
    assert _default.get("c").get("c_a").get("section") == cfg.get("c.c_a.section")
    assert _default.get("c").get("c_b").get("parent") == cfg.get("c.c_b.parent")
    assert _default.get("c").get("c_b").get("section") == cfg.get("c.c_b.section")

    # attribute access
    if isinstance(cfg, Configuration):
        assert _default.get("c").get("empty") == cfg.c.empty
        assert _default.get("c").get("c_a").get("parent") == cfg.c.c_a.parent
        assert _default.get("c").get("c_a").get("section") == cfg.c.c_a.section
        assert _default.get("c").get("c_b").get("parent") == cfg.c.c_b.parent
        assert _default.get("c").get("c_b").get("section") == cfg.c.c_b.section


def assert_default(cfg: Configuration):
    assert _default.get("", "default") == cfg.get("", default="default")


def assert_dict(cfg: Configuration):
    d = cfg.dict()
    assert "a.string_0" in d.keys()
    assert "a.int_0" in d.keys()
    assert "a.int_1" in d.keys()
    assert "a.int_2" in d.keys()
    assert "a.bool_0" in d.keys()
    assert "a.bool_1" in d.keys()

    assert "b.int_arr" in d.keys()
    assert "b.bool_arr" in d.keys()
    assert "b.string_arr" in d.keys()

    assert "c.empty" in d.keys()
    assert "c.c_a" in d.keys()
    assert "c.c_a.parent" in d.keys()
    assert "c.c_a.section" in d.keys()
    assert "c.c_b" in d.keys()
    assert "c.c_b.parent" in d.keys()
    assert "c.c_b.section" in d.keys()

    assert_section_a(d)
    assert_section_b(d)
    assert_section_c(d)


def main():
    """Main function to test YACF"""

    c_default = Configuration(_default).load()
    c_json = Configuration("data/json.json").load()
    c_toml = Configuration("data/toml.toml").load()

    # assert dict, JSON and TOML is parsed properly
    for c in [c_default, c_json, c_toml]:
        assert_section_a(c)
        assert_section_b(c)
        assert_section_c(c)
        assert_default(c)
        assert_dict(c)


if __name__ == "__main__":
    try:
        main()
        print("Test run successful.")
    except Exception as e:
        print(f"Failed tests: {str(e)}")
        traceback.print_exc()
