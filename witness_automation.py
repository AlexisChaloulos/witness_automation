# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)]
# From type library 'Witness.exe'
# On Wed Nov  1 14:09:27 2023
'SIMBA 5.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x3090cf0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{CC0C94B7-C9B9-11D3-99E2-00AA005D7B9B}')
MajorVersion = 5
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	ActionOnExistingFileAppend    =3          # from enum ActionOnExistingFileEnum
	ActionOnExistingFileOverwrite =2          # from enum ActionOnExistingFileEnum
	ActionOnExistingFilePrompt    =1          # from enum ActionOnExistingFileEnum
	ActionOnExistingFileRunWithNoOutput=4          # from enum ActionOnExistingFileEnum
	ArrowArc                      =4          # from enum ArrowStyleEnum
	ArrowDiamond                  =3          # from enum ArrowStyleEnum
	ArrowLines                    =2          # from enum ArrowStyleEnum
	ArrowNone                     =0          # from enum ArrowStyleEnum
	ArrowSingleLine               =5          # from enum ArrowStyleEnum
	ArrowSolid                    =1          # from enum ArrowStyleEnum
	AttributeTypeInteger          =1          # from enum AttributeTypeEnum
	AttributeTypeName             =6          # from enum AttributeTypeEnum
	AttributeTypeReal             =0          # from enum AttributeTypeEnum
	AttributeTypeString           =2          # from enum AttributeTypeEnum
	BreakdownOnAvailableTime      =1          # from enum BreakdownOnEnum
	BreakdownOnBusyTime           =2          # from enum BreakdownOnEnum
	BreakdownOnNumberOfOperations =3          # from enum BreakdownOnEnum
	BreakdownOnTrigger            =4          # from enum BreakdownOnEnum
	NoBreakdown                   =0          # from enum BreakdownOnEnum
	BreakdownStateActive          =2          # from enum BreakdownStateEnum
	BreakdownStateInactive        =1          # from enum BreakdownStateEnum
	BreakdownStateWaitingForLabor =3          # from enum BreakdownStateEnum
	BufferMaximumDelay            =2          # from enum BufferDelayModeEnum
	BufferMinimumAndMaximumDelay  =3          # from enum BufferDelayModeEnum
	BufferMinimumDelay            =1          # from enum BufferDelayModeEnum
	BufferNoDelay                 =0          # from enum BufferDelayModeEnum
	BufferRepeatedMaximumDelay    =4          # from enum BufferDelayModeEnum
	BufferRepeatedMinimumAndMaximumDelay=5          # from enum BufferDelayModeEnum
	BufferEllipse                 =26         # from enum BufferDisplayTypeEnum
	BufferExpression              =11         # from enum BufferDisplayTypeEnum
	BufferIcon                    =0          # from enum BufferDisplayTypeEnum
	BufferLaborQueue              =5          # from enum BufferDisplayTypeEnum
	BufferLine                    =24         # from enum BufferDisplayTypeEnum
	BufferName                    =1          # from enum BufferDisplayTypeEnum
	BufferNotes                   =7          # from enum BufferDisplayTypeEnum
	BufferPartQueue               =2          # from enum BufferDisplayTypeEnum
	BufferPath                    =43         # from enum BufferDisplayTypeEnum
	BufferRectangle               =25         # from enum BufferDisplayTypeEnum
	BufferText                    =6          # from enum BufferDisplayTypeEnum
	BufferInputAtFront            =1          # from enum BufferInputModeModeEnum
	BufferInputAtPosition         =2          # from enum BufferInputModeModeEnum
	BufferInputAtRear             =0          # from enum BufferInputModeModeEnum
	BufferInputByAttributeAscending=3          # from enum BufferInputModeModeEnum
	BufferInputByAttributeDescending=4          # from enum BufferInputModeModeEnum
	BufferOutputAtAnyPosition     =2          # from enum BufferOutputModeModeEnum
	BufferOutputByCondition       =3          # from enum BufferOutputModeModeEnum
	BufferOutputByMaximum         =4          # from enum BufferOutputModeModeEnum
	BufferOutputByMinimum         =5          # from enum BufferOutputModeModeEnum
	BufferOutputFromFront         =0          # from enum BufferOutputModeModeEnum
	BufferOutputFromRear          =1          # from enum BufferOutputModeModeEnum
	BufferStateEmpty              =1          # from enum BufferStateEnum
	BufferStateFull               =3          # from enum BufferStateEnum
	BufferStateOffShift           =0          # from enum BufferStateEnum
	BufferStatePartiallyFull      =2          # from enum BufferStateEnum
	CarrierEllipse                =26         # from enum CarrierDisplayTypeEnum
	CarrierExpression             =11         # from enum CarrierDisplayTypeEnum
	CarrierIcon                   =0          # from enum CarrierDisplayTypeEnum
	CarrierLine                   =24         # from enum CarrierDisplayTypeEnum
	CarrierName                   =1          # from enum CarrierDisplayTypeEnum
	CarrierNotes                  =7          # from enum CarrierDisplayTypeEnum
	CarrierRectangle              =25         # from enum CarrierDisplayTypeEnum
	CarrierText                   =6          # from enum CarrierDisplayTypeEnum
	CarrierStateBlocked           =1          # from enum CarrierStateEnum
	CarrierStateDriveBrokendown   =6          # from enum CarrierStateEnum
	CarrierStateFreeOnSection     =7          # from enum CarrierStateEnum
	CarrierStateLoading           =3          # from enum CarrierStateEnum
	CarrierStateMoving            =5          # from enum CarrierStateEnum
	CarrierStateOffShift          =0          # from enum CarrierStateEnum
	CarrierStateOutsideModel      =8          # from enum CarrierStateEnum
	CarrierStateParked            =2          # from enum CarrierStateEnum
	CarrierStateParking           =9          # from enum CarrierStateEnum
	CarrierStateProcessing        =11         # from enum CarrierStateEnum
	CarrierStateUnloading         =4          # from enum CarrierStateEnum
	CarrierStateUnparking         =10         # from enum CarrierStateEnum
	ConveyorEllipse               =26         # from enum ConveyorDisplayTypeEnum
	ConveyorExpression            =11         # from enum ConveyorDisplayTypeEnum
	ConveyorIcon                  =0          # from enum ConveyorDisplayTypeEnum
	ConveyorLaborQueue            =5          # from enum ConveyorDisplayTypeEnum
	ConveyorLine                  =24         # from enum ConveyorDisplayTypeEnum
	ConveyorName                  =1          # from enum ConveyorDisplayTypeEnum
	ConveyorNotes                 =7          # from enum ConveyorDisplayTypeEnum
	ConveyorPartQueue             =2          # from enum ConveyorDisplayTypeEnum
	ConveyorPath                  =43         # from enum ConveyorDisplayTypeEnum
	ConveyorRectangle             =25         # from enum ConveyorDisplayTypeEnum
	ConveyorText                  =6          # from enum ConveyorDisplayTypeEnum
	ConveyorStateBlocked          =3          # from enum ConveyorStateEnum
	ConveyorStateBrokendown       =5          # from enum ConveyorStateEnum
	ConveyorStateEmpty            =1          # from enum ConveyorStateEnum
	ConveyorStateMovingAndQueued  =4          # from enum ConveyorStateEnum
	ConveyorStateMovingFreely     =2          # from enum ConveyorStateEnum
	ConveyorStateOffShift         =0          # from enum ConveyorStateEnum
	ConveyorStateRestarting       =6          # from enum ConveyorStateEnum
	ConveyorStateWaitingForLaborToRepairFromPath=7          # from enum ConveyorStateEnum
	ConveyorStateWaitingForLaborToTakePartsFromPath=8          # from enum ConveyorStateEnum
	ConveyorTypeFixed             =0          # from enum ConveyorTypeEnum
	ConveyorTypeFixedContinuous   =16         # from enum ConveyorTypeEnum
	ConveyorTypeQueuing           =1          # from enum ConveyorTypeEnum
	ConveyorTypeQueuingContinuous =17         # from enum ConveyorTypeEnum
	DataTableColumnTypeInteger    =1          # from enum DataTableColumnTypeEnum
	DataTableColumnTypeName       =6          # from enum DataTableColumnTypeEnum
	DataTableColumnTypeReal       =0          # from enum DataTableColumnTypeEnum
	DataTableColumnTypeString     =2          # from enum DataTableColumnTypeEnum
	DataTableConnectionErrorHandlingCancelDataTransfer=4          # from enum DataTableConnectionErrorHandlingEnum
	DataTableConnectionErrorHandlingReplaceWithDefaultValue=1          # from enum DataTableConnectionErrorHandlingEnum
	DataTableConnectionErrorHandlingSkipRow=2          # from enum DataTableConnectionErrorHandlingEnum
	DataTableConnectionErrorHandlingStopDataTransfer=3          # from enum DataTableConnectionErrorHandlingEnum
	DataTableConnectionTypeCSV    =1          # from enum DataTableConnectionTypeEnum
	DataTableConnectionTypeDatabase=3          # from enum DataTableConnectionTypeEnum
	DataTableConnectionTypeExcel  =2          # from enum DataTableConnectionTypeEnum
	DataTableConnectionTypeNone   =0          # from enum DataTableConnectionTypeEnum
	DataTableUpdateIntervalExpression=1          # from enum DataTableDisplayUpdateIntervalModeEnum
	DataTableUpdateIntervalImmediate=2          # from enum DataTableDisplayUpdateIntervalModeEnum
	DataTableUpdateIntervalModelStop=0          # from enum DataTableDisplayUpdateIntervalModeEnum
	DataTableIOTypeInput          =1          # from enum DataTableIOTypeEnum
	DataTableIOTypeOutput         =2          # from enum DataTableIOTypeEnum
	Friday                        =5          # from enum DayOfTheWeekEnum
	Monday                        =1          # from enum DayOfTheWeekEnum
	Saturday                      =6          # from enum DayOfTheWeekEnum
	Sunday                        =0          # from enum DayOfTheWeekEnum
	Thursday                      =4          # from enum DayOfTheWeekEnum
	Tuesday                       =2          # from enum DayOfTheWeekEnum
	Wednesday                     =3          # from enum DayOfTheWeekEnum
	DetailReportingModeDetail     =1          # from enum DetailReportingModeEnum
	DetailReportingModeGroup      =0          # from enum DetailReportingModeEnum
	DetailReportingModeNone       =2          # from enum DetailReportingModeEnum
	ElementTypeAttribute          =12         # from enum ElementTypeEnum
	ElementTypeBackDrop           =28         # from enum ElementTypeEnum
	ElementTypeBuffer             =4          # from enum ElementTypeEnum
	ElementTypeCarrier            =33         # from enum ElementTypeEnum
	ElementTypeConveyor           =3          # from enum ElementTypeEnum
	ElementTypeDataTable          =38         # from enum ElementTypeEnum
	ElementTypeDistribution       =10         # from enum ElementTypeEnum
	ElementTypeFile               =14         # from enum ElementTypeEnum
	ElementTypeFluid              =19         # from enum ElementTypeEnum
	ElementTypeFunction           =13         # from enum ElementTypeEnum
	ElementTypeHistogram          =9          # from enum ElementTypeEnum
	ElementTypeLabor              =5          # from enum ElementTypeEnum
	ElementTypeMachine            =2          # from enum ElementTypeEnum
	ElementTypeModule             =27         # from enum ElementTypeEnum
	ElementTypeNetwork            =30         # from enum ElementTypeEnum
	ElementTypePart               =1          # from enum ElementTypeEnum
	ElementTypePartFile           =15         # from enum ElementTypeEnum
	ElementTypePath               =34         # from enum ElementTypeEnum
	ElementTypePiechart           =26         # from enum ElementTypeEnum
	ElementTypePipe               =20         # from enum ElementTypeEnum
	ElementTypeProcessor          =21         # from enum ElementTypeEnum
	ElementTypeSection            =31         # from enum ElementTypeEnum
	ElementTypeShift              =25         # from enum ElementTypeEnum
	ElementTypeStation            =32         # from enum ElementTypeEnum
	ElementTypeTank               =22         # from enum ElementTypeEnum
	ElementTypeTimeseries         =8          # from enum ElementTypeEnum
	ElementTypeTrack              =6          # from enum ElementTypeEnum
	ElementTypeVariable           =11         # from enum ElementTypeEnum
	ElementTypeVehicle            =7          # from enum ElementTypeEnum
	ExpressionTypeInteger         =1          # from enum ExpressionTypeEnum
	ExpressionTypeName            =3          # from enum ExpressionTypeEnum
	ExpressionTypeReal            =0          # from enum ExpressionTypeEnum
	ExpressionTypeString          =2          # from enum ExpressionTypeEnum
	FileModeRead                  =0          # from enum FileModeEnum
	FileModeWrite                 =1          # from enum FileModeEnum
	FileTypeDesigner              =4          # from enum FileTypeEnum
	FileTypeModel                 =0          # from enum FileTypeEnum
	FileTypeModelAndStatus        =1          # from enum FileTypeEnum
	FileTypeModelLibrary          =2          # from enum FileTypeEnum
	FileTypeState                 =6          # from enum FileTypeEnum
	FileTypeWCL                   =3          # from enum FileTypeEnum
	FileTypeXML                   =7          # from enum FileTypeEnum
	FileTypeXMLModule             =8          # from enum FileTypeEnum
	FillStyleBDiagonal            =3          # from enum FillStyleEnum
	FillStyleCross                =5          # from enum FillStyleEnum
	FillStyleDiagonalCross        =6          # from enum FillStyleEnum
	FillStyleFDiagonal            =4          # from enum FillStyleEnum
	FillStyleHollow               =0          # from enum FillStyleEnum
	FillStyleHorizontal           =2          # from enum FillStyleEnum
	FillStyleSolid                =1          # from enum FillStyleEnum
	FillStyleVertical             =7          # from enum FillStyleEnum
	FontStyleBold                 =1          # from enum FontStyleEnum
	FontStyleBoldItalic           =3          # from enum FontStyleEnum
	FontStyleItalic               =2          # from enum FontStyleEnum
	FontStyleRegular              =0          # from enum FontStyleEnum
	FunctionParameterTypeInteger  =0          # from enum FunctionParameterTypeEnum
	FunctionParameterTypeName     =3          # from enum FunctionParameterTypeEnum
	FunctionParameterTypeReal     =1          # from enum FunctionParameterTypeEnum
	FunctionParameterTypeString   =2          # from enum FunctionParameterTypeEnum
	FunctionTypeInteger           =0          # from enum FunctionTypeEnum
	FunctionTypeName              =2          # from enum FunctionTypeEnum
	FunctionTypeReal              =1          # from enum FunctionTypeEnum
	FunctionTypeString            =3          # from enum FunctionTypeEnum
	FunctionTypeVoid              =4          # from enum FunctionTypeEnum
	LaborStateBusy                =2          # from enum LaborStateEnum
	LaborStateBusyOffShift        =3          # from enum LaborStateEnum
	LaborStateIdle                =1          # from enum LaborStateEnum
	MachineEllipse                =26         # from enum MachineDisplayTypeEnum
	MachineExpression             =11         # from enum MachineDisplayTypeEnum
	MachineIcon                   =0          # from enum MachineDisplayTypeEnum
	MachineInputBufferQueue       =3          # from enum MachineDisplayTypeEnum
	MachineLaborQueue             =5          # from enum MachineDisplayTypeEnum
	MachineLine                   =24         # from enum MachineDisplayTypeEnum
	MachineName                   =1          # from enum MachineDisplayTypeEnum
	MachineNotes                  =7          # from enum MachineDisplayTypeEnum
	MachineOutputBufferQueue      =4          # from enum MachineDisplayTypeEnum
	MachinePartQueue              =2          # from enum MachineDisplayTypeEnum
	MachineRectangle              =25         # from enum MachineDisplayTypeEnum
	MachineText                   =6          # from enum MachineDisplayTypeEnum
	OutputFromAny                 =5          # from enum MachineOutputPositionEnum
	OutputFromFront               =1          # from enum MachineOutputPositionEnum
	MachineStateBeingRepaired     =5          # from enum MachineStateEnum
	MachineStateBlocked           =3          # from enum MachineStateEnum
	MachineStateBusy              =2          # from enum MachineStateEnum
	MachineStateEmptying          =10         # from enum MachineStateEnum
	MachineStateFilling           =9          # from enum MachineStateEnum
	MachineStateOffShift          =0          # from enum MachineStateEnum
	MachineStateSettingUp         =4          # from enum MachineStateEnum
	MachineStateWaitingForLaborToCarryPart=18         # from enum MachineStateEnum
	MachineStateWaitingForLaborToCycle=6          # from enum MachineStateEnum
	MachineStateWaitingForLaborToCycleFromPath=15         # from enum MachineStateEnum
	MachineStateWaitingForLaborToRepair=8          # from enum MachineStateEnum
	MachineStateWaitingForLaborToRepairFromPath=17         # from enum MachineStateEnum
	MachineStateWaitingForLaborToSetup=7          # from enum MachineStateEnum
	MachineStateWaitingForLaborToSetupFromPath=16         # from enum MachineStateEnum
	MachineStateWaitingForParts   =1          # from enum MachineStateEnum
	MachineStateWaitingForPartsFromPath=14         # from enum MachineStateEnum
	MachineTypeAssembly           =3          # from enum MachineTypeEnum
	MachineTypeBatch              =2          # from enum MachineTypeEnum
	MachineTypeGeneral            =5          # from enum MachineTypeEnum
	MachineTypeMultipleCycle      =7          # from enum MachineTypeEnum
	MachineTypeMultipleStation    =6          # from enum MachineTypeEnum
	MachineTypeProduction         =4          # from enum MachineTypeEnum
	MachineTypeSingle             =1          # from enum MachineTypeEnum
	ModelEventFlagAll             =-1         # from enum ModelEventFlagsEnum
	ModelEventFlagBatch           =128        # from enum ModelEventFlagsEnum
	ModelEventFlagBegin           =8          # from enum ModelEventFlagsEnum
	ModelEventFlagEndEvent        =4096       # from enum ModelEventFlagsEnum
	ModelEventFlagHeartBeat       =8192       # from enum ModelEventFlagsEnum
	ModelEventFlagLoad            =2          # from enum ModelEventFlagsEnum
	ModelEventFlagNew             =1          # from enum ModelEventFlagsEnum
	ModelEventFlagPause           =512        # from enum ModelEventFlagsEnum
	ModelEventFlagPostAddElement  =16384      # from enum ModelEventFlagsEnum
	ModelEventFlagPreDeleteElement=32768      # from enum ModelEventFlagsEnum
	ModelEventFlagQuantityChanged =65536      # from enum ModelEventFlagsEnum
	ModelEventFlagResume          =1024       # from enum ModelEventFlagsEnum
	ModelEventFlagRun             =64         # from enum ModelEventFlagsEnum
	ModelEventFlagSave            =4          # from enum ModelEventFlagsEnum
	ModelEventFlagSimbaTrigger    =2048       # from enum ModelEventFlagsEnum
	ModelEventFlagStep            =32         # from enum ModelEventFlagsEnum
	ModelEventFlagStop            =16         # from enum ModelEventFlagsEnum
	ModelEventFlagTimeUpdate      =256        # from enum ModelEventFlagsEnum
	ModuleStateEmpty              =0          # from enum ModuleStateEnum
	ModuleStateNotEmpty           =1          # from enum ModuleStateEnum
	NetworkStateOffShift          =0          # from enum NetworkStateEnum
	NetworkStateRunning           =1          # from enum NetworkStateEnum
	NetworkSectionPowered         =0          # from enum NetworkTypeEnum
	NetworkSelfPowered            =1          # from enum NetworkTypeEnum
	PartArrivalTypeActive         =1          # from enum PartArrivalTypeEnum
	PartArrivalTypePassive        =0          # from enum PartArrivalTypeEnum
	PartArrivalTypeWithProfile    =2          # from enum PartArrivalTypeEnum
	PartEllipse                   =26         # from enum PartDisplayTypeEnum
	PartExpression                =11         # from enum PartDisplayTypeEnum
	PartIcon                      =0          # from enum PartDisplayTypeEnum
	PartLine                      =24         # from enum PartDisplayTypeEnum
	PartName                      =1          # from enum PartDisplayTypeEnum
	PartNotes                     =7          # from enum PartDisplayTypeEnum
	PartRectangle                 =25         # from enum PartDisplayTypeEnum
	PartStyle                     =37         # from enum PartDisplayTypeEnum
	PartText                      =6          # from enum PartDisplayTypeEnum
	PartProfileTimeDay12Hour      =1          # from enum PartProfileTimeEnum
	PartProfileTimeDay24Hour      =0          # from enum PartProfileTimeEnum
	PartProfileTimeDay8Hour       =2          # from enum PartProfileTimeEnum
	PartProfileTimeHours          =3          # from enum PartProfileTimeEnum
	PartProfileTimeMinutes        =4          # from enum PartProfileTimeEnum
	PartProfileTimeSimulationTime =5          # from enum PartProfileTimeEnum
	PathEllipse                   =26         # from enum PathDisplayTypeEnum
	PathExpression                =11         # from enum PathDisplayTypeEnum
	PathIcon                      =0          # from enum PathDisplayTypeEnum
	PathLine                      =24         # from enum PathDisplayTypeEnum
	PathName                      =1          # from enum PathDisplayTypeEnum
	PathNotes                     =7          # from enum PathDisplayTypeEnum
	PathPath                      =43         # from enum PathDisplayTypeEnum
	PathRectangle                 =25         # from enum PathDisplayTypeEnum
	PathText                      =6          # from enum PathDisplayTypeEnum
	PathStateBusy                 =2          # from enum PathStateEnum
	PathStateIdle                 =1          # from enum PathStateEnum
	PipeCleaningPurging           =2          # from enum PipeStateEnum
	PipeFlowingNormally           =1          # from enum PipeStateEnum
	PipeOffShift                  =0          # from enum PipeStateEnum
	PipeStopped                   =3          # from enum PipeStateEnum
	PipeWaitingResourcesCleanPurge=5          # from enum PipeStateEnum
	PipeWaitingResourcesFlow      =4          # from enum PipeStateEnum
	PipeWaitingResourcesResume    =6          # from enum PipeStateEnum
	ProcessorCleaning             =4          # from enum ProcessorStateEnum
	ProcessorEmptying             =2          # from enum ProcessorStateEnum
	ProcessorFilling              =1          # from enum ProcessorStateEnum
	ProcessorOffShift             =0          # from enum ProcessorStateEnum
	ProcessorProcessingCycling    =3          # from enum ProcessorStateEnum
	ProcessorStopped              =5          # from enum ProcessorStateEnum
	ProcessorWaitingResourcesClean=9          # from enum ProcessorStateEnum
	ProcessorWaitingResourcesEmpty=8          # from enum ProcessorStateEnum
	ProcessorWaitingResourcesFill =7          # from enum ProcessorStateEnum
	ProcessorWaitingResourcesProcess=6          # from enum ProcessorStateEnum
	ProcessorWaitingResourcesResume=10         # from enum ProcessorStateEnum
	AfterCycle                    =1          # from enum RelationToCycleEnum
	BeforeCycle                   =0          # from enum RelationToCycleEnum
	ReportModeGroup               =2          # from enum ReportModeEnum
	ReportModeIndividual          =1          # from enum ReportModeEnum
	ReportModeNone                =0          # from enum ReportModeEnum
	ReportModeOff                 =0          # from enum ReportModeOnOffEnum
	ReportModeOn                  =2          # from enum ReportModeOnOffEnum
	ReportTypeDIF                 =1          # from enum ReportTypeEnum
	ReportTypeMultipleCSV         =3          # from enum ReportTypeEnum
	ReportTypeRPT                 =0          # from enum ReportTypeEnum
	ReportTypeSingleCSV           =2          # from enum ReportTypeEnum
	ReportTypeXML                 =4          # from enum ReportTypeEnum
	ReportingShiftTimeAsSpecified =2          # from enum ReportingShiftTimeEnum
	ReportingShiftTimeOnAndOff    =1          # from enum ReportingShiftTimeEnum
	ReportingShiftTimeOnOnly      =0          # from enum ReportingShiftTimeEnum
	AccessAddFree                 =1          # from enum SectionAccessMethodEnum
	AccessAdvancedToNextDog       =2          # from enum SectionAccessMethodEnum
	AccessWaitForDog              =0          # from enum SectionAccessMethodEnum
	SectionEllipse                =26         # from enum SectionDisplayTypeEnum
	SectionExpression             =11         # from enum SectionDisplayTypeEnum
	SectionIcon                   =0          # from enum SectionDisplayTypeEnum
	SectionLaborQueue             =5          # from enum SectionDisplayTypeEnum
	SectionLine                   =24         # from enum SectionDisplayTypeEnum
	SectionName                   =1          # from enum SectionDisplayTypeEnum
	SectionNotes                  =7          # from enum SectionDisplayTypeEnum
	SectionPath                   =43         # from enum SectionDisplayTypeEnum
	SectionRectangle              =25         # from enum SectionDisplayTypeEnum
	SectionText                   =6          # from enum SectionDisplayTypeEnum
	SectionStateBrokendownRepairing=2          # from enum SectionStateEnum
	SectionStateOffShift          =0          # from enum SectionStateEnum
	SectionStateRunning           =1          # from enum SectionStateEnum
	SectionStateWaitingForLabor   =3          # from enum SectionStateEnum
	SecurityOptimizerModule       =10         # from enum SecurityModulesEnum
	SetupOnNumberOfOperations     =2          # from enum SetupOnEnum
	SetupOnPartChange             =0          # from enum SetupOnEnum
	SetupOnValueChange            =1          # from enum SetupOnEnum
	ShiftPeriodPeriod             =1          # from enum ShiftPeriodTypeEnum
	ShiftPeriodSubShift           =2          # from enum ShiftPeriodTypeEnum
	ShiftStateOffShift            =0          # from enum ShiftStateEnum
	ShiftStateOnShift             =1          # from enum ShiftStateEnum
	StationCarrierQueue           =44         # from enum StationDisplayTypeEnum
	StationEllipse                =26         # from enum StationDisplayTypeEnum
	StationExpression             =11         # from enum StationDisplayTypeEnum
	StationIcon                   =0          # from enum StationDisplayTypeEnum
	StationLaborQueue             =5          # from enum StationDisplayTypeEnum
	StationLine                   =24         # from enum StationDisplayTypeEnum
	StationName                   =1          # from enum StationDisplayTypeEnum
	StationNotes                  =7          # from enum StationDisplayTypeEnum
	StationRectangle              =25         # from enum StationDisplayTypeEnum
	StationText                   =6          # from enum StationDisplayTypeEnum
	StationLoadingMethodFree      =0          # from enum StationLoadingMethodEnum
	StationLoadingMethodPowered   =1          # from enum StationLoadingMethodEnum
	StationStateArriving          =12         # from enum StationStateEnum
	StationStateBlocked           =3          # from enum StationStateEnum
	StationStateDeparting         =13         # from enum StationStateEnum
	StationStateIdle              =1          # from enum StationStateEnum
	StationStateLoading           =8          # from enum StationStateEnum
	StationStateOffShift          =0          # from enum StationStateEnum
	StationStateParking           =6          # from enum StationStateEnum
	StationStateProcessingCarrier =2          # from enum StationStateEnum
	StationStateRepairing         =4          # from enum StationStateEnum
	StationStateUnloading         =9          # from enum StationStateEnum
	StationStateUnparking         =7          # from enum StationStateEnum
	StationStateWaitingForLaborToProcess=5          # from enum StationStateEnum
	StationStateWaitingForLaborToProcessArrive=29         # from enum StationStateEnum
	StationStateWaitingLaborToLoad=16         # from enum StationStateEnum
	StationStateWaitingLaborToLoadArrive=25         # from enum StationStateEnum
	StationStateWaitingLaborToPark=14         # from enum StationStateEnum
	StationStateWaitingLaborToParkArrive=23         # from enum StationStateEnum
	StationStateWaitingLaborToProcessArrival=18         # from enum StationStateEnum
	StationStateWaitingLaborToProcessArrivalArrive=27         # from enum StationStateEnum
	StationStateWaitingLaborToProcessDeparture=19         # from enum StationStateEnum
	StationStateWaitingLaborToProcessDepartureArrive=28         # from enum StationStateEnum
	StationStateWaitingLaborToProcessRepair=20         # from enum StationStateEnum
	StationStateWaitingLaborToProcessRepairArrive=30         # from enum StationStateEnum
	StationStateWaitingLaborToUnload=17         # from enum StationStateEnum
	StationStateWaitingLaborToUnloadArrive=26         # from enum StationStateEnum
	StationStateWaitingLaborToUnpark=15         # from enum StationStateEnum
	StationStateWaitingLaborToUnparkArrive=24         # from enum StationStateEnum
	StationStateWaitingToLoad     =10         # from enum StationStateEnum
	StationStateWaitingToLoadArrive=21         # from enum StationStateEnum
	StationStateWaitingToUnload   =11         # from enum StationStateEnum
	StationStateWaitingToUnloadArrive=22         # from enum StationStateEnum
	StationTypeBasic              =0          # from enum StationTypeEnum
	StationTypeLoad               =1          # from enum StationTypeEnum
	StationTypeParking            =3          # from enum StationTypeEnum
	StationTypeUnload             =2          # from enum StationTypeEnum
	StationUnloadingMethodFree    =0          # from enum StationUnloadingMethodEnum
	StationUnloadingMethodPowered =1          # from enum StationUnloadingMethodEnum
	TankCleaning                  =2          # from enum TankStateEnum
	TankOffShift                  =0          # from enum TankStateEnum
	TankRunningNormally           =1          # from enum TankStateEnum
	TankWaitingResourcesFlow      =3          # from enum TankStateEnum
	TankWaitingResouresClean      =4          # from enum TankStateEnum
	TextCentered                  =1          # from enum TextFormatEnum
	TextLeft                      =0          # from enum TextFormatEnum
	DisplayCustom                 =1          # from enum TimeDisplayEnum
	DisplayDate                   =4          # from enum TimeDisplayEnum
	DisplayDateAndTime            =6          # from enum TimeDisplayEnum
	DisplayDecimal                =0          # from enum TimeDisplayEnum
	DisplayTimeOfDay              =2          # from enum TimeDisplayEnum
	TimeUnitCustom                =-1         # from enum TimeUnitEnum
	TimeUnitDay                   =3          # from enum TimeUnitEnum
	TimeUnitHour                  =2          # from enum TimeUnitEnum
	TimeUnitMinute                =1          # from enum TimeUnitEnum
	TimeUnitSecond                =0          # from enum TimeUnitEnum
	Custom                        =-1         # from enum TimeUnitEnumEx
	Day                           =3          # from enum TimeUnitEnumEx
	Hour                          =2          # from enum TimeUnitEnumEx
	Minute                        =1          # from enum TimeUnitEnumEx
	Month                         =5          # from enum TimeUnitEnumEx
	Second                        =0          # from enum TimeUnitEnumEx
	Week                          =4          # from enum TimeUnitEnumEx
	Year                          =6          # from enum TimeUnitEnumEx
	TrackLoadAlways               =3          # from enum TrackLoadModeEnum
	TrackLoadByCall               =2          # from enum TrackLoadModeEnum
	TrackLoadConditional          =1          # from enum TrackLoadModeEnum
	TrackLoadNone                 =0          # from enum TrackLoadModeEnum
	TrackStateBlocked             =3          # from enum TrackStateEnum
	TrackStateBusy                =2          # from enum TrackStateEnum
	TrackStateEmpty               =1          # from enum TrackStateEnum
	TrackStopAlways               =3          # from enum TrackStopModeEnum
	TrackStopConditional          =1          # from enum TrackStopModeEnum
	TrackStopNone                 =0          # from enum TrackStopModeEnum
	TrackUnloadAlways             =3          # from enum TrackUnloadModeEnum
	TrackUnloadByCall             =2          # from enum TrackUnloadModeEnum
	TrackUnloadConditional        =1          # from enum TrackUnloadModeEnum
	TrackUnloadNone               =0          # from enum TrackUnloadModeEnum
	TrackUnloadOutputFromAny      =5          # from enum TrackUnloadOutputFromEnum
	TrackUnloadOutputFromFront    =1          # from enum TrackUnloadOutputFromEnum
	TrackUnloadOutputFromRear     =0          # from enum TrackUnloadOutputFromEnum
	UserReportModeAsSpecified     =3          # from enum UserReportModeEnum
	UserReportModeGroup           =2          # from enum UserReportModeEnum
	UserReportModeIndividual      =1          # from enum UserReportModeEnum
	UserReportModeNone            =0          # from enum UserReportModeEnum
	VariableTypeInteger           =1          # from enum VariableTypeEnum
	VariableTypeName              =6          # from enum VariableTypeEnum
	VariableTypeReal              =0          # from enum VariableTypeEnum
	VariableTypeString            =2          # from enum VariableTypeEnum
	VehicleDisplayList            =15         # from enum VehicleDisplayTypeEnum
	VehicleEllipse                =26         # from enum VehicleDisplayTypeEnum
	VehicleExpression             =11         # from enum VehicleDisplayTypeEnum
	VehicleIcon                   =0          # from enum VehicleDisplayTypeEnum
	VehicleLine                   =24         # from enum VehicleDisplayTypeEnum
	VehicleName                   =1          # from enum VehicleDisplayTypeEnum
	VehicleNotes                  =7          # from enum VehicleDisplayTypeEnum
	VehiclePath                   =43         # from enum VehicleDisplayTypeEnum
	VehicleRectangle              =25         # from enum VehicleDisplayTypeEnum
	VehicleText                   =6          # from enum VehicleDisplayTypeEnum
	VehicleStateBlocked           =3          # from enum VehicleStateEnum
	VehicleStateDemanded          =2          # from enum VehicleStateEnum
	VehicleStateIdle              =1          # from enum VehicleStateEnum
	VehicleStateLoaded            =4          # from enum VehicleStateEnum
	VehicleStateLoading           =5          # from enum VehicleStateEnum
	VehicleStateOffShift          =0          # from enum VehicleStateEnum
	VehicleStateOutside           =9          # from enum VehicleStateEnum
	VehicleStateParked            =8          # from enum VehicleStateEnum
	VehicleStateStopped           =7          # from enum VehicleStateEnum
	VehicleStateUnloading         =6          # from enum VehicleStateEnum

from win32com.client import DispatchBaseClass
class IWActivator(DispatchBaseClass):
	'IWActivator Interface'
	CLSID = IID('{58D5DB46-9295-452C-9FDB-1795E61A00A0}')
	coclass_clsid = None

	def Handle(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((12, 1),),Value
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWApplication(DispatchBaseClass):
	'IWApplication Interface'
	CLSID = IID('{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}')
	coclass_clsid = IID('{340F5316-1C07-4BB9-8588-8AF9083B45F9}')

	def Activate(self):
		'Activates the application.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ForceQuit(self):
		'ForceQuit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def Quit(self):
		'Quit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'ErrorsAndWarnings' returns object of type 'IWErrorsAndWarnings'
		"ErrorsAndWarnings": (6, 2, (9, 0), (), "ErrorsAndWarnings", '{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}'),
		# Method 'InputRequest' returns object of type 'IWInputRequest'
		"InputRequest": (7, 2, (9, 0), (), "InputRequest", '{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"ProcessID": (10, 2, (3, 0), (), "ProcessID", None),
		"Version": (2, 2, (8, 0), (), "Version", None),
		"Visible": (4, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Model'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWApplicationViewer(DispatchBaseClass):
	'IWApplicationViewer Interface'
	CLSID = IID('{7FE9DF3A-DF37-43EB-AF81-2EB034A178A1}')
	coclass_clsid = None

	def Activate(self):
		'Activates the application.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ForceQuit(self):
		'ForceQuit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def Quit(self):
		'Quit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'ErrorsAndWarnings' returns object of type 'IWErrorsAndWarnings'
		"ErrorsAndWarnings": (6, 2, (9, 0), (), "ErrorsAndWarnings", '{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}'),
		# Method 'InputRequest' returns object of type 'IWInputRequest'
		"InputRequest": (7, 2, (9, 0), (), "InputRequest", '{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"ProcessID": (10, 2, (3, 0), (), "ProcessID", None),
		"Version": (2, 2, (8, 0), (), "Version", None),
		"Visible": (4, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Model'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWAssemble(DispatchBaseClass):
	'IWAssemble Interface'
	CLSID = IID('{108615F0-4DBE-4D4C-826B-C606578491BA}')
	coclass_clsid = IID('{0E61D6B4-D568-4D42-97AF-946AD57E8293}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWAttribute(DispatchBaseClass):
	'IWAttribute Interface'
	CLSID = IID('{56EF0AE9-1E7D-4892-9C56-837855B9776E}')
	coclass_clsid = IID('{90E44757-6068-437E-9282-EC1F008CA370}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DataType": (103, 2, (3, 0), (), "DataType", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Group": (102, 2, (3, 0), (), "Group", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (3, 0), (), "Quantity", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		"Watch": (104, 2, (11, 0), (), "Watch", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DataType": ((103, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
		"Watch": ((104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWAttributeInstance(DispatchBaseClass):
	'IWAttributeInstance Interface'
	CLSID = IID('{427F8FA1-0EEE-11D5-8579-0020AFF488A2}')
	coclass_clsid = IID('{EB396772-21D0-11D5-8586-0020AFF488A2}')

	# The method Array is actually a property, but must be used as a method to correctly pass the arguments
	def Array(self, Index=defaultNamedNotOptArg):
		'property Array'
		return self._ApplyTypes_(3, 2, (12, 0), ((3, 1),), 'Array', None,Index
			)

	# The method ReferencedElementName is actually a property, but must be used as a method to correctly pass the arguments
	def ReferencedElementName(self, Index=defaultNamedNotOptArg):
		'property ReferencedElementName'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(6, LCID, 2, (8, 0), ((3, 1),),Index
			)

	# The method SetArray is actually a property, but must be used as a method to correctly pass the arguments
	def SetArray(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property Array'
		return self._oleobj_.InvokeTypes(3, LCID, 4, (24, 0), ((3, 1), (12, 1)),Index
			, arg1)

	# The method SetReferencedElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetReferencedElementName(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property ReferencedElementName'
		return self._oleobj_.InvokeTypes(6, LCID, 4, (24, 0), ((3, 1), (8, 1)),Index
			, arg1)

	_prop_map_get_ = {
		"Count": (2, 2, (3, 0), (), "Count", None),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"Name": (4, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"Type": (5, 2, (3, 0), (), "Type", None),
		"Value": (1, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((1, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWAttributeInstances(DispatchBaseClass):
	'IWAttributeInstances Interface'
	CLSID = IID('{427F8FA2-0EEE-11D5-8579-0020AFF488A2}')
	coclass_clsid = IID('{EB396773-21D0-11D5-8586-0020AFF488A2}')

	# Result is of type IWAttributeInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{427F8FA1-0EEE-11D5-8579-0020AFF488A2}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{427F8FA1-0EEE-11D5-8579-0020AFF488A2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{427F8FA1-0EEE-11D5-8579-0020AFF488A2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWAttributeType(DispatchBaseClass):
	'IWAttributeType Interface'
	CLSID = IID('{C3776C0E-DC5F-426C-86B8-D41B92307A40}')
	coclass_clsid = IID('{8D03C4CE-F14E-4819-AA81-67B677C7E6AE}')

	# Result is of type IWAttribute
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, Group=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1), (3, 1), (12, 1)),Name
			, Quantity, Type, Group)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{56EF0AE9-1E7D-4892-9C56-837855B9776E}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBPMViewer(DispatchBaseClass):
	'IWBPMViewer Interface'
	CLSID = IID('{C7DB6FD3-764B-4E78-AFF6-A84F50C7A642}')
	coclass_clsid = None

	def Activate(self):
		'Activates the application.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ForceQuit(self):
		'ForceQuit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def Quit(self):
		'Quit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'ErrorsAndWarnings' returns object of type 'IWErrorsAndWarnings'
		"ErrorsAndWarnings": (6, 2, (9, 0), (), "ErrorsAndWarnings", '{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}'),
		# Method 'InputRequest' returns object of type 'IWInputRequest'
		"InputRequest": (7, 2, (9, 0), (), "InputRequest", '{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"ProcessID": (10, 2, (3, 0), (), "ProcessID", None),
		"Version": (2, 2, (8, 0), (), "Version", None),
		"Visible": (4, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Model'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBackdrop(DispatchBaseClass):
	'IWBackdrop Interface'
	CLSID = IID('{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}')
	coclass_clsid = IID('{8F1E1722-B3BC-49BE-900F-1A1015B3E19B}')

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBuffer(DispatchBaseClass):
	'IWBuffer Interface'
	CLSID = IID('{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}')
	coclass_clsid = IID('{DB0E57F7-7B49-4C88-9B76-8C4D050C1DF1}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(216, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	# The method AverageNumberOfPartsAfterMinDelay is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsAfterMinDelay(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsAfterMinDelay'
		return self._oleobj_.InvokeTypes(214, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AverageNumberOfPartsIn is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsIn(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsIn'
		return self._oleobj_.InvokeTypes(201, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTime is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTime(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTime'
		return self._oleobj_.InvokeTypes(200, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTimeAfterMinDelay is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTimeAfterMinDelay(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTimeAferMinDelay'
		return self._oleobj_.InvokeTypes(213, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(204, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# Result is of type IWPartInstance
	def RemovePart(self):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(217, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(218, LCID, 1, (9, 0), ((12, 1),),Part
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), (),)

	def SetInputAtFront(self):
		'method SetInputAtFront'
		return self._oleobj_.InvokeTypes(161, LCID, 1, (24, 0), (),)

	def SetInputAtPosition(self, Position=defaultNamedNotOptArg):
		'method SetInputAtPosition'
		return self._oleobj_.InvokeTypes(162, LCID, 1, (24, 0), ((12, 1),),Position
			)

	def SetInputAtRear(self):
		'method SetInputAtRear'
		return self._oleobj_.InvokeTypes(160, LCID, 1, (24, 0), (),)

	def SetInputPositionByAttribute(self, Attribute=defaultNamedNotOptArg, Ascending=defaultNamedNotOptArg):
		'method SetInputPositionByAttribute'
		return self._oleobj_.InvokeTypes(163, LCID, 1, (24, 0), ((12, 1), (11, 1)),Attribute
			, Ascending)

	def SetOutputAtFront(self):
		'method SetOutputAtFront'
		return self._oleobj_.InvokeTypes(170, LCID, 1, (24, 0), (),)

	def SetOutputAtRear(self):
		'method SetOutputAtRear'
		return self._oleobj_.InvokeTypes(171, LCID, 1, (24, 0), (),)

	def SetOutputByCondition(self, Condition=defaultNamedNotOptArg, SearchFromFront=defaultNamedNotOptArg):
		'method SetOutputByCondition'
		return self._oleobj_.InvokeTypes(173, LCID, 1, (24, 0), ((12, 1), (11, 1)),Condition
			, SearchFromFront)

	def SetOutputByMaximum(self, Expression=defaultNamedNotOptArg, SearchFromFront=defaultNamedNotOptArg):
		'method SetOutputByMaximum'
		return self._oleobj_.InvokeTypes(174, LCID, 1, (24, 0), ((12, 1), (11, 1)),Expression
			, SearchFromFront)

	def SetOutputByMinimum(self, Expression=defaultNamedNotOptArg, SearchFromFront=defaultNamedNotOptArg):
		'method SetOutputByMinimum'
		return self._oleobj_.InvokeTypes(175, LCID, 1, (24, 0), ((12, 1), (11, 1)),Expression
			, SearchFromFront)

	def SetOutputFromAnyPosition(self, SearchFromFront=defaultNamedNotOptArg):
		'method SetOutputFromAnyPosition'
		return self._oleobj_.InvokeTypes(172, LCID, 1, (24, 0), ((11, 1),),SearchFromFront
			)

	# The method TimeInBufferOfPartAtPosition is actually a property, but must be used as a method to correctly pass the arguments
	def TimeInBufferOfPartAtPosition(self, Position=defaultNamedNotOptArg):
		'property TimeInBufferOfPartAtPosition'
		return self._oleobj_.InvokeTypes(215, LCID, 2, (5, 0), ((12, 1),),Position
			)

	_prop_map_get_ = {
		"ActionsOnEndOfMaximumDelay": (106, 2, (8, 0), (), "ActionsOnEndOfMaximumDelay", None),
		"ActionsOnEndOfMinimumDelay": (105, 2, (8, 0), (), "ActionsOnEndOfMinimumDelay", None),
		"ActionsOnInput": (103, 2, (8, 0), (), "ActionsOnInput", None),
		"ActionsOnOutput": (104, 2, (8, 0), (), "ActionsOnOutput", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		# Method 'BufferInstances' returns object of type 'IWBufferInstances'
		"BufferInstances": (0, 2, (9, 0), (), "BufferInstances", '{5A3597E0-2042-4969-919F-484397BF413B}'),
		"Capacity": (102, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DelayMode": (124, 2, (3, 0), (), "DelayMode", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"ExitRule": (109, 2, (8, 0), (), "ExitRule", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputAttribute": (167, 2, (12, 0), (), "InputAttribute", None),
		"InputMode": (165, 2, (3, 0), (), "InputMode", None),
		"InputPosition": (166, 2, (12, 0), (), "InputPosition", None),
		"MaximumDelay": (123, 2, (12, 0), (), "MaximumDelay", None),
		"MaximumNumberOfPartsIn": (210, 2, (3, 0), (), "MaximumNumberOfPartsIn", None),
		"MaximumPartTimeIn": (212, 2, (5, 0), (), "MaximumPartTimeIn", None),
		# Method 'Measures' returns object of type 'IWBufferMeasures'
		"Measures": (219, 2, (9, 0), (), "Measures", '{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}'),
		"MinimumDelay": (122, 2, (12, 0), (), "MinimumDelay", None),
		"MinimumNumberOfPartsIn": (209, 2, (3, 0), (), "MinimumNumberOfPartsIn", None),
		"MinimumPartTimeIn": (211, 2, (5, 0), (), "MinimumPartTimeIn", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfFreeSpaces": (206, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (203, 2, (3, 0), (), "NumberOfParts", None),
		"NumberOfPartsAfterMinDelay": (205, 2, (3, 0), (), "NumberOfPartsAfterMinDelay", None),
		"OutputCondition": (177, 2, (12, 0), (), "OutputCondition", None),
		"OutputExpression": (178, 2, (12, 0), (), "OutputExpression", None),
		"OutputMode": (176, 2, (3, 0), (), "OutputMode", None),
		"OutputRule": (126, 2, (8, 0), (), "OutputRule", None),
		"OutputSearchFromFront": (179, 2, (11, 0), (), "OutputSearchFromFront", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (120, 2, (3, 0), (), "Reporting", None),
		"ShiftAllowance": (125, 2, (12, 0), (), "ShiftAllowance", None),
		"ShiftName": (121, 2, (12, 0), (), "ShiftName", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"TotalNumberOfPartsIn": (207, 2, (3, 0), (), "TotalNumberOfPartsIn", None),
		"TotalNumberOfPartsOut": (208, 2, (3, 0), (), "TotalNumberOfPartsOut", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnEndOfMaximumDelay": ((106, LCID, 4, 0),()),
		"ActionsOnEndOfMinimumDelay": ((105, LCID, 4, 0),()),
		"ActionsOnInput": ((103, LCID, 4, 0),()),
		"ActionsOnOutput": ((104, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((102, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DelayMode": ((124, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"ExitRule": ((109, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"MaximumDelay": ((123, LCID, 4, 0),()),
		"MinimumDelay": ((122, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputRule": ((126, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((120, LCID, 4, 0),()),
		"ShiftAllowance": ((125, LCID, 4, 0),()),
		"ShiftName": ((121, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'BufferInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "BufferInstances", '{5A3597E0-2042-4969-919F-484397BF413B}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBufferInstance(DispatchBaseClass):
	'IWBufferInstance Interface'
	CLSID = IID('{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}')
	coclass_clsid = IID('{353A4670-5506-4942-83F0-3B60CDC128E8}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	# The method AverageNumberOfPartsAfterMinDelay is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsAfterMinDelay(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsAfterMinDelay'
		return self._oleobj_.InvokeTypes(20, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AverageNumberOfPartsIn is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsIn(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsIn'
		return self._oleobj_.InvokeTypes(5, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTime is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTime(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTime'
		return self._oleobj_.InvokeTypes(4, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTimeAfterMinDelay is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTimeAfterMinDelay(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTimeAferMinDelay'
		return self._oleobj_.InvokeTypes(19, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(10, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# Result is of type IWPartInstance
	def RemovePart(self):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((12, 1),),Part
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# The method TimeInBufferOfPartAtPosition is actually a property, but must be used as a method to correctly pass the arguments
	def TimeInBufferOfPartAtPosition(self, Position=defaultNamedNotOptArg):
		'property TimeInBufferOfPartAtPosition'
		return self._oleobj_.InvokeTypes(21, LCID, 2, (5, 0), ((12, 1),),Position
			)

	_prop_map_get_ = {
		# Method 'Buffer' returns object of type 'IWBuffer'
		"Buffer": (1, 2, (9, 0), (), "Buffer", '{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}'),
		"MaximumNumberOfPartsIn": (16, 2, (3, 0), (), "MaximumNumberOfPartsIn", None),
		"MaximumPartTimeIn": (18, 2, (5, 0), (), "MaximumPartTimeIn", None),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"MinimumNumberOfPartsIn": (15, 2, (3, 0), (), "MinimumNumberOfPartsIn", None),
		"MinimumPartTimeIn": (17, 2, (5, 0), (), "MinimumPartTimeIn", None),
		"NumberOfFreeSpaces": (12, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (9, 2, (3, 0), (), "NumberOfParts", None),
		"NumberOfPartsAfterMinDelay": (11, 2, (3, 0), (), "NumberOfPartsAfterMinDelay", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'PartsIn' returns object of type 'IWPartInstances'
		"PartsIn": (2, 2, (9, 0), (), "PartsIn", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		"State": (3, 2, (3, 0), (), "State", None),
		"TimeTillChangeInShiftState": (8, 2, (5, 0), (), "TimeTillChangeInShiftState", None),
		"TimeTillNextEvent": (7, 2, (5, 0), (), "TimeTillNextEvent", None),
		"TotalNumberOfPartsIn": (13, 2, (3, 0), (), "TotalNumberOfPartsIn", None),
		"TotalNumberOfPartsOut": (14, 2, (3, 0), (), "TotalNumberOfPartsOut", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBufferInstances(DispatchBaseClass):
	'IWBufferInstances Interface'
	CLSID = IID('{5A3597E0-2042-4969-919F-484397BF413B}')
	coclass_clsid = IID('{4E62D659-868B-4718-84A0-245F91232CE3}')

	# Result is of type IWBufferInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWBufferMeasure(DispatchBaseClass):
	'IWBufferMeasure Interface'
	CLSID = IID('{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')
	coclass_clsid = IID('{39A7781C-CAB1-4D5C-B409-ACBAC218779A}')

	_prop_map_get_ = {
		# Method 'DwellTime' returns object of type 'IWMeasureValue'
		"DwellTime": (2, 2, (9, 0), (), "DwellTime", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"PerPartIn": (3, 2, (12, 0), (), "PerPartIn", None),
	}
	_prop_map_put_ = {
		"PerPartIn": ((3, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWBufferMeasures(DispatchBaseClass):
	'IWBufferMeasures Interface'
	CLSID = IID('{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}')
	coclass_clsid = IID('{C3C2BD9F-7169-4413-BE59-93572B2F46B2}')

	# Result is of type IWBufferMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the buffer measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')
		return ret

	# Result is of type IWBufferMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the buffer measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWBufferType(DispatchBaseClass):
	'IWBufferType Interface'
	CLSID = IID('{ED13F315-BB08-49F4-A241-4FE7D898FE44}')
	coclass_clsid = IID('{E31B9C55-790E-46DF-99CB-E07885AE9D02}')

	# Result is of type IWBuffer
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWCarrier(DispatchBaseClass):
	'IWCarrier Interface'
	CLSID = IID('{1F803804-DB54-4D3E-A508-AFFC15277B77}')
	coclass_clsid = IID('{145C2B6F-9CDF-426D-ABAA-E36544E0026F}')

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(110, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		"ActionsOnCreate": (108, 2, (8, 0), (), "ActionsOnCreate", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"AllocatedNetwork": (112, 2, (8, 0), (), "AllocatedNetwork", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		# Method 'CarrierInstances' returns object of type 'IWCarrierInstances'
		"CarrierInstances": (0, 2, (9, 0), (), "CarrierInstances", '{8B98F244-7A42-4233-9432-BABB237EE777}'),
		"CarrierSize": (105, 2, (12, 0), (), "CarrierSize", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"EntryRule": (104, 2, (8, 0), (), "EntryRule", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		# Method 'Network' returns object of type 'IWNetwork'
		"Network": (111, 2, (9, 0), (), "Network", '{00504947-3FAA-4A8F-BF64-4EA4E3416B69}'),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfParts": (113, 2, (3, 0), (), "NumberOfParts", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (103, 2, (3, 0), (), "Reporting", None),
		"RunThrough": (109, 2, (11, 0), (), "RunThrough", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"StartSpacing": (106, 2, (12, 0), (), "StartSpacing", None),
		"StopSpacing": (107, 2, (12, 0), (), "StopSpacing", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnCreate": ((108, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"AllocatedNetwork": ((112, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CarrierSize": ((105, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"EntryRule": ((104, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((103, LCID, 4, 0),()),
		"RunThrough": ((109, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"StartSpacing": ((106, LCID, 4, 0),()),
		"StopSpacing": ((107, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'CarrierInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "CarrierInstances", '{8B98F244-7A42-4233-9432-BABB237EE777}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWCarrierInstance(DispatchBaseClass):
	'IWCarrierInstance Interface'
	CLSID = IID('{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}')
	coclass_clsid = IID('{437FDE2F-0551-4339-B51A-59CDA7F6A287}')

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(9, LCID, 2, (5, 0), ((3, 1), (11, 1)),State
			, OnShiftTime)

	_prop_map_get_ = {
		# Method 'Carrier' returns object of type 'IWCarrier'
		"Carrier": (1, 2, (9, 0), (), "Carrier", '{1F803804-DB54-4D3E-A508-AFFC15277B77}'),
		# Method 'CurrentElement' returns object of type 'IWInstance'
		"CurrentElement": (7, 2, (9, 0), (), "CurrentElement", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		"CurrentElementByName": (8, 2, (8, 0), (), "CurrentElementByName", None),
		"Desc": (3, 2, (12, 0), (), "Desc", None),
		"Icon": (5, 2, (12, 0), (), "Icon", None),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfParts": (14, 2, (3, 0), (), "NumberOfParts", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'PartsIn' returns object of type 'IWPartInstances'
		"PartsIn": (13, 2, (9, 0), (), "PartsIn", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		"Pen": (4, 2, (12, 0), (), "Pen", None),
		"State": (15, 2, (3, 0), (), "State", None),
		"TypeName": (2, 2, (8, 0), (), "TypeName", None),
		# Method 'UserAttributes' returns object of type 'IWAttributeInstances'
		"UserAttributes": (6, 2, (9, 0), (), "UserAttributes", '{427F8FA2-0EEE-11D5-8579-0020AFF488A2}'),
	}
	_prop_map_put_ = {
		"Desc": ((3, LCID, 4, 0),()),
		"Icon": ((5, LCID, 4, 0),()),
		"Pen": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWCarrierInstances(DispatchBaseClass):
	'IWCarrierInstances Interface'
	CLSID = IID('{8B98F244-7A42-4233-9432-BABB237EE777}')
	coclass_clsid = IID('{6ADB5AF9-8FD6-437C-9FD9-FD39260B1A01}')

	# Result is of type IWCarrierInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWCarrierType(DispatchBaseClass):
	'IWCarrierType Interface'
	CLSID = IID('{44C2F7D8-DE76-461E-A15D-FBD6D47DD017}')
	coclass_clsid = IID('{82A079AD-E254-4774-98AC-CA848A60DD37}')

	# Result is of type IWCarrier
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{1F803804-DB54-4D3E-A508-AFFC15277B77}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWColor(DispatchBaseClass):
	'IWColor Interface'
	CLSID = IID('{874FED95-DA11-48E4-B237-FC2CA83DE758}')
	coclass_clsid = IID('{CA7D13A2-FBDA-4FCC-B552-B60468D38BD3}')

	_prop_map_get_ = {
		"Blue": (3, 2, (2, 0), (), "Blue", None),
		"Green": (2, 2, (2, 0), (), "Green", None),
		"Red": (1, 2, (2, 0), (), "Red", None),
	}
	_prop_map_put_ = {
		"Blue": ((3, LCID, 4, 0),()),
		"Green": ((2, LCID, 4, 0),()),
		"Red": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyor(DispatchBaseClass):
	'IWConveyor Interface'
	CLSID = IID('{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}')
	coclass_clsid = IID('{645C5AF8-DE5E-42B9-8CAC-EE7C52560D03}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (11, 0), ((9, 1), (12, 1)),PartInstance
			, Position)

	# The method AverageNumberOfPartsIn is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsIn(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsIn'
		return self._oleobj_.InvokeTypes(115, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTime is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTime(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTime'
		return self._oleobj_.InvokeTypes(116, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(126, LCID, 1, (24, 0), (),)

	# The method NumberOfPartsBetween is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsBetween(self, Position1=defaultNamedNotOptArg, Position2=defaultNamedNotOptArg):
		'property NumberOfPartsBetween'
		return self._oleobj_.InvokeTypes(120, LCID, 2, (3, 0), ((3, 1), (3, 0)),Position1
			, Position2)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(119, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(117, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	# Result is of type IWPartInstance
	def RemovePart(self, Position=defaultNamedNotOptArg):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(129, LCID, 1, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(130, LCID, 1, (9, 0), ((12, 1), (12, 1)),Part
			, Position)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(127, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ActionsOnFront": (109, 2, (8, 0), (), "ActionsOnFront", None),
		"ActionsOnJoin": (108, 2, (8, 0), (), "ActionsOnJoin", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWConveyorBreakdowns'
		"Breakdowns": (114, 2, (9, 0), (), "Breakdowns", '{375E2CD5-8A41-45AF-9469-38744989269C}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		# Method 'ConveyorInstances' returns object of type 'IWConveyorInstances'
		"ConveyorInstances": (0, 2, (9, 0), (), "ConveyorInstances", '{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}'),
		"ConveyorType": (102, 2, (3, 0), (), "ConveyorType", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"IndexTime": (106, 2, (12, 0), (), "IndexTime", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputRule": (111, 2, (8, 0), (), "InputRule", None),
		"Length": (131, 2, (12, 0), (), "Length", None),
		"LengthInParts": (104, 2, (12, 0), (), "LengthInParts", None),
		"MaximumCapacity": (105, 2, (12, 0), (), "MaximumCapacity", None),
		# Method 'Measures' returns object of type 'IWConveyorMeasures'
		"Measures": (136, 2, (9, 0), (), "Measures", '{1E6B62FD-4355-439E-8FA7-A54611B55B11}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfFreeSpaces": (121, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (118, 2, (3, 0), (), "NumberOfParts", None),
		"OutputRule": (112, 2, (8, 0), (), "OutputRule", None),
		"Priority": (103, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"QueueSpacing": (134, 2, (12, 0), (), "QueueSpacing", None),
		"Reporting": (110, 2, (3, 0), (), "Reporting", None),
		"RestartDelay": (107, 2, (12, 0), (), "RestartDelay", None),
		# Method 'Sensors' returns object of type 'IWConveyorSensors'
		"Sensors": (135, 2, (9, 0), (), "Sensors", '{54486179-8C34-4101-831E-23A6D9FE10F6}'),
		"ShiftName": (113, 2, (12, 0), (), "ShiftName", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"Spacing": (133, 2, (12, 0), (), "Spacing", None),
		"Speed": (132, 2, (12, 0), (), "Speed", None),
		"TotalNumberOfPartsIn": (122, 2, (3, 0), (), "TotalNumberOfPartsIn", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnFront": ((109, LCID, 4, 0),()),
		"ActionsOnJoin": ((108, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"ConveyorType": ((102, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"IndexTime": ((106, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"InputRule": ((111, LCID, 4, 0),()),
		"Length": ((131, LCID, 4, 0),()),
		"LengthInParts": ((104, LCID, 4, 0),()),
		"MaximumCapacity": ((105, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputRule": ((112, LCID, 4, 0),()),
		"Priority": ((103, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"QueueSpacing": ((134, LCID, 4, 0),()),
		"Reporting": ((110, LCID, 4, 0),()),
		"RestartDelay": ((107, LCID, 4, 0),()),
		"ShiftName": ((113, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"Spacing": ((133, LCID, 4, 0),()),
		"Speed": ((132, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'ConveyorInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "ConveyorInstances", '{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorBreakdown(DispatchBaseClass):
	'IWConveyorBreakdown Interface'
	CLSID = IID('{330E3D97-24CF-4644-9000-DEEA6EB2306B}')
	coclass_clsid = IID('{37421EC3-04F7-405D-ACCD-CB2D79DF9ABA}')

	_prop_map_get_ = {
		"ActionsOnDown": (5, 2, (8, 0), (), "ActionsOnDown", None),
		"ActionsOnResume": (6, 2, (8, 0), (), "ActionsOnResume", None),
		"BreakdownMode": (1, 2, (3, 0), (), "BreakdownMode", None),
		"LaborRule": (4, 2, (8, 0), (), "LaborRule", None),
		"RepairTime": (3, 2, (12, 0), (), "RepairTime", None),
		"TimeBetweenFailures": (2, 2, (12, 0), (), "TimeBetweenFailures", None),
	}
	_prop_map_put_ = {
		"ActionsOnDown": ((5, LCID, 4, 0),()),
		"ActionsOnResume": ((6, LCID, 4, 0),()),
		"BreakdownMode": ((1, LCID, 4, 0),()),
		"LaborRule": ((4, LCID, 4, 0),()),
		"RepairTime": ((3, LCID, 4, 0),()),
		"TimeBetweenFailures": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorBreakdownInstance(DispatchBaseClass):
	'IWConveyorBreakdownInstance Interface'
	CLSID = IID('{AAB2327A-85B4-41B8-A535-ECFB693A16E7}')
	coclass_clsid = IID('{CC93BB4E-BDC8-4A90-9F3E-7EBDF0D040DC}')

	_prop_map_get_ = {
		"BreakdownNumber": (2, 2, (3, 0), (), "BreakdownNumber", None),
		"BreakdownState": (3, 2, (3, 0), (), "BreakdownState", None),
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (4, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorBreakdownInstances(DispatchBaseClass):
	'IWConveyorBreakdownInstances Interface'
	CLSID = IID('{8278E5B4-CAA4-42E8-AABF-09E7A7535725}')
	coclass_clsid = IID('{2E98B9F5-9406-4019-8225-26A879F6CBE2}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWConveyorBreakdowns(DispatchBaseClass):
	'IWConveyorBreakdowns Interface'
	CLSID = IID('{375E2CD5-8A41-45AF-9469-38744989269C}')
	coclass_clsid = IID('{970B35CB-E87F-4727-B542-43BE71FFF450}')

	def Add(self, Description=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Description
			, Position)

	# Result is of type IWConveyorBreakdown
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{330E3D97-24CF-4644-9000-DEEA6EB2306B}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{330E3D97-24CF-4644-9000-DEEA6EB2306B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{330E3D97-24CF-4644-9000-DEEA6EB2306B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWConveyorInstance(DispatchBaseClass):
	'IWConveyorInstance Interface'
	CLSID = IID('{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}')
	coclass_clsid = IID('{E4159C32-7F0C-41DF-AB41-8269C1AEEA05}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((9, 1), (12, 1)),PartInstance
			, Position)

	# The method AverageNumberOfPartsIn is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsIn(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsIn'
		return self._oleobj_.InvokeTypes(7, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTime is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTime(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTime'
		return self._oleobj_.InvokeTypes(6, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	# The method NumberOfPartsBetween is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsBetween(self, Position1=defaultNamedNotOptArg, Position2=defaultNamedNotOptArg):
		'property NumberOfPartsBetween'
		return self._oleobj_.InvokeTypes(13, LCID, 2, (3, 0), ((3, 1), (3, 0)),Position1
			, Position2)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(12, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(8, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	# Result is of type IWPartInstance
	def RemovePart(self, Position=defaultNamedNotOptArg):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), ((12, 1), (12, 1)),Part
			, Position)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	_prop_map_get_ = {
		# Method 'ActiveBreakdowns' returns object of type 'IWConveyorBreakdownInstances'
		"ActiveBreakdowns": (19, 2, (9, 0), (), "ActiveBreakdowns", '{8278E5B4-CAA4-42E8-AABF-09E7A7535725}'),
		# Method 'Conveyor' returns object of type 'IWConveyor'
		"Conveyor": (1, 2, (9, 0), (), "Conveyor", '{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfFreeSpaces": (14, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (11, 2, (3, 0), (), "NumberOfParts", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'PartsIn' returns object of type 'IWPartInstances'
		"PartsIn": (2, 2, (9, 0), (), "PartsIn", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		"State": (3, 2, (3, 0), (), "State", None),
		"TimeTillChangeInShiftState": (10, 2, (5, 0), (), "TimeTillChangeInShiftState", None),
		"TimeTillNextEvent": (9, 2, (5, 0), (), "TimeTillNextEvent", None),
		"TotalNumberOfPartsIn": (15, 2, (3, 0), (), "TotalNumberOfPartsIn", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorInstances(DispatchBaseClass):
	'IWConveyorInstances Interface'
	CLSID = IID('{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}')
	coclass_clsid = IID('{A7E6802F-5CA6-4489-9F5B-4B06FC0E85C4}')

	# Result is of type IWConveyorInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWConveyorMeasure(DispatchBaseClass):
	'IWConveyorMeasure Interface'
	CLSID = IID('{75DE9907-45CA-4B2B-B584-7851F771FF1E}')
	coclass_clsid = IID('{4458B2E4-FDA8-4241-9882-529C40085984}')

	_prop_map_get_ = {
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorMeasures(DispatchBaseClass):
	'IWConveyorMeasures Interface'
	CLSID = IID('{1E6B62FD-4355-439E-8FA7-A54611B55B11}')
	coclass_clsid = IID('{A33BE52E-CD53-4DFC-B543-733FD618A7C9}')

	# Result is of type IWConveyorMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the conveyor measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{75DE9907-45CA-4B2B-B584-7851F771FF1E}')
		return ret

	# Result is of type IWConveyorMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{75DE9907-45CA-4B2B-B584-7851F771FF1E}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the conveyor measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{75DE9907-45CA-4B2B-B584-7851F771FF1E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{75DE9907-45CA-4B2B-B584-7851F771FF1E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWConveyorSensor(DispatchBaseClass):
	'IWConveyorSensor Interface'
	CLSID = IID('{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}')
	coclass_clsid = IID('{512108B5-3FE7-453E-9169-B91CCCC8F719}')

	_prop_map_get_ = {
		"ActionsOnCover": (104, 2, (8, 0), (), "ActionsOnCover", None),
		"ActionsOnPartOff": (103, 2, (8, 0), (), "ActionsOnPartOff", None),
		"ActionsOnPartOn": (102, 2, (8, 0), (), "ActionsOnPartOn", None),
		"ActionsOnUncover": (105, 2, (8, 0), (), "ActionsOnUncover", None),
		"Position": (101, 2, (12, 0), (), "Position", None),
	}
	_prop_map_put_ = {
		"ActionsOnCover": ((104, LCID, 4, 0),()),
		"ActionsOnPartOff": ((103, LCID, 4, 0),()),
		"ActionsOnPartOn": ((102, LCID, 4, 0),()),
		"ActionsOnUncover": ((105, LCID, 4, 0),()),
		"Position": ((101, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWConveyorSensors(DispatchBaseClass):
	'IWConveyorSensors Interface'
	CLSID = IID('{54486179-8C34-4101-831E-23A6D9FE10F6}')
	coclass_clsid = IID('{1F9233EA-A80D-40E7-B070-03049F936324}')

	def Add(self, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),Position
			)

	# Result is of type IWConveyorSensor
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWConveyorType(DispatchBaseClass):
	'IWConveyorType Interface'
	CLSID = IID('{E7805F03-0261-412A-9F84-2723AD292A9F}')
	coclass_clsid = IID('{E35C70B8-FBAA-4C39-A845-9E45DF62BB63}')

	# Result is of type IWConveyor
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDataTable(DispatchBaseClass):
	'IWDataTable Interface'
	CLSID = IID('{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}')
	coclass_clsid = IID('{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}')

	def LoadData(self):
		'Loads data into all instances using data connection information'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), (),)

	def MakeConnection(self, Type=defaultNamedNotOptArg, Expression=defaultNamedNotOptArg):
		'method MakeConnection'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), ((3, 1), (12, 1)),Type
			, Expression)

	def SaveData(self):
		'Saves data from all instances using data connection information'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Active": (114, 2, (11, 0), (), "Active", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		# Method 'Columns' returns object of type 'IWDataTableColumnItems'
		"Columns": (104, 2, (9, 0), (), "Columns", '{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}'),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"ConnectionErrorHandling": (107, 2, (3, 0), (), "ConnectionErrorHandling", None),
		"ConnectionString": (108, 2, (12, 0), (), "ConnectionString", None),
		"ConnectionType": (106, 2, (3, 0), (), "ConnectionType", None),
		"DataLoadActions": (116, 2, (8, 0), (), "DataLoadActions", None),
		"DataSaveActions": (115, 2, (8, 0), (), "DataSaveActions", None),
		# Method 'DataTableInstances' returns object of type 'IWDataTableInstances'
		"DataTableInstances": (0, 2, (9, 0), (), "DataTableInstances", '{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}'),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"DisplayUpdateInterval": (103, 2, (12, 0), (), "DisplayUpdateInterval", None),
		"DisplayUpdateIntervalMode": (102, 2, (3, 0), (), "DisplayUpdateIntervalMode", None),
		"HasHeaders": (119, 2, (11, 0), (), "HasHeaders", None),
		"IOType": (113, 2, (3, 0), (), "IOType", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputSqlStatement": (117, 2, (8, 0), (), "InputSqlStatement", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"OutputTableName": (118, 2, (8, 0), (), "OutputTableName", None),
		"Priority": (112, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (105, 2, (12, 0), (), "Quantity", None),
		"Reporting": (101, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Active": ((114, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"ConnectionErrorHandling": ((107, LCID, 4, 0),()),
		"DataLoadActions": ((116, LCID, 4, 0),()),
		"DataSaveActions": ((115, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"DisplayUpdateInterval": ((103, LCID, 4, 0),()),
		"DisplayUpdateIntervalMode": ((102, LCID, 4, 0),()),
		"HasHeaders": ((119, LCID, 4, 0),()),
		"IOType": ((113, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"InputSqlStatement": ((117, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputTableName": ((118, LCID, 4, 0),()),
		"Priority": ((112, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((105, LCID, 4, 0),()),
		"Reporting": ((101, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'DataTableInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "DataTableInstances", '{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDataTableColumnItem(DispatchBaseClass):
	'IWDataTableColumnItem Interface'
	CLSID = IID('{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}')
	coclass_clsid = IID('{F0832FC5-9D60-4542-BB68-EACABBE75136}')

	_prop_map_get_ = {
		"MappingName": (3, 2, (8, 0), (), "MappingName", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"MappingName": ((3, LCID, 4, 0),()),
		"Name": ((1, LCID, 4, 0),()),
		"Type": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDataTableColumnItems(DispatchBaseClass):
	'IWDataTableColumnItems Interface'
	CLSID = IID('{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}')
	coclass_clsid = IID('{A6C95EEB-EFDD-4462-91C1-6A6EB787E94B}')

	def Add(self, Name=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, Position=-1):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 49)),Name
			, Type, Position)

	# Result is of type IWDataTableColumnItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWDataTableInstance(DispatchBaseClass):
	'IWDataTableInstance Interface'
	CLSID = IID('{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}')
	coclass_clsid = IID('{EBF1F7CB-5F07-4E2F-B923-DA1873E55206}')

	def Clear(self):
		'Clears all data from the instance'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

	# The method GetValue is actually a property, but must be used as a method to correctly pass the arguments
	def GetValue(self, row=1, column=1):
		'Get/Set the value of a specific cell in the data table instance.'
		return self._ApplyTypes_(100, 2, (12, 0), ((12, 49), (12, 49)), 'GetValue', None,row
			, column)

	def LoadData(self):
		'Loads data into the instance using data connection information'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

	def SaveData(self):
		'Saves data from the instance using data connection information'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

	# The method SetValue is actually a property, but must be used as a method to correctly pass the arguments
	def SetValue(self, row=1, column=1, arg2=defaultUnnamedArg):
		'Get/Set the value of a specific cell in the data table instance.'
		return self._oleobj_.InvokeTypes(100, LCID, 4, (24, 0), ((12, 49), (12, 49), (12, 1)),row
			, column, arg2)

	_prop_map_get_ = {
		# Method 'DataTable' returns object of type 'IWDataTable'
		"DataTable": (2, 2, (9, 0), (), "DataTable", '{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"Rows": (104, 2, (3, 0), (), "Rows", None),
		"Value": (100, 2, (12, 0), ((12, 49), (12, 49)), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((100, LCID, 4, 0),('1',)),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(100, 2, (12, 0), ((12, 49), (12, 49)), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDataTableInstances(DispatchBaseClass):
	'IWDataTableInstances Interface'
	CLSID = IID('{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}')
	coclass_clsid = IID('{4B219466-3B72-4A0C-BC67-A4460E22E7C2}')

	# Result is of type IWDataTableInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'Get a specific data table instance from the DataTable element.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'Get a specific data table instance from the DataTable element.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWDataTableType(DispatchBaseClass):
	'IWDataTableType Interface'
	CLSID = IID('{11F8B66D-0328-4FAD-8154-54AC6DBAB539}')
	coclass_clsid = IID('{7DCDF7AB-9E07-4B20-A73F-A0188D6EDDF4}')

	# Result is of type IWDataTable
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDimensions(DispatchBaseClass):
	'IWDimensions Interface'
	CLSID = IID('{6C98C5C0-21DA-11D5-A1B3-00E02963982C}')
	coclass_clsid = IID('{D3F86990-4072-11D5-A1B8-00E02963982C}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((3, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((3, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWDirectories(DispatchBaseClass):
	'IWDirectories Interface'
	CLSID = IID('{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}')
	coclass_clsid = None

	def Search(self, FileName=defaultNamedNotOptArg, pFileFound=pythoncom.Missing):
		'Searches for the specified file'
		return self._ApplyTypes_(1, 1, (11, 0), ((8, 1), (16392, 2)), 'Search', None,FileName
			, pFileFound)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWDrawTool(DispatchBaseClass):
	'IWDrawTool Interface'
	CLSID = IID('{2C138955-DAF6-456E-9F25-03730158A521}')
	coclass_clsid = IID('{1D60E254-0A19-4E2C-9D3A-F5D9B6ADFDF7}')

	# Result is of type IWPathData
	def CreatePathData(self):
		'method CreatePathData'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePathData', '{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}')
		return ret

	# Result is of type IWPoint
	def CreatePoint(self):
		'method CreatePoint'
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePoint', '{C6034440-1A59-48D8-B463-43918B37FD28}')
		return ret

	def DrawLine(self, StartX=defaultNamedNotOptArg, StartY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg, EndY=defaultNamedNotOptArg):
		'method DrawLine'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),StartX
			, StartY, EndX, EndY)

	def DrawPath(self, PathData=defaultNamedNotOptArg):
		'method DrawPath'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((9, 1),),PathData
			)

	def DrawRectangle(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		'method DrawRectangle'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X
			, Y, Width, Height)

	def DrawText(self, Text=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		'method DrawText'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),Text
			, X, Y)

	def DrawTextBox(self, Text=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg, Format=defaultNamedNotOptArg):
		'method DrawTextBox'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),Text
			, X, Y, Width, Height, Format
			)

	_prop_map_get_ = {
		# Method 'BackgroundColor' returns object of type 'IWColor'
		"BackgroundColor": (6, 2, (9, 0), (), "BackgroundColor", '{874FED95-DA11-48E4-B237-FC2CA83DE758}'),
		"Element": (1, 2, (8, 0), (), "Element", None),
		"FillStyle": (7, 2, (3, 0), (), "FillStyle", None),
		# Method 'Font' returns object of type 'IWFont'
		"Font": (12, 2, (9, 0), (), "Font", '{F1496351-9B02-498C-9FB9-348E0B2AA565}'),
		# Method 'ForegroundColor' returns object of type 'IWColor'
		"ForegroundColor": (5, 2, (9, 0), (), "ForegroundColor", '{874FED95-DA11-48E4-B237-FC2CA83DE758}'),
		"GroupDisplay": (2, 2, (11, 0), (), "GroupDisplay", None),
		"Label": (17, 2, (8, 0), (), "Label", None),
		"LayerNumber": (3, 2, (2, 0), (), "LayerNumber", None),
		"StatusDisplay": (8, 2, (11, 0), (), "StatusDisplay", None),
		"XMemberOffset": (9, 2, (2, 0), (), "XMemberOffset", None),
		"YMemberOffset": (10, 2, (2, 0), (), "YMemberOffset", None),
	}
	_prop_map_put_ = {
		"Element": ((1, LCID, 4, 0),()),
		"FillStyle": ((7, LCID, 4, 0),()),
		"GroupDisplay": ((2, LCID, 4, 0),()),
		"Label": ((17, LCID, 4, 0),()),
		"LayerNumber": ((3, LCID, 4, 0),()),
		"StatusDisplay": ((8, LCID, 4, 0),()),
		"XMemberOffset": ((9, LCID, 4, 0),()),
		"YMemberOffset": ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWElement(DispatchBaseClass):
	'IWElement Interface'
	CLSID = IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')
	coclass_clsid = IID('{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"FullyQualifiedName": (14, 2, (8, 0), (), "FullyQualifiedName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWElements(DispatchBaseClass):
	'IWElements Interface'
	CLSID = IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')
	coclass_clsid = IID('{7CC1ABA0-46BA-423A-8A30-D2F2974CEE63}')

	def Delete(self, Index=defaultNamedNotOptArg):
		'method Delete'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), ((12, 1),),Index
			)

	# Result is of type IWElements
	def FilterOnType(self, Type=defaultNamedNotOptArg, recurseDown=defaultNamedNotOptArg):
		'method FilterOnType'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((3, 1), (11, 1)),Type
			, recurseDown)
		if ret is not None:
			ret = Dispatch(ret, 'FilterOnType', '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')
		return ret

	# Result is of type IWElement
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')
		return ret

	# Result is of type IWElement
	# The method ItemByIdentifier is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByIdentifier(self, Identifier=defaultNamedNotOptArg):
		'property ItemByIdentifier'
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((3, 1),),Identifier
			)
		if ret is not None:
			ret = Dispatch(ret, 'ItemByIdentifier', '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWErrorsAndWarnings(DispatchBaseClass):
	'IWErrorsAndWarnings Interface'
	CLSID = IID('{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}')
	coclass_clsid = IID('{A8990927-8EDC-473B-BA0B-834DF5C23FBF}')

	_prop_map_get_ = {
		"AllowErrors": (1, 2, (11, 0), (), "AllowErrors", None),
		"AllowWarnings": (2, 2, (11, 0), (), "AllowWarnings", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
	}
	_prop_map_put_ = {
		"AllowErrors": ((1, LCID, 4, 0),()),
		"AllowWarnings": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFactors(DispatchBaseClass):
	'IWFactors Interface'
	CLSID = IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')
	coclass_clsid = IID('{BA00DD6A-4545-4AC0-87CC-375C48077E2C}')

	_prop_map_get_ = {
		"Duration": (3, 2, (12, 0), (), "Duration", None),
		"Enabled": (1, 2, (11, 0), (), "Enabled", None),
		"Interval": (2, 2, (12, 0), (), "Interval", None),
	}
	_prop_map_put_ = {
		"Duration": ((3, LCID, 4, 0),()),
		"Enabled": ((1, LCID, 4, 0),()),
		"Interval": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFields(DispatchBaseClass):
	'IWFields Interface'
	CLSID = IID('{739EEB63-2228-4456-AE9B-E7BD3EB736CF}')
	coclass_clsid = IID('{D783B13A-273A-4E8A-805F-75991A508E09}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),Index
			)

	# The method Prompt is actually a property, but must be used as a method to correctly pass the arguments
	def Prompt(self, Index=defaultNamedNotOptArg):
		'property Prompt'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(6, LCID, 2, (8, 0), ((3, 1),),Index
			)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property Item'
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((3, 1), (8, 1)),Index
			, arg1)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Title": (5, 2, (8, 0), (), "Title", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWFile(DispatchBaseClass):
	'IWFile Interface'
	CLSID = IID('{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}')
	coclass_clsid = IID('{3E70BB16-0A94-4BC5-A921-2BCE98CB024D}')

	_prop_map_get_ = {
		"ActionOnExistingFile": (15, 2, (3, 0), (), "ActionOnExistingFile", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (16, 2, (8, 0), (), "DescriptiveName", None),
		"FileName": (101, 2, (8, 0), (), "FileName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionOnExistingFile": ((15, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((16, LCID, 4, 0),()),
		"FileName": ((101, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFileType(DispatchBaseClass):
	'IWFileType Interface'
	CLSID = IID('{92B89E14-6BAA-4D23-8DD5-CB15C77E2D3E}')
	coclass_clsid = IID('{C6097B81-5EA5-4FAB-93FE-741AB26AAE1F}')

	# Result is of type IWFile
	def Define(self, Name=defaultNamedNotOptArg, fileMode=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (3, 1)),Name
			, fileMode)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFont(DispatchBaseClass):
	'IWFont Interface'
	CLSID = IID('{F1496351-9B02-498C-9FB9-348E0B2AA565}')
	coclass_clsid = IID('{2DE39202-734C-49B3-827F-411DCB0856FF}')

	_prop_map_get_ = {
		"Facename": (2, 2, (8, 0), (), "Facename", None),
		"FontStyle": (4, 2, (3, 0), (), "FontStyle", None),
		"Opaque": (3, 2, (11, 0), (), "Opaque", None),
		"PointSize": (1, 2, (2, 0), (), "PointSize", None),
	}
	_prop_map_put_ = {
		"Facename": ((2, LCID, 4, 0),()),
		"FontStyle": ((4, LCID, 4, 0),()),
		"Opaque": ((3, LCID, 4, 0),()),
		"PointSize": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFunction(DispatchBaseClass):
	'IWFunction Interface'
	CLSID = IID('{FC5BF548-99F8-4907-925F-82E0B2FB7835}')
	coclass_clsid = IID('{6E799CC3-0423-4712-9D4F-3081FE6D91A5}')

	def ApplyChanges(self, Type=defaultNamedNotOptArg, Actions=defaultNamedNotOptArg):
		'method ApplyChanges'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1), (8, 1)),Type
			, Actions)

	_prop_map_get_ = {
		"Actions": (102, 2, (8, 0), (), "Actions", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		# Method 'Parameters' returns object of type 'IWFunctionParameters'
		"Parameters": (100, 2, (9, 0), (), "Parameters", '{8693669F-C4C2-4318-AB34-8FF2860AB73B}'),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ReturnType": (101, 2, (3, 0), (), "ReturnType", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		"Watch": (104, 2, (11, 0), (), "Watch", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
		"Watch": ((104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFunctionParameter(DispatchBaseClass):
	'IWFunctionParameter Interface'
	CLSID = IID('{E1347784-EA6C-4A12-813A-F0FD60924578}')
	coclass_clsid = IID('{776DC152-E354-466E-A22E-F8B3BC810AA5}')

	_prop_map_get_ = {
		"Name": (0, 2, (8, 0), (), "Name", None),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Name": ((0, LCID, 4, 0),()),
		"Type": ((1, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWFunctionParameters(DispatchBaseClass):
	'IWFunctionParameters Interface'
	CLSID = IID('{8693669F-C4C2-4318-AB34-8FF2860AB73B}')
	coclass_clsid = IID('{3641AADE-9279-4C7D-8D41-092AE9ACAD8F}')

	def Add(self, Name=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),Name
			, Type, Position)

	# Result is of type IWFunctionParameter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E1347784-EA6C-4A12-813A-F0FD60924578}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E1347784-EA6C-4A12-813A-F0FD60924578}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E1347784-EA6C-4A12-813A-F0FD60924578}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWFunctionType(DispatchBaseClass):
	'IWFunctionType Interface'
	CLSID = IID('{BAE57732-DB47-460F-B339-D8686AB7F649}')
	coclass_clsid = IID('{26A60ABA-817C-459B-BFBF-2E9F8FD16C96}')

	# Result is of type IWFunction
	def Define(self, Name=defaultNamedNotOptArg, Type=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (3, 1)),Name
			, Type)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{FC5BF548-99F8-4907-925F-82E0B2FB7835}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWGraphics(DispatchBaseClass):
	'IWGraphics Interface'
	CLSID = IID('{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}')
	coclass_clsid = IID('{59E05BC6-943D-4E23-AECE-435624AF9AC4}')

	_prop_map_get_ = {
		# Method 'DrawTool' returns object of type 'IWDrawTool'
		"DrawTool": (1, 2, (9, 0), (), "DrawTool", '{2C138955-DAF6-456E-9F25-03730158A521}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWHistogram(DispatchBaseClass):
	'IWHistogram Interface'
	CLSID = IID('{8CFB8503-E585-431A-9863-E1A3D6B9F34E}')
	coclass_clsid = IID('{4CF57EFE-8DD9-4C70-A10A-AEEF3FD68E5D}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWHistogramType(DispatchBaseClass):
	'IWHistogramType Interface'
	CLSID = IID('{CD6C32EB-B24A-4ED0-89FC-AB39EE326295}')
	coclass_clsid = IID('{0A7C4BD3-2E16-4CEF-8D4E-FB4E0AA0F636}')

	# Result is of type IWHistogram
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{8CFB8503-E585-431A-9863-E1A3D6B9F34E}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWInputRequest(DispatchBaseClass):
	'IWInputRequest Interface'
	CLSID = IID('{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}')
	coclass_clsid = IID('{972D79E3-3EA1-4B8E-B33C-0ECA3732EA90}')

	_prop_map_get_ = {
		"AllowInput": (1, 2, (11, 0), (), "AllowInput", None),
	}
	_prop_map_put_ = {
		"AllowInput": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWInstance(DispatchBaseClass):
	'IWInstance Interface'
	CLSID = IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')
	coclass_clsid = IID('{EBF1F7CB-5F07-4E2F-B923-DA1873E55206}')

	_prop_map_get_ = {
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWInstances(DispatchBaseClass):
	'IWInstances Interface'
	CLSID = IID('{83073E66-7AF6-46C0-89D2-F33E7C972377}')
	coclass_clsid = IID('{AE9CA10B-2DCD-4C7A-A849-E0AAA8F90C71}')

	# Result is of type IWInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B663FFB1-235F-11D5-A1B4-00E02963982C}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B663FFB1-235F-11D5-A1B4-00E02963982C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{B663FFB1-235F-11D5-A1B4-00E02963982C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWLabor(DispatchBaseClass):
	'IWLabor Interface'
	CLSID = IID('{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}')
	coclass_clsid = IID('{F5C3DFD0-3DAE-4043-AB52-2F9B2445711B}')

	# The method LaborUnitsAtElement is actually a property, but must be used as a method to correctly pass the arguments
	def LaborUnitsAtElement(self, Element=defaultNamedNotOptArg):
		'property LaborUnitsAtElement'
		return self._oleobj_.InvokeTypes(115, LCID, 2, (3, 0), ((12, 1),),Element
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(107, LCID, 2, (5, 0), ((3, 1), (11, 1)),State
			, OnShiftTime)

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"AvailableLabor": (113, 2, (3, 0), (), "AvailableLabor", None),
		"AverageJobTime": (112, 2, (5, 0), (), "AverageJobTime", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'LaborInstances' returns object of type 'IWLaborInstances'
		"LaborInstances": (0, 2, (9, 0), (), "LaborInstances", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
		# Method 'LaborShifts' returns object of type 'IWLaborShifts'
		"LaborShifts": (102, 2, (9, 0), (), "LaborShifts", '{402F5411-4F7E-11D5-A1C1-00E02963982C}'),
		# Method 'Measures' returns object of type 'IWLaborMeasures'
		"Measures": (116, 2, (9, 0), (), "Measures", '{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfJobsFinished": (109, 2, (5, 0), (), "NumberOfJobsFinished", None),
		"NumberOfJobsInProgress": (111, 2, (5, 0), (), "NumberOfJobsInProgress", None),
		"NumberOfJobsPreEmpted": (110, 2, (5, 0), (), "NumberOfJobsPreEmpted", None),
		"NumberOfJobsStarted": (108, 2, (5, 0), (), "NumberOfJobsStarted", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (106, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((106, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'LaborInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "LaborInstances", '{39150113-B27B-43AA-B116-5EFCF532B027}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWLaborInstance(DispatchBaseClass):
	'IWLaborInstance Interface'
	CLSID = IID('{46FB221B-D834-4B5E-B1EC-582524196017}')
	coclass_clsid = IID('{9C70AC8B-4060-4546-BA5D-8F0DCF16CFEF}')

	# The method LaborUnitsAtElement is actually a property, but must be used as a method to correctly pass the arguments
	def LaborUnitsAtElement(self, Element=defaultNamedNotOptArg):
		'property LaborUnitsAtElement'
		return self._oleobj_.InvokeTypes(16, LCID, 2, (3, 0), ((12, 1),),Element
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(9, LCID, 2, (5, 0), ((3, 1), (11, 1)),State
			, OnShiftTime)

	_prop_map_get_ = {
		"AvailableLabor": (15, 2, (3, 0), (), "AvailableLabor", None),
		"AverageJobTime": (14, 2, (5, 0), (), "AverageJobTime", None),
		# Method 'CurrentElement' returns object of type 'IWInstance'
		"CurrentElement": (7, 2, (9, 0), (), "CurrentElement", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		"CurrentElementByName": (8, 2, (8, 0), (), "CurrentElementByName", None),
		"Desc": (3, 2, (12, 0), (), "Desc", None),
		"Icon": (5, 2, (12, 0), (), "Icon", None),
		# Method 'Labor' returns object of type 'IWLabor'
		"Labor": (1, 2, (9, 0), (), "Labor", '{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfJobsFinished": (11, 2, (5, 0), (), "NumberOfJobsFinished", None),
		"NumberOfJobsInProgress": (13, 2, (5, 0), (), "NumberOfJobsInProgress", None),
		"NumberOfJobsPreEmpted": (12, 2, (5, 0), (), "NumberOfJobsPreEmpted", None),
		"NumberOfJobsStarted": (10, 2, (5, 0), (), "NumberOfJobsStarted", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"Pen": (4, 2, (12, 0), (), "Pen", None),
		"State": (17, 2, (3, 0), (), "State", None),
		"TypeName": (2, 2, (8, 0), (), "TypeName", None),
		# Method 'UserAttributes' returns object of type 'IWAttributeInstances'
		"UserAttributes": (6, 2, (9, 0), (), "UserAttributes", '{427F8FA2-0EEE-11D5-8579-0020AFF488A2}'),
	}
	_prop_map_put_ = {
		"Desc": ((3, LCID, 4, 0),()),
		"Icon": ((5, LCID, 4, 0),()),
		"Pen": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWLaborInstances(DispatchBaseClass):
	'IWLaborInstances Interface'
	CLSID = IID('{39150113-B27B-43AA-B116-5EFCF532B027}')
	coclass_clsid = IID('{DC91B434-6DAC-4512-942D-8F3CDD05ACAF}')

	# Result is of type IWLaborInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{46FB221B-D834-4B5E-B1EC-582524196017}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{46FB221B-D834-4B5E-B1EC-582524196017}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{46FB221B-D834-4B5E-B1EC-582524196017}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWLaborMeasure(DispatchBaseClass):
	'IWLaborMeasure Interface'
	CLSID = IID('{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')
	coclass_clsid = IID('{338B12F3-452B-4C92-9BE4-D41387FD21CB}')

	_prop_map_get_ = {
		# Method 'BusyUse' returns object of type 'IWMeasureValue'
		"BusyUse": (2, 2, (9, 0), (), "BusyUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		# Method 'IdleUse' returns object of type 'IWMeasureValue'
		"IdleUse": (3, 2, (9, 0), (), "IdleUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWLaborMeasures(DispatchBaseClass):
	'IWLaborMeasures Interface'
	CLSID = IID('{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}')
	coclass_clsid = IID('{68B8BE1E-91A4-4DE8-BCB9-E9AB7804577A}')

	# Result is of type IWLaborMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the labor measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')
		return ret

	# Result is of type IWLaborMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the labor measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWLaborRule(DispatchBaseClass):
	'IWLaborRule Interface'
	CLSID = IID('{A1B86D55-E79D-11D4-8556-0020AFF488A2}')
	coclass_clsid = IID('{A1B86D56-E79D-11D4-8556-0020AFF488A2}')

	_prop_map_get_ = {
		"Allowance": (5, 2, (12, 0), (), "Allowance", None),
		"PreEmptLabor": (2, 2, (11, 0), (), "PreEmptLabor", None),
		"PreEmptLevel": (4, 2, (12, 0), (), "PreEmptLevel", None),
		"Rule": (1, 2, (8, 0), (), "Rule", None),
		"TimePenalty": (6, 2, (12, 0), (), "TimePenalty", None),
		"UseLaborDefinedByPartRule": (3, 2, (11, 0), (), "UseLaborDefinedByPartRule", None),
	}
	_prop_map_put_ = {
		"Allowance": ((5, LCID, 4, 0),()),
		"PreEmptLabor": ((2, LCID, 4, 0),()),
		"PreEmptLevel": ((4, LCID, 4, 0),()),
		"Rule": ((1, LCID, 4, 0),()),
		"TimePenalty": ((6, LCID, 4, 0),()),
		"UseLaborDefinedByPartRule": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWLaborRules(DispatchBaseClass):
	'IWLaborRules Interface'
	CLSID = IID('{A1B86D57-E79D-11D4-8556-0020AFF488A2}')
	coclass_clsid = IID('{A1B86D58-E79D-11D4-8556-0020AFF488A2}')

	def Add(self, Name=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Name
			, Position)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWLaborShift(DispatchBaseClass):
	'IWLaborShift Interface'
	CLSID = IID('{402F5410-4F7E-11D5-A1C1-00E02963982C}')
	coclass_clsid = IID('{D3B026A0-50E9-11D5-A1C1-00E02963982C}')

	_prop_map_get_ = {
		"Allowance": (3, 2, (5, 0), (), "Allowance", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Quantity": (2, 2, (3, 0), (), "Quantity", None),
	}
	_prop_map_put_ = {
		"Allowance": ((3, LCID, 4, 0),()),
		"Name": ((1, LCID, 4, 0),()),
		"Quantity": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWLaborShifts(DispatchBaseClass):
	'IWLaborShifts Interface'
	CLSID = IID('{402F5411-4F7E-11D5-A1C1-00E02963982C}')
	coclass_clsid = IID('{D3B026A1-50E9-11D5-A1C1-00E02963982C}')

	def Add(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg, Allowance=defaultNamedNotOptArg, Position=-1):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1), (5, 1), (3, 49)),Name
			, Quantity, Allowance, Position)

	# Result is of type IWLaborShift
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{402F5410-4F7E-11D5-A1C1-00E02963982C}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{402F5410-4F7E-11D5-A1C1-00E02963982C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{402F5410-4F7E-11D5-A1C1-00E02963982C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWLaborType(DispatchBaseClass):
	'IWLaborType Interface'
	CLSID = IID('{32F8A928-07DF-41D1-B490-C3282C7DB4D6}')
	coclass_clsid = IID('{E8307171-6464-4288-8811-77A04CA7282D}')

	# Result is of type IWLabor
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachine(DispatchBaseClass):
	'IWMachine Interface'
	CLSID = IID('{12E061BC-E54B-11D4-8553-0020AFF488A2}')
	coclass_clsid = IID('{12E061BD-E54B-11D4-8553-0020AFF488A2}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(138, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), (),)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, Part=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(137, LCID, 2, (3, 0), ((12, 1),),Part
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(123, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	# Result is of type IWPartInstance
	def RemovePart(self):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(139, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(140, LCID, 1, (9, 0), ((12, 1),),Part
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(135, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWMachineBreakdowns'
		"Breakdowns": (119, 2, (9, 0), (), "Breakdowns", '{8D12737F-BF42-4827-B95C-D891817FAB82}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		# Method 'Cycles' returns object of type 'IWMachineCycles'
		"Cycles": (121, 2, (9, 0), (), "Cycles", '{A1B86D53-E79D-11D4-8556-0020AFF488A2}'),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"EmptyingRule": (114, 2, (8, 0), (), "EmptyingRule", None),
		"EmptyingStationNumber": (117, 2, (12, 0), (), "EmptyingStationNumber", None),
		"EmptyingVolume": (112, 2, (12, 0), (), "EmptyingVolume", None),
		"FillingRule": (115, 2, (8, 0), (), "FillingRule", None),
		"FillingStationNumber": (116, 2, (12, 0), (), "FillingStationNumber", None),
		"FillingVolume": (113, 2, (12, 0), (), "FillingVolume", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputBufferCapacity": (128, 2, (3, 0), (), "InputBufferCapacity", None),
		# Method 'MachineInstances' returns object of type 'IWMachineInstances'
		"MachineInstances": (0, 2, (9, 0), (), "MachineInstances", '{921B4444-BEC7-4203-A45C-724F25DA67BB}'),
		"MachineType": (104, 2, (3, 0), (), "MachineType", None),
		# Method 'Measures' returns object of type 'IWMachineMeasures'
		"Measures": (141, 2, (9, 0), (), "Measures", '{05F69682-BC4D-4B74-A78C-04E88D74CB06}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfOperationsCompleted": (126, 2, (3, 0), (), "NumberOfOperationsCompleted", None),
		"NumberOfParts": (136, 2, (3, 0), (), "NumberOfParts", None),
		"OutputBufferCapacity": (127, 2, (3, 0), (), "OutputBufferCapacity", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (103, 2, (3, 0), (), "Reporting", None),
		# Method 'Setups' returns object of type 'IWMachineSetups'
		"Setups": (120, 2, (9, 0), (), "Setups", '{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}'),
		"ShiftAllowance": (133, 2, (12, 0), (), "ShiftAllowance", None),
		"ShiftName": (132, 2, (12, 0), (), "ShiftName", None),
		"ShiftPenalty": (134, 2, (12, 0), (), "ShiftPenalty", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"EmptyingRule": ((114, LCID, 4, 0),()),
		"EmptyingStationNumber": ((117, LCID, 4, 0),()),
		"EmptyingVolume": ((112, LCID, 4, 0),()),
		"FillingRule": ((115, LCID, 4, 0),()),
		"FillingStationNumber": ((116, LCID, 4, 0),()),
		"FillingVolume": ((113, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"MachineType": ((104, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((103, LCID, 4, 0),()),
		"ShiftAllowance": ((133, LCID, 4, 0),()),
		"ShiftName": ((132, LCID, 4, 0),()),
		"ShiftPenalty": ((134, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'MachineInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "MachineInstances", '{921B4444-BEC7-4203-A45C-724F25DA67BB}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineBreakdown(DispatchBaseClass):
	'IWMachineBreakdown Interface'
	CLSID = IID('{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}')
	coclass_clsid = IID('{2956F9E1-CF7A-4388-8E3B-3BD46C9F5B5A}')

	_prop_map_get_ = {
		"ActionsOnAllocateLabor": (20, 2, (8, 0), (), "ActionsOnAllocateLabor", None),
		"ActionsOnDown": (8, 2, (8, 0), (), "ActionsOnDown", None),
		"ActionsOnFreeLabor": (21, 2, (8, 0), (), "ActionsOnFreeLabor", None),
		"ActionsOnResume": (9, 2, (8, 0), (), "ActionsOnResume", None),
		"BreakdownMode": (10, 2, (3, 0), (), "BreakdownMode", None),
		"BreakdownNumber": (13, 2, (3, 0), (), "BreakdownNumber", None),
		"CheckAtStartOfCycle": (2, 2, (11, 0), (), "CheckAtStartOfCycle", None),
		"Description": (1, 2, (8, 0), (), "Description", None),
		# Method 'Element' returns object of type 'IWElement'
		"Element": (12, 2, (9, 0), (), "Element", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"LaborRule": (14, 2, (8, 0), (), "LaborRule", None),
		"NumberOfOperations": (6, 2, (12, 0), (), "NumberOfOperations", None),
		"OutputAction": (19, 2, (8, 0), (), "OutputAction", None),
		"OutputRule": (18, 2, (8, 0), (), "OutputRule", None),
		"PercentageLifeUsed": (11, 2, (12, 0), (), "PercentageLifeUsed", None),
		"PreEmptAllowance": (16, 2, (12, 0), (), "PreEmptAllowance", None),
		"PreEmptLevel": (15, 2, (12, 0), (), "PreEmptLevel", None),
		"PreEmptPenalty": (17, 2, (12, 0), (), "PreEmptPenalty", None),
		"RepairTime": (5, 2, (12, 0), (), "RepairTime", None),
		"ScrapPart": (3, 2, (11, 0), (), "ScrapPart", None),
		"SetupOnRepair": (4, 2, (11, 0), (), "SetupOnRepair", None),
		"TimeBetweenFailures": (7, 2, (12, 0), (), "TimeBetweenFailures", None),
		"TimeUntilFailure": (22, 2, (12, 0), (), "TimeUntilFailure", None),
	}
	_prop_map_put_ = {
		"ActionsOnAllocateLabor": ((20, LCID, 4, 0),()),
		"ActionsOnDown": ((8, LCID, 4, 0),()),
		"ActionsOnFreeLabor": ((21, LCID, 4, 0),()),
		"ActionsOnResume": ((9, LCID, 4, 0),()),
		"BreakdownMode": ((10, LCID, 4, 0),()),
		"CheckAtStartOfCycle": ((2, LCID, 4, 0),()),
		"Description": ((1, LCID, 4, 0),()),
		"LaborRule": ((14, LCID, 4, 0),()),
		"NumberOfOperations": ((6, LCID, 4, 0),()),
		"OutputAction": ((19, LCID, 4, 0),()),
		"OutputRule": ((18, LCID, 4, 0),()),
		"PercentageLifeUsed": ((11, LCID, 4, 0),()),
		"PreEmptAllowance": ((16, LCID, 4, 0),()),
		"PreEmptLevel": ((15, LCID, 4, 0),()),
		"PreEmptPenalty": ((17, LCID, 4, 0),()),
		"RepairTime": ((5, LCID, 4, 0),()),
		"ScrapPart": ((3, LCID, 4, 0),()),
		"SetupOnRepair": ((4, LCID, 4, 0),()),
		"TimeBetweenFailures": ((7, LCID, 4, 0),()),
		"TimeUntilFailure": ((22, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineBreakdownInstance(DispatchBaseClass):
	'IWMachineBreakdownInstance Interface'
	CLSID = IID('{D4F90213-4DD0-4003-99AA-8DE53FB5E643}')
	coclass_clsid = IID('{FA23351B-6EC3-470E-9D33-6B7466996606}')

	_prop_map_get_ = {
		"BreakdownNumber": (2, 2, (3, 0), (), "BreakdownNumber", None),
		"BreakdownState": (3, 2, (3, 0), (), "BreakdownState", None),
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (4, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineBreakdownInstances(DispatchBaseClass):
	'IWMachineBreakdownInstances Interface'
	CLSID = IID('{1CD3A435-8D00-4CB8-A630-F666460D0372}')
	coclass_clsid = IID('{2C948309-016C-4430-8F8E-8FD6EAB90BFD}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineBreakdowns(DispatchBaseClass):
	'IWMachineBreakdowns Interface'
	CLSID = IID('{8D12737F-BF42-4827-B95C-D891817FAB82}')
	coclass_clsid = IID('{514D7591-4ACC-4E7A-B9F9-5361350218D2}')

	def Add(self, Description=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Description
			, Position)

	# Result is of type IWMachineBreakdown
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineCycle(DispatchBaseClass):
	'IWMachineCycle Interface'
	CLSID = IID('{A1B86D51-E79D-11D4-8556-0020AFF488A2}')
	coclass_clsid = IID('{A1B86D52-E79D-11D4-8556-0020AFF488A2}')

	_prop_map_get_ = {
		"ActionsOnAllocateLabor": (27, 2, (8, 0), (), "ActionsOnAllocateLabor", None),
		"ActionsOnFinish": (9, 2, (8, 0), (), "ActionsOnFinish", None),
		"ActionsOnFreeLabor": (28, 2, (8, 0), (), "ActionsOnFreeLabor", None),
		"ActionsOnInput": (25, 2, (8, 0), (), "ActionsOnInput", None),
		"ActionsOnOutput": (26, 2, (8, 0), (), "ActionsOnOutput", None),
		"ActionsOnStart": (8, 2, (8, 0), (), "ActionsOnStart", None),
		"AssembleIntoPart": (29, 2, (11, 0), (), "AssembleIntoPart", None),
		"BatchMax": (16, 2, (12, 0), (), "BatchMax", None),
		"BatchMin": (15, 2, (12, 0), (), "BatchMin", None),
		"CycleNumber": (12, 2, (3, 0), (), "CycleNumber", None),
		"CycleTime": (6, 2, (12, 0), (), "CycleTime", None),
		"Description": (1, 2, (8, 0), (), "Description", None),
		# Method 'Element' returns object of type 'IWElement'
		"Element": (11, 2, (9, 0), (), "Element", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"FinishQuantity": (7, 2, (12, 0), (), "FinishQuantity", None),
		"InheritAttributeValues": (14, 2, (11, 0), (), "InheritAttributeValues", None),
		"InputQuantity": (2, 2, (12, 0), (), "InputQuantity", None),
		"InputRule": (4, 2, (8, 0), (), "InputRule", None),
		"LaborAssignedUsingRule": (21, 2, (11, 0), (), "LaborAssignedUsingRule", None),
		"LaborRule": (17, 2, (8, 0), (), "LaborRule", None),
		"NumberOfStations": (23, 2, (12, 0), (), "NumberOfStations", None),
		"OutputFromPosition": (10, 2, (3, 0), (), "OutputFromPosition", None),
		"OutputQuantity": (3, 2, (12, 0), (), "OutputQuantity", None),
		"OutputRule": (5, 2, (8, 0), (), "OutputRule", None),
		"PartsPerStation": (22, 2, (12, 0), (), "PartsPerStation", None),
		"PreEmptAllowance": (19, 2, (12, 0), (), "PreEmptAllowance", None),
		"PreEmptLevel": (18, 2, (12, 0), (), "PreEmptLevel", None),
		"PreEmptPenalty": (20, 2, (12, 0), (), "PreEmptPenalty", None),
		"ProduceFromFirstPart": (30, 2, (11, 0), (), "ProduceFromFirstPart", None),
		"ProductionPartType": (13, 2, (12, 0), (), "ProductionPartType", None),
		"SelectPartsToProduce": (31, 2, (11, 0), (), "SelectPartsToProduce", None),
		"UseOldestPart": (24, 2, (11, 0), (), "UseOldestPart", None),
	}
	_prop_map_put_ = {
		"ActionsOnAllocateLabor": ((27, LCID, 4, 0),()),
		"ActionsOnFinish": ((9, LCID, 4, 0),()),
		"ActionsOnFreeLabor": ((28, LCID, 4, 0),()),
		"ActionsOnInput": ((25, LCID, 4, 0),()),
		"ActionsOnOutput": ((26, LCID, 4, 0),()),
		"ActionsOnStart": ((8, LCID, 4, 0),()),
		"AssembleIntoPart": ((29, LCID, 4, 0),()),
		"BatchMax": ((16, LCID, 4, 0),()),
		"BatchMin": ((15, LCID, 4, 0),()),
		"CycleTime": ((6, LCID, 4, 0),()),
		"Description": ((1, LCID, 4, 0),()),
		"FinishQuantity": ((7, LCID, 4, 0),()),
		"InheritAttributeValues": ((14, LCID, 4, 0),()),
		"InputQuantity": ((2, LCID, 4, 0),()),
		"InputRule": ((4, LCID, 4, 0),()),
		"LaborAssignedUsingRule": ((21, LCID, 4, 0),()),
		"LaborRule": ((17, LCID, 4, 0),()),
		"NumberOfStations": ((23, LCID, 4, 0),()),
		"OutputFromPosition": ((10, LCID, 4, 0),()),
		"OutputQuantity": ((3, LCID, 4, 0),()),
		"OutputRule": ((5, LCID, 4, 0),()),
		"PartsPerStation": ((22, LCID, 4, 0),()),
		"PreEmptAllowance": ((19, LCID, 4, 0),()),
		"PreEmptLevel": ((18, LCID, 4, 0),()),
		"PreEmptPenalty": ((20, LCID, 4, 0),()),
		"ProduceFromFirstPart": ((30, LCID, 4, 0),()),
		"ProductionPartType": ((13, LCID, 4, 0),()),
		"SelectPartsToProduce": ((31, LCID, 4, 0),()),
		"UseOldestPart": ((24, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineCycleInstance(DispatchBaseClass):
	'IWMachineCycleInstance Interface'
	CLSID = IID('{901A46A2-B4D6-473D-9B89-A9DABAB418E7}')
	coclass_clsid = IID('{D7462A12-315B-468E-9B24-44AB329B844D}')

	_prop_map_get_ = {
		"CycleNumber": (2, 2, (3, 0), (), "CycleNumber", None),
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (3, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineCycleInstances(DispatchBaseClass):
	'IWMachineCycleInstances Interface'
	CLSID = IID('{35B1CE41-5962-4071-8824-4D43DA7C2DA9}')
	coclass_clsid = IID('{30804F82-C8D0-498A-BB3E-76C1B1B393CC}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineCycles(DispatchBaseClass):
	'IWMachineCycles Interface'
	CLSID = IID('{A1B86D53-E79D-11D4-8556-0020AFF488A2}')
	coclass_clsid = IID('{A1B86D54-E79D-11D4-8556-0020AFF488A2}')

	def Add(self, Description=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Description
			, Position)

	# Result is of type IWMachineCycle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A1B86D51-E79D-11D4-8556-0020AFF488A2}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A1B86D51-E79D-11D4-8556-0020AFF488A2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A1B86D51-E79D-11D4-8556-0020AFF488A2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineInstance(DispatchBaseClass):
	'IWMachineInstance Interface'
	CLSID = IID('{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}')
	coclass_clsid = IID('{725808C2-8F7A-41A1-B348-12EC36BC8FCF}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, Part=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(19, LCID, 2, (3, 0), ((12, 1),),Part
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(15, LCID, 2, (5, 0), ((3, 0), (11, 0)),State
			, OnShiftTime)

	# Result is of type IWPartInstance
	def RemovePart(self):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), ((12, 1),),Part
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	_prop_map_get_ = {
		# Method 'ActiveBreakdowns' returns object of type 'IWMachineBreakdownInstances'
		"ActiveBreakdowns": (3, 2, (9, 0), (), "ActiveBreakdowns", '{1CD3A435-8D00-4CB8-A630-F666460D0372}'),
		# Method 'ActiveCycles' returns object of type 'IWMachineCycleInstances'
		"ActiveCycles": (1, 2, (9, 0), (), "ActiveCycles", '{35B1CE41-5962-4071-8824-4D43DA7C2DA9}'),
		# Method 'ActiveSetups' returns object of type 'IWMachineSetupInstances'
		"ActiveSetups": (2, 2, (9, 0), (), "ActiveSetups", '{897905FC-B806-4835-8AF8-088E6405AD70}'),
		"CurrentCycle": (9, 2, (3, 0), (), "CurrentCycle", None),
		"InputBufferCapacity": (12, 2, (3, 0), (), "InputBufferCapacity", None),
		# Method 'Machine' returns object of type 'IWMachine'
		"Machine": (7, 2, (9, 0), (), "Machine", '{12E061BC-E54B-11D4-8553-0020AFF488A2}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfOperationsCompleted": (14, 2, (3, 0), (), "NumberOfOperationsCompleted", None),
		"NumberOfParts": (18, 2, (3, 0), (), "NumberOfParts", None),
		"OutputBufferCapacity": (13, 2, (3, 0), (), "OutputBufferCapacity", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'PartsInInputBuffer' returns object of type 'IWPartInstances'
		"PartsInInputBuffer": (4, 2, (9, 0), (), "PartsInInputBuffer", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		# Method 'PartsInOutputBuffer' returns object of type 'IWPartInstances'
		"PartsInOutputBuffer": (5, 2, (9, 0), (), "PartsInOutputBuffer", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		# Method 'PartsInProcess' returns object of type 'IWPartInstances'
		"PartsInProcess": (6, 2, (9, 0), (), "PartsInProcess", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		"State": (8, 2, (3, 0), (), "State", None),
		"TimeTillChangeInShiftState": (17, 2, (5, 0), (), "TimeTillChangeInShiftState", None),
		"TimeTillNextEvent": (16, 2, (5, 0), (), "TimeTillNextEvent", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineInstances(DispatchBaseClass):
	'IWMachineInstances Interface'
	CLSID = IID('{921B4444-BEC7-4203-A45C-724F25DA67BB}')
	coclass_clsid = IID('{E6A2B0E2-8C62-43B0-88E1-C462E6CE584B}')

	# Result is of type IWMachineInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineMeasure(DispatchBaseClass):
	'IWMachineMeasure Interface'
	CLSID = IID('{63070342-EC3E-456F-90DA-B849F98EB873}')
	coclass_clsid = IID('{CB6E9DA5-A948-4FD0-9873-1B64E06BADE1}')

	_prop_map_get_ = {
		# Method 'BusyUse' returns object of type 'IWMeasureValue'
		"BusyUse": (2, 2, (9, 0), (), "BusyUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		# Method 'IdleUse' returns object of type 'IWMeasureValue'
		"IdleUse": (3, 2, (9, 0), (), "IdleUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"PerOperation": (4, 2, (12, 0), (), "PerOperation", None),
	}
	_prop_map_put_ = {
		"PerOperation": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineMeasures(DispatchBaseClass):
	'IWMachineMeasures Interface'
	CLSID = IID('{05F69682-BC4D-4B74-A78C-04E88D74CB06}')
	coclass_clsid = IID('{4AEDE750-7BBF-4588-B547-FD7C8200B522}')

	# Result is of type IWMachineMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the machine measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{63070342-EC3E-456F-90DA-B849F98EB873}')
		return ret

	# Result is of type IWMachineMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{63070342-EC3E-456F-90DA-B849F98EB873}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the machine measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{63070342-EC3E-456F-90DA-B849F98EB873}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{63070342-EC3E-456F-90DA-B849F98EB873}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineSetup(DispatchBaseClass):
	'IWMachineSetup Interface'
	CLSID = IID('{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}')
	coclass_clsid = IID('{94A0CFA9-E6D7-11D4-8555-0020AFF488A2}')

	_prop_map_get_ = {
		"ActionsOnAllocateLabor": (17, 2, (8, 0), (), "ActionsOnAllocateLabor", None),
		"ActionsOnFinish": (5, 2, (8, 0), (), "ActionsOnFinish", None),
		"ActionsOnFreeLabor": (18, 2, (8, 0), (), "ActionsOnFreeLabor", None),
		"ActionsOnStart": (4, 2, (8, 0), (), "ActionsOnStart", None),
		"Description": (1, 2, (8, 0), (), "Description", None),
		# Method 'Element' returns object of type 'IWElement'
		"Element": (9, 2, (9, 0), (), "Element", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"LaborRule": (11, 2, (8, 0), (), "LaborRule", None),
		"NeedPart": (16, 2, (11, 0), (), "NeedPart", None),
		"NumberOfOperations": (3, 2, (12, 0), (), "NumberOfOperations", None),
		"OperationsToFirstSetup": (6, 2, (12, 0), (), "OperationsToFirstSetup", None),
		"PreEmptAllowance": (13, 2, (12, 0), (), "PreEmptAllowance", None),
		"PreEmptLevel": (12, 2, (12, 0), (), "PreEmptLevel", None),
		"PreEmptPenalty": (14, 2, (12, 0), (), "PreEmptPenalty", None),
		"SetupMode": (7, 2, (3, 0), (), "SetupMode", None),
		"SetupNumber": (10, 2, (3, 0), (), "SetupNumber", None),
		"SetupTime": (2, 2, (12, 0), (), "SetupTime", None),
		"StationNumber": (8, 2, (12, 0), (), "StationNumber", None),
		"ValueChangeExpression": (15, 2, (12, 0), (), "ValueChangeExpression", None),
	}
	_prop_map_put_ = {
		"ActionsOnAllocateLabor": ((17, LCID, 4, 0),()),
		"ActionsOnFinish": ((5, LCID, 4, 0),()),
		"ActionsOnFreeLabor": ((18, LCID, 4, 0),()),
		"ActionsOnStart": ((4, LCID, 4, 0),()),
		"Description": ((1, LCID, 4, 0),()),
		"LaborRule": ((11, LCID, 4, 0),()),
		"NeedPart": ((16, LCID, 4, 0),()),
		"NumberOfOperations": ((3, LCID, 4, 0),()),
		"OperationsToFirstSetup": ((6, LCID, 4, 0),()),
		"PreEmptAllowance": ((13, LCID, 4, 0),()),
		"PreEmptLevel": ((12, LCID, 4, 0),()),
		"PreEmptPenalty": ((14, LCID, 4, 0),()),
		"SetupMode": ((7, LCID, 4, 0),()),
		"SetupTime": ((2, LCID, 4, 0),()),
		"StationNumber": ((8, LCID, 4, 0),()),
		"ValueChangeExpression": ((15, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineSetupInstance(DispatchBaseClass):
	'IWMachineSetupInstance Interface'
	CLSID = IID('{B66E325C-F3FA-40FE-A3D1-32570E96C8F7}')
	coclass_clsid = IID('{59145A07-9E49-4EE1-B49A-5447C3B692C9}')

	_prop_map_get_ = {
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (3, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
		"SetupNumber": (2, 2, (3, 0), (), "SetupNumber", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMachineSetupInstances(DispatchBaseClass):
	'IWMachineSetupInstances Interface'
	CLSID = IID('{897905FC-B806-4835-8AF8-088E6405AD70}')
	coclass_clsid = IID('{3D903BF9-0617-4B73-BD0E-0D0D10F0B914}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineSetups(DispatchBaseClass):
	'IWMachineSetups Interface'
	CLSID = IID('{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}')
	coclass_clsid = IID('{94A0CFAB-E6D7-11D4-8555-0020AFF488A2}')

	def Add(self, Name=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Name
			, Position)

	# Result is of type IWMachineSetup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWMachineType(DispatchBaseClass):
	'IWMachineType Interface'
	CLSID = IID('{E36854D0-A37A-48AA-B2BE-A5E475428EE4}')
	coclass_clsid = IID('{ED85E9B1-9E8C-4B13-B5F7-5071288D83FF}')

	# Result is of type IWMachine
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{12E061BC-E54B-11D4-8553-0020AFF488A2}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWMeasureValue(DispatchBaseClass):
	'IWMeasureValue Interface'
	CLSID = IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')
	coclass_clsid = IID('{445890C6-E66E-4620-8413-C613D7BD29D3}')

	_prop_map_get_ = {
		"PerTimeUnit": (1, 2, (3, 0), (), "PerTimeUnit", None),
		"Value": (0, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"PerTimeUnit": ((1, LCID, 4, 0),()),
		"Value": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWModel(DispatchBaseClass):
	'IWModel Interface'
	CLSID = IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')
	coclass_clsid = IID('{F14DAB7E-75CA-45F1-976A-0051E43B6B90}')

	def AddHoliday(self, StartDate=defaultNamedNotOptArg, EndDate=defaultNamedNotOptArg):
		'Adds a holiday between the specifed dates'
		return self._oleobj_.InvokeTypes(74, LCID, 1, (24, 0), ((8, 1), (8, 0)),StartDate
			, EndDate)

	def Begin(self):
		'method Begin'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), (),)

	# The method EndPeriod is actually a property, but must be used as a method to correctly pass the arguments
	def EndPeriod(self, Day=defaultNamedNotOptArg, PeriodNumber=defaultNamedNotOptArg):
		'Gets the end time of the period'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(73, LCID, 2, (8, 0), ((3, 1), (12, 1)),Day
			, PeriodNumber)

	def EvaluateExpression(self, Type=defaultNamedNotOptArg, Expression=defaultNamedNotOptArg):
		'method EvaluateExpression'
		return self._ApplyTypes_(30, 1, (12, 0), ((3, 1), (8, 1)), 'EvaluateExpression', None,Type
			, Expression)

	def Generate3D(self):
		'Generate a 3D view of the current model.'
		return self._oleobj_.InvokeTypes(84, LCID, 1, (24, 0), (),)

	def GenerateTrace3D(self):
		'Generate 3D trace commands for the current model.'
		return self._oleobj_.InvokeTypes(94, LCID, 1, (24, 0), (),)

	# Result is of type IWModelEventManager
	def GetModelEventManager(self):
		'Create a new instance of the model event manager'
		ret = self._oleobj_.InvokeTypes(79, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetModelEventManager', '{D8396D00-CC33-47E7-A917-1527DF798EC5}')
		return ret

	def ImmediateActions(self, Statement=defaultNamedNotOptArg):
		'method ImmediateActions'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((8, 1),),Statement
			)

	def IsReservedWord(self, word=defaultNamedNotOptArg):
		'method IsReservedWord'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (11, 0), ((8, 1),),word
			)

	def Load(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, FileType)

	def New(self):
		'method New'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), (),)

	def RemoveDebugInformation(self):
		'Remove debugging information from the model.'
		return self._oleobj_.InvokeTypes(96, LCID, 1, (24, 0), (),)

	def RemoveHolidays(self, StartDate=defaultNamedNotOptArg, EndDate=defaultNamedNotOptArg):
		'Removes holidays between the specifed dates'
		return self._oleobj_.InvokeTypes(75, LCID, 1, (24, 0), ((8, 1), (8, 0)),StartDate
			, EndDate)

	def ReportAll(self, Type=defaultNamedNotOptArg, File=defaultNamedNotOptArg, reportShiftTime=defaultNamedNotOptArg, ReportingMode=defaultNamedNotOptArg
			, DetailReportingMode=defaultNamedNotOptArg):
		'Reports statistics for elements to a file in the specified type format for on or off shift, ReportingMode specifying group individual or as specified reporting, with DetailReportingMode controlling the additional level of detail.'
		return self._oleobj_.InvokeTypes(64, LCID, 1, (24, 0), ((3, 1), (8, 1), (3, 1), (3, 1), (3, 1)),Type
			, File, reportShiftTime, ReportingMode, DetailReportingMode)

	def ReportToFile(self, Type=defaultNamedNotOptArg, File=defaultNamedNotOptArg):
		'method ReportToFile'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((3, 1), (8, 1)),Type
			, File)

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), (),)

	def Run(self, StopTime=defaultNamedOptArg):
		'method Run'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((12, 17),),StopTime
			)

	def RunBatch(self, StopTime=defaultNamedNotOptArg):
		'method RunBatch'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((12, 1),),StopTime
			)

	def RunInitializeActions(self):
		'Runs the actions on initialize for the model if not already run.'
		return self._oleobj_.InvokeTypes(65, LCID, 1, (24, 0), (),)

	def Save(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, FileType)

	def ScheduleEvent(self, EventNo=defaultNamedNotOptArg, AfterTime=defaultNamedNotOptArg):
		'method ScheduleEvent'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((12, 1), (12, 1)),EventNo
			, AfterTime)

	def SetPeriod(self, Day=defaultNamedNotOptArg, PeriodNumber=defaultNamedNotOptArg, StartTime=defaultNamedNotOptArg, EndTime=defaultNamedNotOptArg):
		'Defines a work period'
		return self._oleobj_.InvokeTypes(71, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 1), (12, 1)),Day
			, PeriodNumber, StartTime, EndTime)

	# The method StartPeriod is actually a property, but must be used as a method to correctly pass the arguments
	def StartPeriod(self, Day=defaultNamedNotOptArg, PeriodNumber=defaultNamedNotOptArg):
		'Gets the start time of the period'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(72, LCID, 2, (8, 0), ((3, 1), (12, 1)),Day
			, PeriodNumber)

	def Step(self):
		'method Step'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	def Stop(self):
		'method Stop'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def SyncBegin(self):
		'Restarts the model at its start simulation time. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(58, LCID, 1, (24, 0), (),)

	def SyncLoad(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
		'Loads a Witness model from file. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, FileType)

	def SyncNew(self):
		'Clears the model of all its elements. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (24, 0), (),)

	def SyncRun(self, StopTime=defaultNamedNotOptArg):
		'Runs the model (with animation) up to the stop time. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (24, 0), ((12, 1),),StopTime
			)

	def SyncRunBatch(self, StopTime=defaultNamedNotOptArg):
		'Runs the model (without animation) up to the stop time. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (24, 0), ((12, 1),),StopTime
			)

	def SyncSave(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
		'Saves a Witness model to file. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(63, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, FileType)

	def SyncStep(self):
		'Will perform a run step in synchronized mode'
		return self._oleobj_.InvokeTypes(66, LCID, 1, (24, 0), (),)

	def SyncStop(self):
		'Stops the model running. This method does not return until this operation is complete.'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'AllUserElements' returns object of type 'IWElements'
		"AllUserElements": (85, 2, (9, 0), (), "AllUserElements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'),
		# Method 'Application' returns object of type 'IWApplication'
		"Application": (1, 2, (9, 0), (), "Application", '{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}'),
		# Method 'Assemble' returns object of type 'IWAssemble'
		"Assemble": (19, 2, (9, 0), (), "Assemble", '{108615F0-4DBE-4D4C-826B-C606578491BA}'),
		"Author": (12, 2, (8, 0), (), "Author", None),
		# Method 'Backdrop' returns object of type 'IWBackdrop'
		"Backdrop": (21, 2, (9, 0), (), "Backdrop", '{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}'),
		"BaseTimeUnit": (68, 2, (3, 0), (), "BaseTimeUnit", None),
		"BatchTimeIncrement": (48, 2, (8, 0), (), "BatchTimeIncrement", None),
		"BidirectionalPaths": (37, 2, (11, 0), (), "BidirectionalPaths", None),
		# Method 'BreakdownFactors' returns object of type 'IWFactors'
		"BreakdownFactors": (92, 2, (9, 0), (), "BreakdownFactors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
		"BufferedWalkGraphics": (45, 2, (11, 0), (), "BufferedWalkGraphics", None),
		"ClockDisplay": (76, 2, (3, 0), (), "ClockDisplay", None),
		"ClockNotes": (70, 2, (8, 0), (), "ClockNotes", None),
		"CompleteActions": (88, 2, (8, 0), (), "CompleteActions", None),
		"CurrentTime": (22, 2, (5, 0), (), "CurrentTime", None),
		"DataLoadActions": (90, 2, (8, 0), (), "DataLoadActions", None),
		"DataSaveActions": (89, 2, (8, 0), (), "DataSaveActions", None),
		# Method 'Directories' returns object of type 'IWDirectories'
		"Directories": (81, 2, (9, 0), (), "Directories", '{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}'),
		"Directory": (67, 2, (8, 0), (), "Directory", None),
		# Method 'Elements' returns object of type 'IWElements'
		"Elements": (0, 2, (9, 0), (), "Elements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'),
		"EnableDebugging": (95, 2, (11, 0), (), "EnableDebugging", None),
		"EventFlags": (77, 2, (3, 0), (), "EventFlags", None),
		"FastestRoute": (40, 2, (11, 0), (), "FastestRoute", None),
		# Method 'Graphics' returns object of type 'IWGraphics'
		"Graphics": (56, 2, (9, 0), (), "Graphics", '{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}'),
		"HeartBeatPeriod": (78, 2, (3, 0), (), "HeartBeatPeriod", None),
		"InitializeActions": (34, 2, (8, 0), (), "InitializeActions", None),
		"LaborWalkToIdle": (41, 2, (11, 0), (), "LaborWalkToIdle", None),
		"LaborWalkToMoveParts": (42, 2, (11, 0), (), "LaborWalkToMoveParts", None),
		# Method 'Measures' returns object of type 'IWModelMeasures'
		"Measures": (86, 2, (9, 0), (), "Measures", '{B3951062-2E8D-407D-ABBD-D57FB4FAE705}'),
		"ModelCompleteAt": (87, 2, (8, 0), (), "ModelCompleteAt", None),
		"ModelTimeEventUpdateInterval": (83, 2, (3, 0), (), "ModelTimeEventUpdateInterval", None),
		"MultiplePathRouting": (39, 2, (11, 0), (), "MultiplePathRouting", None),
		"Name": (2, 2, (8, 0), (), "Name", None),
		# Method 'None' returns object of type 'IWNone'
		"NONE": (15, 2, (9, 0), (), "None", '{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}'),
		"Notes": (13, 2, (8, 0), (), "Notes", None),
		"PseudoPathTraverseTime": (43, 2, (12, 0), (), "PseudoPathTraverseTime", None),
		"PseudoPathUpdateInterval": (44, 2, (12, 0), (), "PseudoPathUpdateInterval", None),
		"PseudoPaths": (38, 2, (11, 0), (), "PseudoPaths", None),
		"Replication": (82, 2, (3, 0), (), "Replication", None),
		# Method 'Route' returns object of type 'IWRoute'
		"Route": (20, 2, (9, 0), (), "Route", '{6A8123E6-FF3B-4502-AF3F-243AC818B17C}'),
		"RunTimeIncrement": (47, 2, (8, 0), (), "RunTimeIncrement", None),
		# Method 'Sample' returns object of type 'IWSample'
		"Sample": (14, 2, (9, 0), (), "Sample", '{F079D83C-D0A1-413D-9CC2-D64317021122}'),
		"Saved": (23, 2, (11, 0), (), "Saved", None),
		"Scenario": (91, 2, (8, 0), (), "Scenario", None),
		# Method 'Scrap' returns object of type 'IWScrap'
		"Scrap": (17, 2, (9, 0), (), "Scrap", '{38FB81B4-8091-4A39-8041-56C31FDA7BD0}'),
		# Method 'SetupFactors' returns object of type 'IWFactors'
		"SetupFactors": (93, 2, (9, 0), (), "SetupFactors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
		# Method 'Ship' returns object of type 'IWShip'
		"Ship": (16, 2, (9, 0), (), "Ship", '{81E22460-8112-472B-9E14-96153261E6E0}'),
		"SimbaActions": (53, 2, (8, 0), (), "SimbaActions", None),
		"StartDate": (69, 2, (8, 0), (), "StartDate", None),
		"StartTime": (50, 2, (8, 0), (), "StartTime", None),
		"TimeNow": (54, 2, (5, 0), (), "TimeNow", None),
		"TimeOfNextEvent": (51, 2, (5, 0), (), "TimeOfNextEvent", None),
		"TimeScaleFactor": (46, 2, (8, 0), (), "TimeScaleFactor", None),
		"Title": (11, 2, (8, 0), (), "Title", None),
		# Method 'Types' returns object of type 'IWTypes'
		"Types": (3, 2, (9, 0), (), "Types", '{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}'),
		"UserActions": (35, 2, (8, 0), (), "UserActions", None),
		# Method 'WPMElements' returns object of type 'IWElements'
		"WPMElements": (80, 2, (9, 0), (), "WPMElements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'),
		"WalkMode": (49, 2, (11, 0), (), "WalkMode", None),
		"WarmupPeriod": (36, 2, (8, 0), (), "WarmupPeriod", None),
		# Method 'World' returns object of type 'IWWorld'
		"World": (18, 2, (9, 0), (), "World", '{861CABEB-E70F-4879-AEA6-079D1B13BC1E}'),
	}
	_prop_map_put_ = {
		"Author": ((12, LCID, 4, 0),()),
		"BaseTimeUnit": ((68, LCID, 4, 0),()),
		"BatchTimeIncrement": ((48, LCID, 4, 0),()),
		"BidirectionalPaths": ((37, LCID, 4, 0),()),
		"BufferedWalkGraphics": ((45, LCID, 4, 0),()),
		"ClockDisplay": ((76, LCID, 4, 0),()),
		"ClockNotes": ((70, LCID, 4, 0),()),
		"CompleteActions": ((88, LCID, 4, 0),()),
		"DataLoadActions": ((90, LCID, 4, 0),()),
		"DataSaveActions": ((89, LCID, 4, 0),()),
		"EnableDebugging": ((95, LCID, 4, 0),()),
		"EventFlags": ((77, LCID, 4, 0),()),
		"FastestRoute": ((40, LCID, 4, 0),()),
		"HeartBeatPeriod": ((78, LCID, 4, 0),()),
		"InitializeActions": ((34, LCID, 4, 0),()),
		"LaborWalkToIdle": ((41, LCID, 4, 0),()),
		"LaborWalkToMoveParts": ((42, LCID, 4, 0),()),
		"ModelCompleteAt": ((87, LCID, 4, 0),()),
		"ModelTimeEventUpdateInterval": ((83, LCID, 4, 0),()),
		"MultiplePathRouting": ((39, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((13, LCID, 4, 0),()),
		"PseudoPathTraverseTime": ((43, LCID, 4, 0),()),
		"PseudoPathUpdateInterval": ((44, LCID, 4, 0),()),
		"PseudoPaths": ((38, LCID, 4, 0),()),
		"Replication": ((82, LCID, 4, 0),()),
		"RunTimeIncrement": ((47, LCID, 4, 0),()),
		"Saved": ((23, LCID, 4, 0),()),
		"Scenario": ((91, LCID, 4, 0),()),
		"SimbaActions": ((53, LCID, 4, 0),()),
		"StartDate": ((69, LCID, 4, 0),()),
		"StartTime": ((50, LCID, 4, 0),()),
		"TimeScaleFactor": ((46, LCID, 4, 0),()),
		"Title": ((11, LCID, 4, 0),()),
		"UserActions": ((35, LCID, 4, 0),()),
		"WalkMode": ((49, LCID, 4, 0),()),
		"WarmupPeriod": ((36, LCID, 4, 0),()),
	}
	# Default property for this class is 'Elements'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Elements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWModelEventManager(DispatchBaseClass):
	'IWModelEventManager Interface'
	CLSID = IID('{D8396D00-CC33-47E7-A917-1527DF798EC5}')
	coclass_clsid = IID('{012AE1FD-9E78-4E20-8922-2C6F51E24BFF}')

	_prop_map_get_ = {
		"EventFlags": (1, 2, (3, 0), (), "EventFlags", None),
	}
	_prop_map_put_ = {
		"EventFlags": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWModelMeasure(DispatchBaseClass):
	'IWModelMeasure Interface'
	CLSID = IID('{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}')
	coclass_clsid = IID('{1C98A595-B908-4D1B-9D3D-0D5BA37A1AD3}')

	_prop_map_get_ = {
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Unit": (2, 2, (8, 0), (), "Unit", None),
	}
	_prop_map_put_ = {
		"Name": ((1, LCID, 4, 0),()),
		"Unit": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWModelMeasures(DispatchBaseClass):
	'IWModelMeasures Interface'
	CLSID = IID('{B3951062-2E8D-407D-ABBD-D57FB4FAE705}')
	coclass_clsid = IID('{FE7DAABD-B1F4-4E34-A4DC-334D58DBBE22}')

	def Add(self, Name=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Name
			, Position)

	# Result is of type IWModelMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Currency": (4, 2, (3, 0), (), "Currency", None),
	}
	_prop_map_put_ = {
		"Currency": ((4, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWModule(DispatchBaseClass):
	'IWModule Interface'
	CLSID = IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')
	coclass_clsid = IID('{633281B9-946E-467F-BCB5-03FD7F467FB3}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	# The method AverageNumberOfPartsIn is actually a property, but must be used as a method to correctly pass the arguments
	def AverageNumberOfPartsIn(self, OnShiftTime=defaultNamedNotOptArg):
		'property AverageNumberOfPartsIn'
		return self._oleobj_.InvokeTypes(113, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	# The method AveragePartTime is actually a property, but must be used as a method to correctly pass the arguments
	def AveragePartTime(self, OnShiftTime=defaultNamedNotOptArg):
		'property AveragePartTime'
		return self._oleobj_.InvokeTypes(114, LCID, 2, (5, 0), ((11, 1),),OnShiftTime
			)

	def Load(self, FileName=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def LoadXML(self, FileName=defaultNamedNotOptArg):
		'method Load .wxmdl'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, Part=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(116, LCID, 2, (3, 0), ((12, 1),),Part
			)

	# Result is of type IWPartInstance
	def RemovePart(self):
		'method RemovePart'
		ret = self._oleobj_.InvokeTypes(119, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePart', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	# Result is of type IWPartInstance
	def RemovePartOfType(self, Part=defaultNamedNotOptArg):
		'method RemovePartOfType'
		ret = self._oleobj_.InvokeTypes(120, LCID, 1, (9, 0), ((12, 1),),Part
			)
		if ret is not None:
			ret = Dispatch(ret, 'RemovePartOfType', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def Save(self, FileName=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SaveXML(self, FileName=defaultNamedNotOptArg):
		'method Save .wxmdl'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetPassword(self, OldPassword=defaultNamedNotOptArg, NewPassword=defaultNamedNotOptArg):
		'method SetPassword'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((8, 1), (8, 1)),OldPassword
			, NewPassword)

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"CycleTime": (111, 2, (12, 0), (), "CycleTime", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		# Method 'Elements' returns object of type 'IWElements'
		"Elements": (0, 2, (9, 0), (), "Elements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputElement": (104, 2, (12, 0), (), "InputElement", None),
		"InputRule": (106, 2, (8, 0), (), "InputRule", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfParts": (115, 2, (3, 0), (), "NumberOfParts", None),
		"OutputElement": (105, 2, (12, 0), (), "OutputElement", None),
		"OutputRule": (107, 2, (8, 0), (), "OutputRule", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Reporting": (109, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"Title": (108, 2, (8, 0), (), "Title", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		# Method 'Types' returns object of type 'IWTypes'
		"Types": (101, 2, (9, 0), (), "Types", '{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}'),
		"UseCycleTime": (110, 2, (11, 0), (), "UseCycleTime", None),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		"WalkToModule": (112, 2, (11, 0), (), "WalkToModule", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"CycleTime": ((111, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"InputElement": ((104, LCID, 4, 0),()),
		"InputRule": ((106, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputElement": ((105, LCID, 4, 0),()),
		"OutputRule": ((107, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((109, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"Title": ((108, LCID, 4, 0),()),
		"UseCycleTime": ((110, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
		"WalkToModule": ((112, LCID, 4, 0),()),
	}
	# Default property for this class is 'Elements'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Elements", '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWModuleType(DispatchBaseClass):
	'IWModuleType Interface'
	CLSID = IID('{13523CD8-B0AD-46D1-B2AF-F1F2152085F0}')
	coclass_clsid = IID('{EB08BC01-B2BD-4537-902C-BFD50AD8DFD2}')

	# Result is of type IWModule
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{E4B4D340-1397-4A21-9F52-BB258A913C1A}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWNetwork(DispatchBaseClass):
	'IWNetwork Interface'
	CLSID = IID('{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')
	coclass_clsid = IID('{CBF157ED-DEEC-4462-9C2C-C21FA91B7260}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"NetworkType": (102, 2, (3, 0), (), "NetworkType", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"Priority": (101, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Reporting": (104, 2, (3, 0), (), "Reporting", None),
		"ShiftName": (103, 2, (12, 0), (), "ShiftName", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"NetworkType": ((102, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((101, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((104, LCID, 4, 0),()),
		"ShiftName": ((103, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWNetworkType(DispatchBaseClass):
	'IWNetworkType Interface'
	CLSID = IID('{50443F6F-692C-4F31-B5AE-939CDC74A977}')
	coclass_clsid = IID('{79828EE4-5DD9-4A41-ADC3-9E734F38796F}')

	# Result is of type IWNetwork
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWNone(DispatchBaseClass):
	'IWNone Interface'
	CLSID = IID('{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}')
	coclass_clsid = IID('{5353FA8F-7EE3-428C-ACB7-B007171BCCB5}')

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPart(DispatchBaseClass):
	'IWPart Interface'
	CLSID = IID('{C641E7A1-817B-40FA-849E-7956F1C1A846}')
	coclass_clsid = IID('{3B8D4948-C4B3-4754-987D-DA0814438115}')

	# The method AverageTime is actually a property, but must be used as a method to correctly pass the arguments
	def AverageTime(self, ShiftTime=defaultNamedNotOptArg):
		'property AverageTime'
		return self._oleobj_.InvokeTypes(129, LCID, 2, (5, 0), ((11, 1),),ShiftTime
			)

	# The method AverageWorkInProgress is actually a property, but must be used as a method to correctly pass the arguments
	def AverageWorkInProgress(self, ShiftTime=defaultNamedNotOptArg):
		'property AverageWorkInProgress'
		return self._oleobj_.InvokeTypes(128, LCID, 2, (5, 0), ((11, 1),),ShiftTime
			)

	# Result is of type IWPartInstance
	def CreateInstance(self):
		'method CreateInstance'
		ret = self._oleobj_.InvokeTypes(133, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateInstance', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def ProfileImport(self, Path=defaultNamedNotOptArg):
		'method ProfileImport'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((8, 1),),Path
			)

	_prop_map_get_ = {
		"ActionsOnCreate": (102, 2, (8, 0), (), "ActionsOnCreate", None),
		"ActionsOnFixedAttributes": (111, 2, (8, 0), (), "ActionsOnFixedAttributes", None),
		"ActionsOnLeave": (103, 2, (8, 0), (), "ActionsOnLeave", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"ArrivalType": (101, 2, (3, 0), (), "ArrivalType", None),
		"AverageTime2": (132, 2, (5, 0), (), "AverageTime2", None),
		"AverageWorkInProgress2": (131, 2, (5, 0), (), "AverageWorkInProgress2", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"ContainsFluid": (112, 2, (11, 0), (), "ContainsFluid", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"FirstArrivalAt": (105, 2, (12, 0), (), "FirstArrivalAt", None),
		"FixedAttributeValues": (110, 2, (11, 0), (), "FixedAttributeValues", None),
		"GroupNumber": (113, 2, (12, 0), (), "GroupNumber", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"InputToModelRule": (109, 2, (8, 0), (), "InputToModelRule", None),
		"InterArrivalTime": (107, 2, (12, 0), (), "InterArrivalTime", None),
		"LotSize": (108, 2, (12, 0), (), "LotSize", None),
		"MaximumArrivals": (104, 2, (12, 0), (), "MaximumArrivals", None),
		# Method 'Measures' returns object of type 'IWPartMeasures'
		"Measures": (134, 2, (9, 0), (), "Measures", '{B9E729DD-60D2-4F45-9358-3C8047008411}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberAssembled": (130, 2, (3, 0), (), "NumberAssembled", None),
		"NumberEntered": (123, 2, (3, 0), (), "NumberEntered", None),
		"NumberRejected": (126, 2, (3, 0), (), "NumberRejected", None),
		"NumberScrapped": (125, 2, (3, 0), (), "NumberScrapped", None),
		"NumberShipped": (124, 2, (3, 0), (), "NumberShipped", None),
		# Method 'PartRouteStages' returns object of type 'IWPartRouteStages'
		"PartRouteStages": (114, 2, (9, 0), (), "PartRouteStages", '{DEC15362-502E-11D5-9BD3-00E0295CD2CC}'),
		"ProfileCumulativeTime": (121, 2, (11, 0), (), "ProfileCumulativeTime", None),
		# Method 'ProfileEntries' returns object of type 'IWPartArrivalProfileEntries'
		"ProfileEntries": (116, 2, (9, 0), (), "ProfileEntries", '{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}'),
		"ProfileMultiplier": (118, 2, (12, 0), (), "ProfileMultiplier", None),
		"ProfileRandomNumberStream": (119, 2, (3, 0), (), "ProfileRandomNumberStream", None),
		"ProfileSmoothing": (120, 2, (11, 0), (), "ProfileSmoothing", None),
		"ProfileTimeDisplay": (117, 2, (3, 0), (), "ProfileTimeDisplay", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Reporting": (115, 2, (3, 0), (), "Reporting", None),
		"Shift": (106, 2, (12, 0), (), "Shift", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		"WorkInProgress": (127, 2, (3, 0), (), "WorkInProgress", None),
	}
	_prop_map_put_ = {
		"ActionsOnCreate": ((102, LCID, 4, 0),()),
		"ActionsOnFixedAttributes": ((111, LCID, 4, 0),()),
		"ActionsOnLeave": ((103, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"ArrivalType": ((101, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"ContainsFluid": ((112, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"FirstArrivalAt": ((105, LCID, 4, 0),()),
		"FixedAttributeValues": ((110, LCID, 4, 0),()),
		"GroupNumber": ((113, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"InputToModelRule": ((109, LCID, 4, 0),()),
		"InterArrivalTime": ((107, LCID, 4, 0),()),
		"LotSize": ((108, LCID, 4, 0),()),
		"MaximumArrivals": ((104, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"ProfileCumulativeTime": ((121, LCID, 4, 0),()),
		"ProfileMultiplier": ((118, LCID, 4, 0),()),
		"ProfileRandomNumberStream": ((119, LCID, 4, 0),()),
		"ProfileSmoothing": ((120, LCID, 4, 0),()),
		"ProfileTimeDisplay": ((117, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((115, LCID, 4, 0),()),
		"Shift": ((106, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartArrivalProfileEntries(DispatchBaseClass):
	'IWPartArrivalProfileEntries Interface'
	CLSID = IID('{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}')
	coclass_clsid = IID('{D3E84445-58CB-11D5-9BDB-00E0295CD2CC}')

	def Add(self, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1),),Position
			)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPartArrivalProfileEntry(DispatchBaseClass):
	'IWPartArrivalProfileEntry Interface'
	CLSID = IID('{D3E84441-58CB-11D5-9BDB-00E0295CD2CC}')
	coclass_clsid = IID('{D3E84444-58CB-11D5-9BDB-00E0295CD2CC}')

	_prop_map_get_ = {
		"CumulativeTime": (4, 2, (12, 0), (), "CumulativeTime", None),
		"Length": (1, 2, (12, 0), (), "Length", None),
		"Time": (3, 2, (12, 0), (), "Time", None),
		"Volume": (2, 2, (12, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"Length": ((1, LCID, 4, 0),()),
		"Volume": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartFile(DispatchBaseClass):
	'IWPartFile Interface'
	CLSID = IID('{4C079D1F-F67E-41E5-B770-116E257E6C7C}')
	coclass_clsid = IID('{FDEE5D65-1237-4785-A2B2-F415E6EAC8A5}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"FileName": (101, 2, (8, 0), (), "FileName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"FileName": ((101, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartFileType(DispatchBaseClass):
	'IWPartFileType Interface'
	CLSID = IID('{134FB1F0-5BF0-4678-B815-4042AF976628}')
	coclass_clsid = IID('{9D440E35-55C8-4A09-849E-4E6C16D11A26}')

	# Result is of type IWPartFile
	def Define(self, Name=defaultNamedNotOptArg, fileMode=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (3, 1)),Name
			, fileMode)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{4C079D1F-F67E-41E5-B770-116E257E6C7C}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartInstance(DispatchBaseClass):
	'IWPartInstance Interface'
	CLSID = IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')
	coclass_clsid = IID('{E8B55477-6F44-4C74-BB6F-383D7FCE0841}')

	_prop_map_get_ = {
		"Contents": (6, 2, (12, 0), (), "Contents", None),
		"CurrentStage": (8, 2, (12, 0), (), "CurrentStage", None),
		"Desc": (3, 2, (12, 0), (), "Desc", None),
		"Fluid": (7, 2, (12, 0), (), "Fluid", None),
		"Icon": (5, 2, (12, 0), (), "Icon", None),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'Part' returns object of type 'IWPart'
		"Part": (1, 2, (9, 0), (), "Part", '{C641E7A1-817B-40FA-849E-7956F1C1A846}'),
		"Pen": (4, 2, (12, 0), (), "Pen", None),
		"RoutingCycleTime": (10, 2, (12, 0), (), "RoutingCycleTime", None),
		"RoutingSetupTime": (11, 2, (12, 0), (), "RoutingSetupTime", None),
		"TotalNumberOfStages": (9, 2, (12, 0), (), "TotalNumberOfStages", None),
		"TypeName": (2, 2, (8, 0), (), "TypeName", None),
		# Method 'UserAttributes' returns object of type 'IWAttributeInstances'
		"UserAttributes": (12, 2, (9, 0), (), "UserAttributes", '{427F8FA2-0EEE-11D5-8579-0020AFF488A2}'),
	}
	_prop_map_put_ = {
		"Contents": ((6, LCID, 4, 0),()),
		"CurrentStage": ((8, LCID, 4, 0),()),
		"Desc": ((3, LCID, 4, 0),()),
		"Fluid": ((7, LCID, 4, 0),()),
		"Icon": ((5, LCID, 4, 0),()),
		"Pen": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartInstances(DispatchBaseClass):
	'IWPartInstances Interface'
	CLSID = IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')
	coclass_clsid = IID('{63D176D2-0331-11D5-9B89-00E0295CD2CC}')

	# Result is of type IWPartInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{10538218-737F-44BF-BBC4-7B169F983E1B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{10538218-737F-44BF-BBC4-7B169F983E1B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPartMeasure(DispatchBaseClass):
	'IWPartMeasure Interface'
	CLSID = IID('{3569B25C-2E41-4F11-AB30-2D112546D800}')
	coclass_clsid = IID('{786649BA-17B5-4A15-95AD-FB2109E28BF3}')

	_prop_map_get_ = {
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"PerCreate": (2, 2, (12, 0), (), "PerCreate", None),
		"PerScrapped": (4, 2, (12, 0), (), "PerScrapped", None),
		"PerShipped": (3, 2, (12, 0), (), "PerShipped", None),
	}
	_prop_map_put_ = {
		"PerCreate": ((2, LCID, 4, 0),()),
		"PerScrapped": ((4, LCID, 4, 0),()),
		"PerShipped": ((3, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartMeasures(DispatchBaseClass):
	'IWPartMeasures Interface'
	CLSID = IID('{B9E729DD-60D2-4F45-9358-3C8047008411}')
	coclass_clsid = IID('{B96C1292-8AC4-4486-B26A-29D2A1F5E43C}')

	# Result is of type IWPartMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the part measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{3569B25C-2E41-4F11-AB30-2D112546D800}')
		return ret

	# Result is of type IWPartMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3569B25C-2E41-4F11-AB30-2D112546D800}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the part measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3569B25C-2E41-4F11-AB30-2D112546D800}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{3569B25C-2E41-4F11-AB30-2D112546D800}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPartRouteStage(DispatchBaseClass):
	'IWPartRouteStage Interface'
	CLSID = IID('{DEC15361-502E-11D5-9BD3-00E0295CD2CC}')
	coclass_clsid = IID('{2F373901-5042-11D5-9BD3-00E0295CD2CC}')

	_prop_map_get_ = {
		"Destination": (1, 2, (8, 0), (), "Destination", None),
		"R_CYCLE": (3, 2, (12, 0), (), "R_CYCLE", None),
		"R_SETUP": (2, 2, (12, 0), (), "R_SETUP", None),
		"Stage": (0, 2, (3, 0), (), "Stage", None),
	}
	_prop_map_put_ = {
		"Destination": ((1, LCID, 4, 0),()),
		"R_CYCLE": ((3, LCID, 4, 0),()),
		"R_SETUP": ((2, LCID, 4, 0),()),
	}
	# Default property for this class is 'Stage'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Stage", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPartRouteStages(DispatchBaseClass):
	'IWPartRouteStages Interface'
	CLSID = IID('{DEC15362-502E-11D5-9BD3-00E0295CD2CC}')
	coclass_clsid = IID('{2F373902-5042-11D5-9BD3-00E0295CD2CC}')

	def Add(self, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1),),Position
			)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPartType(DispatchBaseClass):
	'IWPartType Interface'
	CLSID = IID('{E2C6802B-8E63-4E50-AB64-B871071A779B}')
	coclass_clsid = IID('{E252C7AF-6108-4A67-B9AB-A3DFFE45028C}')

	# Result is of type IWPart
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{C641E7A1-817B-40FA-849E-7956F1C1A846}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPath(DispatchBaseClass):
	'IWPath Interface'
	CLSID = IID('{FDB0A591-25D9-44EC-AB08-783742063AA7}')
	coclass_clsid = IID('{9076164B-7A90-4335-AB5F-8BCB6846564E}')

	# The method NumberOfLabor is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfLabor(self, Labor=defaultNamedNotOptArg):
		'property NumberOfLabor'
		return self._oleobj_.InvokeTypes(118, LCID, 2, (3, 0), ((9, 1),),Labor
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, ShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(111, LCID, 2, (5, 0), ((3, 1), (11, 1)),State
			, ShiftTime)

	# The method TimeLeft is actually a property, but must be used as a method to correctly pass the arguments
	def TimeLeft(self, Position=defaultNamedNotOptArg):
		'property TimeLeft'
		return self._oleobj_.InvokeTypes(112, LCID, 2, (5, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"ActionsOnEntry": (104, 2, (8, 0), (), "ActionsOnEntry", None),
		"ActionsOnLeave": (105, 2, (8, 0), (), "ActionsOnLeave", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (16, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (17, 2, (8, 0), (), "DescriptiveName", None),
		"DestinationElement": (103, 2, (12, 0), (), "DestinationElement", None),
		# Method 'Destinations' returns object of type 'IWPathElementExpressions'
		"Destinations": (15, 2, (9, 0), (), "Destinations", '{AB588585-190B-4830-BB71-A88D92BA8451}'),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'InstancesOnPath' returns object of type 'IWInstances'
		"InstancesOnPath": (119, 2, (9, 0), (), "InstancesOnPath", '{83073E66-7AF6-46C0-89D2-F33E7C972377}'),
		"LaborIn": (109, 2, (3, 0), (), "LaborIn", None),
		"LaborOut": (110, 2, (3, 0), (), "LaborOut", None),
		"Length": (113, 2, (3, 0), (), "Length", None),
		# Method 'Measures' returns object of type 'IWPathMeasures'
		"Measures": (120, 2, (9, 0), (), "Measures", '{595E1B97-E9E7-465E-AF63-A243735FB187}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfParts": (117, 2, (3, 0), (), "NumberOfParts", None),
		"PartsIn": (107, 2, (3, 0), (), "PartsIn", None),
		"PartsOut": (108, 2, (3, 0), (), "PartsOut", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Reporting": (106, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"SourceElement": (102, 2, (12, 0), (), "SourceElement", None),
		# Method 'Sources' returns object of type 'IWPathElementExpressions'
		"Sources": (14, 2, (9, 0), (), "Sources", '{AB588585-190B-4830-BB71-A88D92BA8451}'),
		"TraverseTime": (100, 2, (12, 0), (), "TraverseTime", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UpdateInterval": (101, 2, (12, 0), (), "UpdateInterval", None),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnEntry": ((104, LCID, 4, 0),()),
		"ActionsOnLeave": ((105, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((16, LCID, 4, 0),()),
		"DescriptiveName": ((17, LCID, 4, 0),()),
		"DestinationElement": ((103, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((106, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"SourceElement": ((102, LCID, 4, 0),()),
		"TraverseTime": ((100, LCID, 4, 0),()),
		"UpdateInterval": ((101, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPathData(DispatchBaseClass):
	'IWPathData Interface'
	CLSID = IID('{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}')
	coclass_clsid = IID('{C34D5CEC-372F-4362-A4E9-0EF1991752AB}')

	# Result is of type IWPoints
	def Points(self):
		'method Points'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Points', '{D1227816-BAED-4DBB-8F28-B269E166A613}')
		return ret

	_prop_map_get_ = {
		"Center": (3, 2, (11, 0), (), "Center", None),
		"DashLine": (10, 2, (11, 0), (), "DashLine", None),
		"DisplaySize": (6, 2, (3, 0), (), "DisplaySize", None),
		"EndArrow": (9, 2, (3, 0), (), "EndArrow", None),
		"FixedLength": (13, 2, (5, 0), (), "FixedLength", None),
		"Hollow": (2, 2, (11, 0), (), "Hollow", None),
		"InnerWidth": (4, 2, (3, 0), (), "InnerWidth", None),
		"MultipleGraphicGap": (12, 2, (3, 0), (), "MultipleGraphicGap", None),
		"ShowLine": (1, 2, (11, 0), (), "ShowLine", None),
		"StartArrow": (8, 2, (3, 0), (), "StartArrow", None),
		"TravelAtSideOfPath": (11, 2, (11, 0), (), "TravelAtSideOfPath", None),
		"Width": (5, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Center": ((3, LCID, 4, 0),()),
		"DashLine": ((10, LCID, 4, 0),()),
		"DisplaySize": ((6, LCID, 4, 0),()),
		"EndArrow": ((9, LCID, 4, 0),()),
		"FixedLength": ((13, LCID, 4, 0),()),
		"Hollow": ((2, LCID, 4, 0),()),
		"InnerWidth": ((4, LCID, 4, 0),()),
		"MultipleGraphicGap": ((12, LCID, 4, 0),()),
		"ShowLine": ((1, LCID, 4, 0),()),
		"StartArrow": ((8, LCID, 4, 0),()),
		"TravelAtSideOfPath": ((11, LCID, 4, 0),()),
		"Width": ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPathElementExpression(DispatchBaseClass):
	'IWPathElementExpression Interface'
	CLSID = IID('{288D0178-6C4B-4ACF-A344-9553E6714BC5}')
	coclass_clsid = IID('{4700CB1B-4FB7-4938-BA2A-D034D88DE1CC}')

	_prop_map_get_ = {
		"Expression": (0, 2, (8, 0), (), "Expression", None),
	}
	_prop_map_put_ = {
		"Expression": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Expression'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Expression", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPathElementExpressions(DispatchBaseClass):
	'IWPathElementExpressions Interface'
	CLSID = IID('{AB588585-190B-4830-BB71-A88D92BA8451}')
	coclass_clsid = IID('{64AE4DE5-5F48-4B53-849C-4DA165E7ED42}')

	def Add(self, Expression=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'Adds a element expression at the specified position.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Expression
			, Position)

	# Result is of type IWPathElementExpression
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the element expression for the specified index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{288D0178-6C4B-4ACF-A344-9553E6714BC5}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'Removes the element expression at the specified position.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the element expression for the specified index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{288D0178-6C4B-4ACF-A344-9553E6714BC5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{288D0178-6C4B-4ACF-A344-9553E6714BC5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPathMeasure(DispatchBaseClass):
	'IWPathMeasure Interface'
	CLSID = IID('{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')
	coclass_clsid = IID('{BECF2229-7372-452D-9343-0FC2CC7586DB}')

	_prop_map_get_ = {
		# Method 'FixedUse' returns object of type 'IWMeasureValue'
		"FixedUse": (1, 2, (9, 0), (), "FixedUse", '{F357C6B3-3507-4611-96ED-3247D7C687D5}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPathMeasures(DispatchBaseClass):
	'IWPathMeasures Interface'
	CLSID = IID('{595E1B97-E9E7-465E-AF63-A243735FB187}')
	coclass_clsid = IID('{6E4938CE-EAB5-4977-BE54-350B9D31FA37}')

	# Result is of type IWPathMeasure
	def Add(self, Name=defaultNamedNotOptArg):
		'Adds a measure to the path measures.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')
		return ret

	# Result is of type IWPathMeasure
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes a measure from the path measures.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Gets the measure object for the specified one based index or measure name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPathType(DispatchBaseClass):
	'IWPathType Interface'
	CLSID = IID('{BB075195-E18A-4A35-81E4-05E94B6EFF23}')
	coclass_clsid = IID('{0855287B-E575-4AD8-8F87-BBFAA4EFB292}')

	# Result is of type IWPath
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{FDB0A591-25D9-44EC-AB08-783742063AA7}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPiechart(DispatchBaseClass):
	'IWPiechart Interface'
	CLSID = IID('{D160D6FC-8110-41E0-84E2-B1754FAF4596}')
	coclass_clsid = IID('{154A09BA-BEB3-4C2D-A140-E1851D239814}')

	# The method SegmentColor is actually a property, but must be used as a method to correctly pass the arguments
	def SegmentColor(self, Index=defaultNamedNotOptArg):
		'property SegmentColor'
		return self._oleobj_.InvokeTypes(103, LCID, 2, (3, 0), ((3, 1),),Index
			)

	# The method SegmentDescription is actually a property, but must be used as a method to correctly pass the arguments
	def SegmentDescription(self, Index=defaultNamedNotOptArg):
		'property SegmentDescription'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(101, LCID, 2, (8, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"ExtractedSegment": (102, 2, (3, 0), (), "ExtractedSegment", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPiechartType(DispatchBaseClass):
	'IWPiechartType Interface'
	CLSID = IID('{93DF3BB1-0CD3-45F9-B586-197112B69107}')
	coclass_clsid = IID('{F3E728B4-DFB3-443C-AA01-0DE929FB3070}')

	# Result is of type IWPiechart
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{D160D6FC-8110-41E0-84E2-B1754FAF4596}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPipe(DispatchBaseClass):
	'IWPipe Interface'
	CLSID = IID('{EBCA5DAE-76F3-4872-8247-EDD3CED57353}')
	coclass_clsid = IID('{6769DBE4-2DC3-46D8-846F-4A62A62B5B42}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWPipeBreakdowns'
		"Breakdowns": (105, 2, (9, 0), (), "Breakdowns", '{E0B23F84-C932-4AE3-B38D-52D982886FCD}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"Capacity": (103, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		# Method 'PipeInstances' returns object of type 'IWPipeInstances'
		"PipeInstances": (0, 2, (9, 0), (), "PipeInstances", '{60324619-F3C0-4114-9CA4-4DE9533A0849}'),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((103, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'PipeInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "PipeInstances", '{60324619-F3C0-4114-9CA4-4DE9533A0849}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPipeBreakdowns(DispatchBaseClass):
	'IWPipeBreakdowns Interface'
	CLSID = IID('{E0B23F84-C932-4AE3-B38D-52D982886FCD}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPipeInstance(DispatchBaseClass):
	'IWPipeInstance Interface'
	CLSID = IID('{E16C5044-7333-467A-98F1-579B48C09D3A}')
	coclass_clsid = IID('{C5CF2888-AEE4-4AD9-97E0-EA98A8942657}')

	_prop_map_get_ = {
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'Pipe' returns object of type 'IWPipe'
		"Pipe": (1, 2, (9, 0), (), "Pipe", '{EBCA5DAE-76F3-4872-8247-EDD3CED57353}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPipeInstances(DispatchBaseClass):
	'IWPipeInstances Interface'
	CLSID = IID('{60324619-F3C0-4114-9CA4-4DE9533A0849}')
	coclass_clsid = IID('{E02FA232-56F5-4402-82E0-D7CD11D86054}')

	# Result is of type IWPipeInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E16C5044-7333-467A-98F1-579B48C09D3A}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E16C5044-7333-467A-98F1-579B48C09D3A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E16C5044-7333-467A-98F1-579B48C09D3A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWPipeType(DispatchBaseClass):
	'IWPipeType Interface'
	CLSID = IID('{71E7EE98-8043-47F9-9549-0813E776E594}')
	coclass_clsid = IID('{B5B4C2B7-06B5-49A8-B5CC-A31E16620B3D}')

	# Result is of type IWPipe
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{EBCA5DAE-76F3-4872-8247-EDD3CED57353}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPoint(DispatchBaseClass):
	'IWPoint Interface'
	CLSID = IID('{C6034440-1A59-48D8-B463-43918B37FD28}')
	coclass_clsid = IID('{A82FD057-3F6F-4226-92D6-86B4986DE528}')

	_prop_map_get_ = {
		"X": (1, 2, (3, 0), (), "X", None),
		"Y": (2, 2, (3, 0), (), "Y", None),
	}
	_prop_map_put_ = {
		"X": ((1, LCID, 4, 0),()),
		"Y": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWPoints(DispatchBaseClass):
	'IWPoints Interface'
	CLSID = IID('{D1227816-BAED-4DBB-8F28-B269E166A613}')
	coclass_clsid = IID('{6EB0EC81-8790-42B4-BE70-E20DA6DEB0E9}')

	def Add(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	# Result is of type IWPoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C6034440-1A59-48D8-B463-43918B37FD28}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C6034440-1A59-48D8-B463-43918B37FD28}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C6034440-1A59-48D8-B463-43918B37FD28}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWProcessor(DispatchBaseClass):
	'IWProcessor Interface'
	CLSID = IID('{3E62686A-D9BF-464A-B478-DE8559513141}')
	coclass_clsid = IID('{56C71F23-499F-43DF-884E-0E2E0BFAC95F}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWProcessorBreakdowns'
		"Breakdowns": (105, 2, (9, 0), (), "Breakdowns", '{2B044458-8E03-4C1A-AFE5-362A39E4500C}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"Capacity": (103, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"ProcessTime": (104, 2, (12, 0), (), "ProcessTime", None),
		# Method 'ProcessorInstances' returns object of type 'IWProcessorInstances'
		"ProcessorInstances": (0, 2, (9, 0), (), "ProcessorInstances", '{4190AF59-9851-4ADB-8902-A809824D4621}'),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((103, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"ProcessTime": ((104, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'ProcessorInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "ProcessorInstances", '{4190AF59-9851-4ADB-8902-A809824D4621}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWProcessorBreakdowns(DispatchBaseClass):
	'IWProcessorBreakdowns Interface'
	CLSID = IID('{2B044458-8E03-4C1A-AFE5-362A39E4500C}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWProcessorInstance(DispatchBaseClass):
	'IWProcessorInstance Interface'
	CLSID = IID('{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}')
	coclass_clsid = IID('{ED6EF6BA-D94F-4610-A37E-C0F7741518BD}')

	_prop_map_get_ = {
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'Processor' returns object of type 'IWProcessor'
		"Processor": (1, 2, (9, 0), (), "Processor", '{3E62686A-D9BF-464A-B478-DE8559513141}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWProcessorInstances(DispatchBaseClass):
	'IWProcessorInstances Interface'
	CLSID = IID('{4190AF59-9851-4ADB-8902-A809824D4621}')
	coclass_clsid = IID('{6F167138-34BB-4CB8-AB40-458C91C0D08D}')

	# Result is of type IWProcessorInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWProcessorType(DispatchBaseClass):
	'IWProcessorType Interface'
	CLSID = IID('{20F7F5D9-FB97-4B74-8AA2-AE2AC48E47ED}')
	coclass_clsid = IID('{B6997BA0-F387-4C21-8939-FB6E4F79B8D1}')

	# Result is of type IWProcessor
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{3E62686A-D9BF-464A-B478-DE8559513141}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWRandomNumberCoverageBuckets(DispatchBaseClass):
	'IWRandomNumberCoverageBuckets Interface'
	CLSID = IID('{FF833377-93CB-45EB-A66D-E9C311E043C1}')
	coclass_clsid = None

	def Initialise(self, Stream=defaultNamedNotOptArg, subStream=defaultNamedNotOptArg, counts=defaultNamedNotOptArg):
		'Initialises the object'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((3, 1), (3, 1), (16396, 1)),Stream
			, subStream, counts)

	_prop_map_get_ = {
		"StreamIndex": (2, 2, (3, 0), (), "StreamIndex", None),
		"SubStreamIndex": (3, 2, (3, 0), (), "SubStreamIndex", None),
		"counts": (4, 2, (12, 0), (), "counts", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWRandomNumberCoverageBucketsCollection(DispatchBaseClass):
	'IWRandomNumberCoverageBucketsCollection Interface'
	CLSID = IID('{752CA6D4-E88D-4BFF-9638-8B0334C04667}')
	coclass_clsid = None

	# Result is of type IWRandomNumberCoverageBuckets
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Returns the buckets object for the given replication.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FF833377-93CB-45EB-A66D-E9C311E043C1}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Returns the buckets object for the given replication.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FF833377-93CB-45EB-A66D-E9C311E043C1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FF833377-93CB-45EB-A66D-E9C311E043C1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWRandomNumberUsage(DispatchBaseClass):
	'IWRandomNumberUsage Interface'
	CLSID = IID('{30DD08CA-7835-4684-9C1B-46674D674204}')
	coclass_clsid = IID('{968F15BB-1051-4D51-A001-9AB3C62127B1}')

	_prop_map_get_ = {
		# Method 'CoverageBuckets' returns object of type 'IWRandomNumberCoverageBucketsCollection'
		"CoverageBuckets": (2, 2, (9, 0), (), "CoverageBuckets", '{752CA6D4-E88D-4BFF-9638-8B0334C04667}'),
		# Method 'Report' returns object of type 'IWReportData'
		"Report": (1, 2, (9, 0), (), "Report", '{27865A7B-1F7C-4449-957B-D6FDB0BD4052}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWRemoteControl(DispatchBaseClass):
	'Remote Control Interface'
	CLSID = IID('{92D0A727-28A1-4682-A1B2-90BFF5677814}')
	coclass_clsid = IID('{340F5316-1C07-4BB9-8588-8AF9083B45F9}')

	def BackupModel(self, modelPath=defaultNamedNotOptArg):
		'Save the model into a backup mod file'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),modelPath
			)

	_prop_map_get_ = {
		"WclControl": (1, 2, (9, 0), (), "WclControl", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWReport(DispatchBaseClass):
	'IWReport Interface'
	CLSID = IID('{55A4116E-D4E0-4547-8349-AD733DC01C16}')
	coclass_clsid = IID('{84B06A15-3DC4-479F-9F50-28A1F635E897}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWReportData(DispatchBaseClass):
	'IWReportData Interface'
	CLSID = IID('{27865A7B-1F7C-4449-957B-D6FDB0BD4052}')
	coclass_clsid = IID('{04B51A36-E475-47B9-A2CC-ED44D69CBD9C}')

	_prop_map_get_ = {
		"Columns": (1, 2, (12, 0), (), "Columns", None),
		"Data": (2, 2, (12, 0), (), "Data", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWReportType(DispatchBaseClass):
	'IWReportType Interface'
	CLSID = IID('{55FDA6EA-CBF6-4D1D-9CB0-BF7B82A6BC92}')
	coclass_clsid = IID('{4C208E8A-EC47-42BF-A80F-4705A0825A55}')

	# Result is of type IWReport
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{55A4116E-D4E0-4547-8349-AD733DC01C16}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWResponses(DispatchBaseClass):
	'IWResponses Interface'
	CLSID = IID('{21F414EA-AF00-451A-BBF5-D53BF2A8DB7C}')
	coclass_clsid = IID('{86113396-D5B6-4284-8AED-9F647A6A0CAB}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lnIndex=defaultNamedNotOptArg):
		'property Item'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),lnIndex
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Default": (5, 2, (3, 0), (), "Default", None),
		"Response": (6, 2, (3, 0), (), "Response", None),
	}
	_prop_map_put_ = {
		"Default": ((5, LCID, 4, 0),()),
		"Response": ((6, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, lnIndex=defaultNamedNotOptArg):
		'property Item'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),lnIndex
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWRoute(DispatchBaseClass):
	'IWRoute Interface'
	CLSID = IID('{6A8123E6-FF3B-4502-AF3F-243AC818B17C}')
	coclass_clsid = IID('{96F46E30-9B89-4666-9264-B669FDA8E197}')

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSample(DispatchBaseClass):
	'IWSample Interface'
	CLSID = IID('{F079D83C-D0A1-413D-9CC2-D64317021122}')
	coclass_clsid = IID('{988F0373-AFE4-456C-A3F1-B57685ECBD7D}')

	def Antithetic(self, Stream=defaultNamedNotOptArg, On=defaultNamedNotOptArg):
		'method Antithetic : Enables antithetic number generation (1-n), against the specified stream. Default is false. WARNING : Avoid/ Take special care using a stream allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1), (11, 1)),Stream
			, On)

	def Beta(self, Shape=defaultNamedNotOptArg, Scale=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Beta : Returns values from the detailed Beta distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Shape
			, Scale, Stream)

	def Binomial(self, Probability=defaultNamedNotOptArg, NumTrials=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Binomial : Returns values from the detailed Binomial distribution, using the stream specified.: Probability must be (0.0 to 1) : Number of trials (must be +ve). WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((5, 1), (3, 1), (3, 1)),Probability
			, NumTrials, Stream)

	def Erlang(self, Mean=defaultNamedNotOptArg, K=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Erlang : Returns values from the detailed Erlang distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (5, 0), ((5, 1), (3, 1), (3, 1)),Mean
			, K, Stream)

	def Gamma(self, Shape=defaultNamedNotOptArg, Scale=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Gamma : Returns values from the detailed Gamma distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Shape
			, Scale, Stream)

	def IUniform(self, Lowest=defaultNamedNotOptArg, Highest=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method IUniform : Returns Integer values from the detailed Uniform distribution defined by integer limits, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1)),Lowest
			, Highest, Stream)

	def Initialise(self, Stream=defaultNamedNotOptArg, NumberOfObservationsToSkip=defaultNamedNotOptArg):
		'method Initialise : Resets the Stream or all Streams by passing 0 for the Stream parameter. Can be used to wind into the stream for experimentation.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1), (3, 1)),Stream
			, NumberOfObservationsToSkip)

	def LogNormal(self, Mean=defaultNamedNotOptArg, StdDeviation=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method LogNormal : Returns values from the detailed Log Normal distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Mean
			, StdDeviation, Stream)

	def NegExp(self, Mean=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method NegExp : Returns values from the detailed Negative Exponential distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), ((5, 1), (3, 1)),Mean
			, Stream)

	def Normal(self, Mean=defaultNamedNotOptArg, StdDeviation=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Normal : Returns values from the detailed Normal distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Mean
			, StdDeviation, Stream)

	def Poisson(self, Mean=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Poisson : Returns values from the detailed Poisson distribution, using the stream specified. WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((5, 1), (3, 1)),Mean
			, Stream)

	def Random(self, Stream=defaultNamedNotOptArg):
		'method Random : Returns the next number from the specified stream. WARNING : Avoid/ Take special care using a stream allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((3, 1),),Stream
			)

	# The method Seed is actually a property, but must be used as a method to correctly pass the arguments
	def Seed(self, SeedNumber=defaultNamedNotOptArg):
		'Gets a generator seed'
		return self._oleobj_.InvokeTypes(17, LCID, 2, (3, 0), ((3, 1),),SeedNumber
			)

	# The method SetSeed is actually a property, but must be used as a method to correctly pass the arguments
	def SetSeed(self, SeedNumber=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'Gets a generator seed'
		return self._oleobj_.InvokeTypes(17, LCID, 4, (24, 0), ((3, 1), (3, 1)),SeedNumber
			, arg1)

	def TNormal(self, Mean=defaultNamedNotOptArg, StdDeviation=defaultNamedNotOptArg, Min=defaultNamedNotOptArg, Max=defaultNamedNotOptArg
			, Stream=defaultNamedNotOptArg):
		'method TNormal : Returns values from the detailed Truncated Normal distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (5, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (3, 1)),Mean
			, StdDeviation, Min, Max, Stream)

	def Triangle(self, Minimum=defaultNamedNotOptArg, MostLikely=defaultNamedNotOptArg, Maximum=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Triangle : Returns values from the detailed Triangular distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (5, 0), ((5, 1), (5, 1), (5, 1), (3, 1)),Minimum
			, MostLikely, Maximum, Stream)

	def Uniform(self, Lowest=defaultNamedNotOptArg, Highest=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Uniform : Returns double values from the detailed uniform distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Lowest
			, Highest, Stream)

	def Weibull(self, Shape=defaultNamedNotOptArg, Scale=defaultNamedNotOptArg, Stream=defaultNamedNotOptArg):
		'method Weibull: Returns values from the detailed Weibull distribution, using the stream specified.  WARNING : Avoid streams allocated to elements in a running model.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (5, 0), ((5, 1), (5, 1), (3, 1)),Shape
			, Scale, Stream)

	_prop_map_get_ = {
		# Method 'RandomNumberUsage' returns object of type 'IWRandomNumberUsage'
		"RandomNumberUsage": (18, 2, (9, 0), (), "RandomNumberUsage", '{30DD08CA-7835-4684-9C1B-46674D674204}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWScrap(DispatchBaseClass):
	'IWScrap Interface'
	CLSID = IID('{38FB81B4-8091-4A39-8041-56C31FDA7BD0}')
	coclass_clsid = IID('{3805229F-FE67-48C2-AE43-F6E329766A28}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSection(DispatchBaseClass):
	'IWSection Interface'
	CLSID = IID('{1AF98A1D-C6E6-4681-88CC-8DB41A320460}')
	coclass_clsid = IID('{254FF920-4B28-469E-8EB6-B53CA41D5758}')

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(200, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		"ActionsOnEntry": (108, 2, (8, 0), (), "ActionsOnEntry", None),
		"ActionsOnExit": (109, 2, (8, 0), (), "ActionsOnExit", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"AllocatedNetwork": (112, 2, (8, 0), (), "AllocatedNetwork", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWSectionBreakdowns'
		"Breakdowns": (110, 2, (9, 0), (), "Breakdowns", '{43821155-63F6-11D5-85C7-0020AFF488A2}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"Capacity": (207, 2, (12, 0), (), "Capacity", None),
		"CarrierAverageTimeFree": (206, 2, (5, 0), (), "CarrierAverageTimeFree", None),
		"CarrierAverageTimePowered": (205, 2, (5, 0), (), "CarrierAverageTimePowered", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"ConnectionRule": (104, 2, (8, 0), (), "ConnectionRule", None),
		"CurrentNumberOfFreeCarriers": (203, 2, (3, 0), (), "CurrentNumberOfFreeCarriers", None),
		"CurrentNumberOfPoweredCarriers": (202, 2, (3, 0), (), "CurrentNumberOfPoweredCarriers", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"DogSpacing": (107, 2, (12, 0), (), "DogSpacing", None),
		"DriveSpeed": (106, 2, (12, 0), (), "DriveSpeed", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"Length": (105, 2, (12, 0), (), "Length", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		# Method 'Network' returns object of type 'IWNetwork'
		"Network": (111, 2, (9, 0), (), "Network", '{00504947-3FAA-4A8F-BF64-4EA4E3416B69}'),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (103, 2, (3, 0), (), "Reporting", None),
		# Method 'SectionInstances' returns object of type 'IWSectionInstances'
		"SectionInstances": (0, 2, (9, 0), (), "SectionInstances", '{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}'),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"TotalNumberOfCarriers": (201, 2, (3, 0), (), "TotalNumberOfCarriers", None),
		"TotalNumberOfLoadedCarriers": (204, 2, (3, 0), (), "TotalNumberOfLoadedCarriers", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnEntry": ((108, LCID, 4, 0),()),
		"ActionsOnExit": ((109, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"AllocatedNetwork": ((112, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((207, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"ConnectionRule": ((104, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"DogSpacing": ((107, LCID, 4, 0),()),
		"DriveSpeed": ((106, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Length": ((105, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((103, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'SectionInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "SectionInstances", '{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSectionBreakdown(DispatchBaseClass):
	'IWSectionBreakdown Interface'
	CLSID = IID('{43821154-63F6-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{43821150-63F6-11D5-85C7-0020AFF488A2}')

	_prop_map_get_ = {
		"ActionsOnDown": (8, 2, (8, 0), (), "ActionsOnDown", None),
		"ActionsOnResume": (9, 2, (8, 0), (), "ActionsOnResume", None),
		"BreakdownMode": (1, 2, (3, 0), (), "BreakdownMode", None),
		"LaborRule": (4, 2, (8, 0), (), "LaborRule", None),
		"PreEmptAllowance": (6, 2, (12, 0), (), "PreEmptAllowance", None),
		"PreEmptLevel": (5, 2, (12, 0), (), "PreEmptLevel", None),
		"PreEmptPenalty": (7, 2, (12, 0), (), "PreEmptPenalty", None),
		"RepairTime": (3, 2, (12, 0), (), "RepairTime", None),
		"TimeBetweenFailures": (2, 2, (12, 0), (), "TimeBetweenFailures", None),
	}
	_prop_map_put_ = {
		"ActionsOnDown": ((8, LCID, 4, 0),()),
		"ActionsOnResume": ((9, LCID, 4, 0),()),
		"BreakdownMode": ((1, LCID, 4, 0),()),
		"LaborRule": ((4, LCID, 4, 0),()),
		"PreEmptAllowance": ((6, LCID, 4, 0),()),
		"PreEmptLevel": ((5, LCID, 4, 0),()),
		"PreEmptPenalty": ((7, LCID, 4, 0),()),
		"RepairTime": ((3, LCID, 4, 0),()),
		"TimeBetweenFailures": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSectionBreakdownInstance(DispatchBaseClass):
	'IWSectionBreakdownInstance Interface'
	CLSID = IID('{43821156-63F6-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{43821152-63F6-11D5-85C7-0020AFF488A2}')

	_prop_map_get_ = {
		"BreakdownNumber": (2, 2, (3, 0), (), "BreakdownNumber", None),
		"BreakdownState": (3, 2, (3, 0), (), "BreakdownState", None),
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSectionBreakdownInstances(DispatchBaseClass):
	'IWSectionBreakdownInstances Interface'
	CLSID = IID('{43821157-63F6-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{43821153-63F6-11D5-85C7-0020AFF488A2}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWSectionBreakdowns(DispatchBaseClass):
	'IWSectionBreakdowns Interface'
	CLSID = IID('{43821155-63F6-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{43821151-63F6-11D5-85C7-0020AFF488A2}')

	def Add(self, Description=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Description
			, Position)

	# Result is of type IWSectionBreakdown
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{43821154-63F6-11D5-85C7-0020AFF488A2}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{43821154-63F6-11D5-85C7-0020AFF488A2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{43821154-63F6-11D5-85C7-0020AFF488A2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWSectionInstance(DispatchBaseClass):
	'IWSectionInstance Interface'
	CLSID = IID('{865318D8-96F3-40F0-866A-84A937964A79}')
	coclass_clsid = IID('{87663A9D-D546-462E-94A2-C22A4BEC104A}')

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(7, LCID, 2, (5, 0), ((3, 0), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		# Method 'ActiveBreakdowns' returns object of type 'IWSectionBreakdownInstances'
		"ActiveBreakdowns": (12, 2, (9, 0), (), "ActiveBreakdowns", '{43821157-63F6-11D5-85C7-0020AFF488A2}'),
		"CarrierAverageTimeFree": (25, 2, (5, 0), (), "CarrierAverageTimeFree", None),
		"CarrierAverageTimePowered": (24, 2, (5, 0), (), "CarrierAverageTimePowered", None),
		# Method 'CarriersPresent' returns object of type 'IWCarrierInstances'
		"CarriersPresent": (3, 2, (9, 0), (), "CarriersPresent", '{8B98F244-7A42-4233-9432-BABB237EE777}'),
		"CurrentNumberOfFreeCarriers": (22, 2, (3, 0), (), "CurrentNumberOfFreeCarriers", None),
		"CurrentNumberOfPoweredCarriers": (21, 2, (3, 0), (), "CurrentNumberOfPoweredCarriers", None),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (4, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'Section' returns object of type 'IWSection'
		"Section": (1, 2, (9, 0), (), "Section", '{1AF98A1D-C6E6-4681-88CC-8DB41A320460}'),
		"State": (2, 2, (3, 0), (), "State", None),
		"TimeTillNextEvent": (8, 2, (5, 0), (), "TimeTillNextEvent", None),
		"TotalNumberOfCarriers": (20, 2, (3, 0), (), "TotalNumberOfCarriers", None),
		"TotalNumberOfLoadedCarriers": (23, 2, (3, 0), (), "TotalNumberOfLoadedCarriers", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSectionInstances(DispatchBaseClass):
	'IWSectionInstances Interface'
	CLSID = IID('{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}')
	coclass_clsid = IID('{889A626B-57AE-4DBF-AA7B-6B5101807642}')

	# Result is of type IWSectionInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{865318D8-96F3-40F0-866A-84A937964A79}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{865318D8-96F3-40F0-866A-84A937964A79}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{865318D8-96F3-40F0-866A-84A937964A79}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWSectionType(DispatchBaseClass):
	'IWSectionType Interface'
	CLSID = IID('{31A329FB-AA5D-422F-A2A8-881EA066192B}')
	coclass_clsid = IID('{D12CC0A0-CA9E-40E1-9C5C-78A7D82573BC}')

	# Result is of type IWSection
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{1AF98A1D-C6E6-4681-88CC-8DB41A320460}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSecurity(DispatchBaseClass):
	'  Interface'
	CLSID = IID('{6E875BB8-B0E1-4077-B06D-86824D1D29C5}')
	coclass_clsid = None

	def SecurityAquire(self, Value=defaultNamedNotOptArg, pluginID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (11, 0), ((12, 1), (3, 1)),Value
			, pluginID)

	def SecurityRelease(self, Value=defaultNamedNotOptArg, pluginID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((12, 1), (3, 1)),Value
			, pluginID)

	def SecurityStillValid(self, Value=defaultNamedNotOptArg, pluginID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((12, 1), (3, 1)),Value
			, pluginID)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWShift(DispatchBaseClass):
	'IWShift Interface'
	CLSID = IID('{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}')
	coclass_clsid = IID('{C8393854-3713-4403-86C3-14A22119E733}')

	# The method AvailableLaborUnits is actually a property, but must be used as a method to correctly pass the arguments
	def AvailableLaborUnits(self, Labor=defaultNamedNotOptArg):
		'property AvailableLaborUnits'
		return self._oleobj_.InvokeTypes(112, LCID, 2, (3, 0), ((12, 1),),Labor
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(110, LCID, 2, (5, 0), ((3, 1),),State
			)

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"CurrentPeriod": (111, 2, (3, 0), (), "CurrentPeriod", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"EndWorkActions": (104, 2, (8, 0), (), "EndWorkActions", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitialRestTime": (102, 2, (5, 0), (), "InitialRestTime", None),
		"InitialWorkTime": (101, 2, (5, 0), (), "InitialWorkTime", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfCompletedShifts": (113, 2, (5, 0), (), "NumberOfCompletedShifts", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Reporting": (108, 2, (3, 0), (), "Reporting", None),
		# Method 'ShiftPeriods' returns object of type 'IWShiftPeriods'
		"ShiftPeriods": (109, 2, (9, 0), (), "ShiftPeriods", '{520FA171-59C5-11D5-A1C1-00E02963982C}'),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"StartWorkActions": (103, 2, (8, 0), (), "StartWorkActions", None),
		"SubShift": (100, 2, (11, 0), (), "SubShift", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"EndWorkActions": ((104, LCID, 4, 0),()),
		"InitialRestTime": ((102, LCID, 4, 0),()),
		"InitialWorkTime": ((101, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Reporting": ((108, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"StartWorkActions": ((103, LCID, 4, 0),()),
		"SubShift": ((100, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWShiftPeriod(DispatchBaseClass):
	'IWShiftPeriod Interface'
	CLSID = IID('{520FA170-59C5-11D5-A1C1-00E02963982C}')
	coclass_clsid = IID('{87AB0720-5E69-11D5-A1C1-00E02963982C}')

	_prop_map_get_ = {
		"OverTime": (4, 2, (5, 0), (), "OverTime", None),
		"PeriodType": (1, 2, (3, 0), (), "PeriodType", None),
		"RestTime": (3, 2, (5, 0), (), "RestTime", None),
		"SubShiftName": (5, 2, (8, 0), (), "SubShiftName", None),
		"WorkingTime": (2, 2, (5, 0), (), "WorkingTime", None),
	}
	_prop_map_put_ = {
		"OverTime": ((4, LCID, 4, 0),()),
		"PeriodType": ((1, LCID, 4, 0),()),
		"RestTime": ((3, LCID, 4, 0),()),
		"SubShiftName": ((5, LCID, 4, 0),()),
		"WorkingTime": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWShiftPeriods(DispatchBaseClass):
	'IWShiftPeriods Interface'
	CLSID = IID('{520FA171-59C5-11D5-A1C1-00E02963982C}')
	coclass_clsid = IID('{87AB0721-5E69-11D5-A1C1-00E02963982C}')

	def AddPeriod(self, WorkingTime=defaultNamedNotOptArg, RestTime=defaultNamedNotOptArg, OverTime=defaultNamedNotOptArg, Position=-1):
		'method AddPeriod'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (3, 49)),WorkingTime
			, RestTime, OverTime, Position)

	def AddSubShift(self, Name=defaultNamedNotOptArg, Position=-1):
		'method AddSubShift'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49)),Name
			, Position)

	# Result is of type IWShiftPeriod
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{520FA170-59C5-11D5-A1C1-00E02963982C}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{520FA170-59C5-11D5-A1C1-00E02963982C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{520FA170-59C5-11D5-A1C1-00E02963982C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWShiftType(DispatchBaseClass):
	'IWShiftType Interface'
	CLSID = IID('{D843A28F-8C4F-471A-9E14-3E75CD5DD37A}')
	coclass_clsid = IID('{0621844B-FA65-4835-8FBD-86F62DDEE8E8}')

	# Result is of type IWShift
	def Define(self, Name=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWShip(DispatchBaseClass):
	'IWShip Interface'
	CLSID = IID('{81E22460-8112-472B-9E14-96153261E6E0}')
	coclass_clsid = IID('{36FE27BE-07BA-4904-AFB6-9DA93621E6CE}')

	def AddPart(self, PartInstance=defaultNamedNotOptArg):
		'method AddPart'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (11, 0), ((9, 1),),PartInstance
			)

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStandardApplication(DispatchBaseClass):
	'IWStandardApplication Interface'
	CLSID = IID('{BDDBB5BA-2342-4163-9682-BD86F8AF4C84}')
	coclass_clsid = IID('{FA3D85D9-0C0B-4420-B724-0848E2588597}')

	def Activate(self):
		'Activates the application.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ForceQuit(self):
		'ForceQuit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def Quit(self):
		'Quit :\tMethod: Closes the application. This will  delete / invalidate any current Witness objects.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'ErrorsAndWarnings' returns object of type 'IWErrorsAndWarnings'
		"ErrorsAndWarnings": (6, 2, (9, 0), (), "ErrorsAndWarnings", '{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}'),
		# Method 'InputRequest' returns object of type 'IWInputRequest'
		"InputRequest": (7, 2, (9, 0), (), "InputRequest", '{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}'),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"ProcessID": (10, 2, (3, 0), (), "ProcessID", None),
		"Version": (2, 2, (8, 0), (), "Version", None),
		"Visible": (4, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Model'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStation(DispatchBaseClass):
	'IWStation Interface'
	CLSID = IID('{517122AB-6C4C-4996-975C-207AABEF7353}')
	coclass_clsid = IID('{17EE021F-753A-4FE6-8F04-F957F655948F}')

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(200, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		"ActionsOnEntry": (119, 2, (8, 0), (), "ActionsOnEntry", None),
		"ActionsOnExit": (131, 2, (8, 0), (), "ActionsOnExit", None),
		"ActionsOnFinishLoading": (139, 2, (8, 0), (), "ActionsOnFinishLoading", None),
		"ActionsOnFinishUnloading": (148, 2, (8, 0), (), "ActionsOnFinishUnloading", None),
		"ActionsOnParking": (107, 2, (8, 0), (), "ActionsOnParking", None),
		"ActionsOnProcess": (125, 2, (8, 0), (), "ActionsOnProcess", None),
		"ActionsOnStartLoading": (138, 2, (8, 0), (), "ActionsOnStartLoading", None),
		"ActionsOnStartUnloading": (147, 2, (8, 0), (), "ActionsOnStartUnloading", None),
		"ActionsOnUnparking": (113, 2, (8, 0), (), "ActionsOnUnparking", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"AllocatedNetwork": (156, 2, (8, 0), (), "AllocatedNetwork", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		# Method 'Breakdowns' returns object of type 'IWStationBreakdowns'
		"Breakdowns": (154, 2, (9, 0), (), "Breakdowns", '{A5729D61-63D2-11D5-85C7-0020AFF488A2}'),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"ConnectionRule": (105, 2, (8, 0), (), "ConnectionRule", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"EntryCycleTime": (118, 2, (12, 0), (), "EntryCycleTime", None),
		"EntryLaborRule": (120, 2, (8, 0), (), "EntryLaborRule", None),
		"EntryPreEmptAllowance": (122, 2, (12, 0), (), "EntryPreEmptAllowance", None),
		"EntryPreEmptLevel": (121, 2, (12, 0), (), "EntryPreEmptLevel", None),
		"EntryPreEmptPenalty": (123, 2, (12, 0), (), "EntryPreEmptPenalty", None),
		"ExitCycleTime": (130, 2, (12, 0), (), "ExitCycleTime", None),
		"ExitLaborRule": (132, 2, (8, 0), (), "ExitLaborRule", None),
		"ExitPreEmptAllowance": (134, 2, (12, 0), (), "ExitPreEmptAllowance", None),
		"ExitPreEmptLevel": (133, 2, (12, 0), (), "ExitPreEmptLevel", None),
		"ExitPreEmptPenalty": (135, 2, (12, 0), (), "ExitPreEmptPenalty", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"LoadingCycleTime": (137, 2, (12, 0), (), "LoadingCycleTime", None),
		"LoadingInputRule": (144, 2, (8, 0), (), "LoadingInputRule", None),
		"LoadingLaborRule": (140, 2, (8, 0), (), "LoadingLaborRule", None),
		"LoadingMethod": (136, 2, (3, 0), (), "LoadingMethod", None),
		"LoadingPreEmptAllowance": (142, 2, (12, 0), (), "LoadingPreEmptAllowance", None),
		"LoadingPreEmptLevel": (141, 2, (12, 0), (), "LoadingPreEmptLevel", None),
		"LoadingPreEmptPenalty": (143, 2, (12, 0), (), "LoadingPreEmptPenalty", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		# Method 'Network' returns object of type 'IWNetwork'
		"Network": (155, 2, (9, 0), (), "Network", '{00504947-3FAA-4A8F-BF64-4EA4E3416B69}'),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfParts": (203, 2, (3, 0), (), "NumberOfParts", None),
		"ParkingCycleTime": (106, 2, (12, 0), (), "ParkingCycleTime", None),
		"ParkingLaborRule": (108, 2, (8, 0), (), "ParkingLaborRule", None),
		"ParkingPreEmptAllowance": (110, 2, (12, 0), (), "ParkingPreEmptAllowance", None),
		"ParkingPreEmptLevel": (109, 2, (12, 0), (), "ParkingPreEmptLevel", None),
		"ParkingPreEmptPenalty": (111, 2, (12, 0), (), "ParkingPreEmptPenalty", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"ProcessCycleTime": (124, 2, (12, 0), (), "ProcessCycleTime", None),
		"ProcessLaborRule": (126, 2, (8, 0), (), "ProcessLaborRule", None),
		"ProcessPreEmptAllowance": (128, 2, (12, 0), (), "ProcessPreEmptAllowance", None),
		"ProcessPreEmptLevel": (127, 2, (12, 0), (), "ProcessPreEmptLevel", None),
		"ProcessPreEmptPenalty": (129, 2, (12, 0), (), "ProcessPreEmptPenalty", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (103, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'StationInstances' returns object of type 'IWStationInstances'
		"StationInstances": (0, 2, (9, 0), (), "StationInstances", '{503951C9-860E-4251-A8C8-0E26E9046231}'),
		"StationType": (104, 2, (3, 0), (), "StationType", None),
		"TotalNumberOfCarriers": (201, 2, (3, 0), (), "TotalNumberOfCarriers", None),
		"TotalNumberOfParts": (202, 2, (3, 0), (), "TotalNumberOfParts", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UnloadingCycleTime": (146, 2, (12, 0), (), "UnloadingCycleTime", None),
		"UnloadingLaborRule": (149, 2, (8, 0), (), "UnloadingLaborRule", None),
		"UnloadingMethod": (145, 2, (3, 0), (), "UnloadingMethod", None),
		"UnloadingOutputRule": (153, 2, (8, 0), (), "UnloadingOutputRule", None),
		"UnloadingPreEmptAllowance": (151, 2, (12, 0), (), "UnloadingPreEmptAllowance", None),
		"UnloadingPreEmptLevel": (150, 2, (12, 0), (), "UnloadingPreEmptLevel", None),
		"UnloadingPreEmptPenalty": (152, 2, (12, 0), (), "UnloadingPreEmptPenalty", None),
		"UnparkingCycleTime": (112, 2, (12, 0), (), "UnparkingCycleTime", None),
		"UnparkingLaborRule": (114, 2, (8, 0), (), "UnparkingLaborRule", None),
		"UnparkingPreEmptAllowance": (116, 2, (12, 0), (), "UnparkingPreEmptAllowance", None),
		"UnparkingPreEmptLevel": (115, 2, (12, 0), (), "UnparkingPreEmptLevel", None),
		"UnparkingPreEmptPenalty": (117, 2, (12, 0), (), "UnparkingPreEmptPenalty", None),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"ActionsOnEntry": ((119, LCID, 4, 0),()),
		"ActionsOnExit": ((131, LCID, 4, 0),()),
		"ActionsOnFinishLoading": ((139, LCID, 4, 0),()),
		"ActionsOnFinishUnloading": ((148, LCID, 4, 0),()),
		"ActionsOnParking": ((107, LCID, 4, 0),()),
		"ActionsOnProcess": ((125, LCID, 4, 0),()),
		"ActionsOnStartLoading": ((138, LCID, 4, 0),()),
		"ActionsOnStartUnloading": ((147, LCID, 4, 0),()),
		"ActionsOnUnparking": ((113, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"AllocatedNetwork": ((156, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"ConnectionRule": ((105, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"EntryCycleTime": ((118, LCID, 4, 0),()),
		"EntryLaborRule": ((120, LCID, 4, 0),()),
		"EntryPreEmptAllowance": ((122, LCID, 4, 0),()),
		"EntryPreEmptLevel": ((121, LCID, 4, 0),()),
		"EntryPreEmptPenalty": ((123, LCID, 4, 0),()),
		"ExitCycleTime": ((130, LCID, 4, 0),()),
		"ExitLaborRule": ((132, LCID, 4, 0),()),
		"ExitPreEmptAllowance": ((134, LCID, 4, 0),()),
		"ExitPreEmptLevel": ((133, LCID, 4, 0),()),
		"ExitPreEmptPenalty": ((135, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"LoadingCycleTime": ((137, LCID, 4, 0),()),
		"LoadingInputRule": ((144, LCID, 4, 0),()),
		"LoadingLaborRule": ((140, LCID, 4, 0),()),
		"LoadingMethod": ((136, LCID, 4, 0),()),
		"LoadingPreEmptAllowance": ((142, LCID, 4, 0),()),
		"LoadingPreEmptLevel": ((141, LCID, 4, 0),()),
		"LoadingPreEmptPenalty": ((143, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"ParkingCycleTime": ((106, LCID, 4, 0),()),
		"ParkingLaborRule": ((108, LCID, 4, 0),()),
		"ParkingPreEmptAllowance": ((110, LCID, 4, 0),()),
		"ParkingPreEmptLevel": ((109, LCID, 4, 0),()),
		"ParkingPreEmptPenalty": ((111, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"ProcessCycleTime": ((124, LCID, 4, 0),()),
		"ProcessLaborRule": ((126, LCID, 4, 0),()),
		"ProcessPreEmptAllowance": ((128, LCID, 4, 0),()),
		"ProcessPreEmptLevel": ((127, LCID, 4, 0),()),
		"ProcessPreEmptPenalty": ((129, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((103, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"StationType": ((104, LCID, 4, 0),()),
		"UnloadingCycleTime": ((146, LCID, 4, 0),()),
		"UnloadingLaborRule": ((149, LCID, 4, 0),()),
		"UnloadingMethod": ((145, LCID, 4, 0),()),
		"UnloadingOutputRule": ((153, LCID, 4, 0),()),
		"UnloadingPreEmptAllowance": ((151, LCID, 4, 0),()),
		"UnloadingPreEmptLevel": ((150, LCID, 4, 0),()),
		"UnloadingPreEmptPenalty": ((152, LCID, 4, 0),()),
		"UnparkingCycleTime": ((112, LCID, 4, 0),()),
		"UnparkingLaborRule": ((114, LCID, 4, 0),()),
		"UnparkingPreEmptAllowance": ((116, LCID, 4, 0),()),
		"UnparkingPreEmptLevel": ((115, LCID, 4, 0),()),
		"UnparkingPreEmptPenalty": ((117, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'StationInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "StationInstances", '{503951C9-860E-4251-A8C8-0E26E9046231}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStationBreakdown(DispatchBaseClass):
	'IWStationBreakdown Interface'
	CLSID = IID('{A5729D60-63D2-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{BE06CB20-63E6-11D5-85C7-0020AFF488A2}')

	_prop_map_get_ = {
		"ActionsOnDown": (8, 2, (8, 0), (), "ActionsOnDown", None),
		"ActionsOnResume": (9, 2, (8, 0), (), "ActionsOnResume", None),
		"BreakdownMode": (1, 2, (3, 0), (), "BreakdownMode", None),
		"LaborRule": (4, 2, (8, 0), (), "LaborRule", None),
		"PreEmptAllowance": (6, 2, (12, 0), (), "PreEmptAllowance", None),
		"PreEmptLevel": (5, 2, (12, 0), (), "PreEmptLevel", None),
		"PreEmptPenalty": (7, 2, (12, 0), (), "PreEmptPenalty", None),
		"RepairTime": (3, 2, (12, 0), (), "RepairTime", None),
		"TimeBetweenFailures": (2, 2, (12, 0), (), "TimeBetweenFailures", None),
	}
	_prop_map_put_ = {
		"ActionsOnDown": ((8, LCID, 4, 0),()),
		"ActionsOnResume": ((9, LCID, 4, 0),()),
		"BreakdownMode": ((1, LCID, 4, 0),()),
		"LaborRule": ((4, LCID, 4, 0),()),
		"PreEmptAllowance": ((6, LCID, 4, 0),()),
		"PreEmptLevel": ((5, LCID, 4, 0),()),
		"PreEmptPenalty": ((7, LCID, 4, 0),()),
		"RepairTime": ((3, LCID, 4, 0),()),
		"TimeBetweenFailures": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStationBreakdownInstance(DispatchBaseClass):
	'IWStationBreakdownInstance Interface'
	CLSID = IID('{A5729D62-63D2-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{BE06CB21-63E6-11D5-85C7-0020AFF488A2}')

	_prop_map_get_ = {
		"BreakdownNumber": (2, 2, (3, 0), (), "BreakdownNumber", None),
		"BreakdownState": (3, 2, (3, 0), (), "BreakdownState", None),
		# Method 'ElementInstance' returns object of type 'IWInstance'
		"ElementInstance": (1, 2, (9, 0), (), "ElementInstance", '{B663FFB1-235F-11D5-A1B4-00E02963982C}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStationBreakdownInstances(DispatchBaseClass):
	'IWStationBreakdownInstances Interface'
	CLSID = IID('{A5729D63-63D2-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{BE06CB22-63E6-11D5-85C7-0020AFF488A2}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), 'Item', None,Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		return self._ApplyTypes_(0, 2, (12, 0), ((12, 1),), '__call__', None,Index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWStationBreakdowns(DispatchBaseClass):
	'IWStationBreakdowns Interface'
	CLSID = IID('{A5729D61-63D2-11D5-85C7-0020AFF488A2}')
	coclass_clsid = IID('{BE06CB25-63E6-11D5-85C7-0020AFF488A2}')

	def Add(self, Description=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),Description
			, Position)

	# Result is of type IWStationBreakdown
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A5729D60-63D2-11D5-85C7-0020AFF488A2}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Factors' returns object of type 'IWFactors'
		"Factors": (4, 2, (9, 0), (), "Factors", '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A5729D60-63D2-11D5-85C7-0020AFF488A2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A5729D60-63D2-11D5-85C7-0020AFF488A2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWStationInstance(DispatchBaseClass):
	'IWStationInstance Interface'
	CLSID = IID('{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}')
	coclass_clsid = IID('{5C523CCE-E05E-426F-A78A-F90991EA0C0F}')

	def ForcedBreakdown(self):
		'method ForcedBreakdown'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def ForcedRepair(self):
		'method ForcedRepair'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(7, LCID, 2, (5, 0), ((3, 0), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		# Method 'ActiveBreakdowns' returns object of type 'IWStationBreakdownInstances'
		"ActiveBreakdowns": (12, 2, (9, 0), (), "ActiveBreakdowns", '{A5729D63-63D2-11D5-85C7-0020AFF488A2}'),
		# Method 'CarriersPresent' returns object of type 'IWCarrierInstances'
		"CarriersPresent": (3, 2, (9, 0), (), "CarriersPresent", '{8B98F244-7A42-4233-9432-BABB237EE777}'),
		# Method 'LaborPresent' returns object of type 'IWLaborInstances'
		"LaborPresent": (4, 2, (9, 0), (), "LaborPresent", '{39150113-B27B-43AA-B116-5EFCF532B027}'),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfParts": (22, 2, (3, 0), (), "NumberOfParts", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"State": (2, 2, (3, 0), (), "State", None),
		# Method 'Station' returns object of type 'IWStation'
		"Station": (1, 2, (9, 0), (), "Station", '{517122AB-6C4C-4996-975C-207AABEF7353}'),
		"TimeTillNextEvent": (8, 2, (5, 0), (), "TimeTillNextEvent", None),
		"TotalNumberOfCarriers": (20, 2, (3, 0), (), "TotalNumberOfCarriers", None),
		"TotalNumberOfParts": (21, 2, (3, 0), (), "TotalNumberOfParts", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWStationInstances(DispatchBaseClass):
	'IWStationInstances Interface'
	CLSID = IID('{503951C9-860E-4251-A8C8-0E26E9046231}')
	coclass_clsid = IID('{FA88B3AD-568D-459E-8774-202331D9DD5A}')

	# Result is of type IWStationInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWStationType(DispatchBaseClass):
	'IWStationType Interface'
	CLSID = IID('{53CDBD79-5425-4B6E-BB04-203DB2F8155B}')
	coclass_clsid = IID('{FAC4F46E-2F6E-4749-B377-BB31740854AD}')

	# Result is of type IWStation
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{517122AB-6C4C-4996-975C-207AABEF7353}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWSystemElement(DispatchBaseClass):
	'IWSystemElement Interface'
	CLSID = IID('{595FF59A-1729-4781-A427-66C61F9C6DCC}')
	coclass_clsid = IID('{8F1E1722-B3BC-49BE-900F-1A1015B3E19B}')

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTank(DispatchBaseClass):
	'IWTank Interface'
	CLSID = IID('{8D4C9A2A-5367-4819-9911-DD9CA73006F7}')
	coclass_clsid = IID('{E172B608-4CAC-42E9-B756-DEEC0E285673}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"Capacity": (103, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"Priority": (102, 2, (12, 0), (), "Priority", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'TankInstances' returns object of type 'IWTankInstances'
		"TankInstances": (0, 2, (9, 0), (), "TankInstances", '{621E28F2-E65D-456E-8229-D1A8BE6EB63D}'),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((103, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"Priority": ((102, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'TankInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "TankInstances", '{621E28F2-E65D-456E-8229-D1A8BE6EB63D}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTankInstance(DispatchBaseClass):
	'IWTankInstance Interface'
	CLSID = IID('{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}')
	coclass_clsid = IID('{BA36851B-F5F8-4DDE-879C-F85BAD2A8CF1}')

	_prop_map_get_ = {
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'Tank' returns object of type 'IWTank'
		"Tank": (1, 2, (9, 0), (), "Tank", '{8D4C9A2A-5367-4819-9911-DD9CA73006F7}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTankInstances(DispatchBaseClass):
	'IWTankInstances Interface'
	CLSID = IID('{621E28F2-E65D-456E-8229-D1A8BE6EB63D}')
	coclass_clsid = IID('{CA9A3253-9C84-48A5-B1F1-C474D7FF28A9}')

	# Result is of type IWTankInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWTankType(DispatchBaseClass):
	'IWTankType Interface'
	CLSID = IID('{5229A31A-D096-4389-8540-65F371CF0D97}')
	coclass_clsid = IID('{DC41C651-D074-4A96-B802-497B888E1F47}')

	# Result is of type IWTank
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{8D4C9A2A-5367-4819-9911-DD9CA73006F7}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTimeseries(DispatchBaseClass):
	'IWTimeseries Interface'
	CLSID = IID('{BFD54915-A1B1-46C6-87F5-B8B6C567615B}')
	coclass_clsid = IID('{AD5E9293-FD7B-4EA1-B2C8-CB27C2D1BB09}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTimeseriesType(DispatchBaseClass):
	'IWTimeseriesType Interface'
	CLSID = IID('{727F8035-F180-4863-9BAC-561F1D579AD3}')
	coclass_clsid = IID('{CBEB96B5-10E1-4800-A763-5E417B92B34A}')

	# Result is of type IWTimeseries
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{BFD54915-A1B1-46C6-87F5-B8B6C567615B}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTrack(DispatchBaseClass):
	'IWTrack Interface'
	CLSID = IID('{B4FD8014-1552-475F-A679-F2B15A8147A8}')
	coclass_clsid = IID('{0398C500-A610-463B-91A1-F4065CFEFF84}')

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(202, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(200, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(180, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ActionsOnFront": (107, 2, (8, 0), (), "ActionsOnFront", None),
		"ActionsOnJoin": (106, 2, (8, 0), (), "ActionsOnJoin", None),
		"ActionsOnLoad": (144, 2, (8, 0), (), "ActionsOnLoad", None),
		"ActionsOnUnload": (164, 2, (8, 0), (), "ActionsOnUnload", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"BusyTime": (105, 2, (12, 0), (), "BusyTime", None),
		"Capacity": (102, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"LoadCondition": (145, 2, (12, 0), (), "LoadCondition", None),
		"LoadInputRule": (142, 2, (8, 0), (), "LoadInputRule", None),
		"LoadMode": (140, 2, (3, 0), (), "LoadMode", None),
		"LoadQuantity": (143, 2, (12, 0), (), "LoadQuantity", None),
		"LoadTime": (141, 2, (12, 0), (), "LoadTime", None),
		"MaximumSpeed": (104, 2, (12, 0), (), "MaximumSpeed", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfParts": (201, 2, (3, 0), (), "NumberOfParts", None),
		"NumberOfVehicles": (204, 2, (3, 0), (), "NumberOfVehicles", None),
		"OutputRule": (109, 2, (8, 0), (), "OutputRule", None),
		"ParkPosition": (165, 2, (12, 0), (), "ParkPosition", None),
		"PhysicalLength": (103, 2, (12, 0), (), "PhysicalLength", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (110, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"StopCondition": (122, 2, (12, 0), (), "StopCondition", None),
		"StopMode": (120, 2, (3, 0), (), "StopMode", None),
		"StopTime": (121, 2, (12, 0), (), "StopTime", None),
		"TotalNumberOfVehiclesOn": (205, 2, (3, 0), (), "TotalNumberOfVehiclesOn", None),
		# Method 'TrackInstances' returns object of type 'IWTrackInstances'
		"TrackInstances": (0, 2, (9, 0), (), "TrackInstances", '{20892432-3AD4-4D37-807F-5C035DF0638B}'),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UnloadCondition": (166, 2, (12, 0), (), "UnloadCondition", None),
		"UnloadMode": (160, 2, (3, 0), (), "UnloadMode", None),
		"UnloadOutputFrom": (206, 2, (3, 0), (), "UnloadOutputFrom", None),
		"UnloadOutputRule": (162, 2, (8, 0), (), "UnloadOutputRule", None),
		"UnloadQuantity": (163, 2, (12, 0), (), "UnloadQuantity", None),
		"UnloadTime": (161, 2, (12, 0), (), "UnloadTime", None),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		# Method 'WorkSearch' returns object of type 'IWTrackWorkSearchItems'
		"WorkSearch": (111, 2, (9, 0), (), "WorkSearch", '{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}'),
		"Zone": (108, 2, (12, 0), (), "Zone", None),
	}
	_prop_map_put_ = {
		"ActionsOnFront": ((107, LCID, 4, 0),()),
		"ActionsOnJoin": ((106, LCID, 4, 0),()),
		"ActionsOnLoad": ((144, LCID, 4, 0),()),
		"ActionsOnUnload": ((164, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"BusyTime": ((105, LCID, 4, 0),()),
		"Capacity": ((102, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"LoadCondition": ((145, LCID, 4, 0),()),
		"LoadInputRule": ((142, LCID, 4, 0),()),
		"LoadMode": ((140, LCID, 4, 0),()),
		"LoadQuantity": ((143, LCID, 4, 0),()),
		"LoadTime": ((141, LCID, 4, 0),()),
		"MaximumSpeed": ((104, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputRule": ((109, LCID, 4, 0),()),
		"ParkPosition": ((165, LCID, 4, 0),()),
		"PhysicalLength": ((103, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((110, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"StopCondition": ((122, LCID, 4, 0),()),
		"StopMode": ((120, LCID, 4, 0),()),
		"StopTime": ((121, LCID, 4, 0),()),
		"UnloadCondition": ((166, LCID, 4, 0),()),
		"UnloadMode": ((160, LCID, 4, 0),()),
		"UnloadOutputFrom": ((206, LCID, 4, 0),()),
		"UnloadOutputRule": ((162, LCID, 4, 0),()),
		"UnloadQuantity": ((163, LCID, 4, 0),()),
		"UnloadTime": ((161, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
		"Zone": ((108, LCID, 4, 0),()),
	}
	# Default property for this class is 'TrackInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "TrackInstances", '{20892432-3AD4-4D37-807F-5C035DF0638B}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTrackInstance(DispatchBaseClass):
	'IWTrackInstance Interface'
	CLSID = IID('{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')
	coclass_clsid = IID('{EE5EE797-CC64-48C7-83B8-BA8C8561796D}')

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(6, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(4, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	_prop_map_get_ = {
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NumberOfParts": (5, 2, (3, 0), (), "NumberOfParts", None),
		"NumberOfVehicles": (8, 2, (3, 0), (), "NumberOfVehicles", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		"State": (3, 2, (3, 0), (), "State", None),
		"TimeTillNextEvent": (10, 2, (5, 0), (), "TimeTillNextEvent", None),
		"TotalNumberOfVehiclesOn": (9, 2, (3, 0), (), "TotalNumberOfVehiclesOn", None),
		# Method 'Track' returns object of type 'IWTrack'
		"Track": (1, 2, (9, 0), (), "Track", '{B4FD8014-1552-475F-A679-F2B15A8147A8}'),
		# Method 'VehiclesOn' returns object of type 'IWVehicleInstances'
		"VehiclesOn": (2, 2, (9, 0), (), "VehiclesOn", '{33DC7FEE-B353-483D-8F54-E63B63C41B49}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTrackInstances(DispatchBaseClass):
	'IWTrackInstances Interface'
	CLSID = IID('{20892432-3AD4-4D37-807F-5C035DF0638B}')
	coclass_clsid = IID('{08BF91FF-3235-4569-B6FE-952E562B235F}')

	# Result is of type IWTrackInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWTrackType(DispatchBaseClass):
	'IWTrackType Interface'
	CLSID = IID('{7BAF40F7-A453-4B2C-9BC9-3A29F96F0BC0}')
	coclass_clsid = IID('{5A372025-E42D-4ED3-8583-E5341700F635}')

	# Result is of type IWTrack
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{B4FD8014-1552-475F-A679-F2B15A8147A8}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTrackWorkSearchItem(DispatchBaseClass):
	'IWTrackWorkSearchItem Interface'
	CLSID = IID('{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}')
	coclass_clsid = IID('{F0F0BF92-6EF7-11D5-80F0-00E02964AB43}')

	_prop_map_get_ = {
		"Track": (1, 2, (12, 0), (), "Track", None),
	}
	_prop_map_put_ = {
		"Track": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTrackWorkSearchItems(DispatchBaseClass):
	'IWTrackWorkSearchItems Interface'
	CLSID = IID('{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}')
	coclass_clsid = IID('{F0F0BF93-6EF7-11D5-80F0-00E02964AB43}')

	def Add(self, Track=defaultNamedNotOptArg, Position=-1):
		'method Add'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((12, 1), (3, 49)),Track
			, Position)

	# Result is of type IWTrackWorkSearchItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}')
		return ret

	def Remove(self, Position=defaultNamedNotOptArg):
		'method Remove'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Position
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWType(DispatchBaseClass):
	'IWType Interface'
	CLSID = IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')
	coclass_clsid = IID('{90A3C7D3-EBED-44B7-9F9D-DE4E3094A286}')

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWTypes(DispatchBaseClass):
	'IWTypes Interface'
	CLSID = IID('{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}')
	coclass_clsid = IID('{7C3688CE-2F5E-435E-BEB2-5AA084EDEC6E}')

	# The method IndexOf is actually a property, but must be used as a method to correctly pass the arguments
	def IndexOf(self, Key=defaultNamedNotOptArg):
		'property IndexOf'
		return self._oleobj_.InvokeTypes(101, LCID, 2, (3, 0), ((12, 1),),Key
			)

	# Result is of type IWType
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E2D06A1C-239C-42EC-B904-CB0735088E0E}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E2D06A1C-239C-42EC-B904-CB0735088E0E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E2D06A1C-239C-42EC-B904-CB0735088E0E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWUserElement(DispatchBaseClass):
	'IWUserElement Interface'
	CLSID = IID('{C24094DC-99F0-4AD7-9357-9468EEB19259}')
	coclass_clsid = IID('{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}')

	_prop_map_get_ = {
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
	}
	_prop_map_put_ = {
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWUserProperties(DispatchBaseClass):
	'IWUserProperties Interface'
	CLSID = IID('{FA29B843-D512-4287-BABD-71A4484B4ABC}')
	coclass_clsid = IID('{340F5316-1C07-4BB9-8588-8AF9083B45F9}')

	def ContainsUserProperty(self, Key=defaultNamedNotOptArg):
		'Contains the user property value stored with the application.'
		return self._oleobj_.InvokeTypes(9000, LCID, 1, (11, 0), ((8, 1),),Key
			)

	def GetUserProperty(self, Key=defaultNamedNotOptArg):
		'Get the user property value stored with the application.'
		return self._ApplyTypes_(9001, 1, (12, 0), ((8, 1),), 'GetUserProperty', None,Key
			)

	def PutUserProperty(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'Put the user property value stored with the application.'
		return self._oleobj_.InvokeTypes(9002, LCID, 1, (24, 0), ((8, 1), (12, 1)),Key
			, Value)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWVariable(DispatchBaseClass):
	'IWVariable Interface'
	CLSID = IID('{E735E960-17C8-11D5-A1B3-00E02963982C}')
	coclass_clsid = IID('{5F69FB13-188D-11D5-A1B3-00E02963982C}')

	# The method GetReferencedElementName is actually a property, but must be used as a method to correctly pass the arguments
	def GetReferencedElementName(self, dim1=1, dim2=1, dim3=1, dim4=1
			, dim5=1, dim6=1):
		'property ReferencedElementName'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(105, LCID, 2, (8, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49)),dim1
			, dim2, dim3, dim4, dim5, dim6
			)

	# The method GetValue is actually a property, but must be used as a method to correctly pass the arguments
	def GetValue(self, dim1=1, dim2=1, dim3=1, dim4=1
			, dim5=1, dim6=1):
		'property Value'
		return self._ApplyTypes_(103, 2, (12, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49)), 'GetValue', None,dim1
			, dim2, dim3, dim4, dim5, dim6
			)

	def ReDim(self, Dimensions=defaultNamedNotOptArg):
		'Method ReDim'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((8, 1),),Dimensions
			)

	# The method SetReferencedElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetReferencedElementName(self, dim1=1, dim2=1, dim3=1, dim4=1
			, dim5=1, dim6=1, arg6=defaultUnnamedArg):
		'property ReferencedElementName'
		return self._oleobj_.InvokeTypes(105, LCID, 4, (24, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (8, 1)),dim1
			, dim2, dim3, dim4, dim5, dim6
			, arg6)

	# The method SetValue is actually a property, but must be used as a method to correctly pass the arguments
	def SetValue(self, dim1=1, dim2=1, dim3=1, dim4=1
			, dim5=1, dim6=1, arg6=defaultUnnamedArg):
		'property Value'
		return self._oleobj_.InvokeTypes(103, LCID, 4, (24, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (12, 1)),dim1
			, dim2, dim3, dim4, dim5, dim6
			, arg6)

	_prop_map_get_ = {
		"ActionsOnInitialize": (102, 2, (8, 0), (), "ActionsOnInitialize", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"BulkValue": (106, 2, (12, 0), (), "BulkValue", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		# Method 'Dimensions' returns object of type 'IWDimensions'
		"Dimensions": (101, 2, (9, 0), (), "Dimensions", '{6C98C5C0-21DA-11D5-A1B3-00E02963982C}'),
		"DisableResetOnBegin": (120, 2, (11, 0), (), "DisableResetOnBegin", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"ReferencedElementName": (105, 2, (8, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49)), "ReferencedElementName", None),
		"Reporting": (121, 2, (3, 0), (), "Reporting", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		"Value": (103, 2, (12, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49)), "Value", None),
		"VariableType": (104, 2, (3, 0), (), "VariableType", None),
		"Watch": (122, 2, (11, 0), (), "Watch", None),
	}
	_prop_map_put_ = {
		"ActionsOnInitialize": ((102, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"BulkValue": ((106, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"DisableResetOnBegin": ((120, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"ReferencedElementName": ((105, LCID, 4, 0),('1', '1', '1', '1', '1')),
		"Reporting": ((121, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
		"Value": ((103, LCID, 4, 0),('1', '1', '1', '1', '1')),
		"VariableType": ((104, LCID, 4, 0),()),
		"Watch": ((122, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(103, 2, (12, 0), ((3, 49), (3, 49), (3, 49), (3, 49), (3, 49), (3, 49)), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWVariableType(DispatchBaseClass):
	'IWVariableType Interface'
	CLSID = IID('{5AE97C60-17C4-11D5-A1B3-00E02963982C}')
	coclass_clsid = IID('{5F69FB11-188D-11D5-A1B3-00E02963982C}')

	# Result is of type IWVariable
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg, VariableType=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1), (3, 1)),Name
			, Quantity, VariableType)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{E735E960-17C8-11D5-A1B3-00E02963982C}')
		return ret

	# Result is of type IWVariable
	def DefineDynamic(self, Name=defaultNamedNotOptArg, VariableType=defaultNamedNotOptArg):
		'method DefineDynamic'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1), (3, 1)),Name
			, VariableType)
		if ret is not None:
			ret = Dispatch(ret, 'DefineDynamic', '{E735E960-17C8-11D5-A1B3-00E02963982C}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWVehicle(DispatchBaseClass):
	'IWVehicle Interface'
	CLSID = IID('{A64A59DA-690E-428D-894F-99F67F4956CB}')
	coclass_clsid = IID('{E3D209FA-73F5-4C1C-B167-5FF6990B1944}')

	def AssignToCurrentCall(self, OnTrack=defaultNamedNotOptArg):
		'method AssignToCurrentCall'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (24, 0), ((12, 1),),OnTrack
			)

	def Call(self, LoadTrack=defaultNamedNotOptArg, UnloadTrack=defaultNamedNotOptArg, Priority=defaultNamedNotOptArg):
		'method Call'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), ((12, 1), (12, 1), (12, 1)),LoadTrack
			, UnloadTrack, Priority)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(114, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(112, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	def RestartStatistics(self):
		'method RestartStatistics'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (24, 0), (),)

	def Wakeup(self, OnTrack=defaultNamedNotOptArg):
		'method Wakeup'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((12, 1),),OnTrack
			)

	_prop_map_get_ = {
		"ActionsOnEntry": (107, 2, (8, 0), (), "ActionsOnEntry", None),
		"Alias": (13, 2, (8, 0), (), "Alias", None),
		"BreakdownRepairOnMass": (11, 2, (11, 0), (), "BreakdownRepairOnMass", None),
		"BroadcastToWPM": (12, 2, (11, 0), (), "BroadcastToWPM", None),
		"Capacity": (102, 2, (12, 0), (), "Capacity", None),
		"CompleteActions": (14, 2, (8, 0), (), "CompleteActions", None),
		"DescriptiveName": (15, 2, (8, 0), (), "DescriptiveName", None),
		"Identifier": (5, 2, (3, 0), (), "Identifier", None),
		"InitializeActions": (7, 2, (8, 0), (), "InitializeActions", None),
		"LoadedSpeed": (104, 2, (12, 0), (), "LoadedSpeed", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Notes": (6, 2, (8, 0), (), "Notes", None),
		"NumberOfFreeSpaces": (115, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (113, 2, (3, 0), (), "NumberOfParts", None),
		"OutputRule": (110, 2, (8, 0), (), "OutputRule", None),
		"PropertiesActions": (9, 2, (8, 0), (), "PropertiesActions", None),
		"Quantity": (101, 2, (12, 0), (), "Quantity", None),
		"Reporting": (111, 2, (3, 0), (), "Reporting", None),
		"ShiftName": (108, 2, (12, 0), (), "ShiftName", None),
		"ShiftStopImmediate": (109, 2, (11, 0), (), "ShiftStopImmediate", None),
		"ShowInOptimizer": (10, 2, (11, 0), (), "ShowInOptimizer", None),
		"TimeDelayToStart": (105, 2, (12, 0), (), "TimeDelayToStart", None),
		"TimeDelayToStop": (106, 2, (12, 0), (), "TimeDelayToStop", None),
		"TotalDistanceTravelled": (117, 2, (5, 0), (), "TotalDistanceTravelled", None),
		"TotalNumberOfLoads": (116, 2, (3, 0), (), "TotalNumberOfLoads", None),
		# Method 'Type' returns object of type 'IWType'
		"Type": (1, 2, (9, 0), (), "Type", '{E2D06A1C-239C-42EC-B904-CB0735088E0E}'),
		"UnloadedSpeed": (103, 2, (12, 0), (), "UnloadedSpeed", None),
		"UserActions": (8, 2, (8, 0), (), "UserActions", None),
		# Method 'VehicleInstances' returns object of type 'IWVehicleInstances'
		"VehicleInstances": (0, 2, (9, 0), (), "VehicleInstances", '{33DC7FEE-B353-483D-8F54-E63B63C41B49}'),
	}
	_prop_map_put_ = {
		"ActionsOnEntry": ((107, LCID, 4, 0),()),
		"Alias": ((13, LCID, 4, 0),()),
		"BreakdownRepairOnMass": ((11, LCID, 4, 0),()),
		"BroadcastToWPM": ((12, LCID, 4, 0),()),
		"Capacity": ((102, LCID, 4, 0),()),
		"CompleteActions": ((14, LCID, 4, 0),()),
		"DescriptiveName": ((15, LCID, 4, 0),()),
		"InitializeActions": ((7, LCID, 4, 0),()),
		"LoadedSpeed": ((104, LCID, 4, 0),()),
		"Name": ((2, LCID, 4, 0),()),
		"Notes": ((6, LCID, 4, 0),()),
		"OutputRule": ((110, LCID, 4, 0),()),
		"PropertiesActions": ((9, LCID, 4, 0),()),
		"Quantity": ((101, LCID, 4, 0),()),
		"Reporting": ((111, LCID, 4, 0),()),
		"ShiftName": ((108, LCID, 4, 0),()),
		"ShiftStopImmediate": ((109, LCID, 4, 0),()),
		"ShowInOptimizer": ((10, LCID, 4, 0),()),
		"TimeDelayToStart": ((105, LCID, 4, 0),()),
		"TimeDelayToStop": ((106, LCID, 4, 0),()),
		"UnloadedSpeed": ((103, LCID, 4, 0),()),
		"UserActions": ((8, LCID, 4, 0),()),
	}
	# Default property for this class is 'VehicleInstances'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (9, 0), (), "VehicleInstances", '{33DC7FEE-B353-483D-8F54-E63B63C41B49}'))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWVehicleInstance(DispatchBaseClass):
	'IWVehicleInstance Interface'
	CLSID = IID('{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}')
	coclass_clsid = IID('{209279F9-2A76-482E-9502-C0AAF1E0CE53}')

	def AssignToCurrentCall(self, OnTrack=defaultNamedNotOptArg):
		'method AssignToCurrentCall'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((12, 1),),OnTrack
			)

	def Call(self, LoadTrack=defaultNamedNotOptArg, UnloadTrack=defaultNamedNotOptArg, Priority=defaultNamedNotOptArg):
		'method Call'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((12, 1), (12, 1), (12, 1)),LoadTrack
			, UnloadTrack, Priority)

	# The method NumberOfPartsOfType is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfPartsOfType(self, PartType=defaultNamedNotOptArg):
		'property NumberOfPartsOfType'
		return self._oleobj_.InvokeTypes(4, LCID, 2, (3, 0), ((12, 1),),PartType
			)

	# The method PercentageUtilization is actually a property, but must be used as a method to correctly pass the arguments
	def PercentageUtilization(self, State=defaultNamedNotOptArg, OnShiftTime=defaultNamedNotOptArg):
		'property PercentageUtilization'
		return self._oleobj_.InvokeTypes(2, LCID, 2, (5, 0), ((3, 1), (11, 0)),State
			, OnShiftTime)

	def Wakeup(self, OnTrack=defaultNamedNotOptArg):
		'method Wakeup'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((12, 1),),OnTrack
			)

	_prop_map_get_ = {
		"CurrentDestination": (8, 2, (12, 0), (), "CurrentDestination", None),
		"CurrentPosition": (11, 2, (3, 0), (), "CurrentPosition", None),
		# Method 'CurrentTrack' returns object of type 'IWTrackInstance'
		"CurrentTrack": (10, 2, (9, 0), (), "CurrentTrack", '{1BE4C352-3E87-4432-8D0B-CC505F425D4D}'),
		"Desc": (16, 2, (12, 0), (), "Desc", None),
		"Icon": (18, 2, (12, 0), (), "Icon", None),
		"MemberNumber": (1001, 2, (3, 0), (), "MemberNumber", None),
		"NextDestination": (9, 2, (12, 0), (), "NextDestination", None),
		"NumberOfFreeSpaces": (5, 2, (3, 0), (), "NumberOfFreeSpaces", None),
		"NumberOfParts": (3, 2, (3, 0), (), "NumberOfParts", None),
		# Method 'Parent' returns object of type 'IWElement'
		"Parent": (1000, 2, (9, 0), (), "Parent", '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}'),
		# Method 'PartsIn' returns object of type 'IWPartInstances'
		"PartsIn": (15, 2, (9, 0), (), "PartsIn", '{63D176D1-0331-11D5-9B89-00E0295CD2CC}'),
		"Pen": (17, 2, (12, 0), (), "Pen", None),
		"State": (21, 2, (3, 0), (), "State", None),
		"TotalDistanceTravelled": (7, 2, (5, 0), (), "TotalDistanceTravelled", None),
		"TotalNumberOfLoads": (6, 2, (3, 0), (), "TotalNumberOfLoads", None),
		"TypeName": (19, 2, (8, 0), (), "TypeName", None),
		# Method 'UserAttributes' returns object of type 'IWAttributeInstances'
		"UserAttributes": (20, 2, (9, 0), (), "UserAttributes", '{427F8FA2-0EEE-11D5-8579-0020AFF488A2}'),
		# Method 'Vehicle' returns object of type 'IWVehicle'
		"Vehicle": (1, 2, (9, 0), (), "Vehicle", '{A64A59DA-690E-428D-894F-99F67F4956CB}'),
	}
	_prop_map_put_ = {
		"CurrentDestination": ((8, LCID, 4, 0),()),
		"Desc": ((16, LCID, 4, 0),()),
		"Icon": ((18, LCID, 4, 0),()),
		"Pen": ((17, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWVehicleInstances(DispatchBaseClass):
	'IWVehicleInstances Interface'
	CLSID = IID('{33DC7FEE-B353-483D-8F54-E63B63C41B49}')
	coclass_clsid = IID('{CBC7B99E-B2BF-4031-B413-523570170F57}')

	# Result is of type IWVehicleInstance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Position=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Position
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IWVehicleType(DispatchBaseClass):
	'IWVehicleType Interface'
	CLSID = IID('{C5F7EF56-FBC4-45E6-AA34-A6A38547535C}')
	coclass_clsid = IID('{683FB717-BD04-4F21-AB03-0E21A7C72C49}')

	# Result is of type IWVehicle
	def Define(self, Name=defaultNamedNotOptArg, Quantity=defaultNamedNotOptArg):
		'method Define'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, Quantity)
		if ret is not None:
			ret = Dispatch(ret, 'Define', '{A64A59DA-690E-428D-894F-99F67F4956CB}')
		return ret

	_prop_map_get_ = {
		"Identifier": (2, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (3, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (4, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NamePlural": (1, 2, (8, 0), (), "NamePlural", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWWorld(DispatchBaseClass):
	'IWWorld Interface'
	CLSID = IID('{861CABEB-E70F-4879-AEA6-079D1B13BC1E}')
	coclass_clsid = IID('{47D9ECBC-EA3E-41AF-80A4-4CD0185A62BD}')

	_prop_map_get_ = {
		"Identifier": (4, 2, (3, 0), (), "Identifier", None),
		# Method 'Model' returns object of type 'IWModel'
		"Model": (2, 2, (9, 0), (), "Model", '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}'),
		# Method 'Module' returns object of type 'IWModule'
		"Module": (3, 2, (9, 0), (), "Module", '{E4B4D340-1397-4A21-9F52-BB258A913C1A}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IWApplicationEvents:
	'_IWApplicationEvents Interface'
	CLSID = CLSID_Sink = IID('{82355849-4B8B-4B9C-A976-22ED38EACC8B}')
	coclass_clsid = IID('{FA3D85D9-0C0B-4420-B724-0848E2588597}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnQuit",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnQuit(self):
#		'method OnQuit'


class _IWApplicationViewerEvents:
	'_IWApplicationViewerEvents Interface'
	CLSID = CLSID_Sink = IID('{9E52085E-C12A-4AF5-8B2C-E8BDBC253A87}')
	coclass_clsid = IID('{340F5316-1C07-4BB9-8588-8AF9083B45F9}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnQuit",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnQuit(self):
#		'method OnQuit'


class _IWBPMViewerEvents(DispatchBaseClass):
	'_IWBPMViewerEvents Interface'
	CLSID = IID('{1C0AC210-AAAB-4742-AAAF-560EB4672B59}')
	coclass_clsid = None

	def OnQuit(self):
		'method OnQuit'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IWBufferEvents:
	'_IWBufferEvents Interface'
	CLSID = CLSID_Sink = IID('{54E9788A-561B-47CD-89E8-70940A6BE6E3}')
	coclass_clsid = IID('{DB0E57F7-7B49-4C88-9B76-8C4D050C1DF1}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWBufferTypeEvents:
	'_IWBufferTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{EFA48791-AA68-48B8-A766-374C9D362C4F}')
	coclass_clsid = IID('{E31B9C55-790E-46DF-99CB-E07885AE9D02}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWCarrierEvents:
	'_IWCarrierEvents Interface'
	CLSID = CLSID_Sink = IID('{6A224987-FC2D-4AB1-BB79-BAD5DE4175BC}')
	coclass_clsid = IID('{145C2B6F-9CDF-426D-ABAA-E36544E0026F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWCarrierTypeEvents:
	'_IWCarrierTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{8692269E-FAA2-4902-B63A-7710C7FFCF0F}')
	coclass_clsid = IID('{82A079AD-E254-4774-98AC-CA848A60DD37}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWCollection(DispatchBaseClass):
	CLSID = IID('{679E5B61-21DA-11D5-A1B3-00E02963982C}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _IWConveyorEvents:
	'_IWConveyorEvents Interface'
	CLSID = CLSID_Sink = IID('{6F20C840-7DCD-4FED-9434-F6D9C47D9F94}')
	coclass_clsid = IID('{645C5AF8-DE5E-42B9-8CAC-EE7C52560D03}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWConveyorTypeEvents:
	'_IWConveyorTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{E2B72B3B-B5CD-4EE5-A01C-BC6C34BA58CB}')
	coclass_clsid = IID('{E35C70B8-FBAA-4C39-A845-9E45DF62BB63}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWDataTableEvents:
	'_IWDataTableEvents Interface'
	CLSID = CLSID_Sink = IID('{18EA7261-FA3A-4804-929E-DC515094E226}')
	coclass_clsid = IID('{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWDataTableTypeEvents:
	'_IWDataTableTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{86E2E617-B2A1-4B82-9026-159D645DC025}')
	coclass_clsid = IID('{7DCDF7AB-9E07-4B20-A73F-A0188D6EDDF4}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWElementsEvents:
	'_IWElementsEvents Interface'
	CLSID = CLSID_Sink = IID('{B2718466-9171-4B74-B6A4-DB7A3137DC31}')
	coclass_clsid = IID('{7CC1ABA0-46BA-423A-8A30-D2F2974CEE63}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWErrorsAndWarningsEvents:
	'_IWErrorsAndWarningsEvents Interface'
	CLSID = CLSID_Sink = IID('{6AFE1260-66DF-408C-A059-0C471D6644E5}')
	coclass_clsid = IID('{A8990927-8EDC-473B-BA0B-834DF5C23FBF}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnError",
		        2 : "OnWarning",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnError(self, Message=defaultNamedNotOptArg, Responses=defaultNamedNotOptArg):
#		'method OnError'
#	def OnWarning(self, Message=defaultNamedNotOptArg, Responses=defaultNamedNotOptArg):
#		'method OnWarning'


class _IWFileEvents:
	'_IWFileEvents Interface'
	CLSID = CLSID_Sink = IID('{5E58C38B-F2A1-4B33-9169-5F22A107C928}')
	coclass_clsid = IID('{3E70BB16-0A94-4BC5-A921-2BCE98CB024D}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWFileTypeEvents:
	'_IWFileTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{CC381CE2-F4E3-46EE-99AE-9B9B6B16D15D}')
	coclass_clsid = IID('{C6097B81-5EA5-4FAB-93FE-741AB26AAE1F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWHistogramEvents:
	'_IWHistogramEvents Interface'
	CLSID = CLSID_Sink = IID('{2112E57A-21CA-4E68-8694-6B5E5C9251FC}')
	coclass_clsid = IID('{4CF57EFE-8DD9-4C70-A10A-AEEF3FD68E5D}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnHistogramUpdate",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnHistogramUpdate(self, Value=defaultNamedNotOptArg):
#		'method OnHistogramUpdate'


class _IWHistogramTypeEvents:
	'_IWHistogramTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{057615BD-6B39-4A09-9B1D-0785FC02A6CE}')
	coclass_clsid = IID('{0A7C4BD3-2E16-4CEF-8D4E-FB4E0AA0F636}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWInputRequestEvents:
	'_IWInputRequestEvents Interface'
	CLSID = CLSID_Sink = IID('{5198E229-1261-49A7-B7E8-8084AB8C4F50}')
	coclass_clsid = IID('{972D79E3-3EA1-4B8E-B33C-0ECA3732EA90}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnInputRequest",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnInputRequest(self, Fields=defaultNamedNotOptArg):
#		'method OnInputRequest'


class _IWInstanceEvents(DispatchBaseClass):
	'_IWInstanceEvents Interface'
	CLSID = IID('{B663FFB2-235F-11D5-A1B4-00E02963982C}')
	coclass_clsid = None

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IWLaborEvents:
	'_IWLaborEvents Interface'
	CLSID = CLSID_Sink = IID('{248B3E7C-3C90-47EF-A6E6-9BD1437AEBE5}')
	coclass_clsid = IID('{F5C3DFD0-3DAE-4043-AB52-2F9B2445711B}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWLaborTypeEvents:
	'_IWLaborTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{8D3092D9-28BF-4949-B3D6-9A557A70E65C}')
	coclass_clsid = IID('{E8307171-6464-4288-8811-77A04CA7282D}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWMachineEvents:
	'_IWMachineEvents Interface'
	CLSID = CLSID_Sink = IID('{12E061BE-E54B-11D4-8553-0020AFF488A2}')
	coclass_clsid = IID('{12E061BD-E54B-11D4-8553-0020AFF488A2}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWMachineTypeEvents:
	'_IWMachineTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{EFEEB503-BA9A-49A9-8142-424C633327B5}')
	coclass_clsid = IID('{ED85E9B1-9E8C-4B13-B5F7-5071288D83FF}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWModelEvents:
	'_IWModelEvents Interface'
	CLSID = CLSID_Sink = IID('{E39933F0-9C47-4BB6-A18C-1B60B1A7C5C1}')
	coclass_clsid = IID('{F14DAB7E-75CA-45F1-976A-0051E43B6B90}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnNew",
		        2 : "OnLoad",
		        3 : "OnSave",
		        4 : "OnBegin",
		        5 : "OnStop",
		        6 : "OnStep",
		        7 : "OnRun",
		        8 : "OnBatch",
		        9 : "OnTimeUpdate",
		       10 : "OnPause",
		       11 : "OnResume",
		       12 : "OnSimbaTrigger",
		       13 : "OnEndEvent",
		       14 : "OnHeartBeat",
		       15 : "OnPostAddElement",
		       16 : "OnPreDeleteElement",
		       17 : "OnQuantityChanged",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnNew(self):
#		'method OnNew'
#	def OnLoad(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
#		'method OnLoad'
#	def OnSave(self, FileName=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
#		'method OnSave'
#	def OnBegin(self):
#		'method OnBegin'
#	def OnStop(self, Time=defaultNamedNotOptArg):
#		'method OnStop'
#	def OnStep(self, Time=defaultNamedNotOptArg):
#		'method OnStep'
#	def OnRun(self):
#		'method OnRun'
#	def OnBatch(self):
#		'method OnBatch'
#	def OnTimeUpdate(self, Time=defaultNamedNotOptArg):
#		'method OnTimeUpdate'
#	def OnPause(self, Time=defaultNamedNotOptArg):
#		'method OnPause'
#	def OnResume(self):
#		'method OnResume'
#	def OnSimbaTrigger(self, UserData1=defaultNamedNotOptArg, UserData2=defaultNamedNotOptArg):
#		'Raised when the WITNESS SimbaTrigger action statement is executed.'
#	def OnEndEvent(self):
#		'method OnEndEvent'
#	def OnHeartBeat(self):
#		'method OnHeartBeat'
#	def OnPostAddElement(self, Element=defaultNamedNotOptArg):
#		'Raised when WITNESS has just added a new element.'
#	def OnPreDeleteElement(self, Element=defaultNamedNotOptArg):
#		'Raised when WITNESS has just delete an element.'
#	def OnQuantityChanged(self, Element=defaultNamedNotOptArg):
#		'Raised when WITNESS has just changed quantity on an element.'


class _IWModuleEvents:
	'_IWModuleEvents Interface'
	CLSID = CLSID_Sink = IID('{1AA3916B-AE9E-460F-94D6-7D1884D98193}')
	coclass_clsid = IID('{633281B9-946E-467F-BCB5-03FD7F467FB3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWModuleTypeEvents:
	'_IWModuleTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{ED5609C1-C6C9-4DA1-AD2D-30BBD10D7253}')
	coclass_clsid = IID('{EB08BC01-B2BD-4537-902C-BFD50AD8DFD2}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWNetworkEvents:
	'_IWNetworkEvents Interface'
	CLSID = CLSID_Sink = IID('{E31E5BE9-7313-459D-A73F-7C6AF9213408}')
	coclass_clsid = IID('{CBF157ED-DEEC-4462-9C2C-C21FA91B7260}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWNetworkTypeEvents:
	'_IWNetworkTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{9C405C1F-B668-46CD-9601-420DFDD10AFB}')
	coclass_clsid = IID('{79828EE4-5DD9-4A41-ADC3-9E734F38796F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPartEvents:
	'_IWPartEvents Interface'
	CLSID = CLSID_Sink = IID('{9E5B6328-B632-4BF4-B962-5ACFE43E3DDF}')
	coclass_clsid = IID('{3B8D4948-C4B3-4754-987D-DA0814438115}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPartFileEvents:
	'_IWPartFileEvents Interface'
	CLSID = CLSID_Sink = IID('{1DB7C441-5613-493F-8035-DC04FD9E4556}')
	coclass_clsid = IID('{FDEE5D65-1237-4785-A2B2-F415E6EAC8A5}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPartFileTypeEvents:
	'_IWPartFileTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{7FD0856F-EB0D-423B-9CE5-84C4B973E63B}')
	coclass_clsid = IID('{9D440E35-55C8-4A09-849E-4E6C16D11A26}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPartTypeEvents:
	'_IWPartTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{EB466F0D-214B-422A-942A-5BD1AA9F71FD}')
	coclass_clsid = IID('{E252C7AF-6108-4A67-B9AB-A3DFFE45028C}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPathEvents:
	'_IWPathEvents Interface'
	CLSID = CLSID_Sink = IID('{A6384F15-4629-4D19-A11D-3A2470E932C3}')
	coclass_clsid = IID('{9076164B-7A90-4335-AB5F-8BCB6846564E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWPathTypeEvents:
	'_IWPathTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{B76FE3D0-3C76-48C5-ADC0-77FD55D542F1}')
	coclass_clsid = IID('{0855287B-E575-4AD8-8F87-BBFAA4EFB292}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPiechartEvents:
	'_IWPiechartEvents Interface'
	CLSID = CLSID_Sink = IID('{4E8564B0-83AE-45EE-BD9D-1BDE4F0464B6}')
	coclass_clsid = IID('{154A09BA-BEB3-4C2D-A140-E1851D239814}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnPiechartUpdate",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnPiechartUpdate(self, Values=defaultNamedNotOptArg):
#		'method OnPiechartUpdate'


class _IWPiechartTypeEvents:
	'_IWPiechartTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{8D64F32A-FF93-4B89-AA4B-D505D9E66C0A}')
	coclass_clsid = IID('{F3E728B4-DFB3-443C-AA01-0DE929FB3070}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWPipeEvents:
	'_IWPipeEvents Interface'
	CLSID = CLSID_Sink = IID('{5411E9EE-6E73-4913-99DF-A6CBCC9C2A7C}')
	coclass_clsid = IID('{6769DBE4-2DC3-46D8-846F-4A62A62B5B42}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWPipeTypeEvents:
	'_IWPipeTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{371DEEFC-FABA-43A9-B8DA-426A4B6056CC}')
	coclass_clsid = IID('{B5B4C2B7-06B5-49A8-B5CC-A31E16620B3D}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWProcessorEvents:
	'_IWProcessorEvents Interface'
	CLSID = CLSID_Sink = IID('{E1F14EFF-990E-4E95-B39B-7F52A3322590}')
	coclass_clsid = IID('{56C71F23-499F-43DF-884E-0E2E0BFAC95F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWProcessorTypeEvents:
	'_IWProcessorTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{5F1FB1D2-ADE8-42F9-B817-D9B8BA2C33A4}')
	coclass_clsid = IID('{B6997BA0-F387-4C21-8939-FB6E4F79B8D1}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWReportEvents:
	'_IWReportEvents Interface'
	CLSID = CLSID_Sink = IID('{C4FF322C-3736-4D59-811E-EFE00FD7624D}')
	coclass_clsid = IID('{84B06A15-3DC4-479F-9F50-28A1F635E897}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWReportTypeEvents:
	'_IWReportTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{AC26059B-8191-428B-AAA4-161994711AE8}')
	coclass_clsid = IID('{4C208E8A-EC47-42BF-A80F-4705A0825A55}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWSectionEvents:
	'_IWSectionEvents Interface'
	CLSID = CLSID_Sink = IID('{C355F85C-C282-428F-91EC-4497A13D8380}')
	coclass_clsid = IID('{254FF920-4B28-469E-8EB6-B53CA41D5758}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWSectionTypeEvents:
	'_IWSectionTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{14A9716A-FB07-4B0F-B975-19CA14F9F05D}')
	coclass_clsid = IID('{D12CC0A0-CA9E-40E1-9C5C-78A7D82573BC}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWShiftEvents:
	'_IWShiftEvents Interface'
	CLSID = CLSID_Sink = IID('{95F31B86-2998-41E8-99DE-78C8AD9BFB19}')
	coclass_clsid = IID('{C8393854-3713-4403-86C3-14A22119E733}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWShiftTypeEvents:
	'_IWShiftTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{7F0D0280-124B-4916-A0FD-20BA46FE272C}')
	coclass_clsid = IID('{0621844B-FA65-4835-8FBD-86F62DDEE8E8}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWStandardApplicationEvents(DispatchBaseClass):
	'_IWStandardApplicationEvents Interface'
	CLSID = IID('{DE1AD8A2-DFDE-423A-8F5F-24B2CCE23961}')
	coclass_clsid = None

	def OnQuit(self):
		'Raised when the application quit occurs.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IWStationEvents:
	'_IWStationEvents Interface'
	CLSID = CLSID_Sink = IID('{313847F9-79FA-4F91-856A-ABD968A2F5D4}')
	coclass_clsid = IID('{17EE021F-753A-4FE6-8F04-F957F655948F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWStationTypeEvents:
	'_IWStationTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{8B0096ED-9410-4F27-B000-2ACE40BDB5E6}')
	coclass_clsid = IID('{FAC4F46E-2F6E-4749-B377-BB31740854AD}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWTankEvents:
	'_IWTankEvents Interface'
	CLSID = CLSID_Sink = IID('{D279DC2E-E5BE-484E-8FAE-476319D18269}')
	coclass_clsid = IID('{E172B608-4CAC-42E9-B756-DEEC0E285673}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWTankTypeEvents:
	'_IWTankTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{893B28FB-69BC-458D-89B0-24FB9476EF96}')
	coclass_clsid = IID('{DC41C651-D074-4A96-B802-497B888E1F47}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWTimeseriesEvents:
	'_IWTimeseriesEvents Interface'
	CLSID = CLSID_Sink = IID('{93D5C6A9-2E53-47E5-80C0-969E4913C5F6}')
	coclass_clsid = IID('{AD5E9293-FD7B-4EA1-B2C8-CB27C2D1BB09}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnTimeseriesUpdate",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnTimeseriesUpdate(self, Values=defaultNamedNotOptArg):
#		'method OnTimeseriesUpdate'


class _IWTimeseriesTypeEvents:
	'_IWTtimeseriesTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{CC38E78A-2250-4BA5-A50C-A2523E8B66B5}')
	coclass_clsid = IID('{CBEB96B5-10E1-4800-A763-5E417B92B34A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWTrackEvents:
	'_IWTrackEvents Interface'
	CLSID = CLSID_Sink = IID('{1070289C-8889-47D0-978C-42FA0C9BDF85}')
	coclass_clsid = IID('{0398C500-A610-463B-91A1-F4065CFEFF84}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWTrackTypeEvents:
	'_IWTrackTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{9959AEBF-296E-48D7-8BAC-DD05656AAB16}')
	coclass_clsid = IID('{5A372025-E42D-4ED3-8583-E5341700F635}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWVariableEvents:
	'_IWVariableEvents Interface'
	CLSID = CLSID_Sink = IID('{E735E961-17C8-11D5-A1B3-00E02963982C}')
	coclass_clsid = IID('{5F69FB13-188D-11D5-A1B3-00E02963982C}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnValueChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnValueChange(self, Member=defaultNamedNotOptArg):
#		'method OnValueChange'


class _IWVariableTypeEvents:
	'_IVariableTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{5AE97C62-17C4-11D5-A1B3-00E02963982C}')
	coclass_clsid = IID('{5F69FB11-188D-11D5-A1B3-00E02963982C}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


class _IWVehicleEvents:
	'_IWVehicleEvents Interface'
	CLSID = CLSID_Sink = IID('{CEC99D7A-B6A2-45A4-97E5-A3F04281EB82}')
	coclass_clsid = IID('{E3D209FA-73F5-4C1C-B167-5FF6990B1944}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStateChange(self, Member=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg):
#		'method OnStateChange'


class _IWVehicleTypeEvents:
	'_IWVehicleTypeEvents Interface'
	CLSID = CLSID_Sink = IID('{EACC1BC1-9308-40A7-9010-5A1D770AB02E}')
	coclass_clsid = IID('{683FB717-BD04-4F21-AB03-0E21A7C72C49}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


from win32com.client import CoClassBaseClass
class Application(CoClassBaseClass): # A CoClass
	# Application Class
	CLSID = IID('{651D2988-518A-11D4-9AAF-00E0295CD2CC}')
	coclass_sources = [
		_IWApplicationEvents,
	]
	default_source = _IWApplicationEvents
	coclass_interfaces = [
		IWApplication,
		IWUserProperties,
		IWRemoteControl,
	]
	default_interface = IWApplication

class ApplicationViewer(CoClassBaseClass): # A CoClass
	# ApplicationViewer Class
	CLSID = IID('{074E71B1-34AD-4D47-9B9D-167E56C380AC}')
	coclass_sources = [
		_IWApplicationViewerEvents,
	]
	default_source = _IWApplicationViewerEvents
	coclass_interfaces = [
		IWApplication,
		IWUserProperties,
		IWRemoteControl,
	]
	default_interface = IWApplication

class Assemble(CoClassBaseClass): # A CoClass
	# Assemble Class
	CLSID = IID('{0E61D6B4-D568-4D42-97AF-946AD57E8293}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWAssemble,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWAssemble

class Attribute(CoClassBaseClass): # A CoClass
	# Attribute Class
	CLSID = IID('{90E44757-6068-437E-9282-EC1F008CA370}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWAttribute,
		IWElement,
		IWUserElement,
	]
	default_interface = IWAttribute

class AttributeInstance(CoClassBaseClass): # A CoClass
	# AttributeInstance Class
	CLSID = IID('{EB396772-21D0-11D5-8586-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWAttributeInstance,
		IWInstance,
	]
	default_interface = IWAttributeInstance

class AttributeInstances(CoClassBaseClass): # A CoClass
	# AttributeInstances Class
	CLSID = IID('{EB396773-21D0-11D5-8586-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWAttributeInstances,
	]
	default_interface = IWAttributeInstances

class AttributeType(CoClassBaseClass): # A CoClass
	# AttributeType Class
	CLSID = IID('{8D03C4CE-F14E-4819-AA81-67B677C7E6AE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWAttributeType,
	]
	default_interface = IWAttributeType

class BPMViewer(CoClassBaseClass): # A CoClass
	# BPMViewer Class
	CLSID = IID('{340F5316-1C07-4BB9-8588-8AF9083B45F9}')
	coclass_sources = [
		_IWApplicationViewerEvents,
	]
	default_source = _IWApplicationViewerEvents
	coclass_interfaces = [
		IWApplication,
		IWUserProperties,
		IWRemoteControl,
	]
	default_interface = IWApplication

class Backdrop(CoClassBaseClass): # A CoClass
	# Backdrop Class
	CLSID = IID('{8F1E1722-B3BC-49BE-900F-1A1015B3E19B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWBackdrop,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWBackdrop

class Buffer(CoClassBaseClass): # A CoClass
	# Buffer Class
	CLSID = IID('{DB0E57F7-7B49-4C88-9B76-8C4D050C1DF1}')
	coclass_sources = [
		_IWBufferEvents,
	]
	default_source = _IWBufferEvents
	coclass_interfaces = [
		IWBuffer,
		IWElement,
		IWUserElement,
	]
	default_interface = IWBuffer

class BufferInstance(CoClassBaseClass): # A CoClass
	# BufferInstance Class
	CLSID = IID('{353A4670-5506-4942-83F0-3B60CDC128E8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWBufferInstance,
		IWInstance,
	]
	default_interface = IWBufferInstance

class BufferInstances(CoClassBaseClass): # A CoClass
	# BufferInstances Class
	CLSID = IID('{4E62D659-868B-4718-84A0-245F91232CE3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWBufferInstances,
	]
	default_interface = IWBufferInstances

class BufferMeasure(CoClassBaseClass): # A CoClass
	# BufferMeasure Class
	CLSID = IID('{39A7781C-CAB1-4D5C-B409-ACBAC218779A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWBufferMeasure,
	]
	default_interface = IWBufferMeasure

class BufferMeasures(CoClassBaseClass): # A CoClass
	# BufferMeasures Class
	CLSID = IID('{C3C2BD9F-7169-4413-BE59-93572B2F46B2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWBufferMeasures,
	]
	default_interface = IWBufferMeasures

class BufferType(CoClassBaseClass): # A CoClass
	# BufferType Class
	CLSID = IID('{E31B9C55-790E-46DF-99CB-E07885AE9D02}')
	coclass_sources = [
		_IWBufferTypeEvents,
	]
	default_source = _IWBufferTypeEvents
	coclass_interfaces = [
		IWBufferType,
	]
	default_interface = IWBufferType

class Carrier(CoClassBaseClass): # A CoClass
	# Carrier Class
	CLSID = IID('{145C2B6F-9CDF-426D-ABAA-E36544E0026F}')
	coclass_sources = [
		_IWCarrierEvents,
	]
	default_source = _IWCarrierEvents
	coclass_interfaces = [
		IWCarrier,
		IWElement,
		IWUserElement,
	]
	default_interface = IWCarrier

class CarrierInstance(CoClassBaseClass): # A CoClass
	# CarrierInstance Class
	CLSID = IID('{437FDE2F-0551-4339-B51A-59CDA7F6A287}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWCarrierInstance,
		IWInstance,
	]
	default_interface = IWCarrierInstance

class CarrierInstances(CoClassBaseClass): # A CoClass
	# CarrierInstances Class
	CLSID = IID('{6ADB5AF9-8FD6-437C-9FD9-FD39260B1A01}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWCarrierInstances,
	]
	default_interface = IWCarrierInstances

class CarrierType(CoClassBaseClass): # A CoClass
	# CarrierType Class
	CLSID = IID('{82A079AD-E254-4774-98AC-CA848A60DD37}')
	coclass_sources = [
		_IWCarrierTypeEvents,
	]
	default_source = _IWCarrierTypeEvents
	coclass_interfaces = [
		IWCarrierType,
	]
	default_interface = IWCarrierType

class Color(CoClassBaseClass): # A CoClass
	# Color Class
	CLSID = IID('{CA7D13A2-FBDA-4FCC-B552-B60468D38BD3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWColor,
	]
	default_interface = IWColor

class Conveyor(CoClassBaseClass): # A CoClass
	# Conveyor Class
	CLSID = IID('{645C5AF8-DE5E-42B9-8CAC-EE7C52560D03}')
	coclass_sources = [
		_IWConveyorEvents,
	]
	default_source = _IWConveyorEvents
	coclass_interfaces = [
		IWConveyor,
		IWElement,
		IWUserElement,
	]
	default_interface = IWConveyor

class ConveyorBreakdown(CoClassBaseClass): # A CoClass
	# Machine Conveyor Class
	CLSID = IID('{37421EC3-04F7-405D-ACCD-CB2D79DF9ABA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorBreakdown,
	]
	default_interface = IWConveyorBreakdown

class ConveyorBreakdownInstance(CoClassBaseClass): # A CoClass
	# Conveyor Breakdown Instance Class
	CLSID = IID('{CC93BB4E-BDC8-4A90-9F3E-7EBDF0D040DC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorBreakdownInstance,
	]
	default_interface = IWConveyorBreakdownInstance

class ConveyorBreakdownInstances(CoClassBaseClass): # A CoClass
	# Conveyor Breakdown Instances Class
	CLSID = IID('{2E98B9F5-9406-4019-8225-26A879F6CBE2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorBreakdownInstances,
	]
	default_interface = IWConveyorBreakdownInstances

class ConveyorBreakdowns(CoClassBaseClass): # A CoClass
	# Conveyor Breakdowns Class
	CLSID = IID('{970B35CB-E87F-4727-B542-43BE71FFF450}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorBreakdowns,
	]
	default_interface = IWConveyorBreakdowns

class ConveyorInstance(CoClassBaseClass): # A CoClass
	# ConveyorInstance Class
	CLSID = IID('{E4159C32-7F0C-41DF-AB41-8269C1AEEA05}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorInstance,
		IWInstance,
	]
	default_interface = IWConveyorInstance

class ConveyorInstances(CoClassBaseClass): # A CoClass
	# ConveyorInstances Class
	CLSID = IID('{A7E6802F-5CA6-4489-9F5B-4B06FC0E85C4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorInstances,
	]
	default_interface = IWConveyorInstances

class ConveyorMeasure(CoClassBaseClass): # A CoClass
	# ConveyorMeasure Class
	CLSID = IID('{4458B2E4-FDA8-4241-9882-529C40085984}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorMeasure,
	]
	default_interface = IWConveyorMeasure

class ConveyorMeasures(CoClassBaseClass): # A CoClass
	# ConveyorMeasures Class
	CLSID = IID('{A33BE52E-CD53-4DFC-B543-733FD618A7C9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorMeasures,
	]
	default_interface = IWConveyorMeasures

class ConveyorSensor(CoClassBaseClass): # A CoClass
	# ConveyorSensor Class
	CLSID = IID('{512108B5-3FE7-453E-9169-B91CCCC8F719}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorSensor,
	]
	default_interface = IWConveyorSensor

class ConveyorSensors(CoClassBaseClass): # A CoClass
	# ConveyorSensors Class
	CLSID = IID('{1F9233EA-A80D-40E7-B070-03049F936324}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWConveyorSensors,
	]
	default_interface = IWConveyorSensors

class ConveyorType(CoClassBaseClass): # A CoClass
	# ConveyorType Class
	CLSID = IID('{E35C70B8-FBAA-4C39-A845-9E45DF62BB63}')
	coclass_sources = [
		_IWConveyorTypeEvents,
	]
	default_source = _IWConveyorTypeEvents
	coclass_interfaces = [
		IWConveyorType,
	]
	default_interface = IWConveyorType

class DataTable(CoClassBaseClass): # A CoClass
	# DataTable Class
	CLSID = IID('{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}')
	coclass_sources = [
		_IWDataTableEvents,
	]
	default_source = _IWDataTableEvents
	coclass_interfaces = [
		IWDataTable,
		IWElement,
		IWUserElement,
	]
	default_interface = IWDataTable

class DataTableColumnItem(CoClassBaseClass): # A CoClass
	# DataTableColumnItemClass
	CLSID = IID('{F0832FC5-9D60-4542-BB68-EACABBE75136}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDataTableColumnItem,
	]
	default_interface = IWDataTableColumnItem

class DataTableColumnItems(CoClassBaseClass): # A CoClass
	# DataTableColumnItemClass
	CLSID = IID('{A6C95EEB-EFDD-4462-91C1-6A6EB787E94B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDataTableColumnItems,
	]
	default_interface = IWDataTableColumnItems

class DataTableInstance(CoClassBaseClass): # A CoClass
	# Represents a member instance of data table element
	CLSID = IID('{EBF1F7CB-5F07-4E2F-B923-DA1873E55206}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDataTableInstance,
		IWInstance,
	]
	default_interface = IWDataTableInstance

class DataTableInstances(CoClassBaseClass): # A CoClass
	# Represents a collection of member instances for a data table element
	CLSID = IID('{4B219466-3B72-4A0C-BC67-A4460E22E7C2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDataTableInstances,
	]
	default_interface = IWDataTableInstances

class DataTableType(CoClassBaseClass): # A CoClass
	# DataTableType Class
	CLSID = IID('{7DCDF7AB-9E07-4B20-A73F-A0188D6EDDF4}')
	coclass_sources = [
		_IWDataTableTypeEvents,
	]
	default_source = _IWDataTableTypeEvents
	coclass_interfaces = [
		IWDataTableType,
	]
	default_interface = IWDataTableType

class Dimensions(CoClassBaseClass): # A CoClass
	# Dimensions Class
	CLSID = IID('{D3F86990-4072-11D5-A1B8-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDimensions,
	]
	default_interface = IWDimensions

class DrawTool(CoClassBaseClass): # A CoClass
	# DrawTool Class
	CLSID = IID('{1D60E254-0A19-4E2C-9D3A-F5D9B6ADFDF7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWDrawTool,
	]
	default_interface = IWDrawTool

class Element(CoClassBaseClass): # A CoClass
	# Element Class
	CLSID = IID('{2830E4FB-14FA-4958-8765-0F33560C9138}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWElement,
	]
	default_interface = IWElement

class Elements(CoClassBaseClass): # A CoClass
	# Elements Class
	CLSID = IID('{7CC1ABA0-46BA-423A-8A30-D2F2974CEE63}')
	coclass_sources = [
		_IWElementsEvents,
	]
	default_source = _IWElementsEvents
	coclass_interfaces = [
		IWElements,
	]
	default_interface = IWElements

class ErrorsAndWarnings(CoClassBaseClass): # A CoClass
	# ErrorsAndWarnings Class
	CLSID = IID('{A8990927-8EDC-473B-BA0B-834DF5C23FBF}')
	coclass_sources = [
		_IWErrorsAndWarningsEvents,
	]
	default_source = _IWErrorsAndWarningsEvents
	coclass_interfaces = [
		IWErrorsAndWarnings,
	]
	default_interface = IWErrorsAndWarnings

class Factors(CoClassBaseClass): # A CoClass
	# Represents a breakdowns/setups factors object
	CLSID = IID('{BA00DD6A-4545-4AC0-87CC-375C48077E2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFactors,
	]
	default_interface = IWFactors

class Fields(CoClassBaseClass): # A CoClass
	# InputFields Class
	CLSID = IID('{D783B13A-273A-4E8A-805F-75991A508E09}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFields,
	]
	default_interface = IWFields

class File(CoClassBaseClass): # A CoClass
	# File Class
	CLSID = IID('{3E70BB16-0A94-4BC5-A921-2BCE98CB024D}')
	coclass_sources = [
		_IWFileEvents,
	]
	default_source = _IWFileEvents
	coclass_interfaces = [
		IWFile,
		IWElement,
		IWUserElement,
	]
	default_interface = IWFile

class FileType(CoClassBaseClass): # A CoClass
	# FileType Class
	CLSID = IID('{C6097B81-5EA5-4FAB-93FE-741AB26AAE1F}')
	coclass_sources = [
		_IWFileTypeEvents,
	]
	default_source = _IWFileTypeEvents
	coclass_interfaces = [
		IWFileType,
	]
	default_interface = IWFileType

class Function(CoClassBaseClass): # A CoClass
	# Function Class
	CLSID = IID('{6E799CC3-0423-4712-9D4F-3081FE6D91A5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFunction,
		IWElement,
		IWUserElement,
	]
	default_interface = IWFunction

class FunctionParameter(CoClassBaseClass): # A CoClass
	# FunctionParameter Class
	CLSID = IID('{776DC152-E354-466E-A22E-F8B3BC810AA5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFunctionParameter,
	]
	default_interface = IWFunctionParameter

class FunctionParameters(CoClassBaseClass): # A CoClass
	# FunctionParameters Class
	CLSID = IID('{3641AADE-9279-4C7D-8D41-092AE9ACAD8F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFunctionParameters,
	]
	default_interface = IWFunctionParameters

class FunctionType(CoClassBaseClass): # A CoClass
	# FunctionType Class
	CLSID = IID('{26A60ABA-817C-459B-BFBF-2E9F8FD16C96}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFunctionType,
	]
	default_interface = IWFunctionType

class Graphics(CoClassBaseClass): # A CoClass
	# Graphics Class
	CLSID = IID('{59E05BC6-943D-4E23-AECE-435624AF9AC4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWGraphics,
	]
	default_interface = IWGraphics

class Histogram(CoClassBaseClass): # A CoClass
	# Histogram Class
	CLSID = IID('{4CF57EFE-8DD9-4C70-A10A-AEEF3FD68E5D}')
	coclass_sources = [
		_IWHistogramEvents,
	]
	default_source = _IWHistogramEvents
	coclass_interfaces = [
		IWHistogram,
		IWElement,
		IWUserElement,
	]
	default_interface = IWHistogram

class HistogramType(CoClassBaseClass): # A CoClass
	# HistogramType Class
	CLSID = IID('{0A7C4BD3-2E16-4CEF-8D4E-FB4E0AA0F636}')
	coclass_sources = [
		_IWHistogramTypeEvents,
	]
	default_source = _IWHistogramTypeEvents
	coclass_interfaces = [
		IWHistogramType,
	]
	default_interface = IWHistogramType

class InputRequest(CoClassBaseClass): # A CoClass
	# InputRequest Class
	CLSID = IID('{972D79E3-3EA1-4B8E-B33C-0ECA3732EA90}')
	coclass_sources = [
		_IWInputRequestEvents,
	]
	default_source = _IWInputRequestEvents
	coclass_interfaces = [
		IWInputRequest,
	]
	default_interface = IWInputRequest

class Instance(CoClassBaseClass): # A CoClass
	# Instance Class
	CLSID = IID('{D3F86991-4072-11D5-A1B8-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWInstance,
	]
	default_interface = IWInstance

class Instances(CoClassBaseClass): # A CoClass
	# Instances Class
	CLSID = IID('{AE9CA10B-2DCD-4C7A-A849-E0AAA8F90C71}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWInstances,
	]
	default_interface = IWInstances

class Labor(CoClassBaseClass): # A CoClass
	# Labor Class
	CLSID = IID('{F5C3DFD0-3DAE-4043-AB52-2F9B2445711B}')
	coclass_sources = [
		_IWLaborEvents,
	]
	default_source = _IWLaborEvents
	coclass_interfaces = [
		IWLabor,
		IWElement,
		IWUserElement,
	]
	default_interface = IWLabor

class LaborInstance(CoClassBaseClass): # A CoClass
	# LaborInstance Class
	CLSID = IID('{9C70AC8B-4060-4546-BA5D-8F0DCF16CFEF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborInstance,
		IWInstance,
	]
	default_interface = IWLaborInstance

class LaborInstances(CoClassBaseClass): # A CoClass
	# LaborInstances Class
	CLSID = IID('{DC91B434-6DAC-4512-942D-8F3CDD05ACAF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborInstances,
	]
	default_interface = IWLaborInstances

class LaborMeasure(CoClassBaseClass): # A CoClass
	# LaborMeasure Class
	CLSID = IID('{338B12F3-452B-4C92-9BE4-D41387FD21CB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborMeasure,
	]
	default_interface = IWLaborMeasure

class LaborMeasures(CoClassBaseClass): # A CoClass
	# LaborMeasures Class
	CLSID = IID('{68B8BE1E-91A4-4DE8-BCB9-E9AB7804577A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborMeasures,
	]
	default_interface = IWLaborMeasures

class LaborRule(CoClassBaseClass): # A CoClass
	# LaborRule Class
	CLSID = IID('{A1B86D56-E79D-11D4-8556-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborRule,
	]
	default_interface = IWLaborRule

class LaborRules(CoClassBaseClass): # A CoClass
	# LaborRules Class
	CLSID = IID('{A1B86D58-E79D-11D4-8556-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborRules,
	]
	default_interface = IWLaborRules

class LaborShift(CoClassBaseClass): # A CoClass
	# LaborShift Class
	CLSID = IID('{D3B026A0-50E9-11D5-A1C1-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborShift,
	]
	default_interface = IWLaborShift

class LaborShifts(CoClassBaseClass): # A CoClass
	# LaborShifts Class
	CLSID = IID('{D3B026A1-50E9-11D5-A1C1-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWLaborShifts,
	]
	default_interface = IWLaborShifts

class LaborType(CoClassBaseClass): # A CoClass
	# LaborType Class
	CLSID = IID('{E8307171-6464-4288-8811-77A04CA7282D}')
	coclass_sources = [
		_IWLaborTypeEvents,
	]
	default_source = _IWLaborTypeEvents
	coclass_interfaces = [
		IWLaborType,
	]
	default_interface = IWLaborType

class Machine(CoClassBaseClass): # A CoClass
	# Machine Class
	CLSID = IID('{12E061BD-E54B-11D4-8553-0020AFF488A2}')
	coclass_sources = [
		_IWMachineEvents,
	]
	default_source = _IWMachineEvents
	coclass_interfaces = [
		IWMachine,
		IWElement,
		IWUserElement,
	]
	default_interface = IWMachine

class MachineBreakdown(CoClassBaseClass): # A CoClass
	# Machine Breakdown Class
	CLSID = IID('{2956F9E1-CF7A-4388-8E3B-3BD46C9F5B5A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineBreakdown,
	]
	default_interface = IWMachineBreakdown

class MachineBreakdownInstance(CoClassBaseClass): # A CoClass
	# Machine Breakdown Instance Class
	CLSID = IID('{FA23351B-6EC3-470E-9D33-6B7466996606}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineBreakdownInstance,
	]
	default_interface = IWMachineBreakdownInstance

class MachineBreakdownInstances(CoClassBaseClass): # A CoClass
	# Machine Breakdown Instances Class
	CLSID = IID('{2C948309-016C-4430-8F8E-8FD6EAB90BFD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineBreakdownInstances,
	]
	default_interface = IWMachineBreakdownInstances

class MachineBreakdowns(CoClassBaseClass): # A CoClass
	# Machine Breakdowns Class
	CLSID = IID('{514D7591-4ACC-4E7A-B9F9-5361350218D2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineBreakdowns,
	]
	default_interface = IWMachineBreakdowns

class MachineCycle(CoClassBaseClass): # A CoClass
	# MachineCycle Class
	CLSID = IID('{A1B86D52-E79D-11D4-8556-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineCycle,
	]
	default_interface = IWMachineCycle

class MachineCycleInstance(CoClassBaseClass): # A CoClass
	# MachineCycleInstance Class
	CLSID = IID('{D7462A12-315B-468E-9B24-44AB329B844D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineCycleInstance,
	]
	default_interface = IWMachineCycleInstance

class MachineCycleInstances(CoClassBaseClass): # A CoClass
	# MachineCycleInstances Class
	CLSID = IID('{30804F82-C8D0-498A-BB3E-76C1B1B393CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineCycleInstances,
	]
	default_interface = IWMachineCycleInstances

class MachineCycles(CoClassBaseClass): # A CoClass
	# MachineCycles Class
	CLSID = IID('{A1B86D54-E79D-11D4-8556-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineCycles,
	]
	default_interface = IWMachineCycles

class MachineInstance(CoClassBaseClass): # A CoClass
	# MachineInstance Class
	CLSID = IID('{725808C2-8F7A-41A1-B348-12EC36BC8FCF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineInstance,
		IWInstance,
	]
	default_interface = IWMachineInstance

class MachineInstances(CoClassBaseClass): # A CoClass
	# MachineInstances Class
	CLSID = IID('{E6A2B0E2-8C62-43B0-88E1-C462E6CE584B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineInstances,
	]
	default_interface = IWMachineInstances

class MachineMeasure(CoClassBaseClass): # A CoClass
	# MachineMeasure Class
	CLSID = IID('{CB6E9DA5-A948-4FD0-9873-1B64E06BADE1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineMeasure,
	]
	default_interface = IWMachineMeasure

class MachineMeasures(CoClassBaseClass): # A CoClass
	# MachineMeasures Class
	CLSID = IID('{4AEDE750-7BBF-4588-B547-FD7C8200B522}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineMeasures,
	]
	default_interface = IWMachineMeasures

class MachineSetup(CoClassBaseClass): # A CoClass
	# WMachineSetup Class
	CLSID = IID('{94A0CFA9-E6D7-11D4-8555-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineSetup,
	]
	default_interface = IWMachineSetup

class MachineSetupInstance(CoClassBaseClass): # A CoClass
	# MachineSetupInstance Class
	CLSID = IID('{59145A07-9E49-4EE1-B49A-5447C3B692C9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineSetupInstance,
	]
	default_interface = IWMachineSetupInstance

class MachineSetupInstances(CoClassBaseClass): # A CoClass
	# MachineSetupInstances Class
	CLSID = IID('{3D903BF9-0617-4B73-BD0E-0D0D10F0B914}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineSetupInstances,
	]
	default_interface = IWMachineSetupInstances

class MachineSetups(CoClassBaseClass): # A CoClass
	# MachineSetups Class
	CLSID = IID('{94A0CFAB-E6D7-11D4-8555-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMachineSetups,
	]
	default_interface = IWMachineSetups

class MachineType(CoClassBaseClass): # A CoClass
	# MachineType Class
	CLSID = IID('{ED85E9B1-9E8C-4B13-B5F7-5071288D83FF}')
	coclass_sources = [
		_IWMachineTypeEvents,
	]
	default_source = _IWMachineTypeEvents
	coclass_interfaces = [
		IWMachineType,
	]
	default_interface = IWMachineType

class MeasureValue(CoClassBaseClass): # A CoClass
	# MeasureValue Class
	CLSID = IID('{445890C6-E66E-4620-8413-C613D7BD29D3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWMeasureValue,
	]
	default_interface = IWMeasureValue

class Model(CoClassBaseClass): # A CoClass
	# Model Class
	CLSID = IID('{F14DAB7E-75CA-45F1-976A-0051E43B6B90}')
	coclass_sources = [
		_IWModelEvents,
	]
	default_source = _IWModelEvents
	coclass_interfaces = [
		IWModel,
	]
	default_interface = IWModel

class ModelEventManager(CoClassBaseClass): # A CoClass
	# Model Event Manager Class
	CLSID = IID('{012AE1FD-9E78-4E20-8922-2C6F51E24BFF}')
	coclass_sources = [
		_IWModelEvents,
	]
	default_source = _IWModelEvents
	coclass_interfaces = [
		IWModelEventManager,
	]
	default_interface = IWModelEventManager

class ModelMeasure(CoClassBaseClass): # A CoClass
	# ModelMeasure Class
	CLSID = IID('{1C98A595-B908-4D1B-9D3D-0D5BA37A1AD3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWModelMeasure,
	]
	default_interface = IWModelMeasure

class ModelMeasures(CoClassBaseClass): # A CoClass
	# ModelMeasures Class
	CLSID = IID('{FE7DAABD-B1F4-4E34-A4DC-334D58DBBE22}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWModelMeasures,
	]
	default_interface = IWModelMeasures

class Module(CoClassBaseClass): # A CoClass
	# Module Class
	CLSID = IID('{633281B9-946E-467F-BCB5-03FD7F467FB3}')
	coclass_sources = [
		_IWModuleEvents,
	]
	default_source = _IWModuleEvents
	coclass_interfaces = [
		IWModule,
		IWElement,
		IWUserElement,
	]
	default_interface = IWModule

class ModuleType(CoClassBaseClass): # A CoClass
	# ModuleType Class
	CLSID = IID('{EB08BC01-B2BD-4537-902C-BFD50AD8DFD2}')
	coclass_sources = [
		_IWModuleTypeEvents,
	]
	default_source = _IWModuleTypeEvents
	coclass_interfaces = [
		IWModuleType,
	]
	default_interface = IWModuleType

class Network(CoClassBaseClass): # A CoClass
	# Network Class
	CLSID = IID('{CBF157ED-DEEC-4462-9C2C-C21FA91B7260}')
	coclass_sources = [
		_IWNetworkEvents,
	]
	default_source = _IWNetworkEvents
	coclass_interfaces = [
		IWNetwork,
		IWElement,
		IWUserElement,
	]
	default_interface = IWNetwork

class NetworkType(CoClassBaseClass): # A CoClass
	# NetworkType Class
	CLSID = IID('{79828EE4-5DD9-4A41-ADC3-9E734F38796F}')
	coclass_sources = [
		_IWNetworkTypeEvents,
	]
	default_source = _IWNetworkTypeEvents
	coclass_interfaces = [
		IWNetworkType,
	]
	default_interface = IWNetworkType

class NONE(CoClassBaseClass): # A CoClass
	# None Class
	CLSID = IID('{5353FA8F-7EE3-428C-ACB7-B007171BCCB5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWNone,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWNone

class Part(CoClassBaseClass): # A CoClass
	# Part Class
	CLSID = IID('{3B8D4948-C4B3-4754-987D-DA0814438115}')
	coclass_sources = [
		_IWPartEvents,
	]
	default_source = _IWPartEvents
	coclass_interfaces = [
		IWPart,
		IWElement,
		IWUserElement,
	]
	default_interface = IWPart

class PartArrivalProfileEntries(CoClassBaseClass): # A CoClass
	# PartArrivalProfileEntries Class
	CLSID = IID('{D3E84445-58CB-11D5-9BDB-00E0295CD2CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartArrivalProfileEntries,
	]
	default_interface = IWPartArrivalProfileEntries

class PartArrivalProfileEntry(CoClassBaseClass): # A CoClass
	# PartArrivalProfileEntry Class
	CLSID = IID('{D3E84444-58CB-11D5-9BDB-00E0295CD2CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartArrivalProfileEntry,
	]
	default_interface = IWPartArrivalProfileEntry

class PartFile(CoClassBaseClass): # A CoClass
	# PartFile Class
	CLSID = IID('{FDEE5D65-1237-4785-A2B2-F415E6EAC8A5}')
	coclass_sources = [
		_IWPartFileEvents,
	]
	default_source = _IWPartFileEvents
	coclass_interfaces = [
		IWPartFile,
		IWElement,
		IWUserElement,
	]
	default_interface = IWPartFile

class PartFileType(CoClassBaseClass): # A CoClass
	# PartFileType Class
	CLSID = IID('{9D440E35-55C8-4A09-849E-4E6C16D11A26}')
	coclass_sources = [
		_IWPartFileTypeEvents,
	]
	default_source = _IWPartFileTypeEvents
	coclass_interfaces = [
		IWPartFileType,
	]
	default_interface = IWPartFileType

class PartInstance(CoClassBaseClass): # A CoClass
	# PartInstance Class
	CLSID = IID('{E8B55477-6F44-4C74-BB6F-383D7FCE0841}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartInstance,
		IWInstance,
	]
	default_interface = IWPartInstance

class PartInstances(CoClassBaseClass): # A CoClass
	# PartInstances Class
	CLSID = IID('{63D176D2-0331-11D5-9B89-00E0295CD2CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartInstances,
	]
	default_interface = IWPartInstances

class PartMeasure(CoClassBaseClass): # A CoClass
	# PartMeasure Class
	CLSID = IID('{786649BA-17B5-4A15-95AD-FB2109E28BF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartMeasure,
	]
	default_interface = IWPartMeasure

class PartMeasures(CoClassBaseClass): # A CoClass
	# PartMeasures Class
	CLSID = IID('{B96C1292-8AC4-4486-B26A-29D2A1F5E43C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartMeasures,
	]
	default_interface = IWPartMeasures

class PartRouteStage(CoClassBaseClass): # A CoClass
	# PartRouteStage Class
	CLSID = IID('{2F373901-5042-11D5-9BD3-00E0295CD2CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartRouteStage,
	]
	default_interface = IWPartRouteStage

class PartRouteStages(CoClassBaseClass): # A CoClass
	# PartRouteStages Class
	CLSID = IID('{2F373902-5042-11D5-9BD3-00E0295CD2CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPartRouteStages,
	]
	default_interface = IWPartRouteStages

class PartType(CoClassBaseClass): # A CoClass
	# PartType Class
	CLSID = IID('{E252C7AF-6108-4A67-B9AB-A3DFFE45028C}')
	coclass_sources = [
		_IWPartTypeEvents,
	]
	default_source = _IWPartTypeEvents
	coclass_interfaces = [
		IWPartType,
	]
	default_interface = IWPartType

class Path(CoClassBaseClass): # A CoClass
	# Path Class
	CLSID = IID('{9076164B-7A90-4335-AB5F-8BCB6846564E}')
	coclass_sources = [
		_IWPathEvents,
	]
	default_source = _IWPathEvents
	coclass_interfaces = [
		IWPath,
		IWElement,
		IWUserElement,
	]
	default_interface = IWPath

class PathData(CoClassBaseClass): # A CoClass
	# Path Data Class
	CLSID = IID('{C34D5CEC-372F-4362-A4E9-0EF1991752AB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPathData,
	]
	default_interface = IWPathData

class PathElementExpression(CoClassBaseClass): # A CoClass
	# PathElementExpression Class
	CLSID = IID('{4700CB1B-4FB7-4938-BA2A-D034D88DE1CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPathElementExpression,
	]
	default_interface = IWPathElementExpression

class PathElementExpressions(CoClassBaseClass): # A CoClass
	# PathElementExpressions Class
	CLSID = IID('{64AE4DE5-5F48-4B53-849C-4DA165E7ED42}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPathElementExpressions,
	]
	default_interface = IWPathElementExpressions

class PathMeasure(CoClassBaseClass): # A CoClass
	# PathMeasure Class
	CLSID = IID('{BECF2229-7372-452D-9343-0FC2CC7586DB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPathMeasure,
	]
	default_interface = IWPathMeasure

class PathMeasures(CoClassBaseClass): # A CoClass
	# PathMeasures Class
	CLSID = IID('{6E4938CE-EAB5-4977-BE54-350B9D31FA37}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPathMeasures,
	]
	default_interface = IWPathMeasures

class PathType(CoClassBaseClass): # A CoClass
	# PathType Class
	CLSID = IID('{0855287B-E575-4AD8-8F87-BBFAA4EFB292}')
	coclass_sources = [
		_IWPathTypeEvents,
	]
	default_source = _IWPathTypeEvents
	coclass_interfaces = [
		IWPathType,
	]
	default_interface = IWPathType

class Piechart(CoClassBaseClass): # A CoClass
	# Piechart Class
	CLSID = IID('{154A09BA-BEB3-4C2D-A140-E1851D239814}')
	coclass_sources = [
		_IWPiechartEvents,
	]
	default_source = _IWPiechartEvents
	coclass_interfaces = [
		IWPiechart,
		IWElement,
		IWUserElement,
	]
	default_interface = IWPiechart

class PiechartType(CoClassBaseClass): # A CoClass
	# PiechartType Class
	CLSID = IID('{F3E728B4-DFB3-443C-AA01-0DE929FB3070}')
	coclass_sources = [
		_IWPiechartTypeEvents,
	]
	default_source = _IWPiechartTypeEvents
	coclass_interfaces = [
		IWPiechartType,
	]
	default_interface = IWPiechartType

class Pipe(CoClassBaseClass): # A CoClass
	# Pipe Class
	CLSID = IID('{6769DBE4-2DC3-46D8-846F-4A62A62B5B42}')
	coclass_sources = [
		_IWPipeEvents,
	]
	default_source = _IWPipeEvents
	coclass_interfaces = [
		IWPipe,
		IWElement,
		IWUserElement,
	]
	default_interface = IWPipe

class PipeInstance(CoClassBaseClass): # A CoClass
	# PipeInstance Class
	CLSID = IID('{C5CF2888-AEE4-4AD9-97E0-EA98A8942657}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPipeInstance,
		IWInstance,
	]
	default_interface = IWPipeInstance

class PipeInstances(CoClassBaseClass): # A CoClass
	# PipeInstances Class
	CLSID = IID('{E02FA232-56F5-4402-82E0-D7CD11D86054}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPipeInstances,
	]
	default_interface = IWPipeInstances

class PipeType(CoClassBaseClass): # A CoClass
	# PipeType Class
	CLSID = IID('{B5B4C2B7-06B5-49A8-B5CC-A31E16620B3D}')
	coclass_sources = [
		_IWPipeTypeEvents,
	]
	default_source = _IWPipeTypeEvents
	coclass_interfaces = [
		IWPipeType,
	]
	default_interface = IWPipeType

class Point(CoClassBaseClass): # A CoClass
	# Point Class
	CLSID = IID('{A82FD057-3F6F-4226-92D6-86B4986DE528}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPoint,
	]
	default_interface = IWPoint

class Points(CoClassBaseClass): # A CoClass
	# Points Class
	CLSID = IID('{6EB0EC81-8790-42B4-BE70-E20DA6DEB0E9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWPoints,
	]
	default_interface = IWPoints

class Processor(CoClassBaseClass): # A CoClass
	# Processor Class
	CLSID = IID('{56C71F23-499F-43DF-884E-0E2E0BFAC95F}')
	coclass_sources = [
		_IWProcessorEvents,
	]
	default_source = _IWProcessorEvents
	coclass_interfaces = [
		IWProcessor,
		IWElement,
		IWUserElement,
	]
	default_interface = IWProcessor

class ProcessorInstance(CoClassBaseClass): # A CoClass
	# ProcessorInstance Class
	CLSID = IID('{ED6EF6BA-D94F-4610-A37E-C0F7741518BD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWProcessorInstance,
		IWInstance,
	]
	default_interface = IWProcessorInstance

class ProcessorInstances(CoClassBaseClass): # A CoClass
	# ProcessorInstances Class
	CLSID = IID('{6F167138-34BB-4CB8-AB40-458C91C0D08D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWProcessorInstances,
	]
	default_interface = IWProcessorInstances

class ProcessorType(CoClassBaseClass): # A CoClass
	# ProcessorType Class
	CLSID = IID('{B6997BA0-F387-4C21-8939-FB6E4F79B8D1}')
	coclass_sources = [
		_IWProcessorTypeEvents,
	]
	default_source = _IWProcessorTypeEvents
	coclass_interfaces = [
		IWProcessorType,
	]
	default_interface = IWProcessorType

class RandomNumberUsage(CoClassBaseClass): # A CoClass
	# Represents a random number usage object
	CLSID = IID('{968F15BB-1051-4D51-A001-9AB3C62127B1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWRandomNumberUsage,
	]
	default_interface = IWRandomNumberUsage

class Report(CoClassBaseClass): # A CoClass
	# Report Class
	CLSID = IID('{84B06A15-3DC4-479F-9F50-28A1F635E897}')
	coclass_sources = [
		_IWReportEvents,
	]
	default_source = _IWReportEvents
	coclass_interfaces = [
		IWReport,
		IWElement,
		IWUserElement,
	]
	default_interface = IWReport

class ReportData(CoClassBaseClass): # A CoClass
	# Represents a report data object
	CLSID = IID('{04B51A36-E475-47B9-A2CC-ED44D69CBD9C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWReportData,
	]
	default_interface = IWReportData

class ReportType(CoClassBaseClass): # A CoClass
	# ReportType Class
	CLSID = IID('{4C208E8A-EC47-42BF-A80F-4705A0825A55}')
	coclass_sources = [
		_IWReportTypeEvents,
	]
	default_source = _IWReportTypeEvents
	coclass_interfaces = [
		IWReportType,
	]
	default_interface = IWReportType

class Responses(CoClassBaseClass): # A CoClass
	# Responses Class
	CLSID = IID('{86113396-D5B6-4284-8AED-9F647A6A0CAB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWResponses,
	]
	default_interface = IWResponses

class Route(CoClassBaseClass): # A CoClass
	# Route Class
	CLSID = IID('{96F46E30-9B89-4666-9264-B669FDA8E197}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWRoute,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWRoute

class Sample(CoClassBaseClass): # A CoClass
	# Sample Class
	CLSID = IID('{988F0373-AFE4-456C-A3F1-B57685ECBD7D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSample,
	]
	default_interface = IWSample

class Scrap(CoClassBaseClass): # A CoClass
	# Scrap Class
	CLSID = IID('{3805229F-FE67-48C2-AE43-F6E329766A28}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWScrap,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWScrap

class Section(CoClassBaseClass): # A CoClass
	# Section Class
	CLSID = IID('{254FF920-4B28-469E-8EB6-B53CA41D5758}')
	coclass_sources = [
		_IWSectionEvents,
	]
	default_source = _IWSectionEvents
	coclass_interfaces = [
		IWSection,
		IWElement,
		IWUserElement,
	]
	default_interface = IWSection

class SectionBreakdown(CoClassBaseClass): # A CoClass
	# Section breakdown Class
	CLSID = IID('{43821150-63F6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionBreakdown,
	]
	default_interface = IWSectionBreakdown

class SectionBreakdownInstance(CoClassBaseClass): # A CoClass
	# Section Breakdown Instance Class
	CLSID = IID('{43821152-63F6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionBreakdownInstance,
	]
	default_interface = IWSectionBreakdownInstance

class SectionBreakdownInstances(CoClassBaseClass): # A CoClass
	# Section Breakdown Instances Class
	CLSID = IID('{43821153-63F6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionBreakdownInstances,
	]
	default_interface = IWSectionBreakdownInstances

class SectionBreakdowns(CoClassBaseClass): # A CoClass
	# Section Breakdowns Class
	CLSID = IID('{43821151-63F6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionBreakdowns,
	]
	default_interface = IWSectionBreakdowns

class SectionInstance(CoClassBaseClass): # A CoClass
	# SectionInstance Class
	CLSID = IID('{87663A9D-D546-462E-94A2-C22A4BEC104A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionInstance,
		IWInstance,
	]
	default_interface = IWSectionInstance

class SectionInstances(CoClassBaseClass): # A CoClass
	# SectionInstances Class
	CLSID = IID('{889A626B-57AE-4DBF-AA7B-6B5101807642}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSectionInstances,
	]
	default_interface = IWSectionInstances

class SectionType(CoClassBaseClass): # A CoClass
	# SectionType Class
	CLSID = IID('{D12CC0A0-CA9E-40E1-9C5C-78A7D82573BC}')
	coclass_sources = [
		_IWSectionTypeEvents,
	]
	default_source = _IWSectionTypeEvents
	coclass_interfaces = [
		IWSectionType,
	]
	default_interface = IWSectionType

class Shift(CoClassBaseClass): # A CoClass
	# Shift Class
	CLSID = IID('{C8393854-3713-4403-86C3-14A22119E733}')
	coclass_sources = [
		_IWShiftEvents,
	]
	default_source = _IWShiftEvents
	coclass_interfaces = [
		IWShift,
		IWElement,
		IWUserElement,
	]
	default_interface = IWShift

class ShiftPeriod(CoClassBaseClass): # A CoClass
	# ShiftPeriod Class
	CLSID = IID('{87AB0720-5E69-11D5-A1C1-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWShiftPeriod,
	]
	default_interface = IWShiftPeriod

class ShiftPeriods(CoClassBaseClass): # A CoClass
	# ShiftPeriods Class
	CLSID = IID('{87AB0721-5E69-11D5-A1C1-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWShiftPeriods,
	]
	default_interface = IWShiftPeriods

class ShiftType(CoClassBaseClass): # A CoClass
	# ShiftType Class
	CLSID = IID('{0621844B-FA65-4835-8FBD-86F62DDEE8E8}')
	coclass_sources = [
		_IWShiftTypeEvents,
	]
	default_source = _IWShiftTypeEvents
	coclass_interfaces = [
		IWShiftType,
	]
	default_interface = IWShiftType

class Ship(CoClassBaseClass): # A CoClass
	# Ship Class
	CLSID = IID('{36FE27BE-07BA-4904-AFB6-9DA93621E6CE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWShip,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWShip

# This CoClass is known by the name 'SIMBA.StandardApplication.1'
class StandardApplication(CoClassBaseClass): # A CoClass
	# StandardApplication Class
	CLSID = IID('{FA3D85D9-0C0B-4420-B724-0848E2588597}')
	coclass_sources = [
		_IWApplicationEvents,
	]
	default_source = _IWApplicationEvents
	coclass_interfaces = [
		IWStandardApplication,
		IWApplication,
		IWUserProperties,
		IWRemoteControl,
	]
	default_interface = IWStandardApplication

class Station(CoClassBaseClass): # A CoClass
	# Station Class
	CLSID = IID('{17EE021F-753A-4FE6-8F04-F957F655948F}')
	coclass_sources = [
		_IWStationEvents,
	]
	default_source = _IWStationEvents
	coclass_interfaces = [
		IWStation,
		IWElement,
		IWUserElement,
	]
	default_interface = IWStation

class StationBreakdown(CoClassBaseClass): # A CoClass
	# Station breakdown Class
	CLSID = IID('{BE06CB20-63E6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationBreakdown,
	]
	default_interface = IWStationBreakdown

class StationBreakdownInstance(CoClassBaseClass): # A CoClass
	# Station Breakdown Instance Class
	CLSID = IID('{BE06CB21-63E6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationBreakdownInstance,
	]
	default_interface = IWStationBreakdownInstance

class StationBreakdownInstances(CoClassBaseClass): # A CoClass
	# Station Breakdown Instances Class
	CLSID = IID('{BE06CB22-63E6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationBreakdownInstances,
	]
	default_interface = IWStationBreakdownInstances

class StationBreakdowns(CoClassBaseClass): # A CoClass
	# Station Breakdowns Class
	CLSID = IID('{BE06CB25-63E6-11D5-85C7-0020AFF488A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationBreakdowns,
	]
	default_interface = IWStationBreakdowns

class StationInstance(CoClassBaseClass): # A CoClass
	# StationInstance Class
	CLSID = IID('{5C523CCE-E05E-426F-A78A-F90991EA0C0F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationInstance,
		IWInstance,
	]
	default_interface = IWStationInstance

class StationInstances(CoClassBaseClass): # A CoClass
	# StationInstances Class
	CLSID = IID('{FA88B3AD-568D-459E-8774-202331D9DD5A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWStationInstances,
	]
	default_interface = IWStationInstances

class StationType(CoClassBaseClass): # A CoClass
	# StationType Class
	CLSID = IID('{FAC4F46E-2F6E-4749-B377-BB31740854AD}')
	coclass_sources = [
		_IWStationTypeEvents,
	]
	default_source = _IWStationTypeEvents
	coclass_interfaces = [
		IWStationType,
	]
	default_interface = IWStationType

class SystemElement(CoClassBaseClass): # A CoClass
	# UserElement Class
	CLSID = IID('{36EBF252-2CF3-11D5-A1B4-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWSystemElement,
	]
	default_interface = IWSystemElement

class Tank(CoClassBaseClass): # A CoClass
	# Tank Class
	CLSID = IID('{E172B608-4CAC-42E9-B756-DEEC0E285673}')
	coclass_sources = [
		_IWTankEvents,
	]
	default_source = _IWTankEvents
	coclass_interfaces = [
		IWTank,
		IWElement,
		IWUserElement,
	]
	default_interface = IWTank

class TankInstance(CoClassBaseClass): # A CoClass
	# TankInstance Class
	CLSID = IID('{BA36851B-F5F8-4DDE-879C-F85BAD2A8CF1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTankInstance,
		IWInstance,
	]
	default_interface = IWTankInstance

class TankInstances(CoClassBaseClass): # A CoClass
	# TankInstances Class
	CLSID = IID('{CA9A3253-9C84-48A5-B1F1-C474D7FF28A9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTankInstances,
	]
	default_interface = IWTankInstances

class TankType(CoClassBaseClass): # A CoClass
	# TankType Class
	CLSID = IID('{DC41C651-D074-4A96-B802-497B888E1F47}')
	coclass_sources = [
		_IWTankTypeEvents,
	]
	default_source = _IWTankTypeEvents
	coclass_interfaces = [
		IWTankType,
	]
	default_interface = IWTankType

class Timeseries(CoClassBaseClass): # A CoClass
	# Timeseries Class
	CLSID = IID('{AD5E9293-FD7B-4EA1-B2C8-CB27C2D1BB09}')
	coclass_sources = [
		_IWTimeseriesEvents,
	]
	default_source = _IWTimeseriesEvents
	coclass_interfaces = [
		IWTimeseries,
		IWElement,
		IWUserElement,
	]
	default_interface = IWTimeseries

class TimeseriesType(CoClassBaseClass): # A CoClass
	# TimeseriesType Class
	CLSID = IID('{CBEB96B5-10E1-4800-A763-5E417B92B34A}')
	coclass_sources = [
		_IWTimeseriesTypeEvents,
	]
	default_source = _IWTimeseriesTypeEvents
	coclass_interfaces = [
		IWTimeseriesType,
	]
	default_interface = IWTimeseriesType

class Track(CoClassBaseClass): # A CoClass
	# Track Class
	CLSID = IID('{0398C500-A610-463B-91A1-F4065CFEFF84}')
	coclass_sources = [
		_IWTrackEvents,
	]
	default_source = _IWTrackEvents
	coclass_interfaces = [
		IWTrack,
		IWElement,
		IWUserElement,
	]
	default_interface = IWTrack

class TrackInstance(CoClassBaseClass): # A CoClass
	# TrackInstance Class
	CLSID = IID('{EE5EE797-CC64-48C7-83B8-BA8C8561796D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTrackInstance,
		IWInstance,
	]
	default_interface = IWTrackInstance

class TrackInstances(CoClassBaseClass): # A CoClass
	# TrackInstances Class
	CLSID = IID('{08BF91FF-3235-4569-B6FE-952E562B235F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTrackInstances,
	]
	default_interface = IWTrackInstances

class TrackType(CoClassBaseClass): # A CoClass
	# TrackType Class
	CLSID = IID('{5A372025-E42D-4ED3-8583-E5341700F635}')
	coclass_sources = [
		_IWTrackTypeEvents,
	]
	default_source = _IWTrackTypeEvents
	coclass_interfaces = [
		IWTrackType,
	]
	default_interface = IWTrackType

class TrackWorkSearchItem(CoClassBaseClass): # A CoClass
	# TrackWorkSearchItemClass
	CLSID = IID('{F0F0BF92-6EF7-11D5-80F0-00E02964AB43}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTrackWorkSearchItem,
	]
	default_interface = IWTrackWorkSearchItem

class TrackWorkSearchItems(CoClassBaseClass): # A CoClass
	# TrackWorkSearchItems Class
	CLSID = IID('{F0F0BF93-6EF7-11D5-80F0-00E02964AB43}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTrackWorkSearchItems,
	]
	default_interface = IWTrackWorkSearchItems

class Type(CoClassBaseClass): # A CoClass
	# Type Class
	CLSID = IID('{90A3C7D3-EBED-44B7-9F9D-DE4E3094A286}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWType,
	]
	default_interface = IWType

class Types(CoClassBaseClass): # A CoClass
	# Types Class
	CLSID = IID('{7C3688CE-2F5E-435E-BEB2-5AA084EDEC6E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWTypes,
	]
	default_interface = IWTypes

class UserElement(CoClassBaseClass): # A CoClass
	# UserElement Class
	CLSID = IID('{36EBF251-2CF3-11D5-A1B4-00E02963982C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWUserElement,
	]
	default_interface = IWUserElement

class Variable(CoClassBaseClass): # A CoClass
	# Variable Class
	CLSID = IID('{5F69FB13-188D-11D5-A1B3-00E02963982C}')
	coclass_sources = [
		_IWVariableEvents,
	]
	default_source = _IWVariableEvents
	coclass_interfaces = [
		IWVariable,
		IWElement,
		IWUserElement,
	]
	default_interface = IWVariable

class VariableType(CoClassBaseClass): # A CoClass
	# VariableType Class
	CLSID = IID('{5F69FB11-188D-11D5-A1B3-00E02963982C}')
	coclass_sources = [
		_IWVariableTypeEvents,
	]
	default_source = _IWVariableTypeEvents
	coclass_interfaces = [
		IWVariableType,
	]
	default_interface = IWVariableType

class Vehicle(CoClassBaseClass): # A CoClass
	# Vehicle Class
	CLSID = IID('{E3D209FA-73F5-4C1C-B167-5FF6990B1944}')
	coclass_sources = [
		_IWVehicleEvents,
	]
	default_source = _IWVehicleEvents
	coclass_interfaces = [
		IWVehicle,
		IWElement,
		IWUserElement,
	]
	default_interface = IWVehicle

class VehicleInstance(CoClassBaseClass): # A CoClass
	# VehicleInstance Class
	CLSID = IID('{209279F9-2A76-482E-9502-C0AAF1E0CE53}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWVehicleInstance,
		IWInstance,
	]
	default_interface = IWVehicleInstance

class VehicleInstances(CoClassBaseClass): # A CoClass
	# VehicleInstances Class
	CLSID = IID('{CBC7B99E-B2BF-4031-B413-523570170F57}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWVehicleInstances,
	]
	default_interface = IWVehicleInstances

class VehicleType(CoClassBaseClass): # A CoClass
	# VehicleType Class
	CLSID = IID('{683FB717-BD04-4F21-AB03-0E21A7C72C49}')
	coclass_sources = [
		_IWVehicleTypeEvents,
	]
	default_source = _IWVehicleTypeEvents
	coclass_interfaces = [
		IWVehicleType,
	]
	default_interface = IWVehicleType

class WitnessFont(CoClassBaseClass): # A CoClass
	# Font Class
	CLSID = IID('{2DE39202-734C-49B3-827F-411DCB0856FF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWFont,
	]
	default_interface = IWFont

class World(CoClassBaseClass): # A CoClass
	# World class
	CLSID = IID('{47D9ECBC-EA3E-41AF-80A4-4CD0185A62BD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWWorld,
		IWElement,
		IWSystemElement,
	]
	default_interface = IWWorld

IWActivator_vtables_dispatch_ = 1
IWActivator_vtables_ = [
	(( 'Handle' , 'Value' , ), 1, (1, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IWApplication_vtables_dispatch_ = 1
IWApplication_vtables_ = [
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ErrorsAndWarnings' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'InputRequest' , 'pVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ForceQuit' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ProcessID' , 'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IWApplicationViewer_vtables_dispatch_ = 1
IWApplicationViewer_vtables_ = [
]

IWAssemble_vtables_dispatch_ = 1
IWAssemble_vtables_ = [
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 100, (100, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWAttribute_vtables_dispatch_ = 1
IWAttribute_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'Value' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'Value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'Value' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'Value' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 104, (104, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

IWAttributeInstance_vtables_dispatch_ = 1
IWAttributeInstance_vtables_ = [
	(( 'Value' , 'Value' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 1, (1, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Array' , 'Index' , 'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Array' , 'Index' , 'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'Index' , 'Value' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'Index' , 'Value' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IWAttributeInstances_vtables_dispatch_ = 1
IWAttributeInstances_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{427F8FA1-0EEE-11D5-8579-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWAttributeType_vtables_dispatch_ = 1
IWAttributeType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'Type' , 'Group' , 
			 'Attribute' , ), 101, (101, (), [ (8, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , 
			 (12, 1, None, None) , (16393, 10, None, "IID('{56EF0AE9-1E7D-4892-9C56-837855B9776E}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWBPMViewer_vtables_dispatch_ = 1
IWBPMViewer_vtables_ = [
]

IWBackdrop_vtables_dispatch_ = 1
IWBackdrop_vtables_ = [
]

IWBuffer_vtables_dispatch_ = 1
IWBuffer_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'BufferInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{5A3597E0-2042-4969-919F-484397BF413B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInput' , 'pVal' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInput' , 'pVal' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnOutput' , 'pVal' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnOutput' , 'pVal' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEndOfMinimumDelay' , 'pVal' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEndOfMinimumDelay' , 'pVal' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEndOfMaximumDelay' , 'pVal' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEndOfMaximumDelay' , 'pVal' , ), 106, (106, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ExitRule' , 'pVal' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ExitRule' , 'pVal' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 120, (120, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 121, (121, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 121, (121, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'MinimumDelay' , 'pVal' , ), 122, (122, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'MinimumDelay' , 'pVal' , ), 122, (122, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'MaximumDelay' , 'pVal' , ), 123, (123, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MaximumDelay' , 'pVal' , ), 123, (123, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'DelayMode' , 'pVal' , ), 124, (124, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'DelayMode' , 'pVal' , ), 124, (124, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShiftAllowance' , 'pVal' , ), 125, (125, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ShiftAllowance' , 'pVal' , ), 125, (125, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 126, (126, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 126, (126, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 150, (150, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'SetInputAtRear' , ), 160, (160, (), [ ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SetInputAtFront' , ), 161, (161, (), [ ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SetInputAtPosition' , 'Position' , ), 162, (162, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SetInputPositionByAttribute' , 'Attribute' , 'Ascending' , ), 163, (163, (), [ (12, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'InputMode' , 'pVal' , ), 165, (165, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'InputPosition' , 'pVal' , ), 166, (166, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'InputAttribute' , 'pVal' , ), 167, (167, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputAtFront' , ), 170, (170, (), [ ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputAtRear' , ), 171, (171, (), [ ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputFromAnyPosition' , 'SearchFromFront' , ), 172, (172, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputByCondition' , 'Condition' , 'SearchFromFront' , ), 173, (173, (), [ (12, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputByMaximum' , 'Expression' , 'SearchFromFront' , ), 174, (174, (), [ (12, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'SetOutputByMinimum' , 'Expression' , 'SearchFromFront' , ), 175, (175, (), [ (12, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'OutputMode' , 'pVal' , ), 176, (176, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'OutputCondition' , 'pVal' , ), 177, (177, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'OutputExpression' , 'pVal' , ), 178, (178, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'OutputSearchFromFront' , 'pVal' , ), 179, (179, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTime' , 'OnShiftTime' , 'pVal' , ), 200, (200, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsIn' , 'OnShiftTime' , 'pVal' , ), 201, (201, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 204, (204, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsAfterMinDelay' , 'pVal' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsIn' , 'pVal' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsOut' , 'pVal' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'MinimumNumberOfPartsIn' , 'pVal' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNumberOfPartsIn' , 'pVal' , ), 210, (210, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'MinimumPartTimeIn' , 'pVal' , ), 211, (211, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'MaximumPartTimeIn' , 'pVal' , ), 212, (212, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTimeAfterMinDelay' , 'OnShiftTime' , 'pVal' , ), 213, (213, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsAfterMinDelay' , 'OnShiftTime' , 'pVal' , ), 214, (214, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'TimeInBufferOfPartAtPosition' , 'Position' , 'pVal' , ), 215, (215, (), [ (12, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 216, (216, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'PartInstance' , ), 217, (217, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'PartInstance' , ), 218, (218, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 219, (219, (), [ (16393, 10, None, "IID('{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}')") , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
]

IWBufferInstance_vtables_dispatch_ = 1
IWBufferInstance_vtables_ = [
	(( 'Buffer' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PartsIn' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTime' , 'OnShiftTime' , 'pVal' , ), 4, (4, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsIn' , 'OnShiftTime' , 'pVal' , ), 5, (5, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillChangeInShiftState' , 'pVal' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 10, (10, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsAfterMinDelay' , 'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsIn' , 'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsOut' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MinimumNumberOfPartsIn' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNumberOfPartsIn' , 'pVal' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MinimumPartTimeIn' , 'pVal' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'MaximumPartTimeIn' , 'pVal' , ), 18, (18, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTimeAfterMinDelay' , 'OnShiftTime' , 'pVal' , ), 19, (19, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsAfterMinDelay' , 'OnShiftTime' , 'pVal' , ), 20, (20, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TimeInBufferOfPartAtPosition' , 'Position' , 'pVal' , ), 21, (21, (), [ (12, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 22, (22, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'PartInstance' , ), 23, (23, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'PartInstance' , ), 24, (24, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IWBufferInstances_vtables_dispatch_ = 1
IWBufferInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWBufferMeasure_vtables_dispatch_ = 1
IWBufferMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DwellTime' , 'Value' , ), 2, (2, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PerPartIn' , 'Value' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PerPartIn' , 'Value' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWBufferMeasures_vtables_dispatch_ = 1
IWBufferMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWBufferType_vtables_dispatch_ = 1
IWBufferType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWCarrier_vtables_dispatch_ = 1
IWCarrier_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'EntryRule' , 'pVal' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'EntryRule' , 'pVal' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CarrierSize' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CarrierSize' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'StartSpacing' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'StartSpacing' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'StopSpacing' , 'pVal' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'StopSpacing' , 'pVal' , ), 107, (107, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCreate' , 'pVal' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCreate' , 'pVal' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RunThrough' , 'pVal' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RunThrough' , 'pVal' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 110, (110, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pVal' , ), 111, (111, (), [ (16393, 10, None, "IID('{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 112, (112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 112, (112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CarrierInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{8B98F244-7A42-4233-9432-BABB237EE777}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

IWCarrierInstance_vtables_dispatch_ = 1
IWCarrierInstance_vtables_ = [
	(( 'Carrier' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{1F803804-DB54-4D3E-A508-AFFC15277B77}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserAttributes' , 'Attributes' , ), 6, (6, (), [ (16393, 10, None, "IID('{427F8FA2-0EEE-11D5-8579-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CurrentElement' , 'InstanceObject' , ), 7, (7, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CurrentElementByName' , 'InstanceName' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 9, (9, (), [ 
			 (3, 1, None, None) , (11, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PartsIn' , 'pVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IWCarrierInstances_vtables_dispatch_ = 1
IWCarrierInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWCarrierType_vtables_dispatch_ = 1
IWCarrierType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{1F803804-DB54-4D3E-A508-AFFC15277B77}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWColor_vtables_dispatch_ = 1
IWColor_vtables_ = [
	(( 'Red' , 'pVal' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Red' , 'pVal' , ), 1, (1, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Green' , 'pVal' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Green' , 'pVal' , ), 2, (2, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Blue' , 'pVal' , ), 3, (3, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Blue' , 'pVal' , ), 3, (3, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWConveyor_vtables_dispatch_ = 1
IWConveyor_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ConveyorInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ConveyorType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ConveyorType' , 'pVal' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LengthInParts' , 'pVal' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LengthInParts' , 'pVal' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MaximumCapacity' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MaximumCapacity' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IndexTime' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IndexTime' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RestartDelay' , 'pVal' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RestartDelay' , 'pVal' , ), 107, (107, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnJoin' , 'pVal' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnJoin' , 'pVal' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFront' , 'pVal' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFront' , 'pVal' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 110, (110, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 111, (111, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 112, (112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 112, (112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 113, (113, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 113, (113, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'pVal' , ), 114, (114, (), [ (16393, 10, None, "IID('{375E2CD5-8A41-45AF-9469-38744989269C}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsIn' , 'OnShiftTime' , 'pVal' , ), 115, (115, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTime' , 'OnShiftTime' , 'pVal' , ), 116, (116, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 117, (117, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 119, (119, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsBetween' , 'Position1' , 'Position2' , 'pVal' , ), 120, (120, (), [ 
			 (3, 1, None, None) , (3, 0, None, None) , (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsIn' , 'pVal' , ), 122, (122, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 125, (125, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 126, (126, (), [ ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 127, (127, (), [ ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Position' , 'Sucess' , ), 128, (128, (), [ 
			 (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , (12, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'Position' , 'PartInstance' , ), 129, (129, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'Position' , 'PartInstance' , ), 130, (130, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pVal' , ), 131, (131, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pVal' , ), 131, (131, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 132, (132, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 132, (132, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 133, (133, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 133, (133, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'QueueSpacing' , 'pVal' , ), 134, (134, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'QueueSpacing' , 'pVal' , ), 134, (134, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Sensors' , 'Sensors' , ), 135, (135, (), [ (16393, 10, None, "IID('{54486179-8C34-4101-831E-23A6D9FE10F6}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 136, (136, (), [ (16393, 10, None, "IID('{1E6B62FD-4355-439E-8FA7-A54611B55B11}')") , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
]

IWConveyorBreakdown_vtables_dispatch_ = 1
IWConveyorBreakdown_vtables_ = [
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IWConveyorBreakdownInstance_vtables_dispatch_ = 1
IWConveyorBreakdownInstance_vtables_ = [
	(( 'ElementInstance' , 'ElementInstance' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownNumber' , 'BreakdownNumber' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownState' , 'BreakdownState' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'LaborQueue' , ), 4, (4, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWConveyorBreakdownInstances_vtables_dispatch_ = 1
IWConveyorBreakdownInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWConveyorBreakdowns_vtables_dispatch_ = 1
IWConveyorBreakdowns_vtables_ = [
	(( 'Item' , 'Index' , 'Breakdown' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{330E3D97-24CF-4644-9000-DEEA6EB2306B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Description' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWConveyorInstance_vtables_dispatch_ = 1
IWConveyorInstance_vtables_ = [
	(( 'Conveyor' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PartsIn' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTime' , 'OnShiftTime' , 'pVal' , ), 6, (6, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsIn' , 'OnShiftTime' , 'pVal' , ), 7, (7, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 8, (8, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 9, (9, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillChangeInShiftState' , 'pVal' , ), 10, (10, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 12, (12, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsBetween' , 'Position1' , 'Position2' , 'pVal' , ), 13, (13, (), [ 
			 (3, 1, None, None) , (3, 0, None, None) , (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfPartsIn' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActiveBreakdowns' , 'BreakdownInstances' , ), 19, (19, (), [ (16393, 10, None, "IID('{8278E5B4-CAA4-42E8-AABF-09E7A7535725}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Position' , 'Sucess' , ), 20, (20, (), [ 
			 (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , (12, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'Position' , 'PartInstance' , ), 21, (21, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'Position' , 'PartInstance' , ), 22, (22, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IWConveyorInstances_vtables_dispatch_ = 1
IWConveyorInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWConveyorMeasure_vtables_dispatch_ = 1
IWConveyorMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWConveyorMeasures_vtables_dispatch_ = 1
IWConveyorMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{75DE9907-45CA-4B2B-B584-7851F771FF1E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{75DE9907-45CA-4B2B-B584-7851F771FF1E}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWConveyorSensor_vtables_dispatch_ = 1
IWConveyorSensor_vtables_ = [
	(( 'Position' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnPartOn' , 'pVal' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnPartOn' , 'pVal' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnPartOff' , 'pVal' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnPartOff' , 'pVal' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCover' , 'pVal' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCover' , 'pVal' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUncover' , 'pVal' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUncover' , 'pVal' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IWConveyorSensors_vtables_dispatch_ = 1
IWConveyorSensors_vtables_ = [
	(( 'Item' , 'Index' , 'Sensor' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWConveyorType_vtables_dispatch_ = 1
IWConveyorType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWDataTable_vtables_dispatch_ = 1
IWDataTable_vtables_ = [
	(( 'DataTableInstances' , 'Instances' , ), 0, (0, (), [ (16393, 10, None, "IID('{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DisplayUpdateIntervalMode' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DisplayUpdateIntervalMode' , 'pVal' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DisplayUpdateInterval' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DisplayUpdateInterval' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Columns' , 'Columns' , ), 104, (104, (), [ (16393, 10, None, "IID('{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionType' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionErrorHandling' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionErrorHandling' , 'pVal' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionString' , 'pVal' , ), 108, (108, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MakeConnection' , 'Type' , 'Expression' , ), 109, (109, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'LoadData' , ), 110, (110, (), [ ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SaveData' , ), 111, (111, (), [ ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 112, (112, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 112, (112, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'IOType' , 'pVal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'IOType' , 'pVal' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 114, (114, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 114, (114, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'DataSaveActions' , 'Statement' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'DataSaveActions' , 'Statement' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'DataLoadActions' , 'Statement' , ), 116, (116, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'DataLoadActions' , 'Statement' , ), 116, (116, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'InputSqlStatement' , 'Statement' , ), 117, (117, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'InputSqlStatement' , 'Statement' , ), 117, (117, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'OutputTableName' , 'tableName' , ), 118, (118, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'OutputTableName' , 'tableName' , ), 118, (118, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'HasHeaders' , 'Value' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'HasHeaders' , 'Value' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IWDataTableColumnItem_vtables_dispatch_ = 1
IWDataTableColumnItem_vtables_ = [
	(( 'Name' , 'Value' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Value' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Value' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Value' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MappingName' , 'Name' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MappingName' , 'Name' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWDataTableColumnItems_vtables_dispatch_ = 1
IWDataTableColumnItems_vtables_ = [
	(( 'Item' , 'Index' , 'ColumnItem' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Type' , 'Position' , ), 2, (2, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWDataTableInstance_vtables_dispatch_ = 1
IWDataTableInstance_vtables_ = [
	(( 'DataTable' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'row' , 'column' , 'valuePtr' , ), 100, (100, (), [ 
			 (12, 49, '1', None) , (12, 49, '1', None) , (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'row' , 'column' , 'valuePtr' , ), 100, (100, (), [ 
			 (12, 49, '1', None) , (12, 49, '1', None) , (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'row' , 'column' , 'valuePtr' , ), 100, (100, (), [ 
			 (12, 49, '1', None) , (12, 49, '1', None) , (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'row' , 'column' , 'valuePtr' , ), 100, (100, (), [ 
			 (12, 49, '1', None) , (12, 49, '1', None) , (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LoadData' , ), 101, (101, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SaveData' , ), 102, (102, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Rows' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IWDataTableInstances_vtables_dispatch_ = 1
IWDataTableInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWDataTableType_vtables_dispatch_ = 1
IWDataTableType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWDimensions_vtables_dispatch_ = 1
IWDimensions_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWDirectories_vtables_dispatch_ = 1
IWDirectories_vtables_ = [
	(( 'Search' , 'FileName' , 'pFileFound' , 'pFound' , ), 1, (1, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IWDrawTool_vtables_dispatch_ = 1
IWDrawTool_vtables_ = [
	(( 'Element' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Element' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GroupDisplay' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GroupDisplay' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LayerNumber' , 'pVal' , ), 3, (3, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LayerNumber' , 'pVal' , ), 3, (3, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DrawRectangle' , 'X' , 'Y' , 'Width' , 'Height' , 
			 ), 4, (4, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ForegroundColor' , 'pVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{874FED95-DA11-48E4-B237-FC2CA83DE758}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'BackgroundColor' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{874FED95-DA11-48E4-B237-FC2CA83DE758}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'StatusDisplay' , 'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StatusDisplay' , 'pVal' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'XMemberOffset' , 'pVal' , ), 9, (9, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'XMemberOffset' , 'pVal' , ), 9, (9, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'YMemberOffset' , 'pVal' , ), 10, (10, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'YMemberOffset' , 'pVal' , ), 10, (10, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DrawText' , 'Text' , 'X' , 'Y' , ), 11, (11, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{F1496351-9B02-498C-9FB9-348E0B2AA565}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DrawTextBox' , 'Text' , 'X' , 'Y' , 'Width' , 
			 'Height' , 'Format' , ), 13, (13, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreatePathData' , 'PathData' , ), 14, (14, (), [ (16393, 10, None, "IID('{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DrawPath' , 'PathData' , ), 15, (15, (), [ (9, 1, None, "IID('{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreatePoint' , 'Point' , ), 16, (16, (), [ (16393, 10, None, "IID('{C6034440-1A59-48D8-B463-43918B37FD28}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'pVal' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'pVal' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DrawLine' , 'StartX' , 'StartY' , 'EndX' , 'EndY' , 
			 ), 18, (18, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IWElement_vtables_dispatch_ = 1
IWElement_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FullyQualifiedName' , 'pVal' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IWElements_vtables_dispatch_ = 1
IWElements_vtables_ = [
	(( 'Item' , 'Index' , 'theItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'Index' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FilterOnType' , 'Type' , 'recurseDown' , 'ppElements' , ), 102, (102, (), [ 
			 (3, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ItemByIdentifier' , 'Identifier' , 'Element' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWErrorsAndWarnings_vtables_dispatch_ = 1
IWErrorsAndWarnings_vtables_ = [
	(( 'AllowErrors' , 'pVal' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AllowErrors' , 'pVal' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AllowWarnings' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AllowWarnings' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWFactors_vtables_dispatch_ = 1
IWFactors_vtables_ = [
	(( 'Enabled' , 'valuePtr' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'valuePtr' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Interval' , 'valuePtr' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Interval' , 'valuePtr' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Duration' , 'valuePtr' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Duration' , 'valuePtr' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWFields_vtables_dispatch_ = 1
IWFields_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'Title' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Prompt' , 'Index' , 'Prompt' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWFile_vtables_dispatch_ = 1
IWFile_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ActionOnExistingFile' , 'ActionMode' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ActionOnExistingFile' , 'ActionMode' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 16, (16, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IWFileType_vtables_dispatch_ = 1
IWFileType_vtables_ = [
	(( 'Define' , 'Name' , 'fileMode' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWFont_vtables_dispatch_ = 1
IWFont_vtables_ = [
	(( 'PointSize' , 'pVal' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PointSize' , 'pVal' , ), 1, (1, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Facename' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Facename' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Opaque' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Opaque' , 'pVal' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FontStyle' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FontStyle' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IWFunction_vtables_dispatch_ = 1
IWFunction_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Parameters' , 'Parameters' , ), 100, (100, (), [ (16393, 10, None, "IID('{8693669F-C4C2-4318-AB34-8FF2860AB73B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReturnType' , 'Type' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Actions' , 'Statement' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ApplyChanges' , 'Type' , 'Actions' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 104, (104, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

IWFunctionParameter_vtables_dispatch_ = 1
IWFunctionParameter_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWFunctionParameters_vtables_dispatch_ = 1
IWFunctionParameters_vtables_ = [
	(( 'Item' , 'Index' , 'Parameter' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E1347784-EA6C-4A12-813A-F0FD60924578}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Type' , 'Position' , ), 2, (2, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWFunctionType_vtables_dispatch_ = 1
IWFunctionType_vtables_ = [
	(( 'Define' , 'Name' , 'Type' , 'Function' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{FC5BF548-99F8-4907-925F-82E0B2FB7835}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWGraphics_vtables_dispatch_ = 1
IWGraphics_vtables_ = [
	(( 'DrawTool' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{2C138955-DAF6-456E-9F25-03730158A521}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IWHistogram_vtables_dispatch_ = 1
IWHistogram_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IWHistogramType_vtables_dispatch_ = 1
IWHistogramType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{8CFB8503-E585-431A-9863-E1A3D6B9F34E}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWInputRequest_vtables_dispatch_ = 1
IWInputRequest_vtables_ = [
	(( 'AllowInput' , 'pVal' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AllowInput' , 'pVal' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWInstance_vtables_dispatch_ = 1
IWInstance_vtables_ = [
	(( 'Parent' , 'ppParent' , ), 1000, (1000, (), [ (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MemberNumber' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWInstances_vtables_dispatch_ = 1
IWInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWLabor_vtables_dispatch_ = 1
IWLabor_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LaborInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LaborShifts' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{402F5411-4F7E-11D5-A1C1-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 107, (107, (), [ 
			 (3, 1, None, None) , (11, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsStarted' , 'pVal' , ), 108, (108, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsFinished' , 'pVal' , ), 109, (109, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsPreEmpted' , 'pVal' , ), 110, (110, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsInProgress' , 'pVal' , ), 111, (111, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AverageJobTime' , 'pVal' , ), 112, (112, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AvailableLabor' , 'pVal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 114, (114, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'LaborUnitsAtElement' , 'Element' , 'pVal' , ), 115, (115, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 116, (116, (), [ (16393, 10, None, "IID('{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IWLaborInstance_vtables_dispatch_ = 1
IWLaborInstance_vtables_ = [
	(( 'Labor' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserAttributes' , 'Attributes' , ), 6, (6, (), [ (16393, 10, None, "IID('{427F8FA2-0EEE-11D5-8579-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CurrentElement' , 'InstanceObject' , ), 7, (7, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CurrentElementByName' , 'InstanceName' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 9, (9, (), [ 
			 (3, 1, None, None) , (11, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsStarted' , 'pVal' , ), 10, (10, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsFinished' , 'pVal' , ), 11, (11, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsPreEmpted' , 'pVal' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfJobsInProgress' , 'pVal' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AverageJobTime' , 'pVal' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AvailableLabor' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LaborUnitsAtElement' , 'Element' , 'pVal' , ), 16, (16, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IWLaborInstances_vtables_dispatch_ = 1
IWLaborInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{46FB221B-D834-4B5E-B1EC-582524196017}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWLaborMeasure_vtables_dispatch_ = 1
IWLaborMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BusyUse' , 'Value' , ), 2, (2, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IdleUse' , 'Value' , ), 3, (3, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWLaborMeasures_vtables_dispatch_ = 1
IWLaborMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWLaborRule_vtables_dispatch_ = 1
IWLaborRule_vtables_ = [
	(( 'Rule' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Rule' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLabor' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLabor' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseLaborDefinedByPartRule' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseLaborDefinedByPartRule' , 'pVal' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Allowance' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Allowance' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TimePenalty' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TimePenalty' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IWLaborRules_vtables_dispatch_ = 1
IWLaborRules_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWLaborShift_vtables_dispatch_ = 1
IWLaborShift_vtables_ = [
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Allowance' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Allowance' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWLaborShifts_vtables_dispatch_ = 1
IWLaborShifts_vtables_ = [
	(( 'Item' , 'Index' , 'LaborShift' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{402F5410-4F7E-11D5-A1C1-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Quantity' , 'Allowance' , 'Position' , 
			 ), 2, (2, (), [ (8, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWLaborType_vtables_dispatch_ = 1
IWLaborType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWMachine_vtables_dispatch_ = 1
IWMachine_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MachineType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MachineType' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingVolume' , 'pVal' , ), 112, (112, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingVolume' , 'pVal' , ), 112, (112, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FillingVolume' , 'pVal' , ), 113, (113, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FillingVolume' , 'pVal' , ), 113, (113, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingRule' , 'pVal' , ), 114, (114, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingRule' , 'pVal' , ), 114, (114, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FillingRule' , 'pVal' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'FillingRule' , 'pVal' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FillingStationNumber' , 'pVal' , ), 116, (116, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FillingStationNumber' , 'pVal' , ), 116, (116, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingStationNumber' , 'pVal' , ), 117, (117, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'EmptyingStationNumber' , 'pVal' , ), 117, (117, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'pVal' , ), 119, (119, (), [ (16393, 10, None, "IID('{8D12737F-BF42-4827-B95C-D891817FAB82}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Setups' , 'pVal' , ), 120, (120, (), [ (16393, 10, None, "IID('{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Cycles' , 'pVal' , ), 121, (121, (), [ (16393, 10, None, "IID('{A1B86D53-E79D-11D4-8556-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'MachineInstances' , 'Instances' , ), 0, (0, (), [ (16393, 10, None, "IID('{921B4444-BEC7-4203-A45C-724F25DA67BB}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 123, (123, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 124, (124, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 125, (125, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperationsCompleted' , 'pVal' , ), 126, (126, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'OutputBufferCapacity' , 'pVal' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'InputBufferCapacity' , 'pVal' , ), 128, (128, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 132, (132, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 132, (132, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ShiftAllowance' , 'pVal' , ), 133, (133, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ShiftAllowance' , 'pVal' , ), 133, (133, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ShiftPenalty' , 'pVal' , ), 134, (134, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'ShiftPenalty' , 'pVal' , ), 134, (134, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 135, (135, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 136, (136, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'Part' , 'pVal' , ), 137, (137, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 138, (138, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'PartInstance' , ), 139, (139, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'PartInstance' , ), 140, (140, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 141, (141, (), [ (16393, 10, None, "IID('{05F69682-BC4D-4B74-A78C-04E88D74CB06}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
]

IWMachineBreakdown_vtables_dispatch_ = 1
IWMachineBreakdown_vtables_ = [
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'CheckAtStartOfCycle' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CheckAtStartOfCycle' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ScrapPart' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ScrapPart' , 'pVal' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SetupOnRepair' , 'pVal' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetupOnRepair' , 'pVal' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperations' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperations' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'pVal' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'pVal' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'pVal' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'pVal' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'pVal' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownMode' , 'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownMode' , 'pVal' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PercentageLifeUsed' , 'pVal' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PercentageLifeUsed' , 'pVal' , ), 11, (11, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Element' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownNumber' , 'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 15, (15, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 15, (15, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 16, (16, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 16, (16, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 17, (17, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 17, (17, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 18, (18, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'OutputAction' , 'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'OutputAction' , 'pVal' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 20, (20, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 20, (20, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 21, (21, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 21, (21, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'TimeUntilFailure' , 'pVal' , ), 22, (22, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'TimeUntilFailure' , 'pVal' , ), 22, (22, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IWMachineBreakdownInstance_vtables_dispatch_ = 1
IWMachineBreakdownInstance_vtables_ = [
	(( 'ElementInstance' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownNumber' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownState' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWMachineBreakdownInstances_vtables_dispatch_ = 1
IWMachineBreakdownInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineBreakdowns_vtables_dispatch_ = 1
IWMachineBreakdowns_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Description' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWMachineCycle_vtables_dispatch_ = 1
IWMachineCycle_vtables_ = [
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InputQuantity' , 'pVal' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'InputQuantity' , 'pVal' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OutputQuantity' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'OutputQuantity' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CycleTime' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CycleTime' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FinishQuantity' , 'pVal' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FinishQuantity' , 'pVal' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStart' , 'pVal' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStart' , 'pVal' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinish' , 'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinish' , 'pVal' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OutputFromPosition' , 'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'OutputFromPosition' , 'pVal' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Element' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CycleNumber' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ProductionPartType' , 'pVal' , ), 13, (13, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ProductionPartType' , 'pVal' , ), 13, (13, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'InheritAttributeValues' , 'pVal' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'InheritAttributeValues' , 'pVal' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'BatchMin' , 'pVal' , ), 15, (15, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BatchMin' , 'pVal' , ), 15, (15, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BatchMax' , 'pVal' , ), 16, (16, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'BatchMax' , 'pVal' , ), 16, (16, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 18, (18, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 18, (18, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 19, (19, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 19, (19, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 20, (20, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 20, (20, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'LaborAssignedUsingRule' , 'pVal' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'LaborAssignedUsingRule' , 'pVal' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'PartsPerStation' , 'pVal' , ), 22, (22, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'PartsPerStation' , 'pVal' , ), 22, (22, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfStations' , 'pVal' , ), 23, (23, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfStations' , 'pVal' , ), 23, (23, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseOldestPart' , 'pVal' , ), 24, (24, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseOldestPart' , 'pVal' , ), 24, (24, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInput' , 'pVal' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInput' , 'pVal' , ), 25, (25, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnOutput' , 'pVal' , ), 26, (26, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnOutput' , 'pVal' , ), 26, (26, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 27, (27, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 27, (27, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 28, (28, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 28, (28, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'AssembleIntoPart' , 'pVal' , ), 29, (29, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'AssembleIntoPart' , 'pVal' , ), 29, (29, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'ProduceFromFirstPart' , 'pVal' , ), 30, (30, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'ProduceFromFirstPart' , 'pVal' , ), 30, (30, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'SelectPartsToProduce' , 'pVal' , ), 31, (31, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'SelectPartsToProduce' , 'pVal' , ), 31, (31, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
]

IWMachineCycleInstance_vtables_dispatch_ = 1
IWMachineCycleInstance_vtables_ = [
	(( 'ElementInstance' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CycleNumber' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineCycleInstances_vtables_dispatch_ = 1
IWMachineCycleInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineCycles_vtables_dispatch_ = 1
IWMachineCycles_vtables_ = [
	(( 'Item' , 'Index' , 'Cycle' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A1B86D51-E79D-11D4-8556-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Description' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWMachineInstance_vtables_dispatch_ = 1
IWMachineInstance_vtables_ = [
	(( 'ActiveCycles' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{35B1CE41-5962-4071-8824-4D43DA7C2DA9}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActiveSetups' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{897905FC-B806-4835-8AF8-088E6405AD70}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ActiveBreakdowns' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{1CD3A435-8D00-4CB8-A630-F666460D0372}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PartsInInputBuffer' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PartsInOutputBuffer' , 'pVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PartsInProcess' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Machine' , 'pVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{12E061BC-E54B-11D4-8553-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CurrentCycle' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InputBufferCapacity' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'OutputBufferCapacity' , 'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperationsCompleted' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 15, (15, (), [ 
			 (3, 0, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 16, (16, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillChangeInShiftState' , 'pVal' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'Part' , 'pVal' , ), 19, (19, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 20, (20, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'PartInstance' , ), 21, (21, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'PartInstance' , ), 22, (22, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IWMachineInstances_vtables_dispatch_ = 1
IWMachineInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineMeasure_vtables_dispatch_ = 1
IWMachineMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BusyUse' , 'Value' , ), 2, (2, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IdleUse' , 'Value' , ), 3, (3, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PerOperation' , 'Value' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PerOperation' , 'Value' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWMachineMeasures_vtables_dispatch_ = 1
IWMachineMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{63070342-EC3E-456F-90DA-B849F98EB873}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{63070342-EC3E-456F-90DA-B849F98EB873}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWMachineSetup_vtables_dispatch_ = 1
IWMachineSetup_vtables_ = [
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SetupTime' , 'pVal' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetupTime' , 'pVal' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperations' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfOperations' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStart' , 'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStart' , 'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinish' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinish' , 'pVal' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OperationsToFirstSetup' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'OperationsToFirstSetup' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SetupMode' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SetupMode' , 'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StationNumber' , 'pVal' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StationNumber' , 'pVal' , ), 8, (8, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Element' , 'pVal' , ), 9, (9, (), [ (16393, 10, None, "IID('{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetupNumber' , 'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 11, (11, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'pVal' , ), 11, (11, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 12, (12, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 12, (12, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 13, (13, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 13, (13, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 14, (14, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ValueChangeExpression' , 'pVal' , ), 15, (15, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ValueChangeExpression' , 'pVal' , ), 15, (15, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NeedPart' , 'Value' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'NeedPart' , 'Value' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnAllocateLabor' , 'pVal' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFreeLabor' , 'pVal' , ), 18, (18, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IWMachineSetupInstance_vtables_dispatch_ = 1
IWMachineSetupInstance_vtables_ = [
	(( 'ElementInstance' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetupNumber' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineSetupInstances_vtables_dispatch_ = 1
IWMachineSetupInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWMachineSetups_vtables_dispatch_ = 1
IWMachineSetups_vtables_ = [
	(( 'Item' , 'Index' , 'Setup' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWMachineType_vtables_dispatch_ = 1
IWMachineType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{12E061BC-E54B-11D4-8553-0020AFF488A2}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWMeasureValue_vtables_dispatch_ = 1
IWMeasureValue_vtables_ = [
	(( 'Value' , 'Value' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 0, (0, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PerTimeUnit' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PerTimeUnit' , 'Value' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWModel_vtables_dispatch_ = 1
IWModel_vtables_ = [
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Types' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Elements' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , 'FileType' , ), 5, (5, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , 'FileType' , ), 6, (6, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'StopTime' , ), 7, (7, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Stop' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 11, (11, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 11, (11, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Author' , 'pVal' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Author' , 'pVal' , ), 12, (12, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Sample' , 'pVal' , ), 14, (14, (), [ (16393, 10, None, "IID('{F079D83C-D0A1-413D-9CC2-D64317021122}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'None' , 'Value' , ), 15, (15, (), [ (16393, 10, None, "IID('{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Ship' , 'Value' , ), 16, (16, (), [ (16393, 10, None, "IID('{81E22460-8112-472B-9E14-96153261E6E0}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Scrap' , 'Value' , ), 17, (17, (), [ (16393, 10, None, "IID('{38FB81B4-8091-4A39-8041-56C31FDA7BD0}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'World' , 'Value' , ), 18, (18, (), [ (16393, 10, None, "IID('{861CABEB-E70F-4879-AEA6-079D1B13BC1E}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Assemble' , 'Value' , ), 19, (19, (), [ (16393, 10, None, "IID('{108615F0-4DBE-4D4C-826B-C606578491BA}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Route' , 'Value' , ), 20, (20, (), [ (16393, 10, None, "IID('{6A8123E6-FF3B-4502-AF3F-243AC818B17C}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Backdrop' , 'Value' , ), 21, (21, (), [ (16393, 10, None, "IID('{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CurrentTime' , 'pVal' , ), 22, (22, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'pVal' , ), 23, (23, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'pVal' , ), 23, (23, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Begin' , ), 24, (24, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RunBatch' , 'StopTime' , ), 25, (25, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Step' , ), 26, (26, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'New' , ), 27, (27, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'EvaluateExpression' , 'Type' , 'Expression' , 'Value' , ), 30, (30, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ImmediateActions' , 'Statement' , ), 31, (31, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ReportToFile' , 'Type' , 'File' , ), 32, (32, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 33, (33, (), [ ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 34, (34, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 34, (34, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 35, (35, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 35, (35, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'WarmupPeriod' , 'Expression' , ), 36, (36, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'WarmupPeriod' , 'Expression' , ), 36, (36, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BidirectionalPaths' , 'Enabled' , ), 37, (37, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BidirectionalPaths' , 'Enabled' , ), 37, (37, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPaths' , 'Enabled' , ), 38, (38, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPaths' , 'Enabled' , ), 38, (38, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'MultiplePathRouting' , 'Enabled' , ), 39, (39, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'MultiplePathRouting' , 'Enabled' , ), 39, (39, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'FastestRoute' , 'Enabled' , ), 40, (40, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'FastestRoute' , 'Enabled' , ), 40, (40, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'LaborWalkToIdle' , 'Enabled' , ), 41, (41, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'LaborWalkToIdle' , 'Enabled' , ), 41, (41, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'LaborWalkToMoveParts' , 'Enabled' , ), 42, (42, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'LaborWalkToMoveParts' , 'Enabled' , ), 42, (42, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPathTraverseTime' , 'Time' , ), 43, (43, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPathTraverseTime' , 'Time' , ), 43, (43, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPathUpdateInterval' , 'Interval' , ), 44, (44, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'PseudoPathUpdateInterval' , 'Interval' , ), 44, (44, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'BufferedWalkGraphics' , 'Enabled' , ), 45, (45, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'BufferedWalkGraphics' , 'Enabled' , ), 45, (45, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'TimeScaleFactor' , 'Expression' , ), 46, (46, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'TimeScaleFactor' , 'Expression' , ), 46, (46, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'RunTimeIncrement' , 'Expression' , ), 47, (47, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'RunTimeIncrement' , 'Expression' , ), 47, (47, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'BatchTimeIncrement' , 'Expression' , ), 48, (48, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'BatchTimeIncrement' , 'Expression' , ), 48, (48, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'WalkMode' , 'Enabled' , ), 49, (49, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'WalkMode' , 'Enabled' , ), 49, (49, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'StartTime' , 'Expression' , ), 50, (50, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'StartTime' , 'Expression' , ), 50, (50, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'TimeOfNextEvent' , 'pVal' , ), 51, (51, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'ScheduleEvent' , 'EventNo' , 'AfterTime' , ), 52, (52, (), [ (12, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SimbaActions' , 'Statement' , ), 53, (53, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'SimbaActions' , 'Statement' , ), 53, (53, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'TimeNow' , 'pVal' , ), 54, (54, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'IsReservedWord' , 'word' , 'result' , ), 55, (55, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'pVal' , ), 56, (56, (), [ (16393, 10, None, "IID('{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}')") , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SyncNew' , ), 57, (57, (), [ ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'SyncBegin' , ), 58, (58, (), [ ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'SyncRun' , 'StopTime' , ), 59, (59, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'SyncRunBatch' , 'StopTime' , ), 60, (60, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'SyncStop' , ), 61, (61, (), [ ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'SyncLoad' , 'FileName' , 'FileType' , ), 62, (62, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'SyncSave' , 'FileName' , 'FileType' , ), 63, (63, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'ReportAll' , 'Type' , 'File' , 'reportShiftTime' , 'ReportingMode' , 
			 'DetailReportingMode' , ), 64, (64, (), [ (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'RunInitializeActions' , ), 65, (65, (), [ ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'SyncStep' , ), 66, (66, (), [ ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Directory' , 'Directory' , ), 67, (67, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'BaseTimeUnit' , 'pValue' , ), 68, (68, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'BaseTimeUnit' , 'pValue' , ), 68, (68, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'StartDate' , 'pDate' , ), 69, (69, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'StartDate' , 'pDate' , ), 69, (69, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'ClockNotes' , 'pVal' , ), 70, (70, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'ClockNotes' , 'pVal' , ), 70, (70, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'SetPeriod' , 'Day' , 'PeriodNumber' , 'StartTime' , 'EndTime' , 
			 ), 71, (71, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'StartPeriod' , 'Day' , 'PeriodNumber' , 'pVal' , ), 72, (72, (), [ 
			 (3, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'EndPeriod' , 'Day' , 'PeriodNumber' , 'pVal' , ), 73, (73, (), [ 
			 (3, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'AddHoliday' , 'StartDate' , 'EndDate' , ), 74, (74, (), [ (8, 1, None, None) , 
			 (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'RemoveHolidays' , 'StartDate' , 'EndDate' , ), 75, (75, (), [ (8, 1, None, None) , 
			 (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'ClockDisplay' , 'pVal' , ), 76, (76, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'ClockDisplay' , 'pVal' , ), 76, (76, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'EventFlags' , 'pVal' , ), 77, (77, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'EventFlags' , 'pVal' , ), 77, (77, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'HeartBeatPeriod' , 'pVal' , ), 78, (78, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'HeartBeatPeriod' , 'pVal' , ), 78, (78, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'GetModelEventManager' , 'manager' , ), 79, (79, (), [ (16393, 10, None, "IID('{D8396D00-CC33-47E7-A917-1527DF798EC5}')") , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'WPMElements' , 'pVal' , ), 80, (80, (), [ (16393, 10, None, "IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')") , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Directories' , 'pVal' , ), 81, (81, (), [ (16393, 10, None, "IID('{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}')") , ], 1 , 2 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'Replication' , 'pVal' , ), 82, (82, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'Replication' , 'pVal' , ), 82, (82, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'ModelTimeEventUpdateInterval' , 'pVal' , ), 83, (83, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'ModelTimeEventUpdateInterval' , 'pVal' , ), 83, (83, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'Generate3D' , ), 84, (84, (), [ ], 1 , 1 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'AllUserElements' , 'Elements' , ), 85, (85, (), [ (16393, 10, None, "IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')") , ], 1 , 2 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 86, (86, (), [ (16393, 10, None, "IID('{B3951062-2E8D-407D-ABBD-D57FB4FAE705}')") , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'ModelCompleteAt' , 'Expression' , ), 87, (87, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'ModelCompleteAt' , 'Expression' , ), 87, (87, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 88, (88, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 88, (88, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'DataSaveActions' , 'Statement' , ), 89, (89, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'DataSaveActions' , 'Statement' , ), 89, (89, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'DataLoadActions' , 'Statement' , ), 90, (90, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'DataLoadActions' , 'Statement' , ), 90, (90, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'Scenario' , 'Scenario' , ), 91, (91, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'Scenario' , 'Scenario' , ), 91, (91, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownFactors' , 'valuePtr' , ), 92, (92, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'SetupFactors' , 'valuePtr' , ), 93, (93, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'GenerateTrace3D' , ), 94, (94, (), [ ], 1 , 1 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'EnableDebugging' , 'Enabled' , ), 95, (95, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'EnableDebugging' , 'Enabled' , ), 95, (95, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'RemoveDebugInformation' , ), 96, (96, (), [ ], 1 , 1 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
]

IWModelEventManager_vtables_dispatch_ = 1
IWModelEventManager_vtables_ = [
	(( 'EventFlags' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'EventFlags' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWModelMeasure_vtables_dispatch_ = 1
IWModelMeasure_vtables_ = [
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWModelMeasures_vtables_dispatch_ = 1
IWModelMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Measure' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Currency' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Currency' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IWModule_vtables_dispatch_ = 1
IWModule_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Elements' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Types' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InputElement' , 'pVal' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InputElement' , 'pVal' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OutputElement' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'OutputElement' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'InputRule' , 'pVal' , ), 106, (106, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseCycleTime' , 'pVal' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseCycleTime' , 'pVal' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CycleTime' , 'pVal' , ), 111, (111, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CycleTime' , 'pVal' , ), 111, (111, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'WalkToModule' , 'pVal' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'WalkToModule' , 'pVal' , ), 112, (112, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'AverageNumberOfPartsIn' , 'OnShiftTime' , 'pVal' , ), 113, (113, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'AveragePartTime' , 'OnShiftTime' , 'pVal' , ), 114, (114, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'Part' , 'pVal' , ), 116, (116, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'SetPassword' , 'OldPassword' , 'NewPassword' , ), 117, (117, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 118, (118, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RemovePart' , 'PartInstance' , ), 119, (119, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RemovePartOfType' , 'Part' , 'PartInstance' , ), 120, (120, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'LoadXML' , 'FileName' , ), 121, (121, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'SaveXML' , 'FileName' , ), 122, (122, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
]

IWModuleType_vtables_dispatch_ = 1
IWModuleType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWNetwork_vtables_dispatch_ = 1
IWNetwork_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NetworkType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NetworkType' , 'pVal' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IWNetworkType_vtables_dispatch_ = 1
IWNetworkType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWNone_vtables_dispatch_ = 1
IWNone_vtables_ = [
]

IWPart_vtables_dispatch_ = 1
IWPart_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ArrivalType' , 'Type' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ArrivalType' , 'Type' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCreate' , 'Statement' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnCreate' , 'Statement' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLeave' , 'Statement' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLeave' , 'Statement' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MaximumArrivals' , 'Expression' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MaximumArrivals' , 'Expression' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FirstArrivalAt' , 'Expression' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FirstArrivalAt' , 'Expression' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Shift' , 'Expression' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Shift' , 'Expression' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'InterArrivalTime' , 'Expression' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'InterArrivalTime' , 'Expression' , ), 107, (107, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LotSize' , 'Expression' , ), 108, (108, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'LotSize' , 'Expression' , ), 108, (108, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'InputToModelRule' , 'Rule' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'InputToModelRule' , 'Rule' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'FixedAttributeValues' , 'Value' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'FixedAttributeValues' , 'Value' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFixedAttributes' , 'Statement' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFixedAttributes' , 'Statement' , ), 111, (111, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ContainsFluid' , 'Value' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ContainsFluid' , 'Value' , ), 112, (112, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GroupNumber' , 'Expression' , ), 113, (113, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GroupNumber' , 'Expression' , ), 113, (113, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'PartRouteStages' , 'StagesCollection' , ), 114, (114, (), [ (16393, 10, None, "IID('{DEC15362-502E-11D5-9BD3-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 115, (115, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ProfileEntries' , 'Entries' , ), 116, (116, (), [ (16393, 10, None, "IID('{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ProfileTimeDisplay' , 'TimeDisplay' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ProfileTimeDisplay' , 'TimeDisplay' , ), 117, (117, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ProfileMultiplier' , 'Expression' , ), 118, (118, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ProfileMultiplier' , 'Expression' , ), 118, (118, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ProfileRandomNumberStream' , 'StreamNumber' , ), 119, (119, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'ProfileRandomNumberStream' , 'StreamNumber' , ), 119, (119, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ProfileSmoothing' , 'OnOff' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ProfileSmoothing' , 'OnOff' , ), 120, (120, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ProfileCumulativeTime' , 'OnOff' , ), 121, (121, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ProfileCumulativeTime' , 'OnOff' , ), 121, (121, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ProfileImport' , 'Path' , ), 122, (122, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'NumberEntered' , 'Value' , ), 123, (123, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'NumberShipped' , 'Value' , ), 124, (124, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'NumberScrapped' , 'Value' , ), 125, (125, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'NumberRejected' , 'Value' , ), 126, (126, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'WorkInProgress' , 'Value' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'AverageWorkInProgress' , 'ShiftTime' , 'Value' , ), 128, (128, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'AverageTime' , 'ShiftTime' , 'Value' , ), 129, (129, (), [ (11, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'NumberAssembled' , 'Value' , ), 130, (130, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'AverageWorkInProgress2' , 'Value' , ), 131, (131, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'AverageTime2' , 'Value' , ), 132, (132, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'CreateInstance' , 'PartInstance' , ), 133, (133, (), [ (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 134, (134, (), [ (16393, 10, None, "IID('{B9E729DD-60D2-4F45-9358-3C8047008411}')") , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
]

IWPartArrivalProfileEntries_vtables_dispatch_ = 1
IWPartArrivalProfileEntries_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Position' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWPartArrivalProfileEntry_vtables_dispatch_ = 1
IWPartArrivalProfileEntry_vtables_ = [
	(( 'Length' , 'Time' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Time' , ), 1, (1, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'Expression' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'Expression' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'Time' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CumulativeTime' , 'Time' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPartFile_vtables_dispatch_ = 1
IWPartFile_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IWPartFileType_vtables_dispatch_ = 1
IWPartFileType_vtables_ = [
	(( 'Define' , 'Name' , 'fileMode' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{4C079D1F-F67E-41E5-B770-116E257E6C7C}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPartInstance_vtables_dispatch_ = 1
IWPartInstance_vtables_ = [
	(( 'Part' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{C641E7A1-817B-40FA-849E-7956F1C1A846}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Contents' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Contents' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Fluid' , 'pVal' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Fluid' , 'pVal' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CurrentStage' , 'pVal' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CurrentStage' , 'pVal' , ), 8, (8, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfStages' , 'pVal' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RoutingCycleTime' , 'pVal' , ), 10, (10, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RoutingSetupTime' , 'pVal' , ), 11, (11, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UserAttributes' , 'Attributes' , ), 12, (12, (), [ (16393, 10, None, "IID('{427F8FA2-0EEE-11D5-8579-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IWPartInstances_vtables_dispatch_ = 1
IWPartInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWPartMeasure_vtables_dispatch_ = 1
IWPartMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PerCreate' , 'Value' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PerCreate' , 'Value' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PerShipped' , 'Value' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PerShipped' , 'Value' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PerScrapped' , 'Value' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PerScrapped' , 'Value' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IWPartMeasures_vtables_dispatch_ = 1
IWPartMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3569B25C-2E41-4F11-AB30-2D112546D800}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3569B25C-2E41-4F11-AB30-2D112546D800}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWPartRouteStage_vtables_dispatch_ = 1
IWPartRouteStage_vtables_ = [
	(( 'Stage' , 'Number' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'Destination' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'Destination' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'R_SETUP' , 'Expression' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'R_SETUP' , 'Expression' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'R_CYCLE' , 'Expression' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'R_CYCLE' , 'Expression' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IWPartRouteStages_vtables_dispatch_ = 1
IWPartRouteStages_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Position' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWPartType_vtables_dispatch_ = 1
IWPartType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{C641E7A1-817B-40FA-849E-7956F1C1A846}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPath_vtables_dispatch_ = 1
IWPath_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TraverseTime' , 'Expression' , ), 100, (100, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TraverseTime' , 'Expression' , ), 100, (100, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateInterval' , 'Expression' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateInterval' , 'Expression' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SourceElement' , 'Element' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SourceElement' , 'Element' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DestinationElement' , 'Element' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DestinationElement' , 'Element' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'Statement' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'Statement' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLeave' , 'Statement' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLeave' , 'Statement' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'ReportingMode' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'PartsIn' , 'Value' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PartsOut' , 'Value' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'LaborIn' , 'Value' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LaborOut' , 'Value' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'ShiftTime' , 'Value' , ), 111, (111, (), [ 
			 (3, 1, None, None) , (11, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'TimeLeft' , 'Position' , 'Value' , ), 112, (112, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Value' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'Count' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfLabor' , 'Labor' , 'Count' , ), 118, (118, (), [ (9, 1, None, "IID('{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}')") , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'InstancesOnPath' , 'Collection' , ), 119, (119, (), [ (16393, 10, None, "IID('{83073E66-7AF6-46C0-89D2-F33E7C972377}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Sources' , 'pVal' , ), 14, (14, (), [ (16393, 10, None, "IID('{AB588585-190B-4830-BB71-A88D92BA8451}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Destinations' , 'pVal' , ), 15, (15, (), [ (16393, 10, None, "IID('{AB588585-190B-4830-BB71-A88D92BA8451}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Measures' , 'Measures' , ), 120, (120, (), [ (16393, 10, None, "IID('{595E1B97-E9E7-465E-AF63-A243735FB187}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 16, (16, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
]

IWPathData_vtables_dispatch_ = 1
IWPathData_vtables_ = [
	(( 'ShowLine' , 'pVal' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShowLine' , 'pVal' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Hollow' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Hollow' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Center' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Center' , 'pVal' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySize' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySize' , 'pVal' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Points' , 'Points' , ), 7, (7, (), [ (16393, 10, None, "IID('{D1227816-BAED-4DBB-8F28-B269E166A613}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'StartArrow' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StartArrow' , 'pVal' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'EndArrow' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'EndArrow' , 'pVal' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DashLine' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DashLine' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TravelAtSideOfPath' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TravelAtSideOfPath' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MultipleGraphicGap' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'MultipleGraphicGap' , 'pVal' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FixedLength' , 'pVal' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FixedLength' , 'pVal' , ), 13, (13, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IWPathElementExpression_vtables_dispatch_ = 1
IWPathElementExpression_vtables_ = [
	(( 'Expression' , 'pVal' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Expression' , 'pVal' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWPathElementExpressions_vtables_dispatch_ = 1
IWPathElementExpressions_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{288D0178-6C4B-4ACF-A344-9553E6714BC5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Expression' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWPathMeasure_vtables_dispatch_ = 1
IWPathMeasure_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FixedUse' , 'Value' , ), 1, (1, (), [ (16393, 10, None, "IID('{F357C6B3-3507-4611-96ED-3247D7C687D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWPathMeasures_vtables_dispatch_ = 1
IWPathMeasures_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Value' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
	(( 'Add' , 'Name' , 'Item' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWPathType_vtables_dispatch_ = 1
IWPathType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{FDB0A591-25D9-44EC-AB08-783742063AA7}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPiechart_vtables_dispatch_ = 1
IWPiechart_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SegmentDescription' , 'Index' , 'pVal' , ), 101, (101, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ExtractedSegment' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SegmentColor' , 'Index' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IWPiechartType_vtables_dispatch_ = 1
IWPiechartType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{D160D6FC-8110-41E0-84E2-B1754FAF4596}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPipe_vtables_dispatch_ = 1
IWPipe_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PipeInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{60324619-F3C0-4114-9CA4-4DE9533A0849}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'pipeBreakdownsPtr' , ), 105, (105, (), [ (16393, 10, None, "IID('{E0B23F84-C932-4AE3-B38D-52D982886FCD}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IWPipeBreakdowns_vtables_dispatch_ = 1
IWPipeBreakdowns_vtables_ = [
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IWPipeInstance_vtables_dispatch_ = 1
IWPipeInstance_vtables_ = [
	(( 'Pipe' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{EBCA5DAE-76F3-4872-8247-EDD3CED57353}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWPipeInstances_vtables_dispatch_ = 1
IWPipeInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E16C5044-7333-467A-98F1-579B48C09D3A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWPipeType_vtables_dispatch_ = 1
IWPipeType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{EBCA5DAE-76F3-4872-8247-EDD3CED57353}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWPoint_vtables_dispatch_ = 1
IWPoint_vtables_ = [
	(( 'X' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWPoints_vtables_dispatch_ = 1
IWPoints_vtables_ = [
	(( 'Item' , 'Index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C6034440-1A59-48D8-B463-43918B37FD28}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'X' , 'Y' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWProcessor_vtables_dispatch_ = 1
IWProcessor_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ProcessorInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{4190AF59-9851-4ADB-8902-A809824D4621}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ProcessTime' , 'pVal' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ProcessTime' , 'pVal' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'processorBreakdownsPtr' , ), 105, (105, (), [ (16393, 10, None, "IID('{2B044458-8E03-4C1A-AFE5-362A39E4500C}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IWProcessorBreakdowns_vtables_dispatch_ = 1
IWProcessorBreakdowns_vtables_ = [
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IWProcessorInstance_vtables_dispatch_ = 1
IWProcessorInstance_vtables_ = [
	(( 'Processor' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{3E62686A-D9BF-464A-B478-DE8559513141}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWProcessorInstances_vtables_dispatch_ = 1
IWProcessorInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWProcessorType_vtables_dispatch_ = 1
IWProcessorType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{3E62686A-D9BF-464A-B478-DE8559513141}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWRandomNumberCoverageBuckets_vtables_dispatch_ = 1
IWRandomNumberCoverageBuckets_vtables_ = [
	(( 'Initialise' , 'Stream' , 'subStream' , 'counts' , ), 1, (1, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StreamIndex' , 'Stream' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SubStreamIndex' , 'subStream' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'counts' , 'counts' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWRandomNumberCoverageBucketsCollection_vtables_dispatch_ = 1
IWRandomNumberCoverageBucketsCollection_vtables_ = [
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{FF833377-93CB-45EB-A66D-E9C311E043C1}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWRandomNumberUsage_vtables_dispatch_ = 1
IWRandomNumberUsage_vtables_ = [
	(( 'Report' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{27865A7B-1F7C-4449-957B-D6FDB0BD4052}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CoverageBuckets' , 'ppVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{752CA6D4-E88D-4BFF-9638-8B0334C04667}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWRemoteControl_vtables_dispatch_ = 1
IWRemoteControl_vtables_ = [
	(( 'WclControl' , 'retVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BackupModel' , 'modelPath' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWReport_vtables_dispatch_ = 1
IWReport_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IWReportData_vtables_dispatch_ = 1
IWReportData_vtables_ = [
	(( 'Columns' , 'pVal' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'pVal' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWReportType_vtables_dispatch_ = 1
IWReportType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{55A4116E-D4E0-4547-8349-AD733DC01C16}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWResponses_vtables_dispatch_ = 1
IWResponses_vtables_ = [
	(( 'Item' , 'lnIndex' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Default' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Default' , 'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Response' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Response' , 'pVal' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IWRoute_vtables_dispatch_ = 1
IWRoute_vtables_ = [
]

IWSample_vtables_dispatch_ = 1
IWSample_vtables_ = [
	(( 'Random' , 'Stream' , 'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Antithetic' , 'Stream' , 'On' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Binomial' , 'Probability' , 'NumTrials' , 'Stream' , 'Value' , 
			 ), 3, (3, (), [ (5, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Poisson' , 'Mean' , 'Stream' , 'Value' , ), 4, (4, (), [ 
			 (5, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Uniform' , 'Lowest' , 'Highest' , 'Stream' , 'Value' , 
			 ), 5, (5, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IUniform' , 'Lowest' , 'Highest' , 'Stream' , 'Value' , 
			 ), 6, (6, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NegExp' , 'Mean' , 'Stream' , 'Value' , ), 7, (7, (), [ 
			 (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Erlang' , 'Mean' , 'K' , 'Stream' , 'Value' , 
			 ), 8, (8, (), [ (5, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Normal' , 'Mean' , 'StdDeviation' , 'Stream' , 'Value' , 
			 ), 9, (9, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LogNormal' , 'Mean' , 'StdDeviation' , 'Stream' , 'Value' , 
			 ), 10, (10, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Triangle' , 'Minimum' , 'MostLikely' , 'Maximum' , 'Stream' , 
			 'Value' , ), 11, (11, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			 (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Gamma' , 'Shape' , 'Scale' , 'Stream' , 'Value' , 
			 ), 12, (12, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Beta' , 'Shape' , 'Scale' , 'Stream' , 'Value' , 
			 ), 13, (13, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TNormal' , 'Mean' , 'StdDeviation' , 'Min' , 'Max' , 
			 'Stream' , 'Value' , ), 14, (14, (), [ (5, 1, None, None) , (5, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Weibull' , 'Shape' , 'Scale' , 'Stream' , 'Value' , 
			 ), 15, (15, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Initialise' , 'Stream' , 'NumberOfObservationsToSkip' , ), 16, (16, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Seed' , 'SeedNumber' , 'pVal' , ), 17, (17, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Seed' , 'SeedNumber' , 'pVal' , ), 17, (17, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RandomNumberUsage' , 'pVal' , ), 18, (18, (), [ (16393, 10, None, "IID('{30DD08CA-7835-4684-9C1B-46674D674204}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IWScrap_vtables_dispatch_ = 1
IWScrap_vtables_ = [
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 100, (100, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWSection_vtables_dispatch_ = 1
IWSection_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionRule' , 'pVal' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionRule' , 'pVal' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DriveSpeed' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DriveSpeed' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DogSpacing' , 'pVal' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DogSpacing' , 'pVal' , ), 107, (107, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnExit' , 'pVal' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnExit' , 'pVal' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'pVal' , ), 110, (110, (), [ (16393, 10, None, "IID('{43821155-63F6-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pVal' , ), 111, (111, (), [ (16393, 10, None, "IID('{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 112, (112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 112, (112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 200, (200, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfCarriers' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CurrentNumberOfPoweredCarriers' , 'pVal' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CurrentNumberOfFreeCarriers' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfLoadedCarriers' , 'pVal' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'CarrierAverageTimePowered' , 'pVal' , ), 205, (205, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CarrierAverageTimeFree' , 'pVal' , ), 206, (206, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 207, (207, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 207, (207, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SectionInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
]

IWSectionBreakdown_vtables_dispatch_ = 1
IWSectionBreakdown_vtables_ = [
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IWSectionBreakdownInstance_vtables_dispatch_ = 1
IWSectionBreakdownInstance_vtables_ = [
	(( 'ElementInstance' , 'ElementInstance' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownNumber' , 'BreakdownNumber' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownState' , 'BreakdownState' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWSectionBreakdownInstances_vtables_dispatch_ = 1
IWSectionBreakdownInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWSectionBreakdowns_vtables_dispatch_ = 1
IWSectionBreakdowns_vtables_ = [
	(( 'Item' , 'Index' , 'Breakdown' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{43821154-63F6-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Description' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWSectionInstance_vtables_dispatch_ = 1
IWSectionInstance_vtables_ = [
	(( 'Section' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{1AF98A1D-C6E6-4681-88CC-8DB41A320460}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CarriersPresent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{8B98F244-7A42-4233-9432-BABB237EE777}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 7, (7, (), [ 
			 (3, 0, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ActiveBreakdowns' , 'BreakdownInstances' , ), 12, (12, (), [ (16393, 10, None, "IID('{43821157-63F6-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfCarriers' , 'pVal' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CurrentNumberOfPoweredCarriers' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CurrentNumberOfFreeCarriers' , 'pVal' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfLoadedCarriers' , 'pVal' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CarrierAverageTimePowered' , 'pVal' , ), 24, (24, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CarrierAverageTimeFree' , 'pVal' , ), 25, (25, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IWSectionInstances_vtables_dispatch_ = 1
IWSectionInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{865318D8-96F3-40F0-866A-84A937964A79}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWSectionType_vtables_dispatch_ = 1
IWSectionType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{1AF98A1D-C6E6-4681-88CC-8DB41A320460}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWSecurity_vtables_dispatch_ = 1
IWSecurity_vtables_ = [
	(( 'SecurityAquire' , 'Value' , 'pluginID' , 'pSecured' , ), 1610743808, (1610743808, (), [ 
			 (12, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SecurityStillValid' , 'Value' , 'pluginID' , 'pStillValid' , ), 1610743809, (1610743809, (), [ 
			 (12, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SecurityRelease' , 'Value' , 'pluginID' , ), 1610743810, (1610743810, (), [ (12, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWShift_vtables_dispatch_ = 1
IWShift_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SubShift' , 'pVal' , ), 100, (100, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SubShift' , 'pVal' , ), 100, (100, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'InitialWorkTime' , 'pVal' , ), 101, (101, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'InitialWorkTime' , 'pVal' , ), 101, (101, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InitialRestTime' , 'pVal' , ), 102, (102, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InitialRestTime' , 'pVal' , ), 102, (102, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StartWorkActions' , 'pVal' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StartWorkActions' , 'pVal' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'EndWorkActions' , 'pVal' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EndWorkActions' , 'pVal' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ShiftPeriods' , 'ShiftPeriods' , ), 109, (109, (), [ (16393, 10, None, "IID('{520FA171-59C5-11D5-A1C1-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'pVal' , ), 110, (110, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CurrentPeriod' , 'pVal' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'AvailableLaborUnits' , 'Labor' , 'pVal' , ), 112, (112, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfCompletedShifts' , 'pVal' , ), 113, (113, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 114, (114, (), [ ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
]

IWShiftPeriod_vtables_dispatch_ = 1
IWShiftPeriod_vtables_ = [
	(( 'PeriodType' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PeriodType' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'WorkingTime' , 'pVal' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'WorkingTime' , 'pVal' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RestTime' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RestTime' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OverTime' , 'pVal' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OverTime' , 'pVal' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SubShiftName' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SubShiftName' , 'pVal' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IWShiftPeriods_vtables_dispatch_ = 1
IWShiftPeriods_vtables_ = [
	(( 'Item' , 'Index' , 'ShiftPeriod' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{520FA170-59C5-11D5-A1C1-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AddPeriod' , 'WorkingTime' , 'RestTime' , 'OverTime' , 'Position' , 
			 ), 2, (2, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AddSubShift' , 'Name' , 'Position' , ), 3, (3, (), [ (8, 1, None, None) , 
			 (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWShiftType_vtables_dispatch_ = 1
IWShiftType_vtables_ = [
	(( 'Define' , 'Name' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWShip_vtables_dispatch_ = 1
IWShip_vtables_ = [
	(( 'AddPart' , 'PartInstance' , 'Sucess' , ), 100, (100, (), [ (9, 1, None, "IID('{10538218-737F-44BF-BBC4-7B169F983E1B}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWStandardApplication_vtables_dispatch_ = 1
IWStandardApplication_vtables_ = [
]

IWStation_vtables_dispatch_ = 1
IWStation_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StationType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StationType' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionRule' , 'pVal' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionRule' , 'pVal' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ParkingCycleTime' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ParkingCycleTime' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnParking' , 'pVal' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnParking' , 'pVal' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ParkingLaborRule' , 'pVal' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ParkingLaborRule' , 'pVal' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptLevel' , 'pVal' , ), 109, (109, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptLevel' , 'pVal' , ), 109, (109, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptAllowance' , 'pVal' , ), 110, (110, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptAllowance' , 'pVal' , ), 110, (110, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptPenalty' , 'pVal' , ), 111, (111, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ParkingPreEmptPenalty' , 'pVal' , ), 111, (111, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingCycleTime' , 'pVal' , ), 112, (112, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingCycleTime' , 'pVal' , ), 112, (112, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUnparking' , 'pVal' , ), 113, (113, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUnparking' , 'pVal' , ), 113, (113, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingLaborRule' , 'pVal' , ), 114, (114, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingLaborRule' , 'pVal' , ), 114, (114, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptLevel' , 'pVal' , ), 115, (115, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptLevel' , 'pVal' , ), 115, (115, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptAllowance' , 'pVal' , ), 116, (116, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptAllowance' , 'pVal' , ), 116, (116, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptPenalty' , 'pVal' , ), 117, (117, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UnparkingPreEmptPenalty' , 'pVal' , ), 117, (117, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'EntryCycleTime' , 'pVal' , ), 118, (118, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'EntryCycleTime' , 'pVal' , ), 118, (118, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 119, (119, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 119, (119, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'EntryLaborRule' , 'pVal' , ), 120, (120, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'EntryLaborRule' , 'pVal' , ), 120, (120, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptLevel' , 'pVal' , ), 121, (121, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptLevel' , 'pVal' , ), 121, (121, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptAllowance' , 'pVal' , ), 122, (122, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptAllowance' , 'pVal' , ), 122, (122, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptPenalty' , 'pVal' , ), 123, (123, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'EntryPreEmptPenalty' , 'pVal' , ), 123, (123, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'ProcessCycleTime' , 'pVal' , ), 124, (124, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'ProcessCycleTime' , 'pVal' , ), 124, (124, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnProcess' , 'pVal' , ), 125, (125, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnProcess' , 'pVal' , ), 125, (125, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ProcessLaborRule' , 'pVal' , ), 126, (126, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ProcessLaborRule' , 'pVal' , ), 126, (126, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptLevel' , 'pVal' , ), 127, (127, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptLevel' , 'pVal' , ), 127, (127, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptAllowance' , 'pVal' , ), 128, (128, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptAllowance' , 'pVal' , ), 128, (128, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptPenalty' , 'pVal' , ), 129, (129, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'ProcessPreEmptPenalty' , 'pVal' , ), 129, (129, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'ExitCycleTime' , 'pVal' , ), 130, (130, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'ExitCycleTime' , 'pVal' , ), 130, (130, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnExit' , 'pVal' , ), 131, (131, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnExit' , 'pVal' , ), 131, (131, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'ExitLaborRule' , 'pVal' , ), 132, (132, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'ExitLaborRule' , 'pVal' , ), 132, (132, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptLevel' , 'pVal' , ), 133, (133, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptLevel' , 'pVal' , ), 133, (133, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptAllowance' , 'pVal' , ), 134, (134, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptAllowance' , 'pVal' , ), 134, (134, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptPenalty' , 'pVal' , ), 135, (135, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'ExitPreEmptPenalty' , 'pVal' , ), 135, (135, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'LoadingMethod' , 'pVal' , ), 136, (136, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'LoadingMethod' , 'pVal' , ), 136, (136, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'LoadingCycleTime' , 'pVal' , ), 137, (137, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'LoadingCycleTime' , 'pVal' , ), 137, (137, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStartLoading' , 'pVal' , ), 138, (138, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStartLoading' , 'pVal' , ), 138, (138, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinishLoading' , 'pVal' , ), 139, (139, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinishLoading' , 'pVal' , ), 139, (139, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'LoadingLaborRule' , 'pVal' , ), 140, (140, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'LoadingLaborRule' , 'pVal' , ), 140, (140, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptLevel' , 'pVal' , ), 141, (141, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptLevel' , 'pVal' , ), 141, (141, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptAllowance' , 'pVal' , ), 142, (142, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptAllowance' , 'pVal' , ), 142, (142, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptPenalty' , 'pVal' , ), 143, (143, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'LoadingPreEmptPenalty' , 'pVal' , ), 143, (143, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'LoadingInputRule' , 'pVal' , ), 144, (144, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'LoadingInputRule' , 'pVal' , ), 144, (144, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingMethod' , 'pVal' , ), 145, (145, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingMethod' , 'pVal' , ), 145, (145, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingCycleTime' , 'pVal' , ), 146, (146, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingCycleTime' , 'pVal' , ), 146, (146, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStartUnloading' , 'pVal' , ), 147, (147, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnStartUnloading' , 'pVal' , ), 147, (147, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinishUnloading' , 'pVal' , ), 148, (148, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFinishUnloading' , 'pVal' , ), 148, (148, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingLaborRule' , 'pVal' , ), 149, (149, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingLaborRule' , 'pVal' , ), 149, (149, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptLevel' , 'pVal' , ), 150, (150, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptLevel' , 'pVal' , ), 150, (150, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptAllowance' , 'pVal' , ), 151, (151, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptAllowance' , 'pVal' , ), 151, (151, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptPenalty' , 'pVal' , ), 152, (152, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingPreEmptPenalty' , 'pVal' , ), 152, (152, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingOutputRule' , 'pVal' , ), 153, (153, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'UnloadingOutputRule' , 'pVal' , ), 153, (153, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'Breakdowns' , 'pVal' , ), 154, (154, (), [ (16393, 10, None, "IID('{A5729D61-63D2-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pVal' , ), 155, (155, (), [ (16393, 10, None, "IID('{00504947-3FAA-4A8F-BF64-4EA4E3416B69}')") , ], 1 , 2 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 156, (156, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'AllocatedNetwork' , 'pVal' , ), 156, (156, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 200, (200, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfCarriers' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfParts' , 'pVal' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'StationInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{503951C9-860E-4251-A8C8-0E26E9046231}')") , ], 1 , 2 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
]

IWStationBreakdown_vtables_dispatch_ = 1
IWStationBreakdown_vtables_ = [
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownMode' , 'Mode' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TimeBetweenFailures' , 'Expression' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RepairTime' , 'Expression' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LaborRule' , 'Rule' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptLevel' , 'pVal' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptAllowance' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PreEmptPenalty' , 'pVal' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnDown' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnResume' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IWStationBreakdownInstance_vtables_dispatch_ = 1
IWStationBreakdownInstance_vtables_ = [
	(( 'ElementInstance' , 'ElementInstance' , ), 1, (1, (), [ (16393, 10, None, "IID('{B663FFB1-235F-11D5-A1B4-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownNumber' , 'BreakdownNumber' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownState' , 'BreakdownState' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWStationBreakdownInstances_vtables_dispatch_ = 1
IWStationBreakdownInstances_vtables_ = [
	(( 'Item' , 'Index' , 'pvarItem' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWStationBreakdowns_vtables_dispatch_ = 1
IWStationBreakdowns_vtables_ = [
	(( 'Item' , 'Index' , 'Breakdown' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A5729D60-63D2-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Description' , 'Position' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Factors' , 'valuePtr' , ), 4, (4, (), [ (16393, 10, None, "IID('{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWStationInstance_vtables_dispatch_ = 1
IWStationInstance_vtables_ = [
	(( 'Station' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{517122AB-6C4C-4996-975C-207AABEF7353}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CarriersPresent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{8B98F244-7A42-4233-9432-BABB237EE777}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LaborPresent' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{39150113-B27B-43AA-B116-5EFCF532B027}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ForcedBreakdown' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ForcedRepair' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 7, (7, (), [ 
			 (3, 0, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ActiveBreakdowns' , 'BreakdownInstances' , ), 12, (12, (), [ (16393, 10, None, "IID('{A5729D63-63D2-11D5-85C7-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfCarriers' , 'pVal' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfParts' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IWStationInstances_vtables_dispatch_ = 1
IWStationInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWStationType_vtables_dispatch_ = 1
IWStationType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{517122AB-6C4C-4996-975C-207AABEF7353}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWSystemElement_vtables_dispatch_ = 1
IWSystemElement_vtables_ = [
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWTank_vtables_dispatch_ = 1
IWTank_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'TankInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{621E28F2-E65D-456E-8229-D1A8BE6EB63D}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IWTankInstance_vtables_dispatch_ = 1
IWTankInstance_vtables_ = [
	(( 'Tank' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{8D4C9A2A-5367-4819-9911-DD9CA73006F7}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWTankInstances_vtables_dispatch_ = 1
IWTankInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWTankType_vtables_dispatch_ = 1
IWTankType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{8D4C9A2A-5367-4819-9911-DD9CA73006F7}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWTimeseries_vtables_dispatch_ = 1
IWTimeseries_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IWTimeseriesType_vtables_dispatch_ = 1
IWTimeseriesType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{BFD54915-A1B1-46C6-87F5-B8B6C567615B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWTrack_vtables_dispatch_ = 1
IWTrack_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TrackInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{20892432-3AD4-4D37-807F-5C035DF0638B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PhysicalLength' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PhysicalLength' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MaximumSpeed' , 'pVal' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'MaximumSpeed' , 'pVal' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BusyTime' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'BusyTime' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnJoin' , 'pVal' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnJoin' , 'pVal' , ), 106, (106, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFront' , 'pVal' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnFront' , 'pVal' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Zone' , 'pVal' , ), 108, (108, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Zone' , 'pVal' , ), 108, (108, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 110, (110, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'WorkSearch' , 'WorkSearchItems' , ), 111, (111, (), [ (16393, 10, None, "IID('{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'StopMode' , 'pVal' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'StopMode' , 'pVal' , ), 120, (120, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'StopTime' , 'pVal' , ), 121, (121, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'StopTime' , 'pVal' , ), 121, (121, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'StopCondition' , 'pVal' , ), 122, (122, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'StopCondition' , 'pVal' , ), 122, (122, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'LoadMode' , 'pVal' , ), 140, (140, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'LoadMode' , 'pVal' , ), 140, (140, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'LoadTime' , 'pVal' , ), 141, (141, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'LoadTime' , 'pVal' , ), 141, (141, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'LoadInputRule' , 'pVal' , ), 142, (142, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'LoadInputRule' , 'pVal' , ), 142, (142, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'LoadQuantity' , 'pVal' , ), 143, (143, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'LoadQuantity' , 'pVal' , ), 143, (143, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLoad' , 'pVal' , ), 144, (144, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnLoad' , 'pVal' , ), 144, (144, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'LoadCondition' , 'pVal' , ), 145, (145, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'LoadCondition' , 'pVal' , ), 145, (145, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UnloadMode' , 'pVal' , ), 160, (160, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UnloadMode' , 'pVal' , ), 160, (160, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'UnloadTime' , 'pVal' , ), 161, (161, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'UnloadTime' , 'pVal' , ), 161, (161, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'UnloadOutputRule' , 'pVal' , ), 162, (162, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'UnloadOutputRule' , 'pVal' , ), 162, (162, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UnloadQuantity' , 'pVal' , ), 163, (163, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UnloadQuantity' , 'pVal' , ), 163, (163, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUnload' , 'pVal' , ), 164, (164, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnUnload' , 'pVal' , ), 164, (164, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ParkPosition' , 'pVal' , ), 165, (165, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ParkPosition' , 'pVal' , ), 165, (165, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'UnloadCondition' , 'pVal' , ), 166, (166, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'UnloadCondition' , 'pVal' , ), 166, (166, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 180, (180, (), [ ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 200, (200, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 202, (202, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfVehicles' , 'pVal' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfVehiclesOn' , 'pVal' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'UnloadOutputFrom' , 'pVal' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'UnloadOutputFrom' , 'pVal' , ), 206, (206, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
]

IWTrackInstance_vtables_dispatch_ = 1
IWTrackInstance_vtables_ = [
	(( 'Track' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{B4FD8014-1552-475F-A679-F2B15A8147A8}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'VehiclesOn' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{33DC7FEE-B353-483D-8F54-E63B63C41B49}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 4, (4, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 6, (6, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfVehicles' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfVehiclesOn' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TimeTillNextEvent' , 'pVal' , ), 10, (10, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IWTrackInstances_vtables_dispatch_ = 1
IWTrackInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWTrackType_vtables_dispatch_ = 1
IWTrackType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{B4FD8014-1552-475F-A679-F2B15A8147A8}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWTrackWorkSearchItem_vtables_dispatch_ = 1
IWTrackWorkSearchItem_vtables_ = [
	(( 'Track' , 'pVal' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Track' , 'pVal' , ), 1, (1, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IWTrackWorkSearchItems_vtables_dispatch_ = 1
IWTrackWorkSearchItems_vtables_ = [
	(( 'Item' , 'Index' , 'WorkSeachItem' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Track' , 'Position' , ), 2, (2, (), [ (12, 1, None, None) , 
			 (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Position' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWType_vtables_dispatch_ = 1
IWType_vtables_ = [
	(( 'Name' , 'pVal' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'NamePlural' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IWTypes_vtables_dispatch_ = 1
IWTypes_vtables_ = [
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IndexOf' , 'Key' , 'Index' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IWUserElement_vtables_dispatch_ = 1
IWUserElement_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IWUserProperties_vtables_dispatch_ = 1
IWUserProperties_vtables_ = [
	(( 'ContainsUserProperty' , 'Key' , 'result' , ), 9000, (9000, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetUserProperty' , 'Key' , 'Value' , ), 9001, (9001, (), [ (8, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PutUserProperty' , 'Key' , 'Value' , ), 9002, (9002, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWVariable_vtables_dispatch_ = 1
IWVariable_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Dimensions' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{6C98C5C0-21DA-11D5-A1B3-00E02963982C}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInitialize' , 'pVal' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnInitialize' , 'pVal' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 103, (103, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 103, (103, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 103, (103, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 103, (103, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'VariableType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 105, (105, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 105, (105, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 105, (105, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ReferencedElementName' , 'dim1' , 'dim2' , 'dim3' , 'dim4' , 
			 'dim5' , 'dim6' , 'pVal' , ), 105, (105, (), [ (3, 49, '1', None) , 
			 (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , (3, 49, '1', None) , 
			 (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BulkValue' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BulkValue' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReDim' , 'Dimensions' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'VariableType' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'DisableResetOnBegin' , 'pVal' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'DisableResetOnBegin' , 'pVal' , ), 120, (120, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 121, (121, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 122, (122, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Watch' , 'valuePtr' , ), 122, (122, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
]

IWVariableType_vtables_dispatch_ = 1
IWVariableType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'VariableType' , 'pVal' , 
			 ), 101, (101, (), [ (8, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{E735E960-17C8-11D5-A1B3-00E02963982C}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DefineDynamic' , 'Name' , 'VariableType' , 'pVal' , ), 102, (102, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{E735E960-17C8-11D5-A1B3-00E02963982C}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IWVehicle_vtables_dispatch_ = 1
IWVehicle_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{E2D06A1C-239C-42EC-B904-CB0735088E0E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Model' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Module' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E4B4D340-1397-4A21-9F52-BB258A913C1A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Identifier' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Notes' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InitializeActions' , 'Statement' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserActions' , 'Statement' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PropertiesActions' , 'Statement' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'VehicleInstances' , 'pVal' , ), 0, (0, (), [ (16393, 10, None, "IID('{33DC7FEE-B353-483D-8F54-E63B63C41B49}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Quantity' , 'pVal' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pVal' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UnloadedSpeed' , 'pVal' , ), 103, (103, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UnloadedSpeed' , 'pVal' , ), 103, (103, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LoadedSpeed' , 'pVal' , ), 104, (104, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LoadedSpeed' , 'pVal' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'TimeDelayToStart' , 'pVal' , ), 105, (105, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'TimeDelayToStart' , 'pVal' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'TimeDelayToStop' , 'pVal' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'TimeDelayToStop' , 'pVal' , ), 106, (106, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ActionsOnEntry' , 'pVal' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 108, (108, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ShiftName' , 'pVal' , ), 108, (108, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ShiftStopImmediate' , 'pVal' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ShiftStopImmediate' , 'pVal' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 110, (110, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'OutputRule' , 'pVal' , ), 110, (110, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Reporting' , 'pVal' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 112, (112, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 114, (114, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfLoads' , 'pVal' , ), 116, (116, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'TotalDistanceTravelled' , 'pVal' , ), 117, (117, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RestartStatistics' , ), 120, (120, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Call' , 'LoadTrack' , 'UnloadTrack' , 'Priority' , ), 121, (121, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Wakeup' , 'OnTrack' , ), 122, (122, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'AssignToCurrentCall' , 'OnTrack' , ), 123, (123, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ShowInOptimizer' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'BreakdownRepairOnMass' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastToWPM' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'CompleteActions' , 'Statement' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'DescriptiveName' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IWVehicleInstance_vtables_dispatch_ = 1
IWVehicleInstance_vtables_ = [
	(( 'Vehicle' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{A64A59DA-690E-428D-894F-99F67F4956CB}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PercentageUtilization' , 'State' , 'OnShiftTime' , 'pVal' , ), 2, (2, (), [ 
			 (3, 1, None, None) , (11, 0, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfParts' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPartsOfType' , 'PartType' , 'pVal' , ), 4, (4, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfFreeSpaces' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TotalNumberOfLoads' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TotalDistanceTravelled' , 'pVal' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDestination' , 'pVal' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDestination' , 'pVal' , ), 8, (8, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NextDestination' , 'pVal' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CurrentTrack' , 'pVal' , ), 10, (10, (), [ (16393, 10, None, "IID('{1BE4C352-3E87-4432-8D0B-CC505F425D4D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CurrentPosition' , 'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Call' , 'LoadTrack' , 'UnloadTrack' , 'Priority' , ), 12, (12, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Wakeup' , 'OnTrack' , ), 13, (13, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AssignToCurrentCall' , 'OnTrack' , ), 14, (14, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PartsIn' , 'pVal' , ), 15, (15, (), [ (16393, 10, None, "IID('{63D176D1-0331-11D5-9B89-00E0295CD2CC}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 16, (16, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Desc' , 'pVal' , ), 16, (16, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 17, (17, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Pen' , 'pVal' , ), 17, (17, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 18, (18, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Icon' , 'pVal' , ), 18, (18, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UserAttributes' , 'Attributes' , ), 20, (20, (), [ (16393, 10, None, "IID('{427F8FA2-0EEE-11D5-8579-0020AFF488A2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IWVehicleInstances_vtables_dispatch_ = 1
IWVehicleInstances_vtables_ = [
	(( 'Item' , 'Position' , 'Instance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IWVehicleType_vtables_dispatch_ = 1
IWVehicleType_vtables_ = [
	(( 'Define' , 'Name' , 'Quantity' , 'pVal' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{A64A59DA-690E-428D-894F-99F67F4956CB}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IWWorld_vtables_dispatch_ = 1
IWWorld_vtables_ = [
]

IWitnessExtensionModule_vtables_dispatch_ = 0
IWitnessExtensionModule_vtables_ = [
	(( 'Initialize' , 'Application' , ), 1610678272, (1610678272, (), [ (9, 1, None, "IID('{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}')") , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( 'Destroy' , ), 1610678273, (1610678273, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

_IWCollection_vtables_dispatch_ = 1
_IWCollection_vtables_ = [
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 1 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}' : IWApplication,
	'{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}' : IWModel,
	'{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}' : IWTypes,
	'{679E5B61-21DA-11D5-A1B3-00E02963982C}' : _IWCollection,
	'{E2D06A1C-239C-42EC-B904-CB0735088E0E}' : IWType,
	'{E4B4D340-1397-4A21-9F52-BB258A913C1A}' : IWModule,
	'{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}' : IWElements,
	'{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}' : IWElement,
	'{10538218-737F-44BF-BBC4-7B169F983E1B}' : IWPartInstance,
	'{B663FFB1-235F-11D5-A1B4-00E02963982C}' : IWInstance,
	'{C641E7A1-817B-40FA-849E-7956F1C1A846}' : IWPart,
	'{DEC15362-502E-11D5-9BD3-00E0295CD2CC}' : IWPartRouteStages,
	'{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}' : IWPartArrivalProfileEntries,
	'{B9E729DD-60D2-4F45-9358-3C8047008411}' : IWPartMeasures,
	'{3569B25C-2E41-4F11-AB30-2D112546D800}' : IWPartMeasure,
	'{F357C6B3-3507-4611-96ED-3247D7C687D5}' : IWMeasureValue,
	'{427F8FA2-0EEE-11D5-8579-0020AFF488A2}' : IWAttributeInstances,
	'{427F8FA1-0EEE-11D5-8579-0020AFF488A2}' : IWAttributeInstance,
	'{F079D83C-D0A1-413D-9CC2-D64317021122}' : IWSample,
	'{30DD08CA-7835-4684-9C1B-46674D674204}' : IWRandomNumberUsage,
	'{27865A7B-1F7C-4449-957B-D6FDB0BD4052}' : IWReportData,
	'{752CA6D4-E88D-4BFF-9638-8B0334C04667}' : IWRandomNumberCoverageBucketsCollection,
	'{FF833377-93CB-45EB-A66D-E9C311E043C1}' : IWRandomNumberCoverageBuckets,
	'{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}' : IWNone,
	'{595FF59A-1729-4781-A427-66C61F9C6DCC}' : IWSystemElement,
	'{81E22460-8112-472B-9E14-96153261E6E0}' : IWShip,
	'{38FB81B4-8091-4A39-8041-56C31FDA7BD0}' : IWScrap,
	'{861CABEB-E70F-4879-AEA6-079D1B13BC1E}' : IWWorld,
	'{108615F0-4DBE-4D4C-826B-C606578491BA}' : IWAssemble,
	'{6A8123E6-FF3B-4502-AF3F-243AC818B17C}' : IWRoute,
	'{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}' : IWBackdrop,
	'{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}' : IWGraphics,
	'{2C138955-DAF6-456E-9F25-03730158A521}' : IWDrawTool,
	'{874FED95-DA11-48E4-B237-FC2CA83DE758}' : IWColor,
	'{F1496351-9B02-498C-9FB9-348E0B2AA565}' : IWFont,
	'{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}' : IWPathData,
	'{D1227816-BAED-4DBB-8F28-B269E166A613}' : IWPoints,
	'{C6034440-1A59-48D8-B463-43918B37FD28}' : IWPoint,
	'{D8396D00-CC33-47E7-A917-1527DF798EC5}' : IWModelEventManager,
	'{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}' : IWDirectories,
	'{B3951062-2E8D-407D-ABBD-D57FB4FAE705}' : IWModelMeasures,
	'{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}' : IWModelMeasure,
	'{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}' : IWFactors,
	'{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}' : IWErrorsAndWarnings,
	'{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}' : IWInputRequest,
	'{7FE9DF3A-DF37-43EB-AF81-2EB034A178A1}' : IWApplicationViewer,
	'{C7DB6FD3-764B-4E78-AFF6-A84F50C7A642}' : IWBPMViewer,
	'{BDDBB5BA-2342-4163-9682-BD86F8AF4C84}' : IWStandardApplication,
	'{C24094DC-99F0-4AD7-9357-9468EEB19259}' : IWUserElement,
	'{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}' : IWBufferInstance,
	'{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}' : IWBuffer,
	'{5A3597E0-2042-4969-919F-484397BF413B}' : IWBufferInstances,
	'{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}' : IWBufferMeasures,
	'{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}' : IWBufferMeasure,
	'{63D176D1-0331-11D5-9B89-00E0295CD2CC}' : IWPartInstances,
	'{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}' : IWConveyorInstance,
	'{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}' : IWConveyor,
	'{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}' : IWConveyorInstances,
	'{375E2CD5-8A41-45AF-9469-38744989269C}' : IWConveyorBreakdowns,
	'{330E3D97-24CF-4644-9000-DEEA6EB2306B}' : IWConveyorBreakdown,
	'{54486179-8C34-4101-831E-23A6D9FE10F6}' : IWConveyorSensors,
	'{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}' : IWConveyorSensor,
	'{1E6B62FD-4355-439E-8FA7-A54611B55B11}' : IWConveyorMeasures,
	'{75DE9907-45CA-4B2B-B584-7851F771FF1E}' : IWConveyorMeasure,
	'{8278E5B4-CAA4-42E8-AABF-09E7A7535725}' : IWConveyorBreakdownInstances,
	'{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}' : IWDataTableInstance,
	'{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}' : IWDataTable,
	'{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}' : IWDataTableInstances,
	'{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}' : IWDataTableColumnItems,
	'{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}' : IWDataTableColumnItem,
	'{46FB221B-D834-4B5E-B1EC-582524196017}' : IWLaborInstance,
	'{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}' : IWLabor,
	'{39150113-B27B-43AA-B116-5EFCF532B027}' : IWLaborInstances,
	'{402F5411-4F7E-11D5-A1C1-00E02963982C}' : IWLaborShifts,
	'{402F5410-4F7E-11D5-A1C1-00E02963982C}' : IWLaborShift,
	'{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}' : IWLaborMeasures,
	'{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}' : IWLaborMeasure,
	'{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}' : IWMachineInstance,
	'{35B1CE41-5962-4071-8824-4D43DA7C2DA9}' : IWMachineCycleInstances,
	'{897905FC-B806-4835-8AF8-088E6405AD70}' : IWMachineSetupInstances,
	'{1CD3A435-8D00-4CB8-A630-F666460D0372}' : IWMachineBreakdownInstances,
	'{12E061BC-E54B-11D4-8553-0020AFF488A2}' : IWMachine,
	'{8D12737F-BF42-4827-B95C-D891817FAB82}' : IWMachineBreakdowns,
	'{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}' : IWMachineBreakdown,
	'{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}' : IWMachineSetups,
	'{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}' : IWMachineSetup,
	'{A1B86D53-E79D-11D4-8556-0020AFF488A2}' : IWMachineCycles,
	'{A1B86D51-E79D-11D4-8556-0020AFF488A2}' : IWMachineCycle,
	'{921B4444-BEC7-4203-A45C-724F25DA67BB}' : IWMachineInstances,
	'{05F69682-BC4D-4B74-A78C-04E88D74CB06}' : IWMachineMeasures,
	'{63070342-EC3E-456F-90DA-B849F98EB873}' : IWMachineMeasure,
	'{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}' : IWCarrierInstance,
	'{1F803804-DB54-4D3E-A508-AFFC15277B77}' : IWCarrier,
	'{00504947-3FAA-4A8F-BF64-4EA4E3416B69}' : IWNetwork,
	'{8B98F244-7A42-4233-9432-BABB237EE777}' : IWCarrierInstances,
	'{865318D8-96F3-40F0-866A-84A937964A79}' : IWSectionInstance,
	'{1AF98A1D-C6E6-4681-88CC-8DB41A320460}' : IWSection,
	'{43821155-63F6-11D5-85C7-0020AFF488A2}' : IWSectionBreakdowns,
	'{43821154-63F6-11D5-85C7-0020AFF488A2}' : IWSectionBreakdown,
	'{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}' : IWSectionInstances,
	'{43821157-63F6-11D5-85C7-0020AFF488A2}' : IWSectionBreakdownInstances,
	'{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}' : IWStationInstance,
	'{517122AB-6C4C-4996-975C-207AABEF7353}' : IWStation,
	'{A5729D61-63D2-11D5-85C7-0020AFF488A2}' : IWStationBreakdowns,
	'{A5729D60-63D2-11D5-85C7-0020AFF488A2}' : IWStationBreakdown,
	'{503951C9-860E-4251-A8C8-0E26E9046231}' : IWStationInstances,
	'{A5729D63-63D2-11D5-85C7-0020AFF488A2}' : IWStationBreakdownInstances,
	'{1BE4C352-3E87-4432-8D0B-CC505F425D4D}' : IWTrackInstance,
	'{B4FD8014-1552-475F-A679-F2B15A8147A8}' : IWTrack,
	'{20892432-3AD4-4D37-807F-5C035DF0638B}' : IWTrackInstances,
	'{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}' : IWTrackWorkSearchItems,
	'{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}' : IWTrackWorkSearchItem,
	'{33DC7FEE-B353-483D-8F54-E63B63C41B49}' : IWVehicleInstances,
	'{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}' : IWVehicleInstance,
	'{A64A59DA-690E-428D-894F-99F67F4956CB}' : IWVehicle,
	'{83073E66-7AF6-46C0-89D2-F33E7C972377}' : IWInstances,
	'{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}' : IWShift,
	'{520FA171-59C5-11D5-A1C1-00E02963982C}' : IWShiftPeriods,
	'{520FA170-59C5-11D5-A1C1-00E02963982C}' : IWShiftPeriod,
	'{FDB0A591-25D9-44EC-AB08-783742063AA7}' : IWPath,
	'{AB588585-190B-4830-BB71-A88D92BA8451}' : IWPathElementExpressions,
	'{288D0178-6C4B-4ACF-A344-9553E6714BC5}' : IWPathElementExpression,
	'{595E1B97-E9E7-465E-AF63-A243735FB187}' : IWPathMeasures,
	'{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}' : IWPathMeasure,
	'{55A4116E-D4E0-4547-8349-AD733DC01C16}' : IWReport,
	'{E735E960-17C8-11D5-A1B3-00E02963982C}' : IWVariable,
	'{6C98C5C0-21DA-11D5-A1B3-00E02963982C}' : IWDimensions,
	'{FC5BF548-99F8-4907-925F-82E0B2FB7835}' : IWFunction,
	'{8693669F-C4C2-4318-AB34-8FF2860AB73B}' : IWFunctionParameters,
	'{E1347784-EA6C-4A12-813A-F0FD60924578}' : IWFunctionParameter,
	'{56EF0AE9-1E7D-4892-9C56-837855B9776E}' : IWAttribute,
	'{D4F90213-4DD0-4003-99AA-8DE53FB5E643}' : IWMachineBreakdownInstance,
	'{AAB2327A-85B4-41B8-A535-ECFB693A16E7}' : IWConveyorBreakdownInstance,
	'{A5729D62-63D2-11D5-85C7-0020AFF488A2}' : IWStationBreakdownInstance,
	'{43821156-63F6-11D5-85C7-0020AFF488A2}' : IWSectionBreakdownInstance,
	'{901A46A2-B4D6-473D-9B89-A9DABAB418E7}' : IWMachineCycleInstance,
	'{B66E325C-F3FA-40FE-A3D1-32570E96C8F7}' : IWMachineSetupInstance,
	'{71E7EE98-8043-47F9-9549-0813E776E594}' : IWPipeType,
	'{EBCA5DAE-76F3-4872-8247-EDD3CED57353}' : IWPipe,
	'{60324619-F3C0-4114-9CA4-4DE9533A0849}' : IWPipeInstances,
	'{E16C5044-7333-467A-98F1-579B48C09D3A}' : IWPipeInstance,
	'{E0B23F84-C932-4AE3-B38D-52D982886FCD}' : IWPipeBreakdowns,
	'{5229A31A-D096-4389-8540-65F371CF0D97}' : IWTankType,
	'{8D4C9A2A-5367-4819-9911-DD9CA73006F7}' : IWTank,
	'{621E28F2-E65D-456E-8229-D1A8BE6EB63D}' : IWTankInstances,
	'{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}' : IWTankInstance,
	'{20F7F5D9-FB97-4B74-8AA2-AE2AC48E47ED}' : IWProcessorType,
	'{3E62686A-D9BF-464A-B478-DE8559513141}' : IWProcessor,
	'{4190AF59-9851-4ADB-8902-A809824D4621}' : IWProcessorInstances,
	'{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}' : IWProcessorInstance,
	'{2B044458-8E03-4C1A-AFE5-362A39E4500C}' : IWProcessorBreakdowns,
	'{134FB1F0-5BF0-4678-B815-4042AF976628}' : IWPartFileType,
	'{4C079D1F-F67E-41E5-B770-116E257E6C7C}' : IWPartFile,
	'{92B89E14-6BAA-4D23-8DD5-CB15C77E2D3E}' : IWFileType,
	'{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}' : IWFile,
	'{58D5DB46-9295-452C-9FDB-1795E61A00A0}' : IWActivator,
	'{BFD54915-A1B1-46C6-87F5-B8B6C567615B}' : IWTimeseries,
	'{8CFB8503-E585-431A-9863-E1A3D6B9F34E}' : IWHistogram,
	'{D160D6FC-8110-41E0-84E2-B1754FAF4596}' : IWPiechart,
	'{6E875BB8-B0E1-4077-B06D-86824D1D29C5}' : IWSecurity,
	'{92D0A727-28A1-4682-A1B2-90BFF5677814}' : IWRemoteControl,
	'{82355849-4B8B-4B9C-A976-22ED38EACC8B}' : _IWApplicationEvents,
	'{9E52085E-C12A-4AF5-8B2C-E8BDBC253A87}' : _IWApplicationViewerEvents,
	'{1C0AC210-AAAB-4742-AAAF-560EB4672B59}' : _IWBPMViewerEvents,
	'{DE1AD8A2-DFDE-423A-8F5F-24B2CCE23961}' : _IWStandardApplicationEvents,
	'{FA29B843-D512-4287-BABD-71A4484B4ABC}' : IWUserProperties,
	'{E39933F0-9C47-4BB6-A18C-1B60B1A7C5C1}' : _IWModelEvents,
	'{1AA3916B-AE9E-460F-94D6-7D1884D98193}' : _IWModuleEvents,
	'{E2C6802B-8E63-4E50-AB64-B871071A779B}' : IWPartType,
	'{EB466F0D-214B-422A-942A-5BD1AA9F71FD}' : _IWPartTypeEvents,
	'{32F8A928-07DF-41D1-B490-C3282C7DB4D6}' : IWLaborType,
	'{8D3092D9-28BF-4949-B3D6-9A557A70E65C}' : _IWLaborTypeEvents,
	'{727F8035-F180-4863-9BAC-561F1D579AD3}' : IWTimeseriesType,
	'{CC38E78A-2250-4BA5-A50C-A2523E8B66B5}' : _IWTimeseriesTypeEvents,
	'{93DF3BB1-0CD3-45F9-B586-197112B69107}' : IWPiechartType,
	'{8D64F32A-FF93-4B89-AA4B-D505D9E66C0A}' : _IWPiechartTypeEvents,
	'{CD6C32EB-B24A-4ED0-89FC-AB39EE326295}' : IWHistogramType,
	'{057615BD-6B39-4A09-9B1D-0785FC02A6CE}' : _IWHistogramTypeEvents,
	'{7BAF40F7-A453-4B2C-9BC9-3A29F96F0BC0}' : IWTrackType,
	'{9959AEBF-296E-48D7-8BAC-DD05656AAB16}' : _IWTrackTypeEvents,
	'{C5F7EF56-FBC4-45E6-AA34-A6A38547535C}' : IWVehicleType,
	'{EACC1BC1-9308-40A7-9010-5A1D770AB02E}' : _IWVehicleTypeEvents,
	'{E36854D0-A37A-48AA-B2BE-A5E475428EE4}' : IWMachineType,
	'{EFEEB503-BA9A-49A9-8142-424C633327B5}' : _IWMachineTypeEvents,
	'{B2718466-9171-4B74-B6A4-DB7A3137DC31}' : _IWElementsEvents,
	'{B663FFB2-235F-11D5-A1B4-00E02963982C}' : _IWInstanceEvents,
	'{12E061BE-E54B-11D4-8553-0020AFF488A2}' : _IWMachineEvents,
	'{D3E84441-58CB-11D5-9BDB-00E0295CD2CC}' : IWPartArrivalProfileEntry,
	'{DEC15361-502E-11D5-9BD3-00E0295CD2CC}' : IWPartRouteStage,
	'{9E5B6328-B632-4BF4-B962-5ACFE43E3DDF}' : _IWPartEvents,
	'{248B3E7C-3C90-47EF-A6E6-9BD1437AEBE5}' : _IWLaborEvents,
	'{1070289C-8889-47D0-978C-42FA0C9BDF85}' : _IWTrackEvents,
	'{2112E57A-21CA-4E68-8694-6B5E5C9251FC}' : _IWHistogramEvents,
	'{4E8564B0-83AE-45EE-BD9D-1BDE4F0464B6}' : _IWPiechartEvents,
	'{93D5C6A9-2E53-47E5-80C0-969E4913C5F6}' : _IWTimeseriesEvents,
	'{CEC99D7A-B6A2-45A4-97E5-A3F04281EB82}' : _IWVehicleEvents,
	'{6F20C840-7DCD-4FED-9434-F6D9C47D9F94}' : _IWConveyorEvents,
	'{54E9788A-561B-47CD-89E8-70940A6BE6E3}' : _IWBufferEvents,
	'{ED13F315-BB08-49F4-A241-4FE7D898FE44}' : IWBufferType,
	'{EFA48791-AA68-48B8-A766-374C9D362C4F}' : _IWBufferTypeEvents,
	'{C355F85C-C282-428F-91EC-4497A13D8380}' : _IWSectionEvents,
	'{31A329FB-AA5D-422F-A2A8-881EA066192B}' : IWSectionType,
	'{14A9716A-FB07-4B0F-B975-19CA14F9F05D}' : _IWSectionTypeEvents,
	'{313847F9-79FA-4F91-856A-ABD968A2F5D4}' : _IWStationEvents,
	'{53CDBD79-5425-4B6E-BB04-203DB2F8155B}' : IWStationType,
	'{8B0096ED-9410-4F27-B000-2ACE40BDB5E6}' : _IWStationTypeEvents,
	'{6A224987-FC2D-4AB1-BB79-BAD5DE4175BC}' : _IWCarrierEvents,
	'{44C2F7D8-DE76-461E-A15D-FBD6D47DD017}' : IWCarrierType,
	'{8692269E-FAA2-4902-B63A-7710C7FFCF0F}' : _IWCarrierTypeEvents,
	'{13523CD8-B0AD-46D1-B2AF-F1F2152085F0}' : IWModuleType,
	'{ED5609C1-C6C9-4DA1-AD2D-30BBD10D7253}' : _IWModuleTypeEvents,
	'{E7805F03-0261-412A-9F84-2723AD292A9F}' : IWConveyorType,
	'{E2B72B3B-B5CD-4EE5-A01C-BC6C34BA58CB}' : _IWConveyorTypeEvents,
	'{A1B86D55-E79D-11D4-8556-0020AFF488A2}' : IWLaborRule,
	'{A1B86D57-E79D-11D4-8556-0020AFF488A2}' : IWLaborRules,
	'{D843A28F-8C4F-471A-9E14-3E75CD5DD37A}' : IWShiftType,
	'{7F0D0280-124B-4916-A0FD-20BA46FE272C}' : _IWShiftTypeEvents,
	'{BAE57732-DB47-460F-B339-D8686AB7F649}' : IWFunctionType,
	'{C3776C0E-DC5F-426C-86B8-D41B92307A40}' : IWAttributeType,
	'{95F31B86-2998-41E8-99DE-78C8AD9BFB19}' : _IWShiftEvents,
	'{50443F6F-692C-4F31-B5AE-939CDC74A977}' : IWNetworkType,
	'{9C405C1F-B668-46CD-9601-420DFDD10AFB}' : _IWNetworkTypeEvents,
	'{E31E5BE9-7313-459D-A73F-7C6AF9213408}' : _IWNetworkEvents,
	'{BB075195-E18A-4A35-81E4-05E94B6EFF23}' : IWPathType,
	'{B76FE3D0-3C76-48C5-ADC0-77FD55D542F1}' : _IWPathTypeEvents,
	'{A6384F15-4629-4D19-A11D-3A2470E932C3}' : _IWPathEvents,
	'{55FDA6EA-CBF6-4D1D-9CB0-BF7B82A6BC92}' : IWReportType,
	'{AC26059B-8191-428B-AAA4-161994711AE8}' : _IWReportTypeEvents,
	'{C4FF322C-3736-4D59-811E-EFE00FD7624D}' : _IWReportEvents,
	'{5AE97C60-17C4-11D5-A1B3-00E02963982C}' : IWVariableType,
	'{5AE97C62-17C4-11D5-A1B3-00E02963982C}' : _IWVariableTypeEvents,
	'{E735E961-17C8-11D5-A1B3-00E02963982C}' : _IWVariableEvents,
	'{739EEB63-2228-4456-AE9B-E7BD3EB736CF}' : IWFields,
	'{21F414EA-AF00-451A-BBF5-D53BF2A8DB7C}' : IWResponses,
	'{6AFE1260-66DF-408C-A059-0C471D6644E5}' : _IWErrorsAndWarningsEvents,
	'{5198E229-1261-49A7-B7E8-8084AB8C4F50}' : _IWInputRequestEvents,
	'{371DEEFC-FABA-43A9-B8DA-426A4B6056CC}' : _IWPipeTypeEvents,
	'{5411E9EE-6E73-4913-99DF-A6CBCC9C2A7C}' : _IWPipeEvents,
	'{893B28FB-69BC-458D-89B0-24FB9476EF96}' : _IWTankTypeEvents,
	'{D279DC2E-E5BE-484E-8FAE-476319D18269}' : _IWTankEvents,
	'{5F1FB1D2-ADE8-42F9-B817-D9B8BA2C33A4}' : _IWProcessorTypeEvents,
	'{E1F14EFF-990E-4E95-B39B-7F52A3322590}' : _IWProcessorEvents,
	'{7FD0856F-EB0D-423B-9CE5-84C4B973E63B}' : _IWPartFileTypeEvents,
	'{1DB7C441-5613-493F-8035-DC04FD9E4556}' : _IWPartFileEvents,
	'{CC381CE2-F4E3-46EE-99AE-9B9B6B16D15D}' : _IWFileTypeEvents,
	'{5E58C38B-F2A1-4B33-9169-5F22A107C928}' : _IWFileEvents,
	'{11F8B66D-0328-4FAD-8154-54AC6DBAB539}' : IWDataTableType,
	'{86E2E617-B2A1-4B82-9026-159D645DC025}' : _IWDataTableTypeEvents,
	'{18EA7261-FA3A-4804-929E-DC515094E226}' : _IWDataTableEvents,
	'{651D2988-518A-11D4-9AAF-00E0295CD2CC}' : Application,
	'{FA3D85D9-0C0B-4420-B724-0848E2588597}' : StandardApplication,
	'{074E71B1-34AD-4D47-9B9D-167E56C380AC}' : ApplicationViewer,
	'{340F5316-1C07-4BB9-8588-8AF9083B45F9}' : BPMViewer,
	'{012AE1FD-9E78-4E20-8922-2C6F51E24BFF}' : ModelEventManager,
	'{F14DAB7E-75CA-45F1-976A-0051E43B6B90}' : Model,
	'{1C98A595-B908-4D1B-9D3D-0D5BA37A1AD3}' : ModelMeasure,
	'{FE7DAABD-B1F4-4E34-A4DC-334D58DBBE22}' : ModelMeasures,
	'{7C3688CE-2F5E-435E-BEB2-5AA084EDEC6E}' : Types,
	'{90A3C7D3-EBED-44B7-9F9D-DE4E3094A286}' : Type,
	'{E252C7AF-6108-4A67-B9AB-A3DFFE45028C}' : PartType,
	'{E8307171-6464-4288-8811-77A04CA7282D}' : LaborType,
	'{CBEB96B5-10E1-4800-A763-5E417B92B34A}' : TimeseriesType,
	'{0A7C4BD3-2E16-4CEF-8D4E-FB4E0AA0F636}' : HistogramType,
	'{F3E728B4-DFB3-443C-AA01-0DE929FB3070}' : PiechartType,
	'{5A372025-E42D-4ED3-8583-E5341700F635}' : TrackType,
	'{683FB717-BD04-4F21-AB03-0E21A7C72C49}' : VehicleType,
	'{ED85E9B1-9E8C-4B13-B5F7-5071288D83FF}' : MachineType,
	'{7CC1ABA0-46BA-423A-8A30-D2F2974CEE63}' : Elements,
	'{AE9CA10B-2DCD-4C7A-A849-E0AAA8F90C71}' : Instances,
	'{2830E4FB-14FA-4958-8765-0F33560C9138}' : Element,
	'{36EBF251-2CF3-11D5-A1B4-00E02963982C}' : UserElement,
	'{36EBF252-2CF3-11D5-A1B4-00E02963982C}' : SystemElement,
	'{12E061BD-E54B-11D4-8553-0020AFF488A2}' : Machine,
	'{725808C2-8F7A-41A1-B348-12EC36BC8FCF}' : MachineInstance,
	'{4E62D659-868B-4718-84A0-245F91232CE3}' : BufferInstances,
	'{A7E6802F-5CA6-4489-9F5B-4B06FC0E85C4}' : ConveyorInstances,
	'{DC91B434-6DAC-4512-942D-8F3CDD05ACAF}' : LaborInstances,
	'{E6A2B0E2-8C62-43B0-88E1-C462E6CE584B}' : MachineInstances,
	'{6ADB5AF9-8FD6-437C-9FD9-FD39260B1A01}' : CarrierInstances,
	'{889A626B-57AE-4DBF-AA7B-6B5101807642}' : SectionInstances,
	'{FA88B3AD-568D-459E-8774-202331D9DD5A}' : StationInstances,
	'{08BF91FF-3235-4569-B6FE-952E562B235F}' : TrackInstances,
	'{CBC7B99E-B2BF-4031-B413-523570170F57}' : VehicleInstances,
	'{353A4670-5506-4942-83F0-3B60CDC128E8}' : BufferInstance,
	'{E4159C32-7F0C-41DF-AB41-8269C1AEEA05}' : ConveyorInstance,
	'{633281B9-946E-467F-BCB5-03FD7F467FB3}' : Module,
	'{445890C6-E66E-4620-8413-C613D7BD29D3}' : MeasureValue,
	'{BECF2229-7372-452D-9343-0FC2CC7586DB}' : PathMeasure,
	'{6E4938CE-EAB5-4977-BE54-350B9D31FA37}' : PathMeasures,
	'{338B12F3-452B-4C92-9BE4-D41387FD21CB}' : LaborMeasure,
	'{68B8BE1E-91A4-4DE8-BCB9-E9AB7804577A}' : LaborMeasures,
	'{39A7781C-CAB1-4D5C-B409-ACBAC218779A}' : BufferMeasure,
	'{C3C2BD9F-7169-4413-BE59-93572B2F46B2}' : BufferMeasures,
	'{4458B2E4-FDA8-4241-9882-529C40085984}' : ConveyorMeasure,
	'{A33BE52E-CD53-4DFC-B543-733FD618A7C9}' : ConveyorMeasures,
	'{CB6E9DA5-A948-4FD0-9873-1B64E06BADE1}' : MachineMeasure,
	'{4AEDE750-7BBF-4588-B547-FD7C8200B522}' : MachineMeasures,
	'{786649BA-17B5-4A15-95AD-FB2109E28BF3}' : PartMeasure,
	'{B96C1292-8AC4-4486-B26A-29D2A1F5E43C}' : PartMeasures,
	'{3B8D4948-C4B3-4754-987D-DA0814438115}' : Part,
	'{E8B55477-6F44-4C74-BB6F-383D7FCE0841}' : PartInstance,
	'{F5C3DFD0-3DAE-4043-AB52-2F9B2445711B}' : Labor,
	'{9C70AC8B-4060-4546-BA5D-8F0DCF16CFEF}' : LaborInstance,
	'{0398C500-A610-463B-91A1-F4065CFEFF84}' : Track,
	'{154A09BA-BEB3-4C2D-A140-E1851D239814}' : Piechart,
	'{4CF57EFE-8DD9-4C70-A10A-AEEF3FD68E5D}' : Histogram,
	'{AD5E9293-FD7B-4EA1-B2C8-CB27C2D1BB09}' : Timeseries,
	'{EE5EE797-CC64-48C7-83B8-BA8C8561796D}' : TrackInstance,
	'{E3D209FA-73F5-4C1C-B167-5FF6990B1944}' : Vehicle,
	'{209279F9-2A76-482E-9502-C0AAF1E0CE53}' : VehicleInstance,
	'{645C5AF8-DE5E-42B9-8CAC-EE7C52560D03}' : Conveyor,
	'{DB0E57F7-7B49-4C88-9B76-8C4D050C1DF1}' : Buffer,
	'{E31B9C55-790E-46DF-99CB-E07885AE9D02}' : BufferType,
	'{EB08BC01-B2BD-4537-902C-BFD50AD8DFD2}' : ModuleType,
	'{E35C70B8-FBAA-4C39-A845-9E45DF62BB63}' : ConveyorType,
	'{2956F9E1-CF7A-4388-8E3B-3BD46C9F5B5A}' : MachineBreakdown,
	'{514D7591-4ACC-4E7A-B9F9-5361350218D2}' : MachineBreakdowns,
	'{FA23351B-6EC3-470E-9D33-6B7466996606}' : MachineBreakdownInstance,
	'{2C948309-016C-4430-8F8E-8FD6EAB90BFD}' : MachineBreakdownInstances,
	'{37421EC3-04F7-405D-ACCD-CB2D79DF9ABA}' : ConveyorBreakdown,
	'{970B35CB-E87F-4727-B542-43BE71FFF450}' : ConveyorBreakdowns,
	'{CC93BB4E-BDC8-4A90-9F3E-7EBDF0D040DC}' : ConveyorBreakdownInstance,
	'{2E98B9F5-9406-4019-8225-26A879F6CBE2}' : ConveyorBreakdownInstances,
	'{BE06CB20-63E6-11D5-85C7-0020AFF488A2}' : StationBreakdown,
	'{BE06CB25-63E6-11D5-85C7-0020AFF488A2}' : StationBreakdowns,
	'{BE06CB21-63E6-11D5-85C7-0020AFF488A2}' : StationBreakdownInstance,
	'{BE06CB22-63E6-11D5-85C7-0020AFF488A2}' : StationBreakdownInstances,
	'{43821150-63F6-11D5-85C7-0020AFF488A2}' : SectionBreakdown,
	'{43821151-63F6-11D5-85C7-0020AFF488A2}' : SectionBreakdowns,
	'{43821152-63F6-11D5-85C7-0020AFF488A2}' : SectionBreakdownInstance,
	'{43821153-63F6-11D5-85C7-0020AFF488A2}' : SectionBreakdownInstances,
	'{94A0CFA9-E6D7-11D4-8555-0020AFF488A2}' : MachineSetup,
	'{94A0CFAB-E6D7-11D4-8555-0020AFF488A2}' : MachineSetups,
	'{A1B86D52-E79D-11D4-8556-0020AFF488A2}' : MachineCycle,
	'{A1B86D54-E79D-11D4-8556-0020AFF488A2}' : MachineCycles,
	'{A1B86D56-E79D-11D4-8556-0020AFF488A2}' : LaborRule,
	'{A1B86D58-E79D-11D4-8556-0020AFF488A2}' : LaborRules,
	'{59145A07-9E49-4EE1-B49A-5447C3B692C9}' : MachineSetupInstance,
	'{3D903BF9-0617-4B73-BD0E-0D0D10F0B914}' : MachineSetupInstances,
	'{D7462A12-315B-468E-9B24-44AB329B844D}' : MachineCycleInstance,
	'{30804F82-C8D0-498A-BB3E-76C1B1B393CC}' : MachineCycleInstances,
	'{63D176D2-0331-11D5-9B89-00E0295CD2CC}' : PartInstances,
	'{254FF920-4B28-469E-8EB6-B53CA41D5758}' : Section,
	'{87663A9D-D546-462E-94A2-C22A4BEC104A}' : SectionInstance,
	'{D12CC0A0-CA9E-40E1-9C5C-78A7D82573BC}' : SectionType,
	'{17EE021F-753A-4FE6-8F04-F957F655948F}' : Station,
	'{5C523CCE-E05E-426F-A78A-F90991EA0C0F}' : StationInstance,
	'{FAC4F46E-2F6E-4749-B377-BB31740854AD}' : StationType,
	'{145C2B6F-9CDF-426D-ABAA-E36544E0026F}' : Carrier,
	'{437FDE2F-0551-4339-B51A-59CDA7F6A287}' : CarrierInstance,
	'{82A079AD-E254-4774-98AC-CA848A60DD37}' : CarrierType,
	'{CBF157ED-DEEC-4462-9C2C-C21FA91B7260}' : Network,
	'{79828EE4-5DD9-4A41-ADC3-9E734F38796F}' : NetworkType,
	'{C8393854-3713-4403-86C3-14A22119E733}' : Shift,
	'{0621844B-FA65-4835-8FBD-86F62DDEE8E8}' : ShiftType,
	'{26A60ABA-817C-459B-BFBF-2E9F8FD16C96}' : FunctionType,
	'{8D03C4CE-F14E-4819-AA81-67B677C7E6AE}' : AttributeType,
	'{776DC152-E354-466E-A22E-F8B3BC810AA5}' : FunctionParameter,
	'{3641AADE-9279-4C7D-8D41-092AE9ACAD8F}' : FunctionParameters,
	'{6E799CC3-0423-4712-9D4F-3081FE6D91A5}' : Function,
	'{4700CB1B-4FB7-4938-BA2A-D034D88DE1CC}' : PathElementExpression,
	'{64AE4DE5-5F48-4B53-849C-4DA165E7ED42}' : PathElementExpressions,
	'{9076164B-7A90-4335-AB5F-8BCB6846564E}' : Path,
	'{0855287B-E575-4AD8-8F87-BBFAA4EFB292}' : PathType,
	'{84B06A15-3DC4-479F-9F50-28A1F635E897}' : Report,
	'{4C208E8A-EC47-42BF-A80F-4705A0825A55}' : ReportType,
	'{5F69FB11-188D-11D5-A1B3-00E02963982C}' : VariableType,
	'{5F69FB13-188D-11D5-A1B3-00E02963982C}' : Variable,
	'{D783B13A-273A-4E8A-805F-75991A508E09}' : Fields,
	'{86113396-D5B6-4284-8AED-9F647A6A0CAB}' : Responses,
	'{A8990927-8EDC-473B-BA0B-834DF5C23FBF}' : ErrorsAndWarnings,
	'{972D79E3-3EA1-4B8E-B33C-0ECA3732EA90}' : InputRequest,
	'{EB396772-21D0-11D5-8586-0020AFF488A2}' : AttributeInstance,
	'{EB396773-21D0-11D5-8586-0020AFF488A2}' : AttributeInstances,
	'{988F0373-AFE4-456C-A3F1-B57685ECBD7D}' : Sample,
	'{90E44757-6068-437E-9282-EC1F008CA370}' : Attribute,
	'{5353FA8F-7EE3-428C-ACB7-B007171BCCB5}' : NONE,
	'{36FE27BE-07BA-4904-AFB6-9DA93621E6CE}' : Ship,
	'{3805229F-FE67-48C2-AE43-F6E329766A28}' : Scrap,
	'{47D9ECBC-EA3E-41AF-80A4-4CD0185A62BD}' : World,
	'{0E61D6B4-D568-4D42-97AF-946AD57E8293}' : Assemble,
	'{96F46E30-9B89-4666-9264-B669FDA8E197}' : Route,
	'{8F1E1722-B3BC-49BE-900F-1A1015B3E19B}' : Backdrop,
	'{D3F86990-4072-11D5-A1B8-00E02963982C}' : Dimensions,
	'{D3F86991-4072-11D5-A1B8-00E02963982C}' : Instance,
	'{D3E84444-58CB-11D5-9BDB-00E0295CD2CC}' : PartArrivalProfileEntry,
	'{D3E84445-58CB-11D5-9BDB-00E0295CD2CC}' : PartArrivalProfileEntries,
	'{2F373901-5042-11D5-9BD3-00E0295CD2CC}' : PartRouteStage,
	'{2F373902-5042-11D5-9BD3-00E0295CD2CC}' : PartRouteStages,
	'{D3B026A0-50E9-11D5-A1C1-00E02963982C}' : LaborShift,
	'{D3B026A1-50E9-11D5-A1C1-00E02963982C}' : LaborShifts,
	'{87AB0720-5E69-11D5-A1C1-00E02963982C}' : ShiftPeriod,
	'{87AB0721-5E69-11D5-A1C1-00E02963982C}' : ShiftPeriods,
	'{F0F0BF92-6EF7-11D5-80F0-00E02964AB43}' : TrackWorkSearchItem,
	'{F0F0BF93-6EF7-11D5-80F0-00E02964AB43}' : TrackWorkSearchItems,
	'{1D60E254-0A19-4E2C-9D3A-F5D9B6ADFDF7}' : DrawTool,
	'{CA7D13A2-FBDA-4FCC-B552-B60468D38BD3}' : Color,
	'{59E05BC6-943D-4E23-AECE-435624AF9AC4}' : Graphics,
	'{2DE39202-734C-49B3-827F-411DCB0856FF}' : WitnessFont,
	'{C34D5CEC-372F-4362-A4E9-0EF1991752AB}' : PathData,
	'{A82FD057-3F6F-4226-92D6-86B4986DE528}' : Point,
	'{6EB0EC81-8790-42B4-BE70-E20DA6DEB0E9}' : Points,
	'{E02FA232-56F5-4402-82E0-D7CD11D86054}' : PipeInstances,
	'{C5CF2888-AEE4-4AD9-97E0-EA98A8942657}' : PipeInstance,
	'{6769DBE4-2DC3-46D8-846F-4A62A62B5B42}' : Pipe,
	'{B5B4C2B7-06B5-49A8-B5CC-A31E16620B3D}' : PipeType,
	'{CA9A3253-9C84-48A5-B1F1-C474D7FF28A9}' : TankInstances,
	'{BA36851B-F5F8-4DDE-879C-F85BAD2A8CF1}' : TankInstance,
	'{E172B608-4CAC-42E9-B756-DEEC0E285673}' : Tank,
	'{DC41C651-D074-4A96-B802-497B888E1F47}' : TankType,
	'{6F167138-34BB-4CB8-AB40-458C91C0D08D}' : ProcessorInstances,
	'{ED6EF6BA-D94F-4610-A37E-C0F7741518BD}' : ProcessorInstance,
	'{56C71F23-499F-43DF-884E-0E2E0BFAC95F}' : Processor,
	'{B6997BA0-F387-4C21-8939-FB6E4F79B8D1}' : ProcessorType,
	'{FDEE5D65-1237-4785-A2B2-F415E6EAC8A5}' : PartFile,
	'{9D440E35-55C8-4A09-849E-4E6C16D11A26}' : PartFileType,
	'{3E70BB16-0A94-4BC5-A921-2BCE98CB024D}' : File,
	'{C6097B81-5EA5-4FAB-93FE-741AB26AAE1F}' : FileType,
	'{512108B5-3FE7-453E-9169-B91CCCC8F719}' : ConveyorSensor,
	'{1F9233EA-A80D-40E7-B070-03049F936324}' : ConveyorSensors,
	'{5B98F8BF-9209-4A12-B7FC-04B043EEB3C3}' : DataTable,
	'{7DCDF7AB-9E07-4B20-A73F-A0188D6EDDF4}' : DataTableType,
	'{F0832FC5-9D60-4542-BB68-EACABBE75136}' : DataTableColumnItem,
	'{A6C95EEB-EFDD-4462-91C1-6A6EB787E94B}' : DataTableColumnItems,
	'{EBF1F7CB-5F07-4E2F-B923-DA1873E55206}' : DataTableInstance,
	'{4B219466-3B72-4A0C-BC67-A4460E22E7C2}' : DataTableInstances,
	'{BA00DD6A-4545-4AC0-87CC-375C48077E2C}' : Factors,
	'{968F15BB-1051-4D51-A001-9AB3C62127B1}' : RandomNumberUsage,
	'{04B51A36-E475-47B9-A2CC-ED44D69CBD9C}' : ReportData,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}' : 'IWApplication',
	'{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}' : 'IWModel',
	'{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}' : 'IWTypes',
	'{679E5B61-21DA-11D5-A1B3-00E02963982C}' : '_IWCollection',
	'{E2D06A1C-239C-42EC-B904-CB0735088E0E}' : 'IWType',
	'{E4B4D340-1397-4A21-9F52-BB258A913C1A}' : 'IWModule',
	'{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}' : 'IWElements',
	'{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}' : 'IWElement',
	'{10538218-737F-44BF-BBC4-7B169F983E1B}' : 'IWPartInstance',
	'{B663FFB1-235F-11D5-A1B4-00E02963982C}' : 'IWInstance',
	'{C641E7A1-817B-40FA-849E-7956F1C1A846}' : 'IWPart',
	'{DEC15362-502E-11D5-9BD3-00E0295CD2CC}' : 'IWPartRouteStages',
	'{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}' : 'IWPartArrivalProfileEntries',
	'{B9E729DD-60D2-4F45-9358-3C8047008411}' : 'IWPartMeasures',
	'{3569B25C-2E41-4F11-AB30-2D112546D800}' : 'IWPartMeasure',
	'{F357C6B3-3507-4611-96ED-3247D7C687D5}' : 'IWMeasureValue',
	'{427F8FA2-0EEE-11D5-8579-0020AFF488A2}' : 'IWAttributeInstances',
	'{427F8FA1-0EEE-11D5-8579-0020AFF488A2}' : 'IWAttributeInstance',
	'{F079D83C-D0A1-413D-9CC2-D64317021122}' : 'IWSample',
	'{30DD08CA-7835-4684-9C1B-46674D674204}' : 'IWRandomNumberUsage',
	'{27865A7B-1F7C-4449-957B-D6FDB0BD4052}' : 'IWReportData',
	'{752CA6D4-E88D-4BFF-9638-8B0334C04667}' : 'IWRandomNumberCoverageBucketsCollection',
	'{FF833377-93CB-45EB-A66D-E9C311E043C1}' : 'IWRandomNumberCoverageBuckets',
	'{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}' : 'IWNone',
	'{595FF59A-1729-4781-A427-66C61F9C6DCC}' : 'IWSystemElement',
	'{81E22460-8112-472B-9E14-96153261E6E0}' : 'IWShip',
	'{38FB81B4-8091-4A39-8041-56C31FDA7BD0}' : 'IWScrap',
	'{861CABEB-E70F-4879-AEA6-079D1B13BC1E}' : 'IWWorld',
	'{108615F0-4DBE-4D4C-826B-C606578491BA}' : 'IWAssemble',
	'{6A8123E6-FF3B-4502-AF3F-243AC818B17C}' : 'IWRoute',
	'{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}' : 'IWBackdrop',
	'{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}' : 'IWGraphics',
	'{2C138955-DAF6-456E-9F25-03730158A521}' : 'IWDrawTool',
	'{874FED95-DA11-48E4-B237-FC2CA83DE758}' : 'IWColor',
	'{F1496351-9B02-498C-9FB9-348E0B2AA565}' : 'IWFont',
	'{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}' : 'IWPathData',
	'{D1227816-BAED-4DBB-8F28-B269E166A613}' : 'IWPoints',
	'{C6034440-1A59-48D8-B463-43918B37FD28}' : 'IWPoint',
	'{D8396D00-CC33-47E7-A917-1527DF798EC5}' : 'IWModelEventManager',
	'{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}' : 'IWDirectories',
	'{B3951062-2E8D-407D-ABBD-D57FB4FAE705}' : 'IWModelMeasures',
	'{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}' : 'IWModelMeasure',
	'{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}' : 'IWFactors',
	'{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}' : 'IWErrorsAndWarnings',
	'{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}' : 'IWInputRequest',
	'{7FE9DF3A-DF37-43EB-AF81-2EB034A178A1}' : 'IWApplicationViewer',
	'{C7DB6FD3-764B-4E78-AFF6-A84F50C7A642}' : 'IWBPMViewer',
	'{BDDBB5BA-2342-4163-9682-BD86F8AF4C84}' : 'IWStandardApplication',
	'{C24094DC-99F0-4AD7-9357-9468EEB19259}' : 'IWUserElement',
	'{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}' : 'IWBufferInstance',
	'{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}' : 'IWBuffer',
	'{5A3597E0-2042-4969-919F-484397BF413B}' : 'IWBufferInstances',
	'{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}' : 'IWBufferMeasures',
	'{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}' : 'IWBufferMeasure',
	'{63D176D1-0331-11D5-9B89-00E0295CD2CC}' : 'IWPartInstances',
	'{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}' : 'IWConveyorInstance',
	'{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}' : 'IWConveyor',
	'{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}' : 'IWConveyorInstances',
	'{375E2CD5-8A41-45AF-9469-38744989269C}' : 'IWConveyorBreakdowns',
	'{330E3D97-24CF-4644-9000-DEEA6EB2306B}' : 'IWConveyorBreakdown',
	'{54486179-8C34-4101-831E-23A6D9FE10F6}' : 'IWConveyorSensors',
	'{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}' : 'IWConveyorSensor',
	'{1E6B62FD-4355-439E-8FA7-A54611B55B11}' : 'IWConveyorMeasures',
	'{75DE9907-45CA-4B2B-B584-7851F771FF1E}' : 'IWConveyorMeasure',
	'{8278E5B4-CAA4-42E8-AABF-09E7A7535725}' : 'IWConveyorBreakdownInstances',
	'{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}' : 'IWDataTableInstance',
	'{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}' : 'IWDataTable',
	'{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}' : 'IWDataTableInstances',
	'{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}' : 'IWDataTableColumnItems',
	'{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}' : 'IWDataTableColumnItem',
	'{46FB221B-D834-4B5E-B1EC-582524196017}' : 'IWLaborInstance',
	'{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}' : 'IWLabor',
	'{39150113-B27B-43AA-B116-5EFCF532B027}' : 'IWLaborInstances',
	'{402F5411-4F7E-11D5-A1C1-00E02963982C}' : 'IWLaborShifts',
	'{402F5410-4F7E-11D5-A1C1-00E02963982C}' : 'IWLaborShift',
	'{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}' : 'IWLaborMeasures',
	'{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}' : 'IWLaborMeasure',
	'{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}' : 'IWMachineInstance',
	'{35B1CE41-5962-4071-8824-4D43DA7C2DA9}' : 'IWMachineCycleInstances',
	'{897905FC-B806-4835-8AF8-088E6405AD70}' : 'IWMachineSetupInstances',
	'{1CD3A435-8D00-4CB8-A630-F666460D0372}' : 'IWMachineBreakdownInstances',
	'{12E061BC-E54B-11D4-8553-0020AFF488A2}' : 'IWMachine',
	'{8D12737F-BF42-4827-B95C-D891817FAB82}' : 'IWMachineBreakdowns',
	'{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}' : 'IWMachineBreakdown',
	'{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}' : 'IWMachineSetups',
	'{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}' : 'IWMachineSetup',
	'{A1B86D53-E79D-11D4-8556-0020AFF488A2}' : 'IWMachineCycles',
	'{A1B86D51-E79D-11D4-8556-0020AFF488A2}' : 'IWMachineCycle',
	'{921B4444-BEC7-4203-A45C-724F25DA67BB}' : 'IWMachineInstances',
	'{05F69682-BC4D-4B74-A78C-04E88D74CB06}' : 'IWMachineMeasures',
	'{63070342-EC3E-456F-90DA-B849F98EB873}' : 'IWMachineMeasure',
	'{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}' : 'IWCarrierInstance',
	'{1F803804-DB54-4D3E-A508-AFFC15277B77}' : 'IWCarrier',
	'{00504947-3FAA-4A8F-BF64-4EA4E3416B69}' : 'IWNetwork',
	'{8B98F244-7A42-4233-9432-BABB237EE777}' : 'IWCarrierInstances',
	'{865318D8-96F3-40F0-866A-84A937964A79}' : 'IWSectionInstance',
	'{1AF98A1D-C6E6-4681-88CC-8DB41A320460}' : 'IWSection',
	'{43821155-63F6-11D5-85C7-0020AFF488A2}' : 'IWSectionBreakdowns',
	'{43821154-63F6-11D5-85C7-0020AFF488A2}' : 'IWSectionBreakdown',
	'{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}' : 'IWSectionInstances',
	'{43821157-63F6-11D5-85C7-0020AFF488A2}' : 'IWSectionBreakdownInstances',
	'{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}' : 'IWStationInstance',
	'{517122AB-6C4C-4996-975C-207AABEF7353}' : 'IWStation',
	'{A5729D61-63D2-11D5-85C7-0020AFF488A2}' : 'IWStationBreakdowns',
	'{A5729D60-63D2-11D5-85C7-0020AFF488A2}' : 'IWStationBreakdown',
	'{503951C9-860E-4251-A8C8-0E26E9046231}' : 'IWStationInstances',
	'{A5729D63-63D2-11D5-85C7-0020AFF488A2}' : 'IWStationBreakdownInstances',
	'{1BE4C352-3E87-4432-8D0B-CC505F425D4D}' : 'IWTrackInstance',
	'{B4FD8014-1552-475F-A679-F2B15A8147A8}' : 'IWTrack',
	'{20892432-3AD4-4D37-807F-5C035DF0638B}' : 'IWTrackInstances',
	'{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}' : 'IWTrackWorkSearchItems',
	'{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}' : 'IWTrackWorkSearchItem',
	'{33DC7FEE-B353-483D-8F54-E63B63C41B49}' : 'IWVehicleInstances',
	'{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}' : 'IWVehicleInstance',
	'{A64A59DA-690E-428D-894F-99F67F4956CB}' : 'IWVehicle',
	'{83073E66-7AF6-46C0-89D2-F33E7C972377}' : 'IWInstances',
	'{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}' : 'IWShift',
	'{520FA171-59C5-11D5-A1C1-00E02963982C}' : 'IWShiftPeriods',
	'{520FA170-59C5-11D5-A1C1-00E02963982C}' : 'IWShiftPeriod',
	'{FDB0A591-25D9-44EC-AB08-783742063AA7}' : 'IWPath',
	'{AB588585-190B-4830-BB71-A88D92BA8451}' : 'IWPathElementExpressions',
	'{288D0178-6C4B-4ACF-A344-9553E6714BC5}' : 'IWPathElementExpression',
	'{595E1B97-E9E7-465E-AF63-A243735FB187}' : 'IWPathMeasures',
	'{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}' : 'IWPathMeasure',
	'{55A4116E-D4E0-4547-8349-AD733DC01C16}' : 'IWReport',
	'{E735E960-17C8-11D5-A1B3-00E02963982C}' : 'IWVariable',
	'{6C98C5C0-21DA-11D5-A1B3-00E02963982C}' : 'IWDimensions',
	'{FC5BF548-99F8-4907-925F-82E0B2FB7835}' : 'IWFunction',
	'{8693669F-C4C2-4318-AB34-8FF2860AB73B}' : 'IWFunctionParameters',
	'{E1347784-EA6C-4A12-813A-F0FD60924578}' : 'IWFunctionParameter',
	'{56EF0AE9-1E7D-4892-9C56-837855B9776E}' : 'IWAttribute',
	'{D4F90213-4DD0-4003-99AA-8DE53FB5E643}' : 'IWMachineBreakdownInstance',
	'{AAB2327A-85B4-41B8-A535-ECFB693A16E7}' : 'IWConveyorBreakdownInstance',
	'{A5729D62-63D2-11D5-85C7-0020AFF488A2}' : 'IWStationBreakdownInstance',
	'{43821156-63F6-11D5-85C7-0020AFF488A2}' : 'IWSectionBreakdownInstance',
	'{901A46A2-B4D6-473D-9B89-A9DABAB418E7}' : 'IWMachineCycleInstance',
	'{B66E325C-F3FA-40FE-A3D1-32570E96C8F7}' : 'IWMachineSetupInstance',
	'{71E7EE98-8043-47F9-9549-0813E776E594}' : 'IWPipeType',
	'{EBCA5DAE-76F3-4872-8247-EDD3CED57353}' : 'IWPipe',
	'{60324619-F3C0-4114-9CA4-4DE9533A0849}' : 'IWPipeInstances',
	'{E16C5044-7333-467A-98F1-579B48C09D3A}' : 'IWPipeInstance',
	'{E0B23F84-C932-4AE3-B38D-52D982886FCD}' : 'IWPipeBreakdowns',
	'{5229A31A-D096-4389-8540-65F371CF0D97}' : 'IWTankType',
	'{8D4C9A2A-5367-4819-9911-DD9CA73006F7}' : 'IWTank',
	'{621E28F2-E65D-456E-8229-D1A8BE6EB63D}' : 'IWTankInstances',
	'{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}' : 'IWTankInstance',
	'{20F7F5D9-FB97-4B74-8AA2-AE2AC48E47ED}' : 'IWProcessorType',
	'{3E62686A-D9BF-464A-B478-DE8559513141}' : 'IWProcessor',
	'{4190AF59-9851-4ADB-8902-A809824D4621}' : 'IWProcessorInstances',
	'{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}' : 'IWProcessorInstance',
	'{2B044458-8E03-4C1A-AFE5-362A39E4500C}' : 'IWProcessorBreakdowns',
	'{134FB1F0-5BF0-4678-B815-4042AF976628}' : 'IWPartFileType',
	'{4C079D1F-F67E-41E5-B770-116E257E6C7C}' : 'IWPartFile',
	'{92B89E14-6BAA-4D23-8DD5-CB15C77E2D3E}' : 'IWFileType',
	'{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}' : 'IWFile',
	'{58D5DB46-9295-452C-9FDB-1795E61A00A0}' : 'IWActivator',
	'{BFD54915-A1B1-46C6-87F5-B8B6C567615B}' : 'IWTimeseries',
	'{8CFB8503-E585-431A-9863-E1A3D6B9F34E}' : 'IWHistogram',
	'{D160D6FC-8110-41E0-84E2-B1754FAF4596}' : 'IWPiechart',
	'{6E875BB8-B0E1-4077-B06D-86824D1D29C5}' : 'IWSecurity',
	'{92D0A727-28A1-4682-A1B2-90BFF5677814}' : 'IWRemoteControl',
	'{0DADE019-6363-4E84-AD1F-FCE7F272F774}' : 'IWitnessExtensionModule',
	'{FA29B843-D512-4287-BABD-71A4484B4ABC}' : 'IWUserProperties',
	'{E2C6802B-8E63-4E50-AB64-B871071A779B}' : 'IWPartType',
	'{32F8A928-07DF-41D1-B490-C3282C7DB4D6}' : 'IWLaborType',
	'{727F8035-F180-4863-9BAC-561F1D579AD3}' : 'IWTimeseriesType',
	'{93DF3BB1-0CD3-45F9-B586-197112B69107}' : 'IWPiechartType',
	'{CD6C32EB-B24A-4ED0-89FC-AB39EE326295}' : 'IWHistogramType',
	'{7BAF40F7-A453-4B2C-9BC9-3A29F96F0BC0}' : 'IWTrackType',
	'{C5F7EF56-FBC4-45E6-AA34-A6A38547535C}' : 'IWVehicleType',
	'{E36854D0-A37A-48AA-B2BE-A5E475428EE4}' : 'IWMachineType',
	'{D3E84441-58CB-11D5-9BDB-00E0295CD2CC}' : 'IWPartArrivalProfileEntry',
	'{DEC15361-502E-11D5-9BD3-00E0295CD2CC}' : 'IWPartRouteStage',
	'{ED13F315-BB08-49F4-A241-4FE7D898FE44}' : 'IWBufferType',
	'{31A329FB-AA5D-422F-A2A8-881EA066192B}' : 'IWSectionType',
	'{53CDBD79-5425-4B6E-BB04-203DB2F8155B}' : 'IWStationType',
	'{44C2F7D8-DE76-461E-A15D-FBD6D47DD017}' : 'IWCarrierType',
	'{13523CD8-B0AD-46D1-B2AF-F1F2152085F0}' : 'IWModuleType',
	'{E7805F03-0261-412A-9F84-2723AD292A9F}' : 'IWConveyorType',
	'{A1B86D55-E79D-11D4-8556-0020AFF488A2}' : 'IWLaborRule',
	'{A1B86D57-E79D-11D4-8556-0020AFF488A2}' : 'IWLaborRules',
	'{D843A28F-8C4F-471A-9E14-3E75CD5DD37A}' : 'IWShiftType',
	'{BAE57732-DB47-460F-B339-D8686AB7F649}' : 'IWFunctionType',
	'{C3776C0E-DC5F-426C-86B8-D41B92307A40}' : 'IWAttributeType',
	'{50443F6F-692C-4F31-B5AE-939CDC74A977}' : 'IWNetworkType',
	'{BB075195-E18A-4A35-81E4-05E94B6EFF23}' : 'IWPathType',
	'{55FDA6EA-CBF6-4D1D-9CB0-BF7B82A6BC92}' : 'IWReportType',
	'{5AE97C60-17C4-11D5-A1B3-00E02963982C}' : 'IWVariableType',
	'{739EEB63-2228-4456-AE9B-E7BD3EB736CF}' : 'IWFields',
	'{21F414EA-AF00-451A-BBF5-D53BF2A8DB7C}' : 'IWResponses',
	'{11F8B66D-0328-4FAD-8154-54AC6DBAB539}' : 'IWDataTableType',
}


NamesToIIDMap = {
	'IWApplication' : '{36559D86-640F-47CB-B5F3-F12E2E7A0D3B}',
	'IWModel' : '{DD125CA1-9FB5-45D4-83A3-BAB1EF580F5E}',
	'IWTypes' : '{C4C5BB33-6AD5-4EB5-99EC-089CB1615668}',
	'_IWCollection' : '{679E5B61-21DA-11D5-A1B3-00E02963982C}',
	'IWType' : '{E2D06A1C-239C-42EC-B904-CB0735088E0E}',
	'IWModule' : '{E4B4D340-1397-4A21-9F52-BB258A913C1A}',
	'IWElements' : '{40F8CB4F-C2A0-4171-ACB0-5949ACA934D6}',
	'IWElement' : '{55D69C0C-D9C1-4A6F-8B5D-7A4AA9D6B359}',
	'IWPartInstance' : '{10538218-737F-44BF-BBC4-7B169F983E1B}',
	'IWInstance' : '{B663FFB1-235F-11D5-A1B4-00E02963982C}',
	'IWPart' : '{C641E7A1-817B-40FA-849E-7956F1C1A846}',
	'IWPartRouteStages' : '{DEC15362-502E-11D5-9BD3-00E0295CD2CC}',
	'IWPartArrivalProfileEntries' : '{D3E84442-58CB-11D5-9BDB-00E0295CD2CC}',
	'IWPartMeasures' : '{B9E729DD-60D2-4F45-9358-3C8047008411}',
	'IWPartMeasure' : '{3569B25C-2E41-4F11-AB30-2D112546D800}',
	'IWMeasureValue' : '{F357C6B3-3507-4611-96ED-3247D7C687D5}',
	'IWAttributeInstances' : '{427F8FA2-0EEE-11D5-8579-0020AFF488A2}',
	'IWAttributeInstance' : '{427F8FA1-0EEE-11D5-8579-0020AFF488A2}',
	'IWSample' : '{F079D83C-D0A1-413D-9CC2-D64317021122}',
	'IWRandomNumberUsage' : '{30DD08CA-7835-4684-9C1B-46674D674204}',
	'IWReportData' : '{27865A7B-1F7C-4449-957B-D6FDB0BD4052}',
	'IWRandomNumberCoverageBucketsCollection' : '{752CA6D4-E88D-4BFF-9638-8B0334C04667}',
	'IWRandomNumberCoverageBuckets' : '{FF833377-93CB-45EB-A66D-E9C311E043C1}',
	'IWNone' : '{EA4B81B7-F6A4-4F81-9C26-E6865BA7CE5B}',
	'IWSystemElement' : '{595FF59A-1729-4781-A427-66C61F9C6DCC}',
	'IWShip' : '{81E22460-8112-472B-9E14-96153261E6E0}',
	'IWScrap' : '{38FB81B4-8091-4A39-8041-56C31FDA7BD0}',
	'IWWorld' : '{861CABEB-E70F-4879-AEA6-079D1B13BC1E}',
	'IWAssemble' : '{108615F0-4DBE-4D4C-826B-C606578491BA}',
	'IWRoute' : '{6A8123E6-FF3B-4502-AF3F-243AC818B17C}',
	'IWBackdrop' : '{D299DDE7-CCD3-47FE-B2BA-3095EB2CEFEC}',
	'IWGraphics' : '{E4216BCC-AE9D-45A0-88F1-3F822F0B9AD9}',
	'IWDrawTool' : '{2C138955-DAF6-456E-9F25-03730158A521}',
	'IWColor' : '{874FED95-DA11-48E4-B237-FC2CA83DE758}',
	'IWFont' : '{F1496351-9B02-498C-9FB9-348E0B2AA565}',
	'IWPathData' : '{4F6E1B7C-68CA-4A3E-8E3F-1BFF1F4E0272}',
	'IWPoints' : '{D1227816-BAED-4DBB-8F28-B269E166A613}',
	'IWPoint' : '{C6034440-1A59-48D8-B463-43918B37FD28}',
	'IWModelEventManager' : '{D8396D00-CC33-47E7-A917-1527DF798EC5}',
	'IWDirectories' : '{E94F2DF9-9896-4BA5-9A30-CB6B666E7844}',
	'IWModelMeasures' : '{B3951062-2E8D-407D-ABBD-D57FB4FAE705}',
	'IWModelMeasure' : '{EB1DFE00-5DA3-4075-BE07-5F54E95523BB}',
	'IWFactors' : '{59CA8029-2DE0-4F5B-A6B0-7B2D82C2BD24}',
	'IWErrorsAndWarnings' : '{AF73827C-0ED4-41CB-8319-9C43CDA86BF0}',
	'IWInputRequest' : '{6FD360BA-A1CD-45A0-B49C-FF7EC46C9241}',
	'IWApplicationViewer' : '{7FE9DF3A-DF37-43EB-AF81-2EB034A178A1}',
	'IWBPMViewer' : '{C7DB6FD3-764B-4E78-AFF6-A84F50C7A642}',
	'IWStandardApplication' : '{BDDBB5BA-2342-4163-9682-BD86F8AF4C84}',
	'IWUserElement' : '{C24094DC-99F0-4AD7-9357-9468EEB19259}',
	'IWBufferInstance' : '{21336BF5-C186-4E21-8CDD-4DDAA4B405AA}',
	'IWBuffer' : '{7AE8CDC5-4DF8-4BB9-A217-2807DA5EDC59}',
	'IWBufferInstances' : '{5A3597E0-2042-4969-919F-484397BF413B}',
	'IWBufferMeasures' : '{96642DE6-7D66-4EB3-AD99-AF25F4A3B40C}',
	'IWBufferMeasure' : '{605E89B2-1606-4FE2-BD66-97B7CC4AD3CE}',
	'IWPartInstances' : '{63D176D1-0331-11D5-9B89-00E0295CD2CC}',
	'IWConveyorInstance' : '{0F8265CB-B7FD-4EF4-B651-53FB382D64D8}',
	'IWConveyor' : '{A0176BA1-99B8-4D6B-A9F5-6614B9111CCA}',
	'IWConveyorInstances' : '{79D4A4FE-2DFB-4690-B49F-69CEFE21AC3D}',
	'IWConveyorBreakdowns' : '{375E2CD5-8A41-45AF-9469-38744989269C}',
	'IWConveyorBreakdown' : '{330E3D97-24CF-4644-9000-DEEA6EB2306B}',
	'IWConveyorSensors' : '{54486179-8C34-4101-831E-23A6D9FE10F6}',
	'IWConveyorSensor' : '{F5C23FA3-713E-4998-82A6-8CD4C4F6698B}',
	'IWConveyorMeasures' : '{1E6B62FD-4355-439E-8FA7-A54611B55B11}',
	'IWConveyorMeasure' : '{75DE9907-45CA-4B2B-B584-7851F771FF1E}',
	'IWConveyorBreakdownInstances' : '{8278E5B4-CAA4-42E8-AABF-09E7A7535725}',
	'IWDataTableInstance' : '{EFFAF0A2-2692-498B-9F4E-B2C3598EE263}',
	'IWDataTable' : '{203CEEF7-528F-49E4-B5C4-A0A1538D2F50}',
	'IWDataTableInstances' : '{6A7C0D7E-5A09-428B-8446-CA6EEF0B499B}',
	'IWDataTableColumnItems' : '{4ECDF8C2-215F-4B71-BE5B-B1A3A4561B4F}',
	'IWDataTableColumnItem' : '{92B68BB0-DD6B-4409-A5D9-45AB28527B0B}',
	'IWLaborInstance' : '{46FB221B-D834-4B5E-B1EC-582524196017}',
	'IWLabor' : '{2ED2C3F1-C331-4E6A-AB91-3267FC4FAC42}',
	'IWLaborInstances' : '{39150113-B27B-43AA-B116-5EFCF532B027}',
	'IWLaborShifts' : '{402F5411-4F7E-11D5-A1C1-00E02963982C}',
	'IWLaborShift' : '{402F5410-4F7E-11D5-A1C1-00E02963982C}',
	'IWLaborMeasures' : '{72D9FFC6-205E-475E-BF3E-D8BD2BC98D95}',
	'IWLaborMeasure' : '{8ED89E5E-32A4-4494-8BDC-0D29E4BB5597}',
	'IWMachineInstance' : '{25995FAD-6F47-4F24-9B62-E1597C9A6D6E}',
	'IWMachineCycleInstances' : '{35B1CE41-5962-4071-8824-4D43DA7C2DA9}',
	'IWMachineSetupInstances' : '{897905FC-B806-4835-8AF8-088E6405AD70}',
	'IWMachineBreakdownInstances' : '{1CD3A435-8D00-4CB8-A630-F666460D0372}',
	'IWMachine' : '{12E061BC-E54B-11D4-8553-0020AFF488A2}',
	'IWMachineBreakdowns' : '{8D12737F-BF42-4827-B95C-D891817FAB82}',
	'IWMachineBreakdown' : '{FD713D9E-45CA-4BFF-8D20-27A232DEF22F}',
	'IWMachineSetups' : '{94A0CFAA-E6D7-11D4-8555-0020AFF488A2}',
	'IWMachineSetup' : '{94A0CFA8-E6D7-11D4-8555-0020AFF488A2}',
	'IWMachineCycles' : '{A1B86D53-E79D-11D4-8556-0020AFF488A2}',
	'IWMachineCycle' : '{A1B86D51-E79D-11D4-8556-0020AFF488A2}',
	'IWMachineInstances' : '{921B4444-BEC7-4203-A45C-724F25DA67BB}',
	'IWMachineMeasures' : '{05F69682-BC4D-4B74-A78C-04E88D74CB06}',
	'IWMachineMeasure' : '{63070342-EC3E-456F-90DA-B849F98EB873}',
	'IWCarrierInstance' : '{CE8AD434-3BDA-41AA-A5C1-ACADACB93847}',
	'IWCarrier' : '{1F803804-DB54-4D3E-A508-AFFC15277B77}',
	'IWNetwork' : '{00504947-3FAA-4A8F-BF64-4EA4E3416B69}',
	'IWCarrierInstances' : '{8B98F244-7A42-4233-9432-BABB237EE777}',
	'IWSectionInstance' : '{865318D8-96F3-40F0-866A-84A937964A79}',
	'IWSection' : '{1AF98A1D-C6E6-4681-88CC-8DB41A320460}',
	'IWSectionBreakdowns' : '{43821155-63F6-11D5-85C7-0020AFF488A2}',
	'IWSectionBreakdown' : '{43821154-63F6-11D5-85C7-0020AFF488A2}',
	'IWSectionInstances' : '{42A38BD2-7A6A-4ABC-89F8-C0E2B055954B}',
	'IWSectionBreakdownInstances' : '{43821157-63F6-11D5-85C7-0020AFF488A2}',
	'IWStationInstance' : '{CFAFE14C-F651-4F83-864E-6EA0A91A6AB4}',
	'IWStation' : '{517122AB-6C4C-4996-975C-207AABEF7353}',
	'IWStationBreakdowns' : '{A5729D61-63D2-11D5-85C7-0020AFF488A2}',
	'IWStationBreakdown' : '{A5729D60-63D2-11D5-85C7-0020AFF488A2}',
	'IWStationInstances' : '{503951C9-860E-4251-A8C8-0E26E9046231}',
	'IWStationBreakdownInstances' : '{A5729D63-63D2-11D5-85C7-0020AFF488A2}',
	'IWTrackInstance' : '{1BE4C352-3E87-4432-8D0B-CC505F425D4D}',
	'IWTrack' : '{B4FD8014-1552-475F-A679-F2B15A8147A8}',
	'IWTrackInstances' : '{20892432-3AD4-4D37-807F-5C035DF0638B}',
	'IWTrackWorkSearchItems' : '{F0F0BF96-6EF7-11D5-80F0-00E02964AB43}',
	'IWTrackWorkSearchItem' : '{F0F0BF94-6EF7-11D5-80F0-00E02964AB43}',
	'IWVehicleInstances' : '{33DC7FEE-B353-483D-8F54-E63B63C41B49}',
	'IWVehicleInstance' : '{CCE095D1-1FDB-447E-9A8E-7753F8ED2073}',
	'IWVehicle' : '{A64A59DA-690E-428D-894F-99F67F4956CB}',
	'IWInstances' : '{83073E66-7AF6-46C0-89D2-F33E7C972377}',
	'IWShift' : '{66E8C404-910F-4DE1-A13E-DED65DEFE6AA}',
	'IWShiftPeriods' : '{520FA171-59C5-11D5-A1C1-00E02963982C}',
	'IWShiftPeriod' : '{520FA170-59C5-11D5-A1C1-00E02963982C}',
	'IWPath' : '{FDB0A591-25D9-44EC-AB08-783742063AA7}',
	'IWPathElementExpressions' : '{AB588585-190B-4830-BB71-A88D92BA8451}',
	'IWPathElementExpression' : '{288D0178-6C4B-4ACF-A344-9553E6714BC5}',
	'IWPathMeasures' : '{595E1B97-E9E7-465E-AF63-A243735FB187}',
	'IWPathMeasure' : '{0754BD4A-3EF4-4F8A-8DB1-12063E268AF0}',
	'IWReport' : '{55A4116E-D4E0-4547-8349-AD733DC01C16}',
	'IWVariable' : '{E735E960-17C8-11D5-A1B3-00E02963982C}',
	'IWDimensions' : '{6C98C5C0-21DA-11D5-A1B3-00E02963982C}',
	'IWFunction' : '{FC5BF548-99F8-4907-925F-82E0B2FB7835}',
	'IWFunctionParameters' : '{8693669F-C4C2-4318-AB34-8FF2860AB73B}',
	'IWFunctionParameter' : '{E1347784-EA6C-4A12-813A-F0FD60924578}',
	'IWAttribute' : '{56EF0AE9-1E7D-4892-9C56-837855B9776E}',
	'IWMachineBreakdownInstance' : '{D4F90213-4DD0-4003-99AA-8DE53FB5E643}',
	'IWConveyorBreakdownInstance' : '{AAB2327A-85B4-41B8-A535-ECFB693A16E7}',
	'IWStationBreakdownInstance' : '{A5729D62-63D2-11D5-85C7-0020AFF488A2}',
	'IWSectionBreakdownInstance' : '{43821156-63F6-11D5-85C7-0020AFF488A2}',
	'IWMachineCycleInstance' : '{901A46A2-B4D6-473D-9B89-A9DABAB418E7}',
	'IWMachineSetupInstance' : '{B66E325C-F3FA-40FE-A3D1-32570E96C8F7}',
	'IWPipeType' : '{71E7EE98-8043-47F9-9549-0813E776E594}',
	'IWPipe' : '{EBCA5DAE-76F3-4872-8247-EDD3CED57353}',
	'IWPipeInstances' : '{60324619-F3C0-4114-9CA4-4DE9533A0849}',
	'IWPipeInstance' : '{E16C5044-7333-467A-98F1-579B48C09D3A}',
	'IWPipeBreakdowns' : '{E0B23F84-C932-4AE3-B38D-52D982886FCD}',
	'IWTankType' : '{5229A31A-D096-4389-8540-65F371CF0D97}',
	'IWTank' : '{8D4C9A2A-5367-4819-9911-DD9CA73006F7}',
	'IWTankInstances' : '{621E28F2-E65D-456E-8229-D1A8BE6EB63D}',
	'IWTankInstance' : '{0FD2499D-6BF9-489E-8B5B-3B8950FCE2FA}',
	'IWProcessorType' : '{20F7F5D9-FB97-4B74-8AA2-AE2AC48E47ED}',
	'IWProcessor' : '{3E62686A-D9BF-464A-B478-DE8559513141}',
	'IWProcessorInstances' : '{4190AF59-9851-4ADB-8902-A809824D4621}',
	'IWProcessorInstance' : '{C0D12CC3-6F14-4FE4-90D5-1C5E953E5AF6}',
	'IWProcessorBreakdowns' : '{2B044458-8E03-4C1A-AFE5-362A39E4500C}',
	'IWPartFileType' : '{134FB1F0-5BF0-4678-B815-4042AF976628}',
	'IWPartFile' : '{4C079D1F-F67E-41E5-B770-116E257E6C7C}',
	'IWFileType' : '{92B89E14-6BAA-4D23-8DD5-CB15C77E2D3E}',
	'IWFile' : '{176CE2CD-AD99-4228-A9B7-A14BBD7D0788}',
	'IWActivator' : '{58D5DB46-9295-452C-9FDB-1795E61A00A0}',
	'IWTimeseries' : '{BFD54915-A1B1-46C6-87F5-B8B6C567615B}',
	'IWHistogram' : '{8CFB8503-E585-431A-9863-E1A3D6B9F34E}',
	'IWPiechart' : '{D160D6FC-8110-41E0-84E2-B1754FAF4596}',
	'IWSecurity' : '{6E875BB8-B0E1-4077-B06D-86824D1D29C5}',
	'IWRemoteControl' : '{92D0A727-28A1-4682-A1B2-90BFF5677814}',
	'_IWApplicationEvents' : '{82355849-4B8B-4B9C-A976-22ED38EACC8B}',
	'_IWApplicationViewerEvents' : '{9E52085E-C12A-4AF5-8B2C-E8BDBC253A87}',
	'_IWBPMViewerEvents' : '{1C0AC210-AAAB-4742-AAAF-560EB4672B59}',
	'_IWStandardApplicationEvents' : '{DE1AD8A2-DFDE-423A-8F5F-24B2CCE23961}',
	'IWUserProperties' : '{FA29B843-D512-4287-BABD-71A4484B4ABC}',
	'_IWModelEvents' : '{E39933F0-9C47-4BB6-A18C-1B60B1A7C5C1}',
	'_IWModuleEvents' : '{1AA3916B-AE9E-460F-94D6-7D1884D98193}',
	'IWPartType' : '{E2C6802B-8E63-4E50-AB64-B871071A779B}',
	'_IWPartTypeEvents' : '{EB466F0D-214B-422A-942A-5BD1AA9F71FD}',
	'IWLaborType' : '{32F8A928-07DF-41D1-B490-C3282C7DB4D6}',
	'_IWLaborTypeEvents' : '{8D3092D9-28BF-4949-B3D6-9A557A70E65C}',
	'IWTimeseriesType' : '{727F8035-F180-4863-9BAC-561F1D579AD3}',
	'_IWTimeseriesTypeEvents' : '{CC38E78A-2250-4BA5-A50C-A2523E8B66B5}',
	'IWPiechartType' : '{93DF3BB1-0CD3-45F9-B586-197112B69107}',
	'_IWPiechartTypeEvents' : '{8D64F32A-FF93-4B89-AA4B-D505D9E66C0A}',
	'IWHistogramType' : '{CD6C32EB-B24A-4ED0-89FC-AB39EE326295}',
	'_IWHistogramTypeEvents' : '{057615BD-6B39-4A09-9B1D-0785FC02A6CE}',
	'IWTrackType' : '{7BAF40F7-A453-4B2C-9BC9-3A29F96F0BC0}',
	'_IWTrackTypeEvents' : '{9959AEBF-296E-48D7-8BAC-DD05656AAB16}',
	'IWVehicleType' : '{C5F7EF56-FBC4-45E6-AA34-A6A38547535C}',
	'_IWVehicleTypeEvents' : '{EACC1BC1-9308-40A7-9010-5A1D770AB02E}',
	'IWMachineType' : '{E36854D0-A37A-48AA-B2BE-A5E475428EE4}',
	'_IWMachineTypeEvents' : '{EFEEB503-BA9A-49A9-8142-424C633327B5}',
	'_IWElementsEvents' : '{B2718466-9171-4B74-B6A4-DB7A3137DC31}',
	'_IWInstanceEvents' : '{B663FFB2-235F-11D5-A1B4-00E02963982C}',
	'_IWMachineEvents' : '{12E061BE-E54B-11D4-8553-0020AFF488A2}',
	'IWPartArrivalProfileEntry' : '{D3E84441-58CB-11D5-9BDB-00E0295CD2CC}',
	'IWPartRouteStage' : '{DEC15361-502E-11D5-9BD3-00E0295CD2CC}',
	'_IWPartEvents' : '{9E5B6328-B632-4BF4-B962-5ACFE43E3DDF}',
	'_IWLaborEvents' : '{248B3E7C-3C90-47EF-A6E6-9BD1437AEBE5}',
	'_IWTrackEvents' : '{1070289C-8889-47D0-978C-42FA0C9BDF85}',
	'_IWHistogramEvents' : '{2112E57A-21CA-4E68-8694-6B5E5C9251FC}',
	'_IWPiechartEvents' : '{4E8564B0-83AE-45EE-BD9D-1BDE4F0464B6}',
	'_IWTimeseriesEvents' : '{93D5C6A9-2E53-47E5-80C0-969E4913C5F6}',
	'_IWVehicleEvents' : '{CEC99D7A-B6A2-45A4-97E5-A3F04281EB82}',
	'_IWConveyorEvents' : '{6F20C840-7DCD-4FED-9434-F6D9C47D9F94}',
	'_IWBufferEvents' : '{54E9788A-561B-47CD-89E8-70940A6BE6E3}',
	'IWBufferType' : '{ED13F315-BB08-49F4-A241-4FE7D898FE44}',
	'_IWBufferTypeEvents' : '{EFA48791-AA68-48B8-A766-374C9D362C4F}',
	'_IWSectionEvents' : '{C355F85C-C282-428F-91EC-4497A13D8380}',
	'IWSectionType' : '{31A329FB-AA5D-422F-A2A8-881EA066192B}',
	'_IWSectionTypeEvents' : '{14A9716A-FB07-4B0F-B975-19CA14F9F05D}',
	'_IWStationEvents' : '{313847F9-79FA-4F91-856A-ABD968A2F5D4}',
	'IWStationType' : '{53CDBD79-5425-4B6E-BB04-203DB2F8155B}',
	'_IWStationTypeEvents' : '{8B0096ED-9410-4F27-B000-2ACE40BDB5E6}',
	'_IWCarrierEvents' : '{6A224987-FC2D-4AB1-BB79-BAD5DE4175BC}',
	'IWCarrierType' : '{44C2F7D8-DE76-461E-A15D-FBD6D47DD017}',
	'_IWCarrierTypeEvents' : '{8692269E-FAA2-4902-B63A-7710C7FFCF0F}',
	'IWModuleType' : '{13523CD8-B0AD-46D1-B2AF-F1F2152085F0}',
	'_IWModuleTypeEvents' : '{ED5609C1-C6C9-4DA1-AD2D-30BBD10D7253}',
	'IWConveyorType' : '{E7805F03-0261-412A-9F84-2723AD292A9F}',
	'_IWConveyorTypeEvents' : '{E2B72B3B-B5CD-4EE5-A01C-BC6C34BA58CB}',
	'IWLaborRule' : '{A1B86D55-E79D-11D4-8556-0020AFF488A2}',
	'IWLaborRules' : '{A1B86D57-E79D-11D4-8556-0020AFF488A2}',
	'IWShiftType' : '{D843A28F-8C4F-471A-9E14-3E75CD5DD37A}',
	'_IWShiftTypeEvents' : '{7F0D0280-124B-4916-A0FD-20BA46FE272C}',
	'IWFunctionType' : '{BAE57732-DB47-460F-B339-D8686AB7F649}',
	'IWAttributeType' : '{C3776C0E-DC5F-426C-86B8-D41B92307A40}',
	'_IWShiftEvents' : '{95F31B86-2998-41E8-99DE-78C8AD9BFB19}',
	'IWNetworkType' : '{50443F6F-692C-4F31-B5AE-939CDC74A977}',
	'_IWNetworkTypeEvents' : '{9C405C1F-B668-46CD-9601-420DFDD10AFB}',
	'_IWNetworkEvents' : '{E31E5BE9-7313-459D-A73F-7C6AF9213408}',
	'IWPathType' : '{BB075195-E18A-4A35-81E4-05E94B6EFF23}',
	'_IWPathTypeEvents' : '{B76FE3D0-3C76-48C5-ADC0-77FD55D542F1}',
	'_IWPathEvents' : '{A6384F15-4629-4D19-A11D-3A2470E932C3}',
	'IWReportType' : '{55FDA6EA-CBF6-4D1D-9CB0-BF7B82A6BC92}',
	'_IWReportTypeEvents' : '{AC26059B-8191-428B-AAA4-161994711AE8}',
	'_IWReportEvents' : '{C4FF322C-3736-4D59-811E-EFE00FD7624D}',
	'IWVariableType' : '{5AE97C60-17C4-11D5-A1B3-00E02963982C}',
	'_IWVariableTypeEvents' : '{5AE97C62-17C4-11D5-A1B3-00E02963982C}',
	'_IWVariableEvents' : '{E735E961-17C8-11D5-A1B3-00E02963982C}',
	'IWFields' : '{739EEB63-2228-4456-AE9B-E7BD3EB736CF}',
	'IWResponses' : '{21F414EA-AF00-451A-BBF5-D53BF2A8DB7C}',
	'_IWErrorsAndWarningsEvents' : '{6AFE1260-66DF-408C-A059-0C471D6644E5}',
	'_IWInputRequestEvents' : '{5198E229-1261-49A7-B7E8-8084AB8C4F50}',
	'_IWPipeTypeEvents' : '{371DEEFC-FABA-43A9-B8DA-426A4B6056CC}',
	'_IWPipeEvents' : '{5411E9EE-6E73-4913-99DF-A6CBCC9C2A7C}',
	'_IWTankTypeEvents' : '{893B28FB-69BC-458D-89B0-24FB9476EF96}',
	'_IWTankEvents' : '{D279DC2E-E5BE-484E-8FAE-476319D18269}',
	'_IWProcessorTypeEvents' : '{5F1FB1D2-ADE8-42F9-B817-D9B8BA2C33A4}',
	'_IWProcessorEvents' : '{E1F14EFF-990E-4E95-B39B-7F52A3322590}',
	'_IWPartFileTypeEvents' : '{7FD0856F-EB0D-423B-9CE5-84C4B973E63B}',
	'_IWPartFileEvents' : '{1DB7C441-5613-493F-8035-DC04FD9E4556}',
	'_IWFileTypeEvents' : '{CC381CE2-F4E3-46EE-99AE-9B9B6B16D15D}',
	'_IWFileEvents' : '{5E58C38B-F2A1-4B33-9169-5F22A107C928}',
	'IWDataTableType' : '{11F8B66D-0328-4FAD-8154-54AC6DBAB539}',
	'_IWDataTableTypeEvents' : '{86E2E617-B2A1-4B82-9026-159D645DC025}',
	'_IWDataTableEvents' : '{18EA7261-FA3A-4804-929E-DC515094E226}',
	'IWitnessExtensionModule' : '{0DADE019-6363-4E84-AD1F-FCE7F272F774}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

