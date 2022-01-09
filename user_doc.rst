smamodbus
=====================================================

Das Plugin liest die Daten mithilfe von PyModbus (https://pymodbus.readthedocs.io/en/latest/readme.html) vom Wechselrichter, parst diese und schreibt den Wert in das Item zurück.
Die Angabe im Item erfolgt mit dem Trennzeichen - (Minus) und muss wie folgt aussehen:
<Registeradresse SMA>-<Anzahl zusammenhängender SMA Register>-<Datentyp SMA>
Beispiel: 30005-2-U32

.. important::

	Die Platzhalter entsprechen der Beschreibung in der offiziellen MODBUS Spezfifikation von SMA.
	Spezifikation unter https://www.sma.de/produkte/monitoring-control/modbus-protokoll-schnittstelle.html -> Downloads -> Hintergrundwissen

Anforderungen
-------------
Im zu lesenden Wechselrichter muss die Modbus-Schnittstelle aktiviert werden.

.. important::

	Zur Aktivierung der Schnittstelle ist der Installateur-Zugang für den Wechselrichter notwendig.

Notwendige Software
~~~~~~~~~~~~~~~~~~~

* PyModbus


Unterstützte Geräte
~~~~~~~~~~~~~~~~~~~

* SUNNY ISLAND 4.4M-13
* SUNNY TRIPOWER 8.0


Konfiguration
-------------

plugin.yaml
~~~~~~~~~~~

Bitte die Dokumentation lesen, die aus den Metadaten der plugin.yaml erzeugt wurde.


items.yaml
~~~~~~~~~~

Bitte die Dokumentation lesen, die aus den Metadaten der plugin.yaml erzeugt wurde.


Beispiele
---------

Das folgenden Beispiel zeigt, wie ein PV- und Batteriewechselrichter zusammen gelesen werden können.
Je Wechselrichter muss eine Instanz konfiguriert werden. Die Angabe nach dem @ ist der Instanzname.

.. code:: yaml

	PV:
		Typenschild:
			Seriennummer:
				name: Seriennummer
				type: num
				smamodbus@pv: 30005-2-U32
			Geraeteklasse:
				name: Geräteklasse
				type: num
				smamodbus@pv: 30051-2-U32
			Gereatetype:
				name: Gerätetyp
				type: num
				smamodbus@pv: 30053-2-U32
		Leistung:
			name: Leistung in Watt
			#type: num
			smamodbus@pv: 30775-2-S32
			
			NennleistungOk:
				name: Nennleistung im Zustand Ok
				type: num
				smamodbus@pv: 30203-2-U32
		
		Zustand:
			name: Zustand
			type: num
			smamodbus@pv: 30201-2-U32
		
		Gesamtertrag:
			name: Gesamtertrag
			#type: num
			smamodbus@pv: 30513-4-U64
		Tagesertrag:
			name: Tagesertrag in W
			#type: num
			smamodbus@pv: 30539-2-U32
			
	Batterie:
		Typenschild:
			Seriennummer:
				name: Seriennummer
				type: num
				smamodbus@batterie: 30057-2-U32
				
		Ladezustand:
			name: Aktueller Batterieladezustand
			type: num
			smamodbus@batterie: 30845-2-U32 
