# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot25.PWSlot25 import PWSlot25


class test_PWSlot25(TestCase):
    """Test that the widget PWSlot25 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW25(H1=0.11, H2=0.12, W3=0.14, W4=0.15)
        self.widget = PWSlot25(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot25")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_H2.value(), 0.12)
        self.assertEqual(self.widget.lf_W3.value(), 0.14)
        self.assertEqual(self.widget.lf_W4.value(), 0.15)

        self.test_obj.slot = SlotW25(H1=0.21, H2=0.22, W3=0.24, W4=0.25)
        self.widget = PWSlot25(self.test_obj)
        self.assertEqual(self.widget.lf_H1.value(), 0.21)
        self.assertEqual(self.widget.lf_H2.value(), 0.22)
        self.assertEqual(self.widget.lf_W3.value(), 0.24)
        self.assertEqual(self.widget.lf_W4.value(), 0.25)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.32")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W3, 0.32)
        self.assertEqual(self.test_obj.slot.W3, 0.32)

    def test_set_W4(self):
        """Check that the Widget allow to update W4"""
        self.widget.lf_W4.clear()
        QTest.keyClicks(self.widget.lf_W4, "0.33")
        self.widget.lf_W4.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W4, 0.33)
        self.assertEqual(self.test_obj.slot.W4, 0.33)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, 0.35)
        self.assertEqual(self.test_obj.slot.H1, 0.35)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H2, 0.36)
        self.assertEqual(self.test_obj.slot.H2, 0.36)

    def test_output_txt(self):
        """Check that the Output text is computed and correct
        """
        self.test_obj = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=1,
            Wrvd=0.1,
        )
        self.test_obj.slot = SlotW25(Zs=12, W4=150e-3, W3=75e-3, H1=30e-3, H2=150e-3)
        self.widget = PWSlot25(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.1789 m"
        )
