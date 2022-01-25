import adsk.core, adsk.fusion, adsk.cam
__all__ = ['Toolbars', 'WorkSpaces', 'AllPanels', 'AllTabs']

class AllPanels:
	class CAMJobPanel:
		ID = "CAMJobPanel"
		class IronSetup:
			ID = "IronSetup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronNcProgram:
			ID = "IronNcProgram"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronFolder:
			ID = "IronFolder"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class IronPattern:
			ID = "IronPattern"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_manual:
			ID = "IronStrategy_manual"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_probe:
			ID = "IronStrategy_probe"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_probe:
			ID = "SeparatorAfter_IronStrategy_probe"
			Index = 6
		class MSFWmdCreateAggregationAssetWorkingModelCmd:
			ID = "MSFWmdCreateAggregationAssetWorkingModelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
	class CAMInProcessStockPanel:
		ID = "CAMInProcessStockPanel"
		class IronAutomaticIPSGeneration:
			ID = "IronAutomaticIPSGeneration"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditiveJobPanel:
		ID = "CAMAdditiveJobPanel"
		class IronSetup:
			ID = "IronSetup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveImportGCode:
			ID = "IronAdditiveImportGCode"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronAdditiveImportGCode:
			ID = "SeparatorAfter_IronAdditiveImportGCode"
			Index = 2
		class MSFWmdCreateAggregationAssetWorkingModelCmd:
			ID = "MSFWmdCreateAggregationAssetWorkingModelCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditivePositioningPanel:
		ID = "CAMAdditivePositioningPanel"
		class CAMMoveComponentsCommand:
			ID = "CAMMoveComponentsCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_CAMMoveComponentsCommand:
			ID = "SeparatorAfter_CAMMoveComponentsCommand"
			Index = 1
		class IronMinimizeBoundingBox:
			ID = "IronMinimizeBoundingBox"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_additive_optimize_orientation:
			ID = "IronStrategy_additive_optimize_orientation"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_additive_optimize_orientation:
			ID = "SeparatorAfter_IronStrategy_additive_optimize_orientation"
			Index = 4
		class IronPlaceOnPlatform:
			ID = "IronPlaceOnPlatform"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_IronPlaceOnPlatform:
			ID = "SeparatorAfter_IronPlaceOnPlatform"
			Index = 6
		class CollisionDetectionCmd:
			ID = "CollisionDetectionCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
	class CAM2DPanel:
		ID = "CAM2DPanel"
		class IronStrategy_featureRecognition:
			ID = "IronStrategy_featureRecognition"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_contourFeatureFolder:
			ID = "IronStrategy_contourFeatureFolder"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_holeFeatureFolder:
			ID = "IronStrategy_holeFeatureFolder"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_holeFeatureFolder:
			ID = "SeparatorAfter_IronStrategy_holeFeatureFolder"
			Index = 3
		class IronStrategy_adaptive2d:
			ID = "IronStrategy_adaptive2d"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_pocket2d:
			ID = "IronStrategy_pocket2d"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_pocket2d:
			ID = "SeparatorAfter_IronStrategy_pocket2d"
			Index = 6
		class IronStrategy_face:
			ID = "IronStrategy_face"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_contour2d:
			ID = "IronStrategy_contour2d"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_slot:
			ID = "IronStrategy_slot"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_path3d:
			ID = "IronStrategy_path3d"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_path3d:
			ID = "SeparatorAfter_IronStrategy_path3d"
			Index = 11
		class IronStrategy_thread:
			ID = "IronStrategy_thread"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_bore:
			ID = "IronStrategy_bore"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_circular:
			ID = "IronStrategy_circular"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_engrave:
			ID = "IronStrategy_engrave"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_chamfer2d:
			ID = "IronStrategy_chamfer2d"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
	class CAMPanel:
		ID = "CAM3DPanel"
		class IronStrategy_adaptive:
			ID = "IronStrategy_adaptive"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_pocket_new:
			ID = "IronStrategy_pocket_new"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_pocket_new:
			ID = "SeparatorAfter_IronStrategy_pocket_new"
			Index = 2
		class IronStrategy_steep_and_shallow:
			ID = "IronStrategy_steep_and_shallow"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_flat:
			ID = "IronStrategy_flat"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_parallel_new:
			ID = "IronStrategy_parallel_new"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_scallop_new:
			ID = "IronStrategy_scallop_new"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_contour_new:
			ID = "IronStrategy_contour_new"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_ramp:
			ID = "IronStrategy_ramp"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_pencil_new:
			ID = "IronStrategy_pencil_new"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_horizontal_new:
			ID = "IronStrategy_horizontal_new"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_spiral_new:
			ID = "IronStrategy_spiral_new"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_radial_new:
			ID = "IronStrategy_radial_new"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_morphed_spiral:
			ID = "IronStrategy_morphed_spiral"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_project:
			ID = "IronStrategy_project"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_blend:
			ID = "IronStrategy_blend"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_morph:
			ID = "IronStrategy_morph"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_rest_finishing:
			ID = "IronStrategy_rest_finishing"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_flow:
			ID = "IronStrategy_flow"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
	class CAMEditPanel:
		ID = "CAMEditPanel"
		class IronToolpathTrim:
			ID = "IronToolpathTrim"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronToolpathEditDelete:
			ID = "IronToolpathEditDelete"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronToolpathEditLeadsLinks:
			ID = "IronToolpathEditLeadsLinks"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronToolpathEditToolChange:
			ID = "IronToolpathEditToolChange"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronToolpathEditMoveStartPoints:
			ID = "IronToolpathEditMoveStartPoints"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class CAMDrillingPanel:
		ID = "CAMDrillingPanel"
		class IronStrategy_drill:
			ID = "IronStrategy_drill"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronHoleRecognition:
			ID = "IronHoleRecognition"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class CAMMultiAxisPanel:
		ID = "CAMMultiAxisPanel"
		class IronStrategy_swarf5d:
			ID = "IronStrategy_swarf5d"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_multiAxisContour:
			ID = "IronStrategy_multiAxisContour"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_rotary_finishing:
			ID = "IronStrategy_rotary_finishing"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
	class CAMTurningPanel:
		ID = "CAMTurningPanel"
		class IronStrategy_turningFace:
			ID = "IronStrategy_turningFace"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningProfileRoughing:
			ID = "IronStrategy_turningProfileRoughing"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningProfileFinishing:
			ID = "IronStrategy_turningProfileFinishing"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningRoughing:
			ID = "IronStrategy_turningRoughing"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningAdaptiveRoughing:
			ID = "IronStrategy_turningAdaptiveRoughing"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningProfileGroove:
			ID = "IronStrategy_turningProfileGroove"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningGroove:
			ID = "IronStrategy_turningGroove"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningThread:
			ID = "IronStrategy_turningThread"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningChamfer:
			ID = "IronStrategy_turningChamfer"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningPart:
			ID = "IronStrategy_turningPart"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_turningSecondarySpindleGrab:
			ID = "IronStrategy_turningSecondarySpindleGrab"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningSecondarySpindlePull:
			ID = "IronStrategy_turningSecondarySpindlePull"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_turningSecondarySpindleReturn:
			ID = "IronStrategy_turningSecondarySpindleReturn"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
	class CAMWLPCPanel:
		ID = "CAMWLPCPanel"
		class IronStrategy_jet2d:
			ID = "IronStrategy_jet2d"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMInfillPanel:
		ID = "CAMInfillPanel"
		class IronFFFInfillCmd:
			ID = "IronFFFInfillCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMSupportsPanel:
		ID = "CAMSupportsPanel"
		class IronFFFSupportsCmd:
			ID = "IronFFFSupportsCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_areavolume_additive_support:
			ID = "IronStrategy_areavolume_additive_support"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_surroundvolumepolyline_additive_support:
			ID = "IronStrategy_surroundvolumepolyline_additive_support"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_surroundvolumepolyline_additive_support:
			ID = "SeparatorAfter_IronStrategy_surroundvolumepolyline_additive_support"
			Index = 3
		class IronStrategy_areabar_additive_support:
			ID = "IronStrategy_areabar_additive_support"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_downoriented_additive_support:
			ID = "IronStrategy_downoriented_additive_support"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_lattice_additive_support:
			ID = "IronStrategy_lattice_additive_support"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_lattice_additive_support:
			ID = "SeparatorAfter_IronStrategy_lattice_additive_support"
			Index = 7
		class IronStrategy_areapolyline_additive_support:
			ID = "IronStrategy_areapolyline_additive_support"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_edgepolyline_additive_support:
			ID = "IronStrategy_edgepolyline_additive_support"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_clustercontourpolyline_additive_support:
			ID = "IronStrategy_clustercontourpolyline_additive_support"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class IronStrategy_skeletonpolyline_additive_support:
			ID = "IronStrategy_skeletonpolyline_additive_support"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronStrategy_skeletonpolyline_additive_support:
			ID = "SeparatorAfter_IronStrategy_skeletonpolyline_additive_support"
			Index = 12
		class IronStrategy_baseplate_additive_support:
			ID = "IronStrategy_baseplate_additive_support"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
	class CAMDEDPanel:
		ID = "CAMDEDPanel"
		class IronStrategy_feature_construction:
			ID = "IronStrategy_feature_construction"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditiveProcessSimPanel:
		ID = "CAMAdditiveProcessSimPanel"
		class IronAdditiveProcessSimulation:
			ID = "IronAdditiveProcessSimulation"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveProcessSimMesh:
			ID = "IronAdditiveProcessSimMesh"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveProcessSimPreCheck:
			ID = "IronAdditiveProcessSimPreCheck"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveProcessSimSolve:
			ID = "IronAdditiveProcessSimSolve"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_IronAdditiveProcessSimSolve:
			ID = "SeparatorAfter_IronAdditiveProcessSimSolve"
			Index = 4
		class IronAdditiveMeshView:
			ID = "IronAdditiveMeshView"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class IronAdditiveResultsView:
			ID = "IronAdditiveResultsView"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
	class CAMAdditiveProcessSimResultsPanel:
		ID = "CAMAdditiveProcessSimResultsPanel"
		class IronAdditiveProcessSimToggleEdges:
			ID = "IronAdditiveProcessSimToggleEdges"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveProcessSimMinMaxProbe:
			ID = "IronAdditiveProcessSimMinMaxProbe"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveOpenResultsFolder:
			ID = "IronAdditiveOpenResultsFolder"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveProcessSimSolve:
			ID = "IronAdditiveProcessSimSolve"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveExportCompensated:
			ID = "IronAdditiveExportCompensated"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditiveProcessSimActionPanel:
		ID = "CAMAdditiveProcessSimActionPanel"
		class IronAdditiveExportCompensatedSTL:
			ID = "IronAdditiveExportCompensatedSTL"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditiveProcessSimFinishPanel:
		ID = "CAMAdditiveProcessSimFinishPanel"
		class AdditiveResultsStop:
			ID = "AdditiveResultsStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMProbingPanel:
		ID = "CAMProbingPanel"
		class IronStrategy_probe:
			ID = "IronStrategy_probe"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_probe_geometry:
			ID = "IronStrategy_probe_geometry"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_inspectSurface:
			ID = "IronStrategy_inspectSurface"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class PartAlignmentStart_Delayed:
			ID = "PartAlignmentStart_Delayed"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class PartAlignmentStart_Live:
			ID = "PartAlignmentStart_Live"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
	class CAMCMMPanel:
		ID = "CAMCMMPanel"
		class IronStrategy_cmm_inspection_setup:
			ID = "IronStrategy_cmm_inspection_setup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_datum:
			ID = "IronStrategy_datum"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class MeasureSurface:
			ID = "MeasureSurface"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ScanSurface:
			ID = "ScanSurface"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class CAMManualInspectionPanel:
		ID = "CAMManualInspectionPanel"
		class IronCreateInspections:
			ID = "IronCreateInspections"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronRecordManualMeasure:
			ID = "IronRecordManualMeasure"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentEditPanel:
		ID = "CAMPartAlignmentEditPanel"
		class PartAlignment_EditAlignment:
			ID = "PartAlignment_EditAlignment"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentInspectPanel:
		ID = "CAMPartAlignmentInspectPanel"
		class PartAlignment_IronStrategy_inspectSurface:
			ID = "PartAlignment_IronStrategy_inspectSurface"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentPostPanel:
		ID = "CAMPartAlignmentPostPanel"
		class PartAlignment_IronNcProgram:
			ID = "PartAlignment_IronNcProgram"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMLiveAlignmentPostPanel:
		ID = "CAMLiveAlignmentPostPanel"
		class PartAlignmentPostLive:
			ID = "PartAlignmentPostLive"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentResultsPanel:
		ID = "CAMPartAlignmentResultsPanel"
		class PartAlignment_ImportResults:
			ID = "PartAlignment_ImportResults"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PartAlignment_IronPartAlignmentInfo:
			ID = "PartAlignment_IronPartAlignmentInfo"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PartAlignment_IronShowResults:
			ID = "PartAlignment_IronShowResults"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class CAMLiveAlignmentResultsPanel:
		ID = "CAMLiveAlignmentResultsPanel"
		class LivePartAlignment:
			ID = "LivePartAlignment"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PartAlignment_IronPartAlignmentInfo:
			ID = "PartAlignment_IronPartAlignmentInfo"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PartAlignment_IronShowResults:
			ID = "PartAlignment_IronShowResults"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentPostAndExitPanel:
		ID = "CAMPartAlignmentPostAndExitPanel"
		class PartAlignmentPostStop:
			ID = "PartAlignmentPostStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMPartAlignmentFinishPanel:
		ID = "CAMPartAlignmentFinishPanel"
		class PartAlignmentStop_Delayed:
			ID = "PartAlignmentStop_Delayed"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMLiveAlignmentFinishPanel:
		ID = "CAMLiveAlignmentFinishPanel"
		class PartAlignmentStop_Live:
			ID = "PartAlignmentStop_Live"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class CAMActionPanel:
		ID = "CAMActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronSetupSheetSwitchboard:
			ID = "IronSetupSheetSwitchboard"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class CAMProbingActionPanel:
		ID = "CAMProbingActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronSetupSheetSwitchboard:
			ID = "IronSetupSheetSwitchboard"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class ImportResults:
			ID = "ImportResults"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class LiveProbing:
			ID = "LiveProbing"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class IronInspectionReport:
			ID = "IronInspectionReport"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
	class CAMAdditivePrintProfilePanel:
		ID = "CAMAdditivePrintProfilePanel"
		class SimplePrintSettingSelection:
			ID = "SimplePrintSettingSelection"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveEditPrintSetting:
			ID = "IronAdditiveEditPrintSetting"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveBuildStrategy:
			ID = "IronAdditiveBuildStrategy"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class CAMAdditiveActionPanel:
		ID = "CAMAdditiveActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveSimulation:
			ID = "IronAdditiveSimulation"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronAdditiveExportStrategy:
			ID = "IronAdditiveExportStrategy"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_IronAdditiveExportStrategy:
			ID = "SeparatorAfter_IronAdditiveExportStrategy"
			Index = 5
		class IronAdditiveShowPrintStatistics:
			ID = "IronAdditiveShowPrintStatistics"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class Iron3MFExport:
			ID = "Iron3MFExport"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class IronFormlabsExport:
			ID = "IronFormlabsExport"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
	class CAMInspectPanel:
		ID = "CAMInspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
	class CAMManagePanel:
		ID = "CAMManagePanel"
		class IronStrategy_create_form_mill:
			ID = "IronStrategy_create_form_mill"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class IronToolLibrary:
			ID = "IronToolLibrary"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class IronSetupSheetConfigurations:
			ID = "IronSetupSheetConfigurations"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 7
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 11
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
	class CAMAdditiveManagePanel:
		ID = "CAMAdditiveManagePanel"
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronPrintSettingLibrary:
			ID = "IronPrintSettingLibrary"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 5
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 9
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
	class CAMGeometryFeatures:
		ID = "CAMGeometryFeatures"
		class IronStrategy_geometry_contours:
			ID = "IronStrategy_geometry_contours"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_geometry_pockets:
			ID = "IronStrategy_geometry_pockets"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_pocket_recognition:
			ID = "IronStrategy_pocket_recognition"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class IronStrategy_geometry_silhouette:
			ID = "IronStrategy_geometry_silhouette"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class CAMScriptsAddinsPanel:
		ID = "CAMScriptsAddinsPanel"
		class ScriptsManagerCommand:
			ID = "ScriptsManagerCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ExchangeAppStoreCommand:
			ID = "ExchangeAppStoreCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
	class SelectPanel:
		ID = "SelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SelectionPriorityCommands:
			ID = "SelectionPriorityCommands"
			Index = 6
			class SelectBodyPriorityCommand:
				ID = "SelectBodyPriorityCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class SelectFacePriorityCommand:
				ID = "SelectFacePriorityCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class SelectEdgePriorityCommand:
				ID = "SelectEdgePriorityCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class SelectComponentPriorityCommand:
				ID = "SelectComponentPriorityCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
	class ManufacturingSourcesPanel:
		ID = "ManufacturingSourcesPanel"
		class MSFWmdComponentLibraryCmd:
			ID = "MSFWmdComponentLibraryCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class FabricationManagePanel:
		ID = "FabricationManagePanel"
		class MSF_MAGMatLibraryCmd_FusionNesting:
			ID = "MSF.MAGMatLibraryCmd.FusionNesting"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
		class MSF_MSFNestSaveContainerDataCmd_Create:
			ID = "MSF.MSFNestSaveContainerDataCmd.Create"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
		class Nesting_Separator:
			ID = "Nesting.Separator"
			Index = 2
		class MSFNestNameConventionCmd:
			ID = "MSFNestNameConventionCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = False
		class IronStrategy_create_form_mill:
			ID = "IronStrategy_create_form_mill"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class IronToolLibrary:
			ID = "IronToolLibrary"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class IronSetupSheetConfigurations:
			ID = "IronSetupSheetConfigurations"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 11
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 15
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
	class MachineBuilderActivationPanel:
		ID = "MachineBuilderActivationPanel"
		class MachineBuilderStart:
			ID = "MachineBuilder::Start"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class NESTPanel:
		ID = "NESTPanel"
		class MSFNestPrepareNestCmd:
			ID = "MSFNestPrepareNestCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
		class MSF_MAGNestCalculateCmd_Generate:
			ID = "MSF.MAGNestCalculateCmd.Generate"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
	class StoryboardPanel:
		ID = "3DStoryboardPanel"
		class PublisherCreateStoryboardCommand:
			ID = "PublisherCreateStoryboardCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ComponentPanel:
		ID = "3DComponentPanel"
		class PublisherMoveComponentsCommand:
			ID = "PublisherMoveComponentsCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PublisherRestoreHomeCommand:
			ID = "PublisherRestoreHomeCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class PublisherExplodeDirectChildrenCommand:
			ID = "PublisherExplodeDirectChildrenCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class PublisherExplodeAllPartsCommand:
			ID = "PublisherExplodeAllPartsCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class PublisherManualExplodeCommand:
			ID = "PublisherManualExplodeCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class PublisherVisibilityToggleCmd:
			ID = "PublisherVisibilityToggleCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class PublisherAppearanceCommand:
			ID = "PublisherAppearanceCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
	class AnnotationPanel:
		ID = "AnnotationPanel"
		class CalloutCommand:
			ID = "CalloutCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class PublisherViewPanel:
		ID = "PublisherViewPanel"
		class PublisherToggleCameraRecordingCmd:
			ID = "PublisherToggleCameraRecordingCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class PublishVideoPanel:
		ID = "PublishVideoPanel"
		class ExportVideoCommand:
			ID = "ExportVideoCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class FilePanel:
		ID = "FilePanel"
		class NewSingleDocumentCommand:
			ID = "NewSingleDocumentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class NewDocumentCommand:
			ID = "NewDocumentCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class SaveDocumentAsCommand:
			ID = "SaveDocumentAsCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class DiagnosticsPanel:
		ID = "DiagnosticsPanel"
		class HideTextCommandsCommand:
			ID = "HideTextCommandsCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class ShowTextCommandsCommand:
			ID = "ShowTextCommandsCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class HideDebugDialogCommand:
			ID = "HideDebugDialogCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ShowDebugDialogCommand:
			ID = "ShowDebugDialogCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class NTestImportCommand:
			ID = "NTestImportCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class DiagnosticsCommand:
			ID = "DiagnosticsCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class DataBrowserCommand:
			ID = "DataBrowserCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class DumpEntityCommand:
			ID = "DumpEntityCommand"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
		class EntityFinderCommand:
			ID = "EntityFinderCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class TSplineDumpEntityCommand:
			ID = "TSplineDumpEntityCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
		class TSplineSaveAsTSMCommand:
			ID = "TSplineSaveAsTSMCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
		class TSplineDiagnosticCommand:
			ID = "TSplineDiagnosticCommand"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
		class AssemblyInfoCommand:
			ID = "AssemblyInfoCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class SanityCheckCommand:
			ID = "SanityCheckCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
		class ASMDebugOptionsCommand:
			ID = "ASMDebugOptionsCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class ASMDebugChecksCommand:
			ID = "ASMDebugChecksCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class RunTestsCommand:
			ID = "RunTestsCommand"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
		class CollaborationMockDebugCmd:
			ID = "CollaborationMockDebugCmd"
			Index = 17
			isPromoted = True
			isPromotedByDefault = True
		class SketchAutoConstrainCmd:
			ID = "SketchAutoConstrainCmd"
			Index = 18
			isPromoted = True
			isPromotedByDefault = True
	class UIDemo:
		ID = "UIDemo"
		class TestTableCommand:
			ID = "TestTableCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class TestTabBarCommand:
			ID = "TestTabBarCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class TestToolkitCommand:
			ID = "TestToolkitCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class TestOptionGroupCommand:
			ID = "TestOptionGroupCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class TestPropertyDialogCommand:
			ID = "TestPropertyDialogCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class DemoControlsCommand:
			ID = "DemoControlsCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class DemoControls2Command:
			ID = "DemoControls2Command"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
	class SketchCreatePanel:
		ID = "SketchCreatePanel"
		class DrawPolyline:
			ID = "DrawPolyline"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class RectangleDropDown:
			ID = "RectangleDropDown"
			Index = 1
			class ShapeRectangleTwoPoint:
				ID = "ShapeRectangleTwoPoint"
				Index = 0
			class ShapeRectangleThreePoint:
				ID = "ShapeRectangleThreePoint"
				Index = 1
			class ShapeRectangleCenter:
				ID = "ShapeRectangleCenter"
				Index = 2
		class CircleDropDown:
			ID = "CircleDropDown"
			Index = 2
			class CircleCenterRadius:
				ID = "CircleCenterRadius"
				Index = 0
			class CircleTwoPoint:
				ID = "CircleTwoPoint"
				Index = 1
			class CircleThreePoint:
				ID = "CircleThreePoint"
				Index = 2
			class CircleTanTanRadius:
				ID = "CircleTanTanRadius"
				Index = 3
			class CircleThreeTangent:
				ID = "CircleThreeTangent"
				Index = 4
		class ArcDropDown:
			ID = "ArcDropDown"
			Index = 3
			class ArcThreePoint:
				ID = "ArcThreePoint"
				Index = 0
			class ArcCenterTwoPoint:
				ID = "ArcCenterTwoPoint"
				Index = 1
			class ArcTangent:
				ID = "ArcTangent"
				Index = 2
		class PolygonDropDown:
			ID = "PolygonDropDown"
			Index = 4
			class ShapePolygonCircumscribed:
				ID = "ShapePolygonCircumscribed"
				Index = 0
			class ShapePolygonInscribed:
				ID = "ShapePolygonInscribed"
				Index = 1
			class ShapePolygonEdge:
				ID = "ShapePolygonEdge"
				Index = 2
		class CircleElipse:
			ID = "CircleElipse"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SlotDropDown:
			ID = "SlotDropDown"
			Index = 6
			class ShapeSlotCenterToCenter:
				ID = "ShapeSlotCenterToCenter"
				Index = 0
			class ShapeSlotOverall:
				ID = "ShapeSlotOverall"
				Index = 1
			class ShapeSlotCenterPoint:
				ID = "ShapeSlotCenterPoint"
				Index = 2
			class ShapeArcSlotThreePoint:
				ID = "ShapeArcSlotThreePoint"
				Index = 3
			class ShapeArcSlotCenterTwoPoint:
				ID = "ShapeArcSlotCenterTwoPoint"
				Index = 4
		class SplineDropDown:
			ID = "SplineDropDown"
			Index = 7
			class DrawSpline:
				ID = "DrawSpline"
				Index = 0
			class DrawCVMSpline:
				ID = "DrawCVMSpline3D"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class DrawCVMSpline5D:
				ID = "DrawCVMSpline5D"
				Index = 2
		class ConicCurveCmd:
			ID = "ConicCurveCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class DrawPoint:
			ID = "DrawPoint"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class TextCmd:
			ID = "TextCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class MTextCmd:
			ID = "MTextCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_MTextCmd"
			Index = 12
		class FitCurvesToSectionCommand:
			ID = "FitCurvesToSectionCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FitCurvesToSectionCommand:
			ID = "SeparatorAfter_FitCurvesToSectionCommand"
			Index = 14
		class MirrorSketchCommand:
			ID = "MirrorSketchCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
		class CircularSketchPatternCommand:
			ID = "CircularSketchPatternCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class RectangularSketchPatternCommand:
			ID = "RectangularSketchPatternCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_RectangularSketchPatternCommand:
			ID = "SeparatorAfter_RectangularSketchPatternCommand"
			Index = 18
		class ProjectIncludeDropDown:
			ID = "ProjectIncludeDropDown"
			Index = 19
			class ProjectNewCmd:
				ID = "ProjectNewCmd"
				Index = 0
			class IntersectCmd:
				ID = "IntersectCmd"
				Index = 1
			class meshIntersect:
				ID = "meshIntersect"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
			class SeparatorAfter_IntersectCmd:
				ID = "SeparatorAfter_IntersectCmd"
				Index = 2
			class IncludeGeometry:
				ID = "Include3DGeometry"
				Index = 3
			class SeparatorAfter_IncludeGeometry:
				ID = "SeparatorAfter_Include3DGeometry"
				Index = 4
			class ProjectToSurface:
				ID = "ProjectToSurface"
				Index = 5
			class IntersectionCurve:
				ID = "IntersectionCurve"
				Index = 6
		class SeparatorAfter_ProjectIncludeDropDown:
			ID = "SeparatorAfter_ProjectIncludeDropDown"
			Index = 20
		class SketchDimension:
			ID = "SketchDimension"
			Index = 21
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SketchDimension:
			ID = "SeparatorAfter_SketchDimension"
			Index = 22
	class PCBSketchCreatePanel:
		ID = "PCB3DSketchCreatePanel"
		class DrawPolyline:
			ID = "DrawPolyline"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class RectangleDropDown:
			ID = "RectangleDropDown"
			Index = 1
			class ShapeRectangleTwoPoint:
				ID = "ShapeRectangleTwoPoint"
				Index = 0
			class ShapeRectangleThreePoint:
				ID = "ShapeRectangleThreePoint"
				Index = 1
			class ShapeRectangleCenter:
				ID = "ShapeRectangleCenter"
				Index = 2
		class CircleDropDown:
			ID = "CircleDropDown"
			Index = 2
			class CircleCenterRadius:
				ID = "CircleCenterRadius"
				Index = 0
			class CircleTwoPoint:
				ID = "CircleTwoPoint"
				Index = 1
			class CircleThreePoint:
				ID = "CircleThreePoint"
				Index = 2
			class CircleTanTanRadius:
				ID = "CircleTanTanRadius"
				Index = 3
			class CircleThreeTangent:
				ID = "CircleThreeTangent"
				Index = 4
		class ArcDropDown:
			ID = "ArcDropDown"
			Index = 3
			class ArcThreePoint:
				ID = "ArcThreePoint"
				Index = 0
			class ArcCenterTwoPoint:
				ID = "ArcCenterTwoPoint"
				Index = 1
			class ArcTangent:
				ID = "ArcTangent"
				Index = 2
		class PolygonDropDown:
			ID = "PolygonDropDown"
			Index = 4
			class ShapePolygonCircumscribed:
				ID = "ShapePolygonCircumscribed"
				Index = 0
			class ShapePolygonInscribed:
				ID = "ShapePolygonInscribed"
				Index = 1
			class ShapePolygonEdge:
				ID = "ShapePolygonEdge"
				Index = 2
		class SlotDropDown:
			ID = "SlotDropDown"
			Index = 5
			class ShapeSlotCenterToCenter:
				ID = "ShapeSlotCenterToCenter"
				Index = 0
			class ShapeSlotOverall:
				ID = "ShapeSlotOverall"
				Index = 1
			class ShapeSlotCenterPoint:
				ID = "ShapeSlotCenterPoint"
				Index = 2
			class ShapeArcSlotThreePoint:
				ID = "ShapeArcSlotThreePoint"
				Index = 3
			class ShapeArcSlotCenterTwoPoint:
				ID = "ShapeArcSlotCenterTwoPoint"
				Index = 4
		class SplineDropDown:
			ID = "SplineDropDown"
			Index = 6
			class DrawCVMSpline:
				ID = "DrawCVMSpline3D"
				Index = 0
				isPromoted = True
				isPromotedByDefault = True
		class ConicCurveCmd:
			ID = "ConicCurveCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class DrawPoint:
			ID = "DrawPoint"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class TextCmd:
			ID = "TextCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class MTextCmd:
			ID = "MTextCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_MTextCmd"
			Index = 11
		class SeparatorAfter_SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_SeparatorAfter_MTextCmd"
			Index = 12
		class MirrorSketchCommand:
			ID = "MirrorSketchCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
		class CircularSketchPatternCommand:
			ID = "CircularSketchPatternCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class RectangularSketchPatternCommand:
			ID = "RectangularSketchPatternCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_RectangularSketchPatternCommand:
			ID = "SeparatorAfter_RectangularSketchPatternCommand"
			Index = 16
		class ProjectIncludeDropDown:
			ID = "ProjectIncludeDropDown"
			Index = 17
			class ProjectNewCmd:
				ID = "ProjectNewCmd"
				Index = 0
			class IntersectCmd:
				ID = "IntersectCmd"
				Index = 1
			class SeparatorAfter_IntersectCmd:
				ID = "SeparatorAfter_IntersectCmd"
				Index = 2
			class IncludeGeometry:
				ID = "Include3DGeometry"
				Index = 3
			class SeparatorAfter_IncludeGeometry:
				ID = "SeparatorAfter_Include3DGeometry"
				Index = 4
			class ProjectToSurface:
				ID = "ProjectToSurface"
				Index = 5
			class IntersectionCurve:
				ID = "IntersectionCurve"
				Index = 6
		class SeparatorAfter_ProjectIncludeDropDown:
			ID = "SeparatorAfter_ProjectIncludeDropDown"
			Index = 18
		class SketchDimension:
			ID = "SketchDimension"
			Index = 19
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SketchDimension:
			ID = "SeparatorAfter_SketchDimension"
			Index = 20
	class SketchModifyPanel:
		ID = "SketchModifyPanel"
		class FilletSketchCmd:
			ID = "FilletSketchCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SketchChamferDropDown:
			ID = "SketchChamferDropDown"
			Index = 1
			class ChamferSketchEqualDistance:
				ID = "ChamferSketchEqualDistance"
				Index = 0
			class ChamferSketchDistanceAngle:
				ID = "ChamferSketchDistanceAngle"
				Index = 1
			class ChamferSketchDistanceDistance:
				ID = "ChamferSketchDistanceDistance"
				Index = 2
		class TrimSketchCmd:
			ID = "TrimSketchCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ExtendSketchCmd:
			ID = "ExtendSketchCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class BreakSketchCmd:
			ID = "BreakSketchCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SketchScaleCmd:
			ID = "SketchScaleCmd"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class Offset:
			ID = "Offset"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_Offset:
			ID = "SeparatorAfter_Offset"
			Index = 7
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = False
	class SketchConstraintsPanel:
		ID = "SketchConstraintsPanel"
		class ConstraintHorizontalVertical:
			ID = "ConstraintHorizontalVertical"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintCoincident:
			ID = "ConstraintCoincident"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintTangent:
			ID = "ConstraintTangent"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintEqual:
			ID = "ConstraintEqual"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintParallel:
			ID = "ConstraintParallel"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintPerpendicular:
			ID = "ConstraintPerpendicular"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintFix:
			ID = "ConstraintFix"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintMidPoint:
			ID = "ConstraintMidPoint"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintConcentric:
			ID = "ConstraintConcentric"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintCollinear:
			ID = "ConstraintCollinear"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintSymmetry:
			ID = "ConstraintSymmetry"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
		class ConstraintSmooth:
			ID = "ConstraintSmooth"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
	class SolidCreatePanel:
		ID = "SolidCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class TSplineBaseFeatureCreationCommand:
			ID = "TSplineBaseFeatureCreationCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = True
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 4
		class Extrude:
			ID = "Extrude"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class Revolve:
			ID = "Revolve"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class Sweep:
			ID = "Sweep"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class SolidLoft:
			ID = "SolidLoft"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
		class FusionRibCommand:
			ID = "FusionRibCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionWebCommand:
			ID = "FusionWebCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class EmbossCmd:
			ID = "EmbossCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_EmbossCmd:
			ID = "SeparatorAfter_EmbossCmd"
			Index = 12
		class FusionHoleCommand:
			ID = "FusionHoleCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
		class FusionThreadCommand:
			ID = "FusionThreadCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionThreadCommand:
			ID = "SeparatorAfter_FusionThreadCommand"
			Index = 15
		class PrimitiveBox:
			ID = "PrimitiveBox"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class PrimitiveCylinder:
			ID = "PrimitiveCylinder"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class PrimitiveSphere:
			ID = "PrimitiveSphere"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
		class PrimitiveTorus:
			ID = "PrimitiveTorus"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class PrimitiveCoil:
			ID = "PrimitiveCoil"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class PrimitivePipe:
			ID = "PrimitivePipe"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_PrimitivePipe:
			ID = "SeparatorAfter_PrimitivePipe"
			Index = 22
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 23
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 24
			isPromoted = True
			isPromotedByDefault = False
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 25
		class FusionSurfaceThickenCommand:
			ID = "FusionSurfaceThickenCommand"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
		class SurfaceSculpt:
			ID = "SurfaceSculpt"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_SurfaceSculpt:
			ID = "SeparatorAfter_SurfaceSculpt"
			Index = 28
		class FusionFindFeaturesCommand:
			ID = "FusionFindFeaturesCommand"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
		class EnclosureCommand:
			ID = "EnclosureCommand"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_EnclosureCommand:
			ID = "SeparatorAfter_EnclosureCommand"
			Index = 31
		class MeshBaseFeatureCreationCommand:
			ID = "MeshBaseFeatureCreationCommand"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
		class MeshPlanarSectionCommand:
			ID = "MeshPlanarSectionCommand"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MeshPlanarSectionCommand:
			ID = "SeparatorAfter_MeshPlanarSectionCommand"
			Index = 34
		class BaseFeatureCreationCommand:
			ID = "BaseFeatureCreationCommand"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
		class PCBCreateCmd:
			ID = "PCBCreateCmd"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
		class PCBDeriveCmd:
			ID = "PCBDeriveCmd"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
	class GeneratePanel:
		ID = "GeneratePanel"
		class AutomatedModelingCommand:
			ID = "AutomatedModelingCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class SolidModifyPanel:
		ID = "SolidModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = False
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionShellBodyCommand:
			ID = "FusionShellBodyCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class FusionDraftCommand:
			ID = "FusionDraftCommand"
			Index = 7
			isPromoted = True
			isPromotedByDefault = False
		class ModifyScale:
			ID = "ModifyScale"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
		class FusionCombineCommand:
			ID = "FusionCombineCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
		class FusionOffsetFacesCommand:
			ID = "FusionOffsetFacesCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class Tion_MoveCommand:
			ID = "Tion_MoveCommand"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
		class Tion_InsetFaceTool:
			ID = "Tion_InsetFaceTool"
			Index = 12
			isPromoted = True
			isPromotedByDefault = True
		class FusionReplaceFaceCommand:
			ID = "FusionReplaceFaceCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
		class FusionPartingLineSplitCmd:
			ID = "FusionPartingLineSplitCmd"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionPartingLineSplitCmd:
			ID = "SeparatorAfter_FusionPartingLineSplitCmd"
			Index = 17
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 18
			isPromoted = True
			isPromotedByDefault = True
		class AlignCmd:
			ID = "AlignCmd"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 21
		class ArrangeCommand:
			ID = "ArrangeCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class SimplifyDropDown:
			ID = "SimplifyDropDown"
			Index = 23
			class FusionRemoveFeaturesCommand:
				ID = "FusionRemoveFeaturesCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class FusionRemoveFacesCommand:
				ID = "FusionRemoveFacesCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class ReplaceWithPrimitivesCommand:
				ID = "ReplaceWithPrimitivesCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
		class SeparatorAfter_SimplifyDropDown:
			ID = "SeparatorAfter_SimplifyDropDown"
			Index = 24
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 28
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 29
			isPromoted = True
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 31
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 33
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
		class Tion_GetUICommand:
			ID = "Tion_GetUICommand"
			Index = 34
			isPromoted = True
			isPromotedByDefault = True
		class Tion_LoftCut:
			ID = "Tion_LoftCut"
			Index = 35
			isPromoted = True
			isPromotedByDefault = True
	class SheetMetalCreatePanel:
		ID = "SheetMetalCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionSheetMetalFlangeCommand:
			ID = "FusionSheetMetalFlangeCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class SheetMetalBendCmd:
			ID = "SheetMetalBendCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class ConvertToSheetMetalCmd:
			ID = "ConvertToSheetMetalCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class DMConvertToSheetMetalCmd:
			ID = "DMConvertToSheetMetalCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 7
		class Extrude:
			ID = "Extrude"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_Extrude:
			ID = "SeparatorAfter_Extrude"
			Index = 9
		class FusionHoleCommand:
			ID = "FusionHoleCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class FusionThreadCommand:
			ID = "FusionThreadCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionThreadCommand:
			ID = "SeparatorAfter_FusionThreadCommand"
			Index = 12
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 13
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 15
		class FusionSheetMetalFlatPatternCmd:
			ID = "FusionSheetMetalFlatPatternCmd"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
	class SheetMetalModifyPanel:
		ID = "SheetMetalModifyPanel"
		class SeparatorAfter_:
			ID = "SeparatorAfter_"
			Index = 0
		class FusionSheetmetalUnfoldCommand:
			ID = "FusionSheetmetalUnfoldCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionSheetMetalRulesCommand:
			ID = "FusionSheetMetalRulesCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionSheetMetalRulesCommand:
			ID = "SeparatorAfter_FusionSheetMetalRulesCommand"
			Index = 3
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 6
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class AlignCmd:
			ID = "AlignCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 10
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 14
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 17
	class AssemblePanel:
		ID = "AssemblePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = True
		class JointAssembleCmdNew:
			ID = "JointAssembleCmdNew"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class JointAsBuiltCmd:
			ID = "JointAsBuiltCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = False
		class JointOrigin:
			ID = "JointOrigin"
			Index = 3
			isPromoted = True
			isPromotedByDefault = False
		class RigidGroupCmd:
			ID = "RigidGroupCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_RigidGroupCmd:
			ID = "SeparatorAfter_RigidGroupCmd"
			Index = 5
		class FusionMoveJointsCommand:
			ID = "FusionMoveJointsCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionMotionRelationshipCommand:
			ID = "FusionMotionRelationshipCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionMotionRelationshipCommand:
			ID = "SeparatorAfter_FusionMotionRelationshipCommand"
			Index = 8
		class EnableContactSetsCmd:
			ID = "EnableContactSetsCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class EnableAllContactCmd:
			ID = "EnableAllContactCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class DisableAllContactCmd:
			ID = "DisableAllContactCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class ContactSetCmd:
			ID = "ContactSetCmd"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_ContactSetCmd:
			ID = "SeparatorAfter_ContactSetCmd"
			Index = 13
		class FusionMotionStudyCommand:
			ID = "FusionMotionStudyCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
	class AssembleModifyPanel:
		ID = "AssembleModifyPanel"
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class AlignCmd:
			ID = "AlignCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
	class AssembleUtilityPanel:
		ID = "AssembleUtilityPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 3
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 12
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
	class SurfaceCreatePanel:
		ID = "SurfaceCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 3
		class SurfaceExtrude:
			ID = "SurfaceExtrude"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class SurfaceRevolve:
			ID = "SurfaceRevolve"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class SurfaceSweep:
			ID = "SurfaceSweep"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class SurfaceLoft:
			ID = "SurfaceLoft"
			Index = 7
			isPromoted = True
			isPromotedByDefault = False
		class FusionSurfacePatchCommand:
			ID = "FusionSurfacePatchCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceRuledCommand:
			ID = "FusionSurfaceRuledCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionSurfaceOffsetCommand:
			ID = "FusionSurfaceOffsetCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionSurfaceOffsetCommand:
			ID = "SeparatorAfter_FusionSurfaceOffsetCommand"
			Index = 11
		class SurfPrimitiveBox:
			ID = "SurfPrimitiveBox"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class SurfPrimitiveCylinder:
			ID = "SurfPrimitiveCylinder"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class SurfPrimitiveSphere:
			ID = "SurfPrimitiveSphere"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class SurfPrimitiveTorus:
			ID = "SurfPrimitiveTorus"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class SurfPrimitiveCoil:
			ID = "SurfPrimitiveCoil"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class SurfPrimitivePipe:
			ID = "SurfPrimitivePipe"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_SurfPrimitivePipe:
			ID = "SeparatorAfter_SurfPrimitivePipe"
			Index = 18
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 19
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 21
		class FusionSurfaceThickenCommand:
			ID = "FusionSurfaceThickenCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class SurfaceSculpt:
			ID = "SurfaceSculpt"
			Index = 23
			isPromoted = True
			isPromotedByDefault = False
	class SurfaceModifyPanel:
		ID = "SurfaceModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionSurfaceTrimCommand:
			ID = "FusionSurfaceTrimCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceUntrimCommand:
			ID = "FusionSurfaceUntrimCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class FusionExtendCommand:
			ID = "FusionExtendCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceStitchCommand:
			ID = "FusionSurfaceStitchCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceUnStitchCommand:
			ID = "FusionSurfaceUnStitchCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceMergeCommand:
			ID = "FusionSurfaceMergeCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class FusionSurfaceReverseNormalCommand:
			ID = "FusionSurfaceReverseNormalCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class ModifyScale:
			ID = "ModifyScale"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionSplitBodyCommand:
			ID = "SeparatorAfter_FusionSplitBodyCommand"
			Index = 16
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 17
			isPromoted = True
			isPromotedByDefault = False
		class Tion_SurfaceCopyTool:
			ID = "Tion_SurfaceCopyTool"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
		class AlignCmd:
			ID = "AlignCmd"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 21
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 23
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
		class SeparatorAfter_MeshDropDown:
			ID = "SeparatorAfter_MeshDropDown"
			Index = 24
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 28
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
	class TSplinePrimitivePanel:
		ID = "TSplinePrimitivePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SketchCreate:
			ID = "SeparatorAfter_SketchCreate"
			Index = 2
		class TSplinePrimitiveBoxCommand:
			ID = "TSplinePrimitiveBoxCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class TSplinePrimitivePlaneCommand:
			ID = "TSplinePrimitivePlaneCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class TSplinePrimitiveCylinderCommand:
			ID = "TSplinePrimitiveCylinderCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class TSplinePrimitiveSphereCommand:
			ID = "TSplinePrimitiveSphereCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class TSplinePrimitiveTorusCommand:
			ID = "TSplinePrimitiveTorusCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class TSplinePrimitiveQuadBallCommand:
			ID = "TSplinePrimitiveQuadBallCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class TSplinePrimitivePipe:
			ID = "TSplinePrimitivePipe"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplinePrimitivePipe:
			ID = "SeparatorAfter_TSplinePrimitivePipe"
			Index = 10
		class TSplineAppendFaceCommand:
			ID = "TSplineAppendFaceCommand"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_TSplineAppendFaceCommand:
			ID = "SeparatorAfter_TSplineAppendFaceCommand"
			Index = 12
		class TSplineExtrudeCommand:
			ID = "TSplineExtrudeCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class TSplineRevolveCommand:
			ID = "TSplineRevolveCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class TSplineSweepCommand:
			ID = "TSplineSweepCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class TSplineLoft:
			ID = "TSplineLoft"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
	class TSplineModifyPanel:
		ID = "TSplineModifyPanel"
		class TSplineEditCommand:
			ID = "TSplineEditCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class TSplineEditByCurveCmd:
			ID = "TSplineEditByCurveCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineEditByCurveCmd:
			ID = "SeparatorAfter_TSplineEditByCurveCmd"
			Index = 2
		class TSplineInsertEdgeCommand:
			ID = "TSplineInsertEdgeCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class TSplineSubsetCmd:
			ID = "TSplineSubsetCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class TSplineInsertPointCommand:
			ID = "TSplineInsertPointCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineInsertPointCommand:
			ID = "SeparatorAfter_TSplineInsertPointCommand"
			Index = 6
		class TSplineMergeEdgeCmd:
			ID = "TSplineMergeEdgeCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class TSplineBridgeSubDCmd:
			ID = "TSplineBridgeSubDCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class TSplineFillHoleCmd:
			ID = "TSplineFillHoleCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class TSplineEraseAndFillCmd:
			ID = "TSplineEraseAndFillCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class TSplineWeldCommand:
			ID = "TSplineWeldCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class TSplineUnWeldCommand:
			ID = "TSplineUnWeldCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineUnWeldCommand:
			ID = "SeparatorAfter_TSplineUnWeldCommand"
			Index = 13
		class TSplineCreasedEdgeCommand:
			ID = "TSplineCreasedEdgeCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class TSplineUnCreaseEdgeCmd:
			ID = "TSplineUnCreaseEdgeCmd"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class TSplineBevelEdgeCommand:
			ID = "TSplineBevelEdgeCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class TSplineSlideEdgeCommand:
			ID = "TSplineSlideEdgeCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineSlideEdgeCommand:
			ID = "SeparatorAfter_TSplineSlideEdgeCommand"
			Index = 18
		class TSplineSmoothCmd:
			ID = "TSplineSmoothCmd"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class TSplineCylindrifyCmd:
			ID = "TSplineCylindrifyCmd"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class TSplinePullSubDCmd:
			ID = "TSplinePullSubDCmd"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
		class TSplineFlattenSubDCmd:
			ID = "TSplineFlattenSubDCmd"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class TSplineStraightenCmd:
			ID = "TSplineStraightenCmd"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
		class TSplineMatchCmd:
			ID = "TSplineMatchCmd"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
		class TSplineInterpolateSubDCmd:
			ID = "TSplineInterpolateSubDCmd"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineInterpolateSubDCmd:
			ID = "SeparatorAfter_TSplineInterpolateSubDCmd"
			Index = 26
		class TSplineThickenCommand:
			ID = "TSplineThickenCommand"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineThickenCommand:
			ID = "SeparatorAfter_TSplineThickenCommand"
			Index = 28
		class FreezeDropDown:
			ID = "FreezeDropDown"
			Index = 29
			class TSplineFreezeCmd:
				ID = "TSplineFreezeCmd"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class TSplineUnFreezeCmd:
				ID = "TSplineUnFreezeCmd"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
		class SeparatorAfter_FreezeDropDown:
			ID = "SeparatorAfter_FreezeDropDown"
			Index = 30
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 31
			isPromoted = False
			isPromotedByDefault = False
		class AlignCmd:
			ID = "AlignCmd"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 34
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
	class TSplineSymmetryPanel:
		ID = "TSplineSymmetryPanel"
		class TSplineInternalMirrorSymmetryCmd:
			ID = "TSplineInternalMirrorSymmetryCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class TSplineInternalCircularSymmetryCmd:
			ID = "TSplineInternalCircularSymmetryCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineInternalCircularSymmetryCmd:
			ID = "SeparatorAfter_TSplineInternalCircularSymmetryCmd"
			Index = 2
		class TSplineReflectionMirrorSymmetryCmd:
			ID = "TSplineReflectionMirrorSymmetryCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class TSplineReflectionCircularSymmetryCmd:
			ID = "TSplineReflectionCircularSymmetryCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineReflectionCircularSymmetryCmd:
			ID = "SeparatorAfter_TSplineReflectionCircularSymmetryCmd"
			Index = 5
		class TSplineClearSymmetryCommand:
			ID = "TSplineClearSymmetryCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class TSplineIsolateSymmetryCmd:
			ID = "TSplineIsolateSymmetryCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
	class TSplineUtilitiesPanel:
		ID = "TSplineUtilitiesPanel"
		class TSplineToggleTessModeCmd:
			ID = "TSplineToggleTessModeCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_TSplineToggleTessModeCmd:
			ID = "SeparatorAfter_TSplineToggleTessModeCmd"
			Index = 1
		class TSplineRepairBodyCmd:
			ID = "TSplineRepairBodyCmd"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class TSplineMakeUniformCmd:
			ID = "TSplineMakeUniformCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSplineMakeUniformCmd:
			ID = "SeparatorAfter_TSplineMakeUniformCmd"
			Index = 4
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_TSpline2BRepCommand:
			ID = "SeparatorAfter_TSpline2BRepCommand"
			Index = 6
		class TSplineCapSettingCommand:
			ID = "TSplineCapSettingCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
	class MeshPrimitivePanel:
		ID = "MeshPrimitivePanel"
		class InsertAlignMeshCommand:
			ID = "InsertAlignMeshCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class BRep2MeshCommand:
			ID = "BRep2MeshCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class MeshModifyPanel:
		ID = "MeshModifyPanel"
		class MeshRemeshCommand:
			ID = "MeshRemeshCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class MeshReduceCommand:
			ID = "MeshReduceCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class MeshMakeSolidCommand:
			ID = "MeshMakeSolidCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MeshMakeSolidCommand:
			ID = "SeparatorAfter_MeshMakeSolidCommand"
			Index = 3
		class MeshReplaceCommand:
			ID = "MeshReplaceCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class MeshSmoothCommand:
			ID = "MeshSmoothCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class MeshPlaneCutCommand:
			ID = "MeshPlaneCutCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class MeshReverseNormalsCommand:
			ID = "MeshReverseNormalsCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class MeshDeleteTrianglesCommand:
			ID = "MeshDeleteTrianglesCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MeshDeleteTrianglesCommand:
			ID = "SeparatorAfter_MeshDeleteTrianglesCommand"
			Index = 9
		class MeshSubsetCommand:
			ID = "MeshSubsetCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class MeshCombineCommand:
			ID = "MeshCombineCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_MeshCombineCommand:
			ID = "SeparatorAfter_MeshCombineCommand"
			Index = 12
		class FaceGroupsDropDown:
			ID = "FaceGroupsDropDown"
			Index = 13
			class MeshGenerateFGCommand:
				ID = "MeshGenerateFGCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class MeshCreateFGCommand:
				ID = "MeshCreateFGCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class MeshClearFGCommand:
				ID = "MeshClearFGCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
		class SeparatorAfter_FaceGroupsDropDown:
			ID = "SeparatorAfter_FaceGroupsDropDown"
			Index = 14
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
		class ModifyScale:
			ID = "ModifyScale"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
	class PCBCreatePanel:
		ID = "PCBCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionCreateNewComponentCommand:
			ID = "SeparatorAfter_FusionCreateNewComponentCommand"
			Index = 1
		class PCBCreateCmd:
			ID = "PCBCreateCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class PCBDefineBoardCmd:
			ID = "PCBDefineBoardCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class PCBModifyPanel:
		ID = "PCBModifyPanel"
		class PCBImprintCmd:
			ID = "PCBImprintCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PCBBoardSketchEditCmd:
			ID = "PCBBoardSketchEditCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PCBMoveComponentsCmd:
			ID = "PCBMoveComponentsCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class PCBFlipComponentCmd:
			ID = "PCBFlipComponentCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class PCBStatusCmd:
			ID = "PCBStatusCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class PCBPanel:
		ID = "PCB3DPanel"
		class PCBFlipComponentCmd:
			ID = "PCB3DFlipComponentCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PCBMoveComponentsCmd:
			ID = "PCB3DMoveComponentsCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PCBExportBrdCmd:
			ID = "PCBExportBrdCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class PCBLinkToBrdCmd:
			ID = "PCBLinkToBrdCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class PCBHoleCmd:
			ID = "PCBHoleCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class ConstructionPanel:
		ID = "ConstructionPanel"
		class WorkPlaneOffsetFromPlaneCommand:
			ID = "WorkPlaneOffsetFromPlaneCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class WorkPlaneFromLineAndAngleCommand:
			ID = "WorkPlaneFromLineAndAngleCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
		class WorkPlaneTangentToCylinderCommand:
			ID = "WorkPlaneTangentToCylinderCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class WorkPlaneFromTwoPlanesCommand:
			ID = "WorkPlaneFromTwoPlanesCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = False
		class WorkPlaneFromTwoLinesCommand:
			ID = "WorkPlaneFromTwoLinesCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class WorkPlaneFromThreePointsCommand:
			ID = "WorkPlaneFromThreePointsCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class WorkPlaneFromPointAndFaceCommand:
			ID = "WorkPlaneFromPointAndFaceCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class WorkPlaneAlongPathCommand:
			ID = "WorkPlaneAlongPathCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class WorkPlaneFromPointAndNormalCommand:
			ID = "WorkPlaneFromPointAndNormalCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_WorkPlaneFromPointAndNormalCommand:
			ID = "SeparatorAfter_WorkPlaneFromPointAndNormalCommand"
			Index = 9
		class WorkAxisThroughCylinderCommand:
			ID = "WorkAxisThroughCylinderCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class WorkAxisNormalToFaceCommand:
			ID = "WorkAxisNormalToFaceCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class WorkAxisFromTwoPlanesCommand:
			ID = "WorkAxisFromTwoPlanesCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class WorkAxisFromTwoPointsCommand:
			ID = "WorkAxisFromTwoPointsCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class WorkAxisFromLineCommand:
			ID = "WorkAxisFromLineCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class WorkAxisFromPointAndFaceCommand:
			ID = "WorkAxisFromPointAndFaceCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_WorkAxisFromPointAndFaceCommand:
			ID = "SeparatorAfter_WorkAxisFromPointAndFaceCommand"
			Index = 16
		class WorkPointFromPointCommand:
			ID = "WorkPointFromPointCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointFromTwoLinesCommand:
			ID = "WorkPointFromTwoLinesCommand"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointFromThreePlanesCommand:
			ID = "WorkPointFromThreePlanesCommand"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointFromCircleOrSphereCommand:
			ID = "WorkPointFromCircleOrSphereCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointFromLineAndPlaneCommand:
			ID = "WorkPointFromLineAndPlaneCommand"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointAlongPathCommand:
			ID = "WorkPointAlongPathCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class WorkPointFromCoordsCommand:
			ID = "WorkPointFromCoordsCommand"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
	class InspectPanel:
		ID = "InspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 3
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class FusionIsoCurveAnalysisCommand:
			ID = "FusionIsoCurveAnalysisCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 13
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
	class InspectMeshPanel:
		ID = "InspectMeshPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_MeasureCommand:
			ID = "SeparatorAfter_MeasureCommand"
			Index = 1
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
	class ToolsInspectPanel:
		ID = "ToolsInspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 2
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionIsoCurveAnalysisCommand:
			ID = "FusionIsoCurveAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 12
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
		class zxynine_anymacro_BuiltinAlignView:
			ID = "zxynine_anymacro_BuiltinAlignView"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class zxynine_anymacro_BuiltinChangeView:
			ID = "zxynine_anymacro_BuiltinChangeView"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class zxynine_anymacro_BuiltinChangeViewOrientation:
			ID = "zxynine_anymacro_BuiltinChangeViewOrientation"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
	class InsertPanel:
		ID = "InsertPanel"
		class InsertDialogCommand:
			ID = "InsertDialogCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class PullDeriveCommand:
			ID = "PullDeriveCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
		class FusionAddEditDecalCommand:
			ID = "FusionAddEditDecalCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class FusionAddCanvasCommand:
			ID = "FusionAddCanvasCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class FusionAddBackgroundCanvasCommand:
			ID = "FusionAddBackgroundCanvasCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionAddBackgroundCanvasCommand:
			ID = "SeparatorAfter_FusionAddBackgroundCanvasCommand"
			Index = 5
		class TSplineImportCommand:
			ID = "TSplineImportCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class SketchImportSVG:
			ID = "SketchImportSVG"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class ImportDxfFileCommand:
			ID = "ImportDxfFileCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class InsertMcMasterCarrComponentCommand:
			ID = "InsertMcMasterCarrComponentCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class ParaMeshInsertAlignCommand:
			ID = "ParaMeshInsertAlignCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = False
	class StopPackagePanel:
		ID = "StopPackagePanel"
		class PackageStop:
			ID = "Package3DStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ReturnLibraryPanel:
		ID = "ReturnLibraryPanel"
		class ReturnLibrary:
			ID = "ReturnLibrary"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class PackagePanel:
		ID = "PackagePanel"
		class PackageInsertCommand:
			ID = "PackageInsertCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PackageFlipCommand:
			ID = "PackageFlipCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PackageMoveCommand:
			ID = "PackageMoveCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class PackagePanel:
		ID = "Package3DPanel"
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PackageGenerator:
			ID = "PackageGenerator"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class cmd_id_Axial:
			ID = "cmd_id_Axial"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_BGA:
			ID = "cmd_id_BGA"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Chip:
			ID = "cmd_id_Chip"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Soic:
			ID = "cmd_id_Soic"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_DFN2:
			ID = "cmd_id_DFN2"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_DFN3:
			ID = "cmd_id_DFN3"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_DFN4:
			ID = "cmd_id_DFN4"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_header_right_angle:
			ID = "cmd_id_header_right_angle"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_header_right_angle_socket:
			ID = "cmd_id_header_right_angle_socket"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_header_straight:
			ID = "cmd_id_header_straight"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_header_straight_socket:
			ID = "cmd_id_header_straight_socket"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Son:
			ID = "cmd_id_Son"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Chip_led:
			ID = "cmd_id_Chip_led"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Qfp:
			ID = "cmd_id_Qfp"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Qfn:
			ID = "cmd_id_Qfn"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_chiparray_2side_convex:
			ID = "cmd_id_chiparray_2side_convex"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_chiparray_2side_flat_concave:
			ID = "cmd_id_chiparray_2side_flat_concave"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_chiparray_4side_flat:
			ID = "cmd_id_chiparray_4side_flat"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_sot143:
			ID = "cmd_id_sot143"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_sot223:
			ID = "cmd_id_sot223"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_sot23:
			ID = "cmd_id_sot23"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_sotfl:
			ID = "cmd_id_sotfl"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Plcc:
			ID = "cmd_id_Plcc"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Oscillator_j:
			ID = "cmd_id_Oscillator_j"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Oscillator_l:
			ID = "cmd_id_Oscillator_l"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Soj:
			ID = "cmd_id_Soj"
			Index = 28
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_crystal:
			ID = "cmd_id_crystal"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_crystal_hc49:
			ID = "cmd_id_crystal_hc49"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_dip:
			ID = "cmd_id_dip"
			Index = 31
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_ecap:
			ID = "cmd_id_ecap"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Melf:
			ID = "cmd_id_Melf"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Molded:
			ID = "cmd_id_Molded"
			Index = 34
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_female_standoff:
			ID = "cmd_id_female_standoff"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_male_female_standoff:
			ID = "cmd_id_male_female_standoff"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Sod:
			ID = "cmd_id_Sod"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Snaplock:
			ID = "cmd_id_Snaplock"
			Index = 38
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Radial:
			ID = "cmd_id_Radial"
			Index = 39
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Radial_Round_Led:
			ID = "cmd_id_Radial_Round_Led"
			Index = 40
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Cornerconcave:
			ID = "cmd_id_Cornerconcave"
			Index = 41
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_Sodfl:
			ID = "cmd_id_Sodfl"
			Index = 42
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_TODPAK:
			ID = "cmd_id_TODPAK"
			Index = 43
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_surafce_mount_header_female:
			ID = "cmd_id_surafce_mount_header_female"
			Index = 44
			isPromoted = False
			isPromotedByDefault = False
		class cmd_id_surface_mount_pin_header_male:
			ID = "cmd_id_surface_mount_pin_header_male"
			Index = 45
			isPromoted = False
			isPromotedByDefault = False
	class MakePanel:
		ID = "MakePanel"
		class ThreeDprintCmdDef:
			ID = "ThreeDprintCmdDef"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class SolidScriptsAddinsPanel:
		ID = "SolidScriptsAddinsPanel"
		class ScriptsManagerCommand:
			ID = "ScriptsManagerCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ExchangeAppStoreCommand:
			ID = "ExchangeAppStoreCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class OpenFoldersseparatorTop:
			ID = "OpenFoldersseparatorTop"
			Index = 2
		class OpenFoldersrootDropdown:
			ID = "OpenFoldersrootDropdown"
			Index = 3
			class OpenFoldersFusionInstall:
				ID = "OpenFoldersFusionInstall"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersFusionApi:
				ID = "OpenFoldersFusionApi"
				Index = 1
				class OpenFoldersFusionApiCpp:
					ID = "OpenFoldersFusionApiCpp"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class OpenFoldersFusionApiPython:
					ID = "OpenFoldersFusionApiPython"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
			class OpenFoldersFusionPython:
				ID = "OpenFoldersFusionPython"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersFusionPythonseparator:
				ID = "OpenFoldersFusionPythonseparator"
				Index = 3
			class OpenFoldersAutodesk:
				ID = "OpenFoldersAutodesk"
				Index = 4
				class OpenFoldersAutodeskLocal:
					ID = "OpenFoldersAutodeskLocal"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class OpenFoldersAutodeskRoaming:
					ID = "OpenFoldersAutodeskRoaming"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
			class OpenFoldersAutodeskseparator:
				ID = "OpenFoldersAutodeskseparator"
				Index = 5
			class OpenFoldersDesktop:
				ID = "OpenFoldersDesktop"
				Index = 6
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersTempFiles:
				ID = "OpenFoldersTempFiles"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAppdata:
				ID = "OpenFoldersAppdata"
				Index = 8
				class OpenFoldersAppdataLocal:
					ID = "OpenFoldersAppdataLocal"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class OpenFoldersAppdataRoaming:
					ID = "OpenFoldersAppdataRoaming"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
			class OpenFoldersAppdataseparator:
				ID = "OpenFoldersAppdataseparator"
				Index = 9
			class OpenFoldersSettings:
				ID = "OpenFoldersSettings"
				Index = 10
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersSettingsseparator:
				ID = "OpenFoldersSettingsseparator"
				Index = 11
		class OpenFoldersrootDropdownUndoc:
			ID = "OpenFoldersrootDropdownUndoc"
			Index = 4
			class OpenFoldersRootDirectory:
				ID = "OpenFoldersRootDirectory"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersExecutableDirectory:
				ID = "OpenFoldersExecutableDirectory"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersLocalizationDirectory:
				ID = "OpenFoldersLocalizationDirectory"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersCoreAddInDirectory:
				ID = "OpenFoldersCoreAddInDirectory"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersStringTableDirectory:
				ID = "OpenFoldersStringTableDirectory"
				Index = 4
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAppDirectory:
				ID = "OpenFoldersAppDirectory"
				Index = 5
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersSharedExtensionDirectory:
				ID = "OpenFoldersSharedExtensionDirectory"
				Index = 6
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersTemporaryDirectory:
				ID = "OpenFoldersTemporaryDirectory"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersUnbrandedUserDataDirectory:
				ID = "OpenFoldersUnbrandedUserDataDirectory"
				Index = 8
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersUserDataDirectory:
				ID = "OpenFoldersUserDataDirectory"
				Index = 9
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAllUsersDataDirectory:
				ID = "OpenFoldersAllUsersDataDirectory"
				Index = 10
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersUnbrandedUserAppPluginsDirectory:
				ID = "OpenFoldersUnbrandedUserAppPluginsDirectory"
				Index = 11
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersBootstrapOptionDirectory:
				ID = "OpenFoldersBootstrapOptionDirectory"
				Index = 12
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersOptionsDirectory:
				ID = "OpenFoldersOptionsDirectory"
				Index = 13
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersCloudCacheDirectory:
				ID = "OpenFoldersCloudCacheDirectory"
				Index = 14
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersScriptsDirectory:
				ID = "OpenFoldersScriptsDirectory"
				Index = 15
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAutorunScriptsDirectory:
				ID = "OpenFoldersAutorunScriptsDirectory"
				Index = 16
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersSamplesScriptsDirectory:
				ID = "OpenFoldersSamplesScriptsDirectory"
				Index = 17
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersProgramDataScriptsDirectory:
				ID = "OpenFoldersProgramDataScriptsDirectory"
				Index = 18
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAppDataScriptsDirectory:
				ID = "OpenFoldersAppDataScriptsDirectory"
				Index = 19
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersManuallyInstalledScriptsDirectory:
				ID = "OpenFoldersManuallyInstalledScriptsDirectory"
				Index = 20
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersMaterialsDirectory:
				ID = "OpenFoldersMaterialsDirectory"
				Index = 21
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersTestTempDirectory:
				ID = "OpenFoldersTestTempDirectory"
				Index = 22
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersScratchDirectory:
				ID = "OpenFoldersScratchDirectory"
				Index = 23
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersResultDirectory:
				ID = "OpenFoldersResultDirectory"
				Index = 24
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersSampleDirectory:
				ID = "OpenFoldersSampleDirectory"
				Index = 25
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAppLogFilePath:
				ID = "OpenFoldersAppLogFilePath"
				Index = 26
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersCacheDirectory:
				ID = "OpenFoldersCacheDirectory"
				Index = 27
				isPromoted = False
				isPromotedByDefault = False
			class OpenFoldersAutoSaveDirectory:
				ID = "OpenFoldersAutoSaveDirectory"
				Index = 28
				isPromoted = False
				isPromotedByDefault = False
		class OpenFoldersseparatorBottom:
			ID = "OpenFoldersseparatorBottom"
			Index = 5
	class UtilityPanel:
		ID = "UtilityPanel"
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class SelectPanel:
		ID = "SelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SelectionToolsDropDown:
			ID = "SelectionToolsDropDown"
			Index = 6
			class SelectByNameCommand:
				ID = "SelectByNameCommand"
				Index = 0
			class SelectByBoundaryCommand:
				ID = "SelectByBoundaryCommand"
				Index = 1
			class FusionSelectBodiesBySizeCommand:
				ID = "FusionSelectBodiesBySizeCommand"
				Index = 2
			class SelectByInvertCommand:
				ID = "SelectByInvertCommand"
				Index = 3
		class SeparatorAfter_SelectionToolsDropDown:
			ID = "SeparatorAfter_SelectionToolsDropDown"
			Index = 7
		class FusionDragCompControlsCmd:
			ID = "FusionDragCompControlsCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class thomasa88_NoComponentDrag_Enable:
			ID = "thomasa88_NoComponentDrag_Enable"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDragCompControlsCmd:
			ID = "SeparatorAfter_FusionDragCompControlsCmd"
			Index = 10
		class SelectionPriorityCommandsDropDown:
			ID = "SelectionPriorityCommandsDropDown"
			Index = 11
			class SelectBodyPriorityCommand:
				ID = "SelectBodyPriorityCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class SelectFacePriorityCommand:
				ID = "SelectFacePriorityCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class SelectEdgePriorityCommand:
				ID = "SelectEdgePriorityCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class SelectComponentPriorityCommand:
				ID = "SelectComponentPriorityCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
	class NewPanel:
		ID = "NewPanel"
		class NC1:
			ID = "NC1"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class NC4:
			ID = "NC4"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class NC8:
			ID = "NC8"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class NC7:
			ID = "NC7"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class NC11:
			ID = "NC11"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class uuid_7f8371cc_20b6_4d72_b138_8a0afa782f1c:
			ID = "7f8371cc-20b6-4d72-b138-8a0afa782f1c"
			Index = 5
		class NC2:
			ID = "NC2"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class NC3:
			ID = "NC3"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class NC6:
			ID = "NC6"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class NC5:
			ID = "NC5"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class uuid_63f02fba_311d_4269_89c3_7195c7fe12aa:
			ID = "63f02fba-311d-4269-89c3-7195c7fe12aa"
			Index = 10
		class NC9:
			ID = "NC9"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class NC10:
			ID = "NC10"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
	class MeshSelectPanel:
		ID = "MeshSelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SeparatorAfter_SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_SeparatorAfter_selectPaint"
			Index = 6
		class FusionShowSelectionPanelCmd:
			ID = "FusionShowSelectionPanelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionShowSelectionPanelCmd:
			ID = "SeparatorAfter_FusionShowSelectionPanelCmd"
			Index = 8
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
	class StopSketchPanel:
		ID = "StopSketchPanel"
		class SketchStop:
			ID = "SketchStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopBaseFeaturePanel:
		ID = "StopBaseFeaturePanel"
		class BaseFeatureStop:
			ID = "BaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopTSplineBaseFeaturePanel:
		ID = "StopTSplineBaseFeaturePanel"
		class TSplineBaseFeatureStop:
			ID = "TSplineBaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopMeshBaseFeaturePanel:
		ID = "StopMeshBaseFeaturePanel"
		class MeshBaseFeatureStop:
			ID = "MeshBaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class SnapshotPanel:
		ID = "SnapshotPanel"
		class SnapshotCmd:
			ID = "SnapshotCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class AsBuiltPositionsCmd:
			ID = "AsBuiltPositionsCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class FinishSnapshotEditPanel:
		ID = "FinishSnapshotEditPanel"
		class SnapshotEditAccept:
			ID = "SnapshotEditAccept"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SnapshotEditCancel:
			ID = "SnapshotEditCancel"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
	class SnapshotSolidModifyPanel:
		ID = "SnapshotSolidModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionShellBodyCommand:
			ID = "FusionShellBodyCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionDraftCommand:
			ID = "FusionDraftCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class ModifyScale:
			ID = "ModifyScale"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class FusionCombineCommand:
			ID = "FusionCombineCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionReplaceFaceCommand:
			ID = "FusionReplaceFaceCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class FusionPartingLineSplitCmd:
			ID = "FusionPartingLineSplitCmd"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionPartingLineSplitCmd:
			ID = "SeparatorAfter_FusionPartingLineSplitCmd"
			Index = 14
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
		class AlignCmd:
			ID = "AlignCmd"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 18
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 21
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 23
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
	class SheetmetalRefoldPanel:
		ID = "SheetmetalRefoldPanel"
		class FusionSheetmetalRefoldCommand:
			ID = "FusionSheetmetalRefoldCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopPCBPanel:
		ID = "StopPCBPanel"
		class PCBStop:
			ID = "PCBStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ReturnPanel:
		ID = "ReturnPanel"
		class ReturnToEnvironmentCommand:
			ID = "ReturnToEnvironmentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ReturnToExternalAppCmdDefINV:
			ID = "ReturnToExternalAppCmdDefINV"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class ReturnToExternalAppCmdDefACAD:
			ID = "ReturnToExternalAppCmdDefACAD"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ReturnToExternalAppCmdDefMoldflow:
			ID = "ReturnToExternalAppCmdDefMoldflow"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class RenderSetupPanel:
		ID = "RenderSetupPanel"
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class RenderingEnvCmd:
			ID = "RenderingEnvCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionAddEditDecalCommand:
			ID = "FusionAddEditDecalCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class TextureMappingCommand:
			ID = "TextureMappingCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class InCanvasRenderPanel:
		ID = "InCanvasRenderPanel"
		class InCanvasRenderCommand:
			ID = "InCanvasRenderCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class InCanvasRenderSettingsCommand:
			ID = "InCanvasRenderSettingsCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class SaveAsImageCommand:
			ID = "SaveAsImageCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class RenderPanel:
		ID = "RenderPanel"
		class A360RenderCommand:
			ID = "A360RenderCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ToolsPanel:
		ID = "ToolsPanel"
		class selectWindow:
			ID = "selectWindow"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class AssignPanel:
		ID = "AssignPanel"
		class PIMAssignItemNumberCmd:
			ID = "PIMAssignItemNumberCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ReleasePanel:
		ID = "ReleasePanel"
		class PIMQuickReleaseCmd:
			ID = "PIMQuickReleaseCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PIMECOReleaseCmd:
			ID = "PIMECOReleaseCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
	class NESTPanel:
		ID = "NESTPanel"
		class MSFNestAuthoringCmd:
			ID = "MSFNestAuthoringCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
	class ParaMeshCreatePanel:
		ID = "ParaMeshCreatePanel"
		class ParaMeshInsertAlignCommand:
			ID = "ParaMeshInsertAlignCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshTessellateCommand:
			ID = "ParaMeshTessellateCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_ParaMeshTessellateCommand:
			ID = "SeparatorAfter_ParaMeshTessellateCommand"
			Index = 2
		class ParaMeshPlanarSectionCommand:
			ID = "ParaMeshPlanarSectionCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class ParaMeshPreparePanel:
		ID = "ParaMeshPreparePanel"
		class ParaMeshRepairCommand:
			ID = "ParaMeshRepairCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshCalculateFaceGroupsCommand:
			ID = "ParaMeshCalculateFaceGroupsCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshMergeFaceGroupsCommand:
			ID = "ParaMeshMergeFaceGroupsCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshCreateFaceGroupCommand:
			ID = "ParaMeshCreateFaceGroupCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
	class ParaMeshModifyPanel:
		ID = "ParaMeshModifyPanel"
		class ParaMeshBaseFeatureCreateCommand:
			ID = "ParaMeshBaseFeatureCreateCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshRemeshCommand:
			ID = "ParaMeshRemeshCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshReduceCommand:
			ID = "ParaMeshReduceCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshPlaneCutCommand:
			ID = "ParaMeshPlaneCutCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshHollowCommand:
			ID = "ParaMeshHollowCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshCombineCommand:
			ID = "ParaMeshCombineCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshSmoothCommand:
			ID = "ParaMeshSmoothCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class ParaMeshReverseNormalsCommand:
			ID = "ParaMeshReverseNormalsCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class ParaMeshEraseAndFillCommand:
			ID = "ParaMeshEraseAndFillCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_ParaMeshEraseAndFillCommand:
			ID = "SeparatorAfter_ParaMeshEraseAndFillCommand"
			Index = 9
		class ParaMeshExtractCommand:
			ID = "ParaMeshExtractCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_ParaMeshExtractCommand:
			ID = "SeparatorAfter_ParaMeshExtractCommand"
			Index = 11
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 12
			isPromoted = True
			isPromotedByDefault = True
		class ParaMeshScaleCommand:
			ID = "ParaMeshScaleCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 15
		class ParaMeshConvertCommand:
			ID = "ParaMeshConvertCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class ParaMeshLatticeCommand:
			ID = "ParaMeshLatticeCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
		class ParaMeshToQuadMeshCommand:
			ID = "ParaMeshToQuadMeshCommand"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_ParaMeshToQuadMeshCommand:
			ID = "SeparatorAfter_ParaMeshToQuadMeshCommand"
			Index = 19
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_AppearanceCommand:
			ID = "SeparatorAfter_AppearanceCommand"
			Index = 22
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
	class ParaMeshSelectPanel:
		ID = "ParaMeshSelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SeparatorAfter_SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_SeparatorAfter_selectPaint"
			Index = 6
		class ParaMeshShowSelectionPanelCmd:
			ID = "ParaMeshShowSelectionPanelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_ParaMeshShowSelectionPanelCmd:
			ID = "SeparatorAfter_ParaMeshShowSelectionPanelCmd"
			Index = 8
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
	class ParaMeshExportPanel:
		ID = "ParaMeshExportPanel"
		class ParaMeshExportCommand:
			ID = "ParaMeshExportCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ThreeDprintCmdDef:
			ID = "ThreeDprintCmdDef"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
	class ParaMeshBaseFeatureStopPanel:
		ID = "ParaMeshBaseFeatureStopPanel"
		class ParaMeshBaseFeatureStopCommand:
			ID = "ParaMeshBaseFeatureStopCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class zxynine_anyMacroPanel:
		ID = "zxynine_anyMacroPanel"
		class zxynine_anyMacroDropdown:
			ID = "zxynine_anyMacroDropdown"
			Index = 0
			class zxynine_anyMacroList:
				ID = "zxynine_anyMacroList"
				Index = 0
				isPromoted = True
				isPromotedByDefault = True
			class zxynine_anyMacroClearRecord:
				ID = "zxynine_anyMacroClearRecord"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class zxynine_anyMacroBuildMacro:
				ID = "zxynine_anyMacroBuildMacro"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class zxynine_anyMacroList_Seperator:
				ID = "zxynine_anyMacroList_Seperator"
				Index = 3
		class zxynine_anyMacroPremadeMacrosDropdown:
			ID = "zxynine_anyMacroPremadeMacrosDropdown"
			Index = 1
			class zxynine_anyMacroListEmpty:
				ID = "zxynine_anyMacroListEmpty"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class zxynine_anyMacroListEmpty_Seperator:
				ID = "zxynine_anyMacroListEmpty_Seperator"
				Index = 1
			class AnyMacro_Builtin_Align_Camera_group:
				ID = "AnyMacro_Builtin_Align_Camera_group"
				Index = 2
				class AnyMacro_Builtin_Align_Camera:
					ID = "AnyMacro_Builtin_Align_Camera"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class AnyMacro_Builtin_Align_Camera_delete:
					ID = "AnyMacro_Builtin_Align_Camera_delete"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
		class zxynine_anyMacroHaltFire:
			ID = "zxynine_anyMacroHaltFire"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class zxynine_anyMacroBlockConsecutive:
			ID = "zxynine_anyMacroBlockConsecutive"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
	class thomasa88_anyShortcutPanel:
		ID = "thomasa88_anyShortcutPanel"
		class thomasa88_anyShortcutPremadeDropdown:
			ID = "thomasa88_anyShortcutPremadeDropdown"
			Index = 0
			class thomasa88_anyShortcutListLookAtSketchCommand:
				ID = "thomasa88_anyShortcutListLookAtSketchCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutListLookAtSketchOrSelectedCommand:
				ID = "thomasa88_anyShortcutListLookAtSketchOrSelectedCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutListActivateContainingOrComponentCommand:
				ID = "thomasa88_anyShortcutListActivateContainingOrComponentCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinRepeatCommand:
				ID = "thomasa88_anyShortcutBuiltinRepeatCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinAlignView:
				ID = "thomasa88_anyShortcutBuiltinAlignView"
				Index = 4
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinChangeView:
				ID = "thomasa88_anyShortcutBuiltinChangeView"
				Index = 5
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinChangeAlignView:
				ID = "thomasa88_anyShortcutBuiltinChangeAlignView"
				Index = 6
				isPromoted = False
				isPromotedByDefault = False
			class tion_buttonTest:
				ID = "tion_buttonTest"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinTimelineList:
				ID = "thomasa88_anyShortcutBuiltinTimelineList"
				Index = 8
				class thomasa88_anyShortcutListRollToBeginning:
					ID = "thomasa88_anyShortcutListRollToBeginning"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutListRollBack:
					ID = "thomasa88_anyShortcutListRollBack"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutListRollForward:
					ID = "thomasa88_anyShortcutListRollForward"
					Index = 2
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutListRollToEnd:
					ID = "thomasa88_anyShortcutListRollToEnd"
					Index = 3
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutListHistoryPlay:
					ID = "thomasa88_anyShortcutListHistoryPlay"
					Index = 4
					isPromoted = False
					isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinViewList:
				ID = "thomasa88_anyShortcutBuiltinViewList"
				Index = 9
				class thomasa88_anyShortcutBuiltinViewFront:
					ID = "thomasa88_anyShortcutBuiltinViewFront"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinViewBack:
					ID = "thomasa88_anyShortcutBuiltinViewBack"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinViewTop:
					ID = "thomasa88_anyShortcutBuiltinViewTop"
					Index = 2
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinViewBottom:
					ID = "thomasa88_anyShortcutBuiltinViewBottom"
					Index = 3
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinViewLeft:
					ID = "thomasa88_anyShortcutBuiltinViewLeft"
					Index = 4
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinViewRight:
					ID = "thomasa88_anyShortcutBuiltinViewRight"
					Index = 5
					isPromoted = False
					isPromotedByDefault = False
			class thomasa88_anyShortcutBuiltinCornerViewList:
				ID = "thomasa88_anyShortcutBuiltinCornerViewList"
				Index = 10
				class thomasa88_anyShortcutBuiltinCornerViewListIsoTopRight:
					ID = "thomasa88_anyShortcutBuiltinCornerViewListIsoTopRight"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinCornerViewListIsoTopLeft:
					ID = "thomasa88_anyShortcutBuiltinCornerViewListIsoTopLeft"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinCornerViewListIsoBottomRight:
					ID = "thomasa88_anyShortcutBuiltinCornerViewListIsoBottomRight"
					Index = 2
					isPromoted = False
					isPromotedByDefault = False
				class thomasa88_anyShortcutBuiltinCornerViewListIsoBottomLeft:
					ID = "thomasa88_anyShortcutBuiltinCornerViewListIsoBottomLeft"
					Index = 3
					isPromoted = False
					isPromotedByDefault = False
		class thomasa88_anyShortcutDropdown:
			ID = "thomasa88_anyShortcutDropdown"
			Index = 1
			class thomasa88_anyShortcutList:
				ID = "thomasa88_anyShortcutList"
				Index = 0
				isPromoted = True
				isPromotedByDefault = True
			class uuid_26c8ae4d_d59b_4d1a_8f3b_2ec854ea0357:
				ID = "26c8ae4d-d59b-4d1a-8f3b-2ec854ea0357"
				Index = 1
	class ViewsPanel:
		ID = "ViewsPanel"
		class FusionDrawingViewBaseCommand:
			ID = "FusionDrawingViewBaseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewBaseTemplateCommand:
			ID = "FusionDrawingViewBaseTemplateCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewProjectCommand:
			ID = "FusionDrawingViewProjectCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewProjectTemplateCommand:
			ID = "FusionDrawingViewProjectTemplateCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewSimpleSectionCommand:
			ID = "FusionDrawingViewSimpleSectionCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewSectionCommand:
			ID = "FusionDrawingViewSectionCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingViewDetailCommand:
			ID = "FusionDrawingViewDetailCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingViewDetailCommand:
			ID = "SeparatorAfter_FusionDrawingViewDetailCommand"
			Index = 7
		class FusionBrokenViewCommand:
			ID = "FusionBrokenViewCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionBrokenViewCommand:
			ID = "SeparatorAfter_FusionBrokenViewCommand"
			Index = 9
		class FusionDrawingSketchCommand:
			ID = "FusionDrawingSketchCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
	class DrawingPanel:
		ID = "DrawingPanel"
		class FusionDrawingLineCommand:
			ID = "FusionDrawingLineCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingRectangleCommand:
			ID = "FusionDrawingRectangleCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingCircleCommand:
			ID = "FusionDrawingCircleCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingArcCommand:
			ID = "FusionDrawingArcCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingArrowCommand:
			ID = "FusionDrawingArrowCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class ModifyPanel:
		ID = "ModifyPanel"
		class FusionDrawingMoveCmd:
			ID = "FusionDrawingMoveCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDocRotateCmd:
			ID = "FusionDocRotateCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingCopyCommand:
			ID = "FusionDrawingCopyCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingTrimCommand:
			ID = "FusionDrawingTrimCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingExtendCommand:
			ID = "FusionDrawingExtendCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingOffsetCommand:
			ID = "FusionDrawingOffsetCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingEraseCmd:
			ID = "FusionDrawingEraseCmd"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
	class GeometryPanel:
		ID = "GeometryPanel"
		class FusionDrawingCenterlineCommand:
			ID = "FusionDrawingCenterlineCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingCentermarkCommand:
			ID = "FusionDrawingCentermarkCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingCenterPatternCommand:
			ID = "FusionDrawingCenterPatternCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingCenterPatternCommand:
			ID = "SeparatorAfter_FusionDrawingCenterPatternCommand"
			Index = 3
		class FusionDrawingEdgeExtensionCmd:
			ID = "FusionDrawingEdgeExtensionCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
	class DimensionsPanel:
		ID = "DimensionsPanel"
		class FusionDrawingSingleDimensionCmd:
			ID = "FusionDrawingSingleDimensionCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingOrdinateDimensionCmd:
			ID = "FusionDrawingOrdinateDimensionCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingOrdinateDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingOrdinateDimensionCmd"
			Index = 2
		class FusionDrawingLinearDimensionCmd:
			ID = "FusionDrawingLinearDimensionCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingAlignedDimensionCmd:
			ID = "FusionDrawingAlignedDimensionCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingAngularDimensionCmd:
			ID = "FusionDrawingAngularDimensionCmd"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingRadialDimensionCmd:
			ID = "FusionDrawingRadialDimensionCmd"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingDiameterDimensionCmd:
			ID = "FusionDrawingDiameterDimensionCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDrawingDiameterDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingDiameterDimensionCmd"
			Index = 8
		class FusionDrawingBaselineDimensionCmd:
			ID = "FusionDrawingBaselineDimensionCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingChainDimensionCmd:
			ID = "FusionDrawingChainDimensionCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDrawingChainDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingChainDimensionCmd"
			Index = 11
		class FusionDrawingDimensionBreakCmd:
			ID = "FusionDrawingDimensionBreakCmd"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
	class TextPanel:
		ID = "TextPanel"
		class FusionDrawingMTextCommand:
			ID = "FusionDrawingMTextCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingMTextCommand:
			ID = "SeparatorAfter_FusionDrawingMTextCommand"
			Index = 1
		class FusionDrawingNoteCommand:
			ID = "FusionDrawingNoteCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingLeaderCommand:
			ID = "FusionDrawingLeaderCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingHoleThreadNoteLeaderCommand:
			ID = "FusionDrawingHoleThreadNoteLeaderCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingBendNoteLeaderCommand:
			ID = "FusionDrawingBendNoteLeaderCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingAttDefCommand:
			ID = "FusionDrawingAttDefCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
	class InspectPanel:
		ID = "InspectPanel"
		class FusionDrawingMeasureCommand:
			ID = "FusionDrawingMeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class SymbolsPanel:
		ID = "SymbolsPanel"
		class FusionDrawingSurfaceTextureCmd:
			ID = "FusionDrawingSurfaceTextureCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingSurfaceTextureCmd:
			ID = "SeparatorAfter_FusionDrawingSurfaceTextureCmd"
			Index = 1
		class FusionDrawingFeatureControlFrameCmd:
			ID = "FusionDrawingFeatureControlFrameCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingDatumIdCmd:
			ID = "FusionDrawingDatumIdCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingDatumIdCmd:
			ID = "SeparatorAfter_FusionDrawingDatumIdCmd"
			Index = 4
		class FusionDrawingWeldSymbolCmd:
			ID = "FusionDrawingWeldSymbolCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingTaperSlopeSymbolCmd:
			ID = "FusionDrawingTaperSlopeSymbolCmd"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
	class InsertPanel:
		ID = "InsertPanel"
		class FusionDrawingImageInsertCommand:
			ID = "FusionDrawingImageInsertCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingBlockEditorImageInsertCommand:
			ID = "FusionDrawingBlockEditorImageInsertCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingTemplateImageInsertCommand:
			ID = "FusionDrawingTemplateImageInsertCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class BillOfMaterialsPanel:
		ID = "BillOfMaterialsPanel"
		class FusionDrawingCreatePartsListCommand:
			ID = "FusionDrawingCreatePartsListCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingNewTableCommand:
			ID = "FusionDrawingNewTableCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingNewTableTemplateCommand:
			ID = "FusionDrawingNewTableTemplateCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingEmptyTableCommand:
			ID = "FusionDrawingEmptyTableCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDrawingEmptyTableCommand:
			ID = "SeparatorAfter_FusionDrawingEmptyTableCommand"
			Index = 4
		class FusionDrawingPartsListTableCommand:
			ID = "FusionDrawingPartsListTableCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingBalloonCommand:
			ID = "FusionDrawingBalloonCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
		class SeparatorAfter_FusionDrawingBalloonCommand:
			ID = "SeparatorAfter_FusionDrawingBalloonCommand"
			Index = 7
		class FusionDrawingBendTableCommand:
			ID = "FusionDrawingBendTableCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingBendIDCommand:
			ID = "FusionDrawingBendIDCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDrawingBendIDCommand:
			ID = "SeparatorAfter_FusionDrawingBendIDCommand"
			Index = 10
		class FusionDrawingRevisionTableCommand:
			ID = "FusionDrawingRevisionTableCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingRevMarkerCommand:
			ID = "FusionDrawingRevMarkerCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class FusionDocRevCloudCommand:
			ID = "FusionDocRevCloudCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
		class SeparatorAfter_FusionDocRevCloudCommand:
			ID = "SeparatorAfter_FusionDocRevCloudCommand"
			Index = 14
		class FusionDrawingRenumberCommand:
			ID = "FusionDrawingRenumberCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingAlignBalloonCommand:
			ID = "FusionDrawingAlignBalloonCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
	class BlockPanel:
		ID = "BlockPanel"
		class FusionDrawingBlockCloseCommand:
			ID = "FusionDrawingBlockCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingBorderCloseCommand:
			ID = "FusionDrawingBorderCloseCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class FusionDrawingSketchCloseCommand:
			ID = "FusionDrawingSketchCloseCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class StopBlockEditPanel:
		ID = "StopBlockEditPanel"
		class FusionDrawingBlockCloseCommand:
			ID = "FusionDrawingBlockCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopBorderEditPanel:
		ID = "StopBorderEditPanel"
		class FusionDrawingBorderCloseCommand:
			ID = "FusionDrawingBorderCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class StopSketchEditPanel:
		ID = "StopSketchEditPanel"
		class FusionDrawingSketchCloseCommand:
			ID = "FusionDrawingSketchCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class OutputPanel:
		ID = "OutputPanel"
		class FusionDrawingExportPDFCommand:
			ID = "FusionDrawingExportPDFCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class ExportFusionDrawingDocumentCommand:
			ID = "ExportFusionDrawingDocumentCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingExportDXFCommand:
			ID = "FusionDrawingExportDXFCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
		class ExportFusionDrawingTemplateCommand:
			ID = "ExportFusionDrawingTemplateCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingExportPartsListCommand:
			ID = "FusionDrawingExportPartsListCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class FusionDrawingDebugCommand:
			ID = "FusionDrawingDebugCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
	class AssignPanel:
		ID = "AssignPanel"
		class PIMAssignItemNumberCmd:
			ID = "PIMAssignItemNumberCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class ReleasePanel:
		ID = "ReleasePanel"
		class PIMQuickReleaseCmd:
			ID = "PIMQuickReleaseCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PIMECOReleaseCmd:
			ID = "PIMECOReleaseCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
