"""
This file implements a few primitive tests for the configuration framework.

Since the framework itself is quite simple, I skipped elaborate testes and just
implemented one integration test.
"""

from yacf import Configuration, utils

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
            "child": "a",
        },
        "c_b": {
            "parent": "c",
            "child": "b",
        },
    },
}


def assertSectionA(cfg: Configuration):
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


def assertSectionB(cfg: Configuration):
    # Regular access
    assert _default.get("b").get("int_arr") == cfg._get("b").get("int_arr")
    assert _default.get("b").get("bool_arr") == cfg._get("b").get("bool_arr")
    assert _default.get("b").get("string_arr") == cfg._get("b").get("string_arr")

    # dot access
    assert _default.get("b").get("int_arr") == cfg._get("b.int_arr")
    assert _default.get("b").get("bool_arr") == cfg._get("b.bool_arr")
    assert _default.get("b").get("string_arr") == cfg._get("b.string_arr")


def assertSectionC(cfg: Configuration):
    # Regular access
    assert _default.get("c").get("empty") == cfg.get("c").get("empty")
    assert _default.get("c").get("c_a").get("parent") == cfg.get("c").get("c_a").get(
        "parent"
    )
    assert _default.get("c").get("c_a").get("child") == cfg.get("c").get("c_a").get(
        "child"
    )
    assert _default.get("c").get("c_b").get("parent") == cfg.get("c").get("c_b").get(
        "parent"
    )
    assert _default.get("c").get("c_b").get("child") == cfg.get("c").get("c_b").get(
        "child"
    )

    # dot access
    assert _default.get("c").get("empty") == cfg.get("c.empty")
    assert _default.get("c").get("c_a").get("parent") == cfg.get("c.c_a.parent")
    assert _default.get("c").get("c_a").get("child") == cfg.get("c.c_a.child")
    assert _default.get("c").get("c_b").get("parent") == cfg.get("c.c_b.parent")
    assert _default.get("c").get("c_b").get("child") == cfg.get("c.c_b.child")


def main():
    """Main function to test YACF"""

    c_default = Configuration(_default).load()
    c_json = Configuration("data/json.json").load()
    c_toml = Configuration("data/toml.toml").load()

    # assert dict, JSON and TOML is parsed properly
    for c in [c_default, c_json, c_toml]:
        assertSectionA(c_default)
        assertSectionB(c_default)
        assertSectionC(c_default)


if __name__ == "__main__":
    main()