class AllTabs:
	class MillingTab:
		ID = "MillingTab"
		class CAMJobPanel (AllPanels.CAMJobPanel):
			Index = 0
		class CAM2DPanel (AllPanels.CAM2DPanel):
			Index = 4
		class CAMPanel (AllPanels.CAMPanel):
			Index = 5
		class CAMDrillingPanel (AllPanels.CAMDrillingPanel):
			Index = 7
		class CAMMultiAxisPanel (AllPanels.CAMMultiAxisPanel):
			Index = 8
		class CAMDEDPanel (AllPanels.CAMDEDPanel):
			Index = 13
		class CAMEditPanel (AllPanels.CAMEditPanel):
			Index = 6
		class CAMActionPanel (AllPanels.CAMActionPanel):
			Index = 30
		class CAMManagePanel (AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class TurningTab:
		ID = "TurningTab"
		class CAMJobPanel (AllPanels.CAMJobPanel):
			Index = 0
		class CAMTurningPanel (AllPanels.CAMTurningPanel):
			Index = 9
		class CAMDrillingPanel (AllPanels.CAMDrillingPanel):
			Index = 7
		class CAMActionPanel (AllPanels.CAMActionPanel):
			Index = 30
		class CAMManagePanel (AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class AdditiveTab:
		ID = "AdditiveTab"
		class CAMAdditiveJobPanel (AllPanels.CAMAdditiveJobPanel):
			Index = 2
		class CAMAdditivePositioningPanel (AllPanels.CAMAdditivePositioningPanel):
			Index = 3
		class CAMAdditivePrintProfilePanel (AllPanels.CAMAdditivePrintProfilePanel):
			Index = 32
		class CAMInfillPanel (AllPanels.CAMInfillPanel):
			Index = 11
		class CAMSupportsPanel (AllPanels.CAMSupportsPanel):
			Index = 12
		class CAMDEDPanel (AllPanels.CAMDEDPanel):
			Index = 13
		class CAMEditPanel (AllPanels.CAMEditPanel):
			Index = 6
		class CAMAdditiveProcessSimPanel (AllPanels.CAMAdditiveProcessSimPanel):
			Index = 14
		class CAMAdditiveActionPanel (AllPanels.CAMAdditiveActionPanel):
			Index = 33
		class CAMAdditiveManagePanel (AllPanels.CAMAdditiveManagePanel):
			Index = 36
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class AdditiveResultsTab:
		ID = "AdditiveResultsTab"
		class CAMAdditiveProcessSimResultsPanel (AllPanels.CAMAdditiveProcessSimResultsPanel):
			Index = 15
		class CAMAdditiveProcessSimActionPanel (AllPanels.CAMAdditiveProcessSimActionPanel):
			Index = 16
		class CAMAdditiveProcessSimFinishPanel (AllPanels.CAMAdditiveProcessSimFinishPanel):
			Index = 17
	class ProbingTab:
		ID = "ProbingTab"
		class CAMJobPanel (AllPanels.CAMJobPanel):
			Index = 0
		class CAMProbingPanel (AllPanels.CAMProbingPanel):
			Index = 18
		class CAMCMMPanel (AllPanels.CAMCMMPanel):
			Index = 19
		class CAMManualInspectionPanel (AllPanels.CAMManualInspectionPanel):
			Index = 20
		class CAMProbingActionPanel (AllPanels.CAMProbingActionPanel):
			Index = 31
		class CAMManagePanel (AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class FabricationTab:
		ID = "FabricationTab"
		class ManufacturingSourcesPanel (AllPanels.ManufacturingSourcesPanel):
			Index = 40
		class NESTPanel (AllPanels.NESTPanel):
			Index = 43
		class CAMJobPanel (AllPanels.CAMJobPanel):
			Index = 0
		class CAMWLPCPanel (AllPanels.CAMWLPCPanel):
			Index = 10
		class CAMActionPanel (AllPanels.CAMActionPanel):
			Index = 30
		class FabricationManagePanel (AllPanels.FabricationManagePanel):
			Index = 41
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class UtilitiesTab:
		ID = "UtilitiesTab"
		class CAMInProcessStockPanel (AllPanels.CAMInProcessStockPanel):
			Index = 1
		class CAMManagePanel (AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel (AllPanels.CAMInspectPanel):
			Index = 34
		class CAMScriptsAddinsPanel (AllPanels.CAMScriptsAddinsPanel):
			Index = 38
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
		class MachineBuilderActivationPanel (AllPanels.MachineBuilderActivationPanel):
			Index = 42
	class PartAlignmentTab:
		ID = "PartAlignmentTab"
		class CAMPartAlignmentEditPanel (AllPanels.CAMPartAlignmentEditPanel):
			Index = 21
		class CAMPartAlignmentInspectPanel (AllPanels.CAMPartAlignmentInspectPanel):
			Index = 22
		class CAMPartAlignmentPostPanel (AllPanels.CAMPartAlignmentPostPanel):
			Index = 23
		class CAMPartAlignmentResultsPanel (AllPanels.CAMPartAlignmentResultsPanel):
			Index = 25
		class CAMPartAlignmentPostAndExitPanel (AllPanels.CAMPartAlignmentPostAndExitPanel):
			Index = 27
		class CAMPartAlignmentFinishPanel (AllPanels.CAMPartAlignmentFinishPanel):
			Index = 28
	class LiveAlignmentTab:
		ID = "LiveAlignmentTab"
		class CAMPartAlignmentEditPanel (AllPanels.CAMPartAlignmentEditPanel):
			Index = 21
		class CAMPartAlignmentInspectPanel (AllPanels.CAMPartAlignmentInspectPanel):
			Index = 22
		class CAMLiveAlignmentPostPanel (AllPanels.CAMLiveAlignmentPostPanel):
			Index = 24
		class CAMLiveAlignmentResultsPanel (AllPanels.CAMLiveAlignmentResultsPanel):
			Index = 26
		class CAMLiveAlignmentFinishPanel (AllPanels.CAMLiveAlignmentFinishPanel):
			Index = 29
	class FeaturesTab:
		ID = "FeaturesTab"
		class CAMGeometryFeatures (AllPanels.CAMGeometryFeatures):
			Index = 37
		class SelectPanel (AllPanels.SelectPanel):
			Index = 39
	class MfgSolidTab:
		ID = "MfgSolidTab"
		class WMDComponentsManagerPanel (AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 4
		class GeneratePanel (AllPanels.GeneratePanel):
			Index = 5
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 6
		class WMDComponentsPanel (AllPanels.WMDComponentsPanel):
			Index = 46
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel (AllPanels.FinishPreparePanel):
			Index = 47
	class MfgSurfaceTab:
		ID = "MfgSurfaceTab"
		class WMDComponentsManagerPanel (AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 12
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 13
		class WMDComponentsPanel (AllPanels.WMDComponentsPanel):
			Index = 46
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel (AllPanels.FinishPreparePanel):
			Index = 47
	class MfgParaMeshOuterTab:
		ID = "MfgParaMeshOuterTab"
		class WMDComponentsManagerPanel (AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class ParaMeshCreatePanel (AllPanels.ParaMeshCreatePanel):
			Index = 40
		class ParaMeshPreparePanel (AllPanels.ParaMeshPreparePanel):
			Index = 41
		class ParaMeshModifyPanel (AllPanels.ParaMeshModifyPanel):
			Index = 42
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class ParaMeshSelectPanel (AllPanels.ParaMeshSelectPanel):
			Index = 43
		class ParaMeshExportPanel (AllPanels.ParaMeshExportPanel):
			Index = 44
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel (AllPanels.FinishPreparePanel):
			Index = 47
	class MfgFormTab:
		ID = "MfgFormTab"
		class TSplinePrimitivePanel (AllPanels.TSplinePrimitivePanel):
			Index = 14
		class TSplineModifyPanel (AllPanels.TSplineModifyPanel):
			Index = 15
		class TSplineSymmetryPanel (AllPanels.TSplineSymmetryPanel):
			Index = 16
		class TSplineUtilitiesPanel (AllPanels.TSplineUtilitiesPanel):
			Index = 17
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class StopTSplineBaseFeaturePanel (AllPanels.StopTSplineBaseFeaturePanel):
			Index = 33
	class MfgToolsTab:
		ID = "MfgToolsTab"
		class MakePanel (AllPanels.MakePanel):
			Index = 26
		class SolidScriptsAddinsPanel (AllPanels.SolidScriptsAddinsPanel):
			Index = 27
		class UtilityPanel (AllPanels.UtilityPanel):
			Index = 28
		class ToolsInspectPanel (AllPanels.ToolsInspectPanel):
			Index = 23
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel (AllPanels.FinishPreparePanel):
			Index = 47
	class MfgLbrPackageTab:
		ID = "MfgLbrPackage3DTab"
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class ReturnLibraryPanel (AllPanels.ReturnLibraryPanel):
			Index = 25
	class MfgBasefeatureSolidTab:
		ID = "MfgBasefeatureSolidTab"
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 4
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 6
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class StopBaseFeaturePanel (AllPanels.StopBaseFeaturePanel):
			Index = 32
	class MfgBasefeatureSurfaceTab:
		ID = "MfgBasefeatureSurfaceTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 12
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 13
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class StopBaseFeaturePanel (AllPanels.StopBaseFeaturePanel):
			Index = 32
	class MfgSketchTab:
		ID = "MfgSketchTab"
		class SketchCreatePanel (AllPanels.SketchCreatePanel):
			Index = 0
		class SketchModifyPanel (AllPanels.SketchModifyPanel):
			Index = 2
		class SketchConstraintsPanel (AllPanels.SketchConstraintsPanel):
			Index = 3
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class InsertPanel (AllPanels.InsertPanel):
			Index = 24
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class StopSketchPanel (AllPanels.StopSketchPanel):
			Index = 31
	class MfgEditSnapshotTab:
		ID = "MfgEditSnapshotTab"
		class SnapshotSolidModifyPanel (AllPanels.SnapshotSolidModifyPanel):
			Index = 37
		class InspectPanel (AllPanels.InspectPanel):
			Index = 21
		class SelectPanel (AllPanels.SelectPanel):
			Index = 29
		class FinishSnapshotEditPanel (AllPanels.FinishSnapshotEditPanel):
			Index = 36
	class Animation:
		ID = "Animation"
		class StoryboardPanel (AllPanels.StoryboardPanel):
			Index = 0
		class ComponentPanel (AllPanels.ComponentPanel):
			Index = 1
		class AnnotationPanel (AllPanels.AnnotationPanel):
			Index = 2
		class PublisherViewPanel (AllPanels.PublisherViewPanel):
			Index = 3
		class PublishVideoPanel (AllPanels.PublishVideoPanel):
			Index = 4
	class SolidTab:
		ID = "SolidTab"
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 7
		class GeneratePanel (AllPanels.GeneratePanel):
			Index = 8
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 9
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 44
	class SurfaceTab:
		ID = "SurfaceTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 15
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 16
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 44
	class ParaMeshOuterTab:
		ID = "ParaMeshOuterTab"
		class ParaMeshCreatePanel (AllPanels.ParaMeshCreatePanel):
			Index = 57
		class ParaMeshPreparePanel (AllPanels.ParaMeshPreparePanel):
			Index = 58
		class ParaMeshModifyPanel (AllPanels.ParaMeshModifyPanel):
			Index = 59
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class ParaMeshSelectPanel (AllPanels.ParaMeshSelectPanel):
			Index = 60
		class ParaMeshExportPanel (AllPanels.ParaMeshExportPanel):
			Index = 61
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 44
	class FormTab:
		ID = "FormTab"
		class TSplinePrimitivePanel (AllPanels.TSplinePrimitivePanel):
			Index = 17
		class TSplineModifyPanel (AllPanels.TSplineModifyPanel):
			Index = 18
		class TSplineSymmetryPanel (AllPanels.TSplineSymmetryPanel):
			Index = 19
		class TSplineUtilitiesPanel (AllPanels.TSplineUtilitiesPanel):
			Index = 20
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopTSplineBaseFeaturePanel (AllPanels.StopTSplineBaseFeaturePanel):
			Index = 42
	class SheetMetalTab:
		ID = "SheetMetalTab"
		class SheetMetalCreatePanel (AllPanels.SheetMetalCreatePanel):
			Index = 10
		class SheetMetalModifyPanel (AllPanels.SheetMetalModifyPanel):
			Index = 11
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class SheetmetalRefoldPanel (AllPanels.SheetmetalRefoldPanel):
			Index = 47
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 44
	class ToolsTab:
		ID = "ToolsTab"
		class MakePanel (AllPanels.MakePanel):
			Index = 35
		class NESTPanel (AllPanels.NESTPanel):
			Index = 56
		class SolidScriptsAddinsPanel (AllPanels.SolidScriptsAddinsPanel):
			Index = 36
		class UtilityPanel (AllPanels.UtilityPanel):
			Index = 37
		class ToolsInspectPanel (AllPanels.ToolsInspectPanel):
			Index = 29
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel (AllPanels.SnapshotPanel):
			Index = 44
		class NewPanel (AllPanels.NewPanel):
			Index = 63
		class zxynine_anyMacroPanel (AllPanels.zxynine_anyMacroPanel):
			Index = 64
		class thomasa88_anyShortcutPanel (AllPanels.thomasa88_anyShortcutPanel):
			Index = 65
	class ManageTab:
		ID = "ManageTab"
		class AssignPanel (AllPanels.AssignPanel):
			Index = 54
		class ReleasePanel (AllPanels.ReleasePanel):
			Index = 55
	class PCBTab:
		ID = "PCBTab"
		class PCBCreatePanel (AllPanels.PCBCreatePanel):
			Index = 23
		class PCBModifyPanel (AllPanels.PCBModifyPanel):
			Index = 24
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopPCBPanel (AllPanels.StopPCBPanel):
			Index = 48
	class PCBTab:
		ID = "PCB3DTab"
		class PCBPanel (AllPanels.PCBPanel):
			Index = 25
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
	class PackageTab:
		ID = "Package3DTab"
		class PackagePanel (AllPanels.PackagePanel):
			Index = 34
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopPackagePanel (AllPanels.StopPackagePanel):
			Index = 31
	class LbrPackageTab:
		ID = "LbrPackage3DTab"
		class PackagePanel (AllPanels.PackagePanel):
			Index = 33
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class ReturnLibraryPanel (AllPanels.ReturnLibraryPanel):
			Index = 32
	class BasefeatureSolidTab:
		ID = "BasefeatureSolidTab"
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 7
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 9
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel (AllPanels.StopBaseFeaturePanel):
			Index = 41
	class BasefeatureSurfaceTab:
		ID = "BasefeatureSurfaceTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 15
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 16
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel (AllPanels.StopBaseFeaturePanel):
			Index = 41
	class SketchTab:
		ID = "SketchTab"
		class SketchCreatePanel (AllPanels.SketchCreatePanel):
			Index = 3
		class SketchModifyPanel (AllPanels.SketchModifyPanel):
			Index = 5
		class SketchConstraintsPanel (AllPanels.SketchConstraintsPanel):
			Index = 6
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopSketchPanel (AllPanels.StopSketchPanel):
			Index = 40
	class EditSnapshotTab:
		ID = "EditSnapshotTab"
		class SnapshotSolidModifyPanel (AllPanels.SnapshotSolidModifyPanel):
			Index = 46
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class FinishSnapshotEditPanel (AllPanels.FinishSnapshotEditPanel):
			Index = 45
	class PCBSketchTab:
		ID = "PCBSketchTab"
		class PCBSketchCreatePanel (AllPanels.PCBSketchCreatePanel):
			Index = 4
		class SketchModifyPanel (AllPanels.SketchModifyPanel):
			Index = 5
		class SketchConstraintsPanel (AllPanels.SketchConstraintsPanel):
			Index = 6
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class InsertPanel (AllPanels.InsertPanel):
			Index = 30
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopSketchPanel (AllPanels.StopSketchPanel):
			Index = 40
	class PCBBasefeatureSolidTab:
		ID = "PCBBasefeatureSolidTab"
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class SelectPanel (AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel (AllPanels.StopBaseFeaturePanel):
			Index = 41
	class RenderTab:
		ID = "RenderTab"
		class RenderSetupPanel (AllPanels.RenderSetupPanel):
			Index = 50
		class InCanvasRenderPanel (AllPanels.InCanvasRenderPanel):
			Index = 51
		class RenderPanel (AllPanels.RenderPanel):
			Index = 52
	class ParaMeshBaseFeatureTab:
		ID = "ParaMeshBaseFeatureTab"
		class ParaMeshPreparePanel (AllPanels.ParaMeshPreparePanel):
			Index = 58
		class ParaMeshModifyPanel (AllPanels.ParaMeshModifyPanel):
			Index = 59
		class AssemblePanel (AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel (AllPanels.InspectPanel):
			Index = 27
		class ParaMeshSelectPanel (AllPanels.ParaMeshSelectPanel):
			Index = 60
		class ParaMeshExportPanel (AllPanels.ParaMeshExportPanel):
			Index = 61
		class ParaMeshBaseFeatureStopPanel (AllPanels.ParaMeshBaseFeatureStopPanel):
			Index = 62
	class FusionDocTab:
		ID = "FusionDocTab"
		class ViewsPanel (AllPanels.ViewsPanel):
			Index = 0
		class DrawingPanel (AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel (AllPanels.ModifyPanel):
			Index = 2
		class GeometryPanel (AllPanels.GeometryPanel):
			Index = 3
		class DimensionsPanel (AllPanels.DimensionsPanel):
			Index = 4
		class TextPanel (AllPanels.TextPanel):
			Index = 5
		class InspectPanel (AllPanels.InspectPanel):
			Index = 6
		class SymbolsPanel (AllPanels.SymbolsPanel):
			Index = 7
		class InsertPanel (AllPanels.InsertPanel):
			Index = 8
		class BillOfMaterialsPanel (AllPanels.BillOfMaterialsPanel):
			Index = 9
		class BlockPanel (AllPanels.BlockPanel):
			Index = 10
		class StopSketchEditPanel (AllPanels.StopSketchEditPanel):
			Index = 13
		class OutputPanel (AllPanels.OutputPanel):
			Index = 14
	class ManageTab:
		ID = "ManageTab"
		class AssignPanel (AllPanels.AssignPanel):
			Index = 15
		class ReleasePanel (AllPanels.ReleasePanel):
			Index = 16
	class TitleBlockTab:
		ID = "TitleBlockTab"
		class DrawingPanel (AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel (AllPanels.ModifyPanel):
			Index = 2
		class TextPanel (AllPanels.TextPanel):
			Index = 5
		class InspectPanel (AllPanels.InspectPanel):
			Index = 6
		class InsertPanel (AllPanels.InsertPanel):
			Index = 8
		class StopBlockEditPanel (AllPanels.StopBlockEditPanel):
			Index = 11
	class BorderTab:
		ID = "BorderTab"
		class DrawingPanel (AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel (AllPanels.ModifyPanel):
			Index = 2
		class TextPanel (AllPanels.TextPanel):
			Index = 5
		class InspectPanel (AllPanels.InspectPanel):
			Index = 6
		class InsertPanel (AllPanels.InsertPanel):
			Index = 8
		class StopBorderEditPanel (AllPanels.StopBorderEditPanel):
			Index = 12
	class SketchTab:
		ID = "SketchTab"
		class DrawingPanel (AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel (AllPanels.ModifyPanel):
			Index = 2
		class TextPanel (AllPanels.TextPanel):
			Index = 5
		class InspectPanel (AllPanels.InspectPanel):
			Index = 6
		class InsertPanel (AllPanels.InsertPanel):
			Index = 8
		class StopSketchEditPanel (AllPanels.StopSketchEditPanel):
			Index = 13
	class GenSolidTab:
		ID = "GenSolidTab"
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 0
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 1
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class EditModelSelectPanel (AllPanels.EditModelSelectPanel):
			Index = 17
		class FinishEditModelPanel (AllPanels.FinishEditModelPanel):
			Index = 18
	class GenSurfaceTab:
		ID = "GenSurfaceTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 3
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 4
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class EditModelSelectPanel (AllPanels.EditModelSelectPanel):
			Index = 17
		class FinishEditModelPanel (AllPanels.FinishEditModelPanel):
			Index = 18
	class GenSketchTab:
		ID = "GenSketchTab"
		class SketchCreatePanel (AllPanels.SketchCreatePanel):
			Index = 10
		class SketchModifyPanel (AllPanels.SketchModifyPanel):
			Index = 11
		class SketchConstraintsPanel (AllPanels.SketchConstraintsPanel):
			Index = 12
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class InsertPanel (AllPanels.InsertPanel):
			Index = 9
		class SelectPanel (AllPanels.SelectPanel):
			Index = 8
		class StopSketchPanel (AllPanels.StopSketchPanel):
			Index = 13
	class SimSolidTab:
		ID = "SimSolidTab"
		class SolidCreatePanel (AllPanels.SolidCreatePanel):
			Index = 0
		class SolidModifyPanel (AllPanels.SolidModifyPanel):
			Index = 1
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel (AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel (AllPanels.FinishSimplifyPanel):
			Index = 18
	class SimSurfaceTab:
		ID = "SimSurfaceTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 3
		class SurfaceModifyPanel (AllPanels.SurfaceModifyPanel):
			Index = 4
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel (AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel (AllPanels.FinishSimplifyPanel):
			Index = 18
	class IdealizeTab:
		ID = "IdealizeTab"
		class SurfaceCreatePanel (AllPanels.SurfaceCreatePanel):
			Index = 3
		class IdealizeModifyPanel (AllPanels.IdealizeModifyPanel):
			Index = 5
		class ShellsPanel (AllPanels.ShellsPanel):
			Index = 6
		class ConstructionPanel (AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel (AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel (AllPanels.FinishSimplifyPanel):
			Index = 18
	class SketchTab:
		ID = "SketchTab"
		class SketchCreatePanel (AllPanels.SketchCreatePanel):
			Index = 10
		class SketchModifyPanel (AllPanels.SketchModifyPanel):
			Index = 11
		class SketchConstraintsPanel (AllPanels.SketchConstraintsPanel):
			Index = 12
		class SketchInspectPanel (AllPanels.SketchInspectPanel):
			Index = 7
		class InsertPanel (AllPanels.InsertPanel):
			Index = 9
		class SelectPanel (AllPanels.SelectPanel):
			Index = 8
		class StopSketchPanel (AllPanels.StopSketchPanel):
			Index = 13
	class ToolsTab:
		ID = "ToolsTab"
		class ReturnPanel (AllPanels.ReturnPanel):
			Index = 19
	class SimSetupTab:
		ID = "SimSetupTab"
		class StudyPanel (AllPanels.StudyPanel):
			Index = 12
		class SimplifyPanel (AllPanels.SimplifyPanel):
			Index = 13
		class MaterialsPanel (AllPanels.MaterialsPanel):
			Index = 14
		class ConstraintsPanel (AllPanels.ConstraintsPanel):
			Index = 26
		class LoadsPanel (AllPanels.LoadsPanel):
			Index = 27
		class ContactsPanel (AllPanels.ContactsPanel):
			Index = 28
		class DisplayPanel (AllPanels.DisplayPanel):
			Index = 15
		class OptimizationPanel (AllPanels.OptimizationPanel):
			Index = 29
		class ManagePanel (AllPanels.ManagePanel):
			Index = 5
		class SolvePanel (AllPanels.SolvePanel):
			Index = 3
		class AnsysPanel (AllPanels.AnsysPanel):
			Index = 4
		class ResultsCmdPanel (AllPanels.ResultsCmdPanel):
			Index = 31
		class InspectPanel (AllPanels.InspectPanel):
			Index = 18
		class SelectPanel (AllPanels.SelectPanel):
			Index = 20
	class SimResultsTab:
		ID = "SimResultsTab"
		class ResultToolsPanel (AllPanels.ResultToolsPanel):
			Index = 0
		class ComparePanel (AllPanels.ComparePanel):
			Index = 1
		class DeformationPanel (AllPanels.DeformationPanel):
			Index = 2
		class ResultsDisplayPanel (AllPanels.ResultsDisplayPanel):
			Index = 16
		class ResultsManagePanel (AllPanels.ResultsManagePanel):
			Index = 6
		class ResultsInspectPanel (AllPanels.ResultsInspectPanel):
			Index = 19
		class SelectPanel (AllPanels.SelectPanel):
			Index = 20
		class FinishResultsPanel (AllPanels.FinishResultsPanel):
			Index = 22
	class CompareTab:
		ID = "CompareTab"
		class SynchronizePanel (AllPanels.SynchronizePanel):
			Index = 7
		class ResultsAnimatePanel (AllPanels.ResultsAnimatePanel):
			Index = 8
		class ResultsOptionsPanel (AllPanels.ResultsOptionsPanel):
			Index = 9
		class CompareLayoutsPanel (AllPanels.CompareLayoutsPanel):
			Index = 10
		class PostMeshPanel (AllPanels.PostMeshPanel):
			Index = 11
		class FinishSimComparePanel (AllPanels.FinishSimComparePanel):
			Index = 21
class WorkSpaces:
	class FusionSolidEnvironment:
		ID = "FusionSolidEnvironment"
		class Tabs:
			class SolidTab (AllTabs.SolidTab):
				Index = 0
			class SurfaceTab (AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab (AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab (AllTabs.FormTab):
				Index = 2
			class SheetMetalTab (AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab (AllTabs.ToolsTab):
				Index = 4
			class ManageTab (AllTabs.ManageTab):
				Index = 5
			class PCBTab (AllTabs.PCBTab):
				Index = 6
			class PackageTab (AllTabs.PackageTab):
				Index = 8
			class BasefeatureSolidTab (AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab (AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab (AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab (AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab (AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCBSketchCreatePanel = AllPanels.PCBSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCBPanel = AllPanels.PCBPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			PackagePanel = AllPanels.PackagePanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			zxynine_anyMacroPanel = AllPanels.zxynine_anyMacroPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
	class GenerativeEnvironment:
		ID = "GenerativeEnvironment"
		class Tabs:
			class DefineTab (AllTabs.DefineTab):
				Index = 0
			class ExploreTab (AllTabs.ExploreTab):
				Index = 1
			class OutcomeViewTab (AllTabs.OutcomeViewTab):
				Index = 2
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			GenStudyPanel1 = AllPanels.GenStudyPanel1
			GenModelPanel = AllPanels.GenModelPanel
			GuidePanel = AllPanels.GuidePanel
			GenDesignSpacePanel = AllPanels.GenDesignSpacePanel
			GenDesignConditionsPanel = AllPanels.GenDesignConditionsPanel
			GenDesignCriteriaPanel = AllPanels.GenDesignCriteriaPanel
			GenMaterialsPanel = AllPanels.GenMaterialsPanel
			GenSolvePanel = AllPanels.GenSolvePanel
			GenExplore = AllPanels.GenExplore
			ExploreDisplayPanel = AllPanels.ExploreDisplayPanel
			ExploreDesignSpaceViewPanel = AllPanels.ExploreDesignSpaceViewPanel
			ExploreComparePanel = AllPanels.ExploreComparePanel
			ExploreExportPanel = AllPanels.ExploreExportPanel
			ExploreExportDataPanel = AllPanels.ExploreExportDataPanel
			ExploreTagPanel = AllPanels.ExploreTagPanel
			FinishOutcomeViewPanel = AllPanels.FinishOutcomeViewPanel
			FinishExplorePanel = AllPanels.FinishExplorePanel
			GenInspectPanel = AllPanels.GenInspectPanel
			GenSelectPanel = AllPanels.GenSelectPanel
	class PCBEnvironment:
		ID = "PCBEnvironment"
		class Tabs:
			class SolidTab (AllTabs.SolidTab):
				Index = 0
			class SurfaceTab (AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab (AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab (AllTabs.FormTab):
				Index = 2
			class SheetMetalTab (AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab (AllTabs.ToolsTab):
				Index = 4
			class ManageTab (AllTabs.ManageTab):
				Index = 5
			class PCBTab (AllTabs.PCBTab):
				Index = 6
			class PackageTab (AllTabs.PackageTab):
				Index = 8
			class BasefeatureSolidTab (AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab (AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab (AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab (AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab (AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCBSketchCreatePanel = AllPanels.PCBSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCBPanel = AllPanels.PCBPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			PackagePanel = AllPanels.PackagePanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			zxynine_anyMacroPanel = AllPanels.zxynine_anyMacroPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
	class PCBEnvironment:
		ID = "PCB3DEnvironment"
		class Tabs:
			class PCBTab (AllTabs.PCBTab):
				Index = 7
			class PCBSketchTab (AllTabs.PCBSketchTab):
				Index = 14
			class PCBBasefeatureSolidTab (AllTabs.PCBBasefeatureSolidTab):
				Index = 15
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCBSketchCreatePanel = AllPanels.PCBSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCBPanel = AllPanels.PCBPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			PackagePanel = AllPanels.PackagePanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			zxynine_anyMacroPanel = AllPanels.zxynine_anyMacroPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
	class PackageEnvironment:
		ID = "Package3DEnvironment"
		class Tabs:
			class SolidTab (AllTabs.SolidTab):
				Index = 0
			class SurfaceTab (AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab (AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab (AllTabs.FormTab):
				Index = 2
			class SheetMetalTab (AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab (AllTabs.ToolsTab):
				Index = 4
			class ManageTab (AllTabs.ManageTab):
				Index = 5
			class PCBTab (AllTabs.PCBTab):
				Index = 6
			class PackageTab (AllTabs.PackageTab):
				Index = 8
			class BasefeatureSolidTab (AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab (AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab (AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab (AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab (AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCBSketchCreatePanel = AllPanels.PCBSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCBPanel = AllPanels.PCBPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			PackagePanel = AllPanels.PackagePanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			zxynine_anyMacroPanel = AllPanels.zxynine_anyMacroPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
	class FusionRenderEnvironment:
		ID = "FusionRenderEnvironment"
		class Tabs:
			class RenderTab (AllTabs.RenderTab):
				Index = 16
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCBSketchCreatePanel = AllPanels.PCBSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCBPanel = AllPanels.PCBPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			PackagePanel = AllPanels.PackagePanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			zxynine_anyMacroPanel = AllPanels.zxynine_anyMacroPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
	class PublisherEnvironment:
		ID = "Publisher3DEnvironment"
		class Tabs:
			class Animation (AllTabs.Animation):
				Index = 0
		class Panels:
			StoryboardPanel = AllPanels.StoryboardPanel
			ComponentPanel = AllPanels.ComponentPanel
			AnnotationPanel = AllPanels.AnnotationPanel
			PublisherViewPanel = AllPanels.PublisherViewPanel
			PublishVideoPanel = AllPanels.PublishVideoPanel
	class SimulationEnvironment:
		ID = "SimulationEnvironment"
		class Tabs:
			class SimSetupTab (AllTabs.SimSetupTab):
				Index = 0
			class SimResultsTab (AllTabs.SimResultsTab):
				Index = 1
			class CompareTab (AllTabs.CompareTab):
				Index = 2
		class Panels:
			ResultToolsPanel = AllPanels.ResultToolsPanel
			ComparePanel = AllPanels.ComparePanel
			DeformationPanel = AllPanels.DeformationPanel
			SolvePanel = AllPanels.SolvePanel
			AnsysPanel = AllPanels.AnsysPanel
			ManagePanel = AllPanels.ManagePanel
			ResultsManagePanel = AllPanels.ResultsManagePanel
			SynchronizePanel = AllPanels.SynchronizePanel
			ResultsAnimatePanel = AllPanels.ResultsAnimatePanel
			ResultsOptionsPanel = AllPanels.ResultsOptionsPanel
			CompareLayoutsPanel = AllPanels.CompareLayoutsPanel
			PostMeshPanel = AllPanels.PostMeshPanel
			StudyPanel = AllPanels.StudyPanel
			SimplifyPanel = AllPanels.SimplifyPanel
			MaterialsPanel = AllPanels.MaterialsPanel
			DisplayPanel = AllPanels.DisplayPanel
			ResultsDisplayPanel = AllPanels.ResultsDisplayPanel
			ResultsSolvePanel = AllPanels.ResultsSolvePanel
			InspectPanel = AllPanels.InspectPanel
			ResultsInspectPanel = AllPanels.ResultsInspectPanel
			SelectPanel = AllPanels.SelectPanel
			FinishSimComparePanel = AllPanels.FinishSimComparePanel
			FinishResultsPanel = AllPanels.FinishResultsPanel
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			ConstraintsPanel = AllPanels.ConstraintsPanel
			LoadsPanel = AllPanels.LoadsPanel
			ContactsPanel = AllPanels.ContactsPanel
			OptimizationPanel = AllPanels.OptimizationPanel
			ResultsPanel = AllPanels.ResultsPanel
			ResultsCmdPanel = AllPanels.ResultsCmdPanel
	class CAMEnvironment:
		ID = "CAMEnvironment"
		class Tabs:
			class MillingTab (AllTabs.MillingTab):
				Index = 0
			class TurningTab (AllTabs.TurningTab):
				Index = 1
			class AdditiveTab (AllTabs.AdditiveTab):
				Index = 2
			class AdditiveResultsTab (AllTabs.AdditiveResultsTab):
				Index = 3
			class ProbingTab (AllTabs.ProbingTab):
				Index = 4
			class FabricationTab (AllTabs.FabricationTab):
				Index = 5
			class UtilitiesTab (AllTabs.UtilitiesTab):
				Index = 6
			class PartAlignmentTab (AllTabs.PartAlignmentTab):
				Index = 7
			class LiveAlignmentTab (AllTabs.LiveAlignmentTab):
				Index = 8
			class FeaturesTab (AllTabs.FeaturesTab):
				Index = 9
		class Panels:
			CAMJobPanel = AllPanels.CAMJobPanel
			CAMInProcessStockPanel = AllPanels.CAMInProcessStockPanel
			CAMAdditiveJobPanel = AllPanels.CAMAdditiveJobPanel
			CAMAdditivePositioningPanel = AllPanels.CAMAdditivePositioningPanel
			CAM2DPanel = AllPanels.CAM2DPanel
			CAMPanel = AllPanels.CAMPanel
			CAMEditPanel = AllPanels.CAMEditPanel
			CAMDrillingPanel = AllPanels.CAMDrillingPanel
			CAMMultiAxisPanel = AllPanels.CAMMultiAxisPanel
			CAMTurningPanel = AllPanels.CAMTurningPanel
			CAMWLPCPanel = AllPanels.CAMWLPCPanel
			CAMInfillPanel = AllPanels.CAMInfillPanel
			CAMSupportsPanel = AllPanels.CAMSupportsPanel
			CAMDEDPanel = AllPanels.CAMDEDPanel
			CAMAdditiveProcessSimPanel = AllPanels.CAMAdditiveProcessSimPanel
			CAMAdditiveProcessSimResultsPanel = AllPanels.CAMAdditiveProcessSimResultsPanel
			CAMAdditiveProcessSimActionPanel = AllPanels.CAMAdditiveProcessSimActionPanel
			CAMAdditiveProcessSimFinishPanel = AllPanels.CAMAdditiveProcessSimFinishPanel
			CAMProbingPanel = AllPanels.CAMProbingPanel
			CAMCMMPanel = AllPanels.CAMCMMPanel
			CAMManualInspectionPanel = AllPanels.CAMManualInspectionPanel
			CAMPartAlignmentEditPanel = AllPanels.CAMPartAlignmentEditPanel
			CAMPartAlignmentInspectPanel = AllPanels.CAMPartAlignmentInspectPanel
			CAMPartAlignmentPostPanel = AllPanels.CAMPartAlignmentPostPanel
			CAMLiveAlignmentPostPanel = AllPanels.CAMLiveAlignmentPostPanel
			CAMPartAlignmentResultsPanel = AllPanels.CAMPartAlignmentResultsPanel
			CAMLiveAlignmentResultsPanel = AllPanels.CAMLiveAlignmentResultsPanel
			CAMPartAlignmentPostAndExitPanel = AllPanels.CAMPartAlignmentPostAndExitPanel
			CAMPartAlignmentFinishPanel = AllPanels.CAMPartAlignmentFinishPanel
			CAMLiveAlignmentFinishPanel = AllPanels.CAMLiveAlignmentFinishPanel
			CAMActionPanel = AllPanels.CAMActionPanel
			CAMProbingActionPanel = AllPanels.CAMProbingActionPanel
			CAMAdditivePrintProfilePanel = AllPanels.CAMAdditivePrintProfilePanel
			CAMAdditiveActionPanel = AllPanels.CAMAdditiveActionPanel
			CAMInspectPanel = AllPanels.CAMInspectPanel
			CAMManagePanel = AllPanels.CAMManagePanel
			CAMAdditiveManagePanel = AllPanels.CAMAdditiveManagePanel
			CAMGeometryFeatures = AllPanels.CAMGeometryFeatures
			CAMScriptsAddinsPanel = AllPanels.CAMScriptsAddinsPanel
			SelectPanel = AllPanels.SelectPanel
			ManufacturingSourcesPanel = AllPanels.ManufacturingSourcesPanel
			FabricationManagePanel = AllPanels.FabricationManagePanel
			MachineBuilderActivationPanel = AllPanels.MachineBuilderActivationPanel
			NESTPanel = AllPanels.NESTPanel
	class FusionDocumentationEnvironment:
		ID = "FusionDocumentationEnvironment"
		class Tabs:
			class FusionDocTab (AllTabs.FusionDocTab):
				Index = 0
			class ManageTab (AllTabs.ManageTab):
				Index = 1
			class TitleBlockTab (AllTabs.TitleBlockTab):
				Index = 2
			class BorderTab (AllTabs.BorderTab):
				Index = 3
			class SketchTab (AllTabs.SketchTab):
				Index = 4
		class Panels:
			ViewsPanel = AllPanels.ViewsPanel
			DrawingPanel = AllPanels.DrawingPanel
			ModifyPanel = AllPanels.ModifyPanel
			GeometryPanel = AllPanels.GeometryPanel
			DimensionsPanel = AllPanels.DimensionsPanel
			TextPanel = AllPanels.TextPanel
			InspectPanel = AllPanels.InspectPanel
			SymbolsPanel = AllPanels.SymbolsPanel
			InsertPanel = AllPanels.InsertPanel
			BillOfMaterialsPanel = AllPanels.BillOfMaterialsPanel
			BlockPanel = AllPanels.BlockPanel
			StopBlockEditPanel = AllPanels.StopBlockEditPanel
			StopBorderEditPanel = AllPanels.StopBorderEditPanel
			StopSketchEditPanel = AllPanels.StopSketchEditPanel
			OutputPanel = AllPanels.OutputPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
	class ElectronEmptyLbrEnvironment:
		ID = "ElectronEmptyLbrEnvironment"
		class Tabs:
			class LbrEmptyTab (AllTabs.LbrEmptyTab):
				Index = 0
			class LbrDocumentTab (AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab (AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab (AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronDeviceEnvironment:
		ID = "ElectronDeviceEnvironment"
		class Tabs:
			class LbrDeviceTab (AllTabs.LbrDeviceTab):
				Index = 1
			class LbrDocumentTab (AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab (AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab (AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronFootprintEnvironment:
		ID = "ElectronFootprintEnvironment"
		class Tabs:
			class LbrFootprintTab (AllTabs.LbrFootprintTab):
				Index = 2
			class LbrDocumentTab (AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab (AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab (AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronSymbolEnvironment:
		ID = "ElectronSymbolEnvironment"
		class Tabs:
			class LbrSymbolTab (AllTabs.LbrSymbolTab):
				Index = 3
			class LbrDocumentTab (AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab (AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab (AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronPackageEnvironment:
		ID = "ElectronPackageEnvironment"
		class Tabs:
			class LbrDocumentTab (AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab (AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab (AllTabs.LbrManagementTab):
				Index = 6
			class LbrPackageTab (AllTabs.LbrPackageTab):
				Index = 7
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
